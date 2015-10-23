import Data.Function (on)
import Data.Map (fromListWith, toList)

choose :: [a] -> Int -> [[a]]
choose _ 0 = [[]]
choose [] _ = []
choose (x:xs) n = [x:ys | ys <- choose xs (n - 1)] ++ choose xs n

sqrt' :: Integral a => a -> a
sqrt' = floor . sqrt . fromIntegral

gridLines :: Integral a => a -> [(a, a)]
gridLines r = (r - 1, 2) : (d, 2) : (toList $ fromListWith (+) [(count x y, 4) | x <- [1..r - 1], y <- [x + 1..sqrt' (r ^ 2 - 1 - x ^ 2)], gcd x y == 1])
    where count x y = floor . sqrt $ on (/) fromIntegral (r ^ 2 - 1) (x ^ 2 + y ^ 2)
          d = floor $ fromIntegral r / sqrt 2

solve :: Integral a => a -> a
solve r = sum . map count $ concatMap (choose (gridLines r)) [1, 2, 3]
    where count [(g, n)] = g ^ 3 * (n * (n - 1) * (n - 2) `div` 3)
          count [(g1, n1), (g2, n2)] = g1 * n1 * g2 * n2 * (g1 * (n1 - 1) + g2 * (n2 - 1))
          count gs = 2 * (product $ map (uncurry (*)) gs)

main = print $ solve 105
