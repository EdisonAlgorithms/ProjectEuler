solve a b l | a * b > l = 0
            | b * c > l = (l `div` a - b) `div` a + 1
            | otherwise = 1 + (solve a c l) + (solve b c l)
    where c = a + b

main = print $ solve 1 100 l + 49
    where l = (10 ^ 8) `div` 2
