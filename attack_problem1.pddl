(define (problem take_over_linux)
(:domain network)
(:objects
	agent1
	start_comp_win10_1
	comp_win7_1
	comp_win7_2
	comp_win7_3
    comp_win10_2
	comp_win10_3
	comp_ubuntu16_1
	comp_ubuntu16_2
	comp_ubuntu16_3
	goal_comp_linux_1
	)
(:init
	(win7 comp_win7_1)
	(win7 comp_win7_2)
	(win7 comp_win7_3)
	(win10 start_comp_win10_1)
	(win10 comp_win10_2)
	(win10 comp_win10_3)
	(ubuntu16 comp_ubuntu16_1)
	(ubuntu16 comp_ubuntu16_2)
	(ubuntu16 comp_ubuntu16_3)
	(linux goal_comp_linux_1)

	(connect start_comp_win10_1 comp_win7_1)
    (connect comp_win7_1 comp_win7_2)
    (connect comp_win7_2 comp_win7_3)
    (connect comp_win7_3 comp_win10_2)
    (connect comp_win10_2 comp_win10_3)
    (connect comp_win10_3 comp_ubuntu16_1)
    (connect comp_ubuntu16_1 comp_ubuntu16_2)
    (connect comp_ubuntu16_2 comp_ubuntu16_3)
    (connect comp_ubuntu16_3 goal_comp_linux_1)

    (agent agent1)
    (at agent1 start_comp_win10_1)
        )
(:goal
   (and  (at agent1 goal_comp_linux_1) )
	)
)