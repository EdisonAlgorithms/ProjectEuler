import Data.List ((\\))
import Data.Ratio ((%), denominator)

sqrt' :: Integer -> Integer
sqrt' = floor . sqrt . fromIntegral

next :: (Integral a) => a -> a -> (a, (a, a)) -> (a, (a, a))
next x s (a, (p, q)) = let p' = a * q - p
                           q' = (x - p' * p') `div` q
                       in ((s + p') `div` q', (p', q'))

fractions :: Integer -> [Integer]
fractions x = map fst $ iterate (next x (sqrt' x)) (sqrt' x, (0, 1))

convergents :: Integer -> [(Integer, Integer)]
convergents x = cs
    where cs = (1, 0) : zipWith3 f (fractions x) cs ((0, 1) : cs)
          f a (n1, d1) (n2, d2) = (a * n1 + n2, a * d1 + d2)

bestDenominator :: Integer -> Integer -> Integer
bestDenominator d x 
    | abs ((n1 % d1) ^ 2 - x') < abs (s ^ 2 - x') = d1
    | otherwise = denominator s
    where x' = fromIntegral x
          ((n1, d1) : (n2, d2) : _) = reverse . takeWhile ((<= d) . snd) $ convergents x
          s = (n1 * ((d - d2) `div` d1) + n2) % (d1 * ((d - d2) `div` d1) + d2)

solve :: Integer -> Integer -> Integer
solve d n = sum . map (bestDenominator d) $ [2..n] \\ (map (^2) [2..sqrt' n])

main :: IO ()
main = print $ solve (10 ^ 12) 100000
