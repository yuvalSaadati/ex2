(define (domain network)
(:predicates
	 (at ?g ?comp) (agent ?g) (win7 ?a) (win10 ?a) (linux ?a) (ubuntu16 ?a) (connect ?a ?b) (attack ?g ?a))

(:action move-attack
 :parameters ( ?g ?a ?b)
 :precondition
	(and (agent ?g) (at ?g ?a) (connect ?a ?b) )
 :effect
	(and (at ?g ?b) (attack ?g ?b) (not (at ?g ?a))))

)