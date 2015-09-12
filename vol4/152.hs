import Data.Ratio
import Data.List
import Data.Ord (comparing)
import Data.Function (on)

invSq n = 1 % (n * n)
sumInvSq = sum . map invSq

subsets (x:xs) = let s = subsets xs in s ++ map (x :) s
subsets _ = [[]]

pfree s x p = [(y, t) | t <- subsets s, let y = x + sumInvSq t,
                        denominator y `mod` p /= 0]

only23 = foldl func [(0, [[]])] [13, 7, 5]
    where
        func a p = 
            collect $ [(y, u ++v) |
            (x, s) <- a,
            (y, v) <- pfree (terms p) x p,
            u <- s]
        terms p = 
            [n * p | 
             n <- [1..80 `div` p],
             all (\q -> n `mod` q /= 0) $
             11 : takeWhile (>= p) [13, 7, 5]
            ]
        collect = 
            map (\z -> (fst $ head z, map snd z)) .
            groupBy fstEq . sortBy cmpFst
        fstEq = (==) `on` fst
        cmpFst = comparing fst

findInvSq x y = 
    func x $ zip3 y (map invSq y) (map sumInvSq $ init $ tails y)
    where
        func 0 _ = [[]]
        func x ((n, i, s):ns)
            | i > x = func x ns
            | s < x = []
            | otherwise = map (n:) (func (x - i) ns) ++ func x ns
        func _ _ = []

all23 = [n | a <- [0..4], b <- [0..2], let n = 2^a * 3^b, n <= 80]

solutions = 
    [sort $ u ++ v|
     (x, s) <- only23,
     u <- findInvSq (1 % 2 - x) all23,
     v <- s
    ]

main = do
    print $ length solutions
