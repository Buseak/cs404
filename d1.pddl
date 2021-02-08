;Header and description

(define (domain d1)

;remove requirements that are not needed
(:requirements :adl)
(:types ;todo: enumerate types and their hierarchy here, e.g. car truck bus - vehicle
    object
)

; un-comment following line if constants are needed
(:constants fox goose beans - object)

(:predicates ;todo: define predicates here
    (onLeft ?o)
)


(:action cross
    :parameters (?o - object)
    :precondition
    (or ;
    (and (= ?o goose) (onLeft goose) (onLeft fox) (onLeft beans))
    (and (= ?o beans) (onLeft fox) (not (onLeft goose)) (onLeft beans))
    (and (= ?o goose) (onLeft fox) (not (onLeft goose)) (not (onLeft beans)))
    (and (= ?o fox) (onLeft fox) (onLeft goose) (not (onLeft beans)))
    (and (= ?o goose) (onLeft goose) (not (onLeft beans)) (not (onLeft fox)))

    (and (= ?o fox) (onLeft fox) (not (onLeft goose)) (onLeft beans))
    (and (= ?o goose) (onLeft beans) (not (onLeft fox)) (not (onLeft goose)))
    (and (= ?o beans) (not (onLeft fox)) (onLeft goose) (onLeft beans))
    )

    :effect (and (when  (and (= ?o goose) (onLeft goose) (onLeft fox) (onLeft beans))  (not (onLeft ?o)) ) ;goose to right
                 (when (and (= ?o beans) (onLeft fox) (not (onLeft goose)) (onLeft beans)) (not (onLeft ?o)) ) ;beans to right
                 (when (and (= ?o goose) (onLeft fox) (not (onLeft goose)) (not (onLeft beans))) (onLeft ?o)) ;goose to left
                 (when (and (= ?o fox) (onLeft fox) (onLeft goose) (not (onLeft beans))) (not (onLeft ?o))) ;fox to right
                 (when (and (= ?o goose) (onLeft goose) (not (onLeft beans)) (not (onLeft fox))) (not (onLeft ?o))) ;goose to right

                 (when (and (= ?o fox) (onLeft fox) (not (onLeft goose)) (onLeft beans)) (not (onLeft ?o))) ;fox to right
                 (when (and (= ?o goose) (onLeft beans) (not (onLeft fox)) (not (onLeft goose)))  (onLeft ?o)) ;goose to left
                 (when (and (= ?o beans) (not (onLeft fox)) (onLeft goose) (onLeft beans)) (not (onLeft ?o))) ;beans to right
     )
)


)