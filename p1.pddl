(define (problem p1) (:domain d1)
(:objects

)

(:init
    ;todo: put the initial state's facts and numeric values here
    (onLeft fox)
    (onLeft goose)
    (onLeft beans)

)

(:goal (and
    ;todo: put the goal condition here
     (not (onLeft fox)) (not (onLeft goose)) (not (onLeft beans))
))

;un-comment the following line if metric is needed
;(:metric minimize (???))
)
