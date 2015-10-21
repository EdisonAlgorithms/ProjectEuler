import Data.List

permutation :: Eq a =>  [a] -> [[a]]
permutation [] = [[]]
permutation xs = [y:ys | y <- xs, ys <- permutation $ delete y xs]

listToNum :: Num a => [a] -> a
listToNum = foldl (\a b -> 10 * a + b) 0

numToList :: Integral a => a -> [a]
numToList = reverse . unfoldr f
    where f 0 = Nothing
          f x = let (q, r) = divMod x 10 in Just (r, q)

main :: IO ()
main = print $ head [x | x <- map listToNum $ permutation [9,8..0],
           d <- [12, 15..48],
           x `mod` d == 0,
           let q = numToList $ x `div` d,
           let s = numToList d ++ q,
           s \\ [0..9] == [0],
           any (\z -> q!!(z+1)*d < 100) $ findIndices (== 0) $ init q]   
