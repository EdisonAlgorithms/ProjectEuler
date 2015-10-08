fun n = 
    sum [
        (2 * n3 + 5 * n2 + 2 * n) `div` 8,
        2 * (n3 `div` 2 - n `div` 6), 
        6 * sum[
            (n * (n + 1) * (n + 2)) `div` 6,
            (2 * n3 + 5 * n2 + 2 * n) `div` 8,
            (2 * n3 + 3 * n2 - 3 * n) `div` 18,
            (2 * n3 + 3 * n2 - 3 * n) `div` 10
        ],
        3 * ((22 * n3 + 45 * n2 - 4 * n) `div` 48)
    ]
    where
        n3 = n ^ 3
        n2 = n ^ 2
main = do
    print $ fun 36
