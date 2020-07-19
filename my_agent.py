# name : yuval saadati
# id: 205956634
import random
import sys
from valid_actions import ValidActions
# the maximum goals in current state
max_goals = 0
# the minimum steps the agent pass to get maximum goals
min_step = 0
# amount of sub-goals of the problem
reached_goals = 0
# list of all the options that have done
all_done_options = []



class Executor(object):


    def __init__(self):
        super(Executor, self).__init__()

    def initialize(self, services):
        global reached_goals
        self.services = services
        reached_goals = len(self.services.goal_tracking.uncompleted_goals[0].parts)
        self.valid_actions_options = ValidActions(self.services.parser, self.services.pddl, self.services.perception)

    def sum_goals(self, state):
        # sum the sub-goals in the given state
        count = 0
        for sub_goal in self.services.goal_tracking.uncompleted_goals[0].parts:
            if self.services.parser.test_condition(sub_goal, state):
                count += 1
        return count

    def max_goals(self, state, k, options_done, steps):
        # Recursive function : The input of the function is new state after applying action on the state from the
        # calling function. The output is the maximum goals the agent can achieve in k steps from that new state to
        # the goal of the given problem. The 'list options_done' save all the options that used and 'steps' count the
        # agent steps

        global max_goals
        global min_step
        global reached_goals
        if k > 0:
            options = self.valid_actions_options.get(state)
            for option in options:
                if option not in options_done:
                    if option not in all_done_options:
                        if self.sum_goals(state) == reached_goals:
                            # in that state the agent reached all goals
                            max_goals = self.sum_goals(state)
                            min_step = steps
                            return max_goals
                        steps += 1
                        options_done.append(option)
                        k -= 1

                        new_state_from_option = self.services.parser.copy_state(state)
                        self.services.parser.apply_action_to_state(option, new_state_from_option,
                                                                   check_preconditions=False)
                        if k == 0:
                            # the agent can move only k steps
                            if self.sum_goals(new_state_from_option) > max_goals:
                                max_goals = self.sum_goals(new_state_from_option)
                                min_step = steps
                                return max_goals
                            if self.sum_goals(new_state_from_option) == max_goals:
                                if steps < min_step:
                                    min_step = steps
                                    return max_goals
                        self.max_goals(new_state_from_option, k, options_done, steps)

        if k == 0:
            # the agent passed k steps
            if self.sum_goals(state) > max_goals:
                max_goals = self.sum_goals(state)
                min_step = steps
            if self.sum_goals(state) == max_goals:
                # will choose the option with minimum steps
                if steps < min_step:
                    min_step = steps

        return max_goals

    def next_action(self):
        #  return the next action to apply
        global all_done_options
        global max_goals
        global min_step

        if self.services.goal_tracking.reached_all_goals():
            return None

        current_state = self.services.perception.get_state()
        options = self.valid_actions_options.get(current_state)
        # saving the best option from all options
        save_option = None
        # saving the options with minimum steps
        save_min_steps = 0
        # the maximum goals the agent collected from all options
        max_goals_all_options = 0
        for option in options:
            if option not in all_done_options:
                new_state_from_option = self.services.parser.copy_state(current_state)
                self.services.parser.apply_action_to_state(option, new_state_from_option, check_preconditions=True)
                max_goals = 0
                min_step = 0
                current_goals = self.max_goals(new_state_from_option, 4, [option], 0)
                if max_goals > max_goals_all_options:
                    max_goals_all_options = max_goals
                    save_option = option
                    save_min_steps = min_step
                elif max_goals == max_goals_all_options:
                    if min_step < save_min_steps:
                        # choosing the options with minimum steps
                        save_min_steps = min_step
                        save_option = option
        if save_option != None:
            all_done_options.append(save_option)
            return save_option
        else:
            random_option = random.choice(options)
            all_done_options.append(random_option)
            return random.choice(options)
