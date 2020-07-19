# name : yuval saadati
# id: 205956634
import sys

from pddlsim.local_simulator import LocalSimulator
from my_agent import Executor


domain_path = "attack_domain.pddl"
problem1_path = "attack_problem1.pddl"
problem2_path = "attack_problem2.pddl"
print LocalSimulator().run(domain_path, problem2_path, Executor())
#print LocalSimulator().run(str(sys.argv[1]), str(sys.argv[2]), Executor())