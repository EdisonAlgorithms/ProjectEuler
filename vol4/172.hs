factorial n = product [1..toInteger n]

fallingFactorial  n k = product [n - fromInteger i | i <- [0..toInteger k - 1]]

combinations n 0 = 1
combinations n k = fallingFactorial n k `div` factorial k

solve 0 _ = 0
solve d p
    | p < 4 = d ^ p
    | otherwise = sum [(combinations p k) * (solve (d - 1) (p - k)) | k <- [0..3]]

main = do
    print $ (solve 10 18) * 9 `div` 10
