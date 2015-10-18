import Data.Map (toList, fromListWith)
import Control.Arrow ((***))
import Data.List (sort)

type State = ((Double, Double, Double), Int)

curve :: (Floating a) => a -> a -> a -> a
curve a b c = a + b + c + 2 * sqrt (a * b + a * c + b * c)

next :: State -> ((Double, Int), [State])
next ((a, b, c), n) = ((r, n), zip s $ repeat n)
    where r = 1 / (curve (1 / a) (1 / b) (1 / c))
          s = [(r, a, b), (r, a, c), (r, b, c)]

reduce :: Ord k => [(k, Int)] -> [(k, Int)]
reduce = toList . fromListWith (+)

step :: ([(Double, Int)], [State]) -> ([(Double, Int)], [State])
step (_, s) =  (reduce *** reduce . concat) . unzip $ map next s

solve :: Int -> Double
solve m = (pi - cover) / pi
    where   cover = sum . map area . concat . take (m + 1) . map fst . iterate step $ initial
            area (r, n) = pi * r * r * fromIntegral n
            initial = ([(r1, 3)], [(s1, 1), (s2, 3)])
            r1 = 2 * sqrt 3 - 3
            s1 = (r1, r1, r1)
            s2 = (-1, r1, r1)   
          
main = print $ solve 10