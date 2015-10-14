solve p = sum [
    10 * n + d |
    t <- [1..9],
    d <- [1..9],
    let (n, m) = divMod ((p - t) * d) (10 * t - 1),
        m == 0,
        10 * n >= p
    ]

main = do
    print $ (`mod` (10 ^ 5)) $ sum [solve e | i <- [1..99], let e = 10 ^ i]
