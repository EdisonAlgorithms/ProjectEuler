solve 0 = (1, 0)
solve n
    | even n = (a + b, b)
    | odd n = (a, a + b)
    where 
        (a, b) = solve (n `div` 2)

main = do
    print . fst $ solve (10 ^ 25)
