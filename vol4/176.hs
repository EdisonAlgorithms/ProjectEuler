-- k = 47547
-- 2 * k + 1 = 95095 = 5 * 7 * 11 * 13 * 19
factor = [5, 7, 11, 13, 19]
primes = [2, 3, 5, 7, 11]

solve = product [a ^ b | (a, b) <- zip primes power]
    where power = reverse $ map (\x -> (x - 1) `div` 2) (init factor) ++ [(last factor + 1) `div` 2] 

main = print solve
