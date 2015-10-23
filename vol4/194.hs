choose :: (Integral a) => a -> a -> a
choose n r = (product [n - r + 1..n]) `div` (product [1..r])

solve :: Integer -> Integer -> Integer -> Integer
solve a b n = n * (n - 1) * (p_a ^ a) * (p_b ^ b) * (choose (a + b) a)
    where p_a = sum $ zipWith (*) [4,54,198,264,120] cs
          p_b = sum $ zipWith (*) [6,76,240,288,120] cs
          cs = map (choose (n - 2)) [1..5]

main = print $ (solve 25 75 1984) `mod` (10 ^ 8)
