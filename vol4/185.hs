{-# LANGUAGE NPlusKPatterns #-}

import Data.Array
import Data.List
import Data.Char

type Candidate = Array Int [Int]
type Guess = (Int, [Int])
type Mind = (Candidate, [Guess])

guesses = [
 (2,[5,6,1,6,1,8,5,6,5,0,5,1,8,2,9,3]),
 (1,[3,8,4,7,4,3,9,6,4,7,2,9,3,0,4,7]),
 (3,[5,8,5,5,4,6,2,9,4,0,8,1,0,5,8,7]),
 (3,[9,7,4,2,8,5,5,5,0,7,0,6,8,3,5,3]),
 (3,[4,2,9,6,8,4,9,6,4,3,6,0,7,5,4,3]),
 (1,[3,1,7,4,2,4,8,4,3,9,4,6,5,8,5,8]),
 (2,[4,5,1,3,5,5,9,0,9,4,1,4,6,1,1,7]),
 (3,[7,8,9,0,9,7,1,5,4,8,9,0,8,0,6,7]),
 (1,[8,1,5,7,3,5,6,3,4,4,1,1,8,4,8,3]),
 (2,[2,6,1,5,2,5,0,7,4,4,3,8,6,8,9,9]),
 (3,[8,6,9,0,0,9,5,8,5,1,5,2,6,2,5,4]),
 (1,[6,3,7,5,7,1,1,9,1,5,0,7,7,0,5,0]),
 (1,[6,9,1,3,8,5,9,1,7,3,1,2,1,3,6,0]),
 (2,[6,4,4,2,8,8,9,0,5,5,0,4,2,7,6,8]),
 (0,[2,3,2,1,3,8,6,1,0,4,3,0,3,8,4,5]),
 (2,[2,3,2,6,5,0,9,4,7,1,2,7,1,4,4,8]),
 (2,[5,2,5,1,5,8,3,3,7,9,6,4,4,3,2,2]),
 (3,[1,7,4,8,2,7,0,4,7,6,7,5,8,2,7,6]),
 (1,[4,8,9,5,7,2,2,6,5,2,1,9,0,3,0,6]),
 (3,[3,0,4,1,6,3,1,1,1,7,2,2,4,6,3,5]),
 (3,[1,8,4,1,2,3,6,4,5,4,3,2,4,5,8,9]),
 (2,[2,6,5,9,8,6,2,6,3,7,3,1,6,8,6,7])]

answer :: Mind -> Bool
answer (c, gs) = all (\x -> length x == 1 && x /= [10]) (elems c) && null gs

impossible :: Mind -> Bool
impossible (c, gs) = any (== [10]) (elems c) || any (not . active) gs
    where active (k, ns) = 0 <= k && k <= length (filter (>= 0) ns)

unique :: Candidate -> [(Int, Int)]
unique = map (\(d, [n, 10]) -> (d, n)) . filter (\x -> length (snd x) == 2) . assocs

fill :: Mind -> (Int, Int) -> Mind
fill (c, gs) (d, n) = (c // [(d, [n])], map fill' gs)
    where fill' (k, ns) = let (xs, y:zs) = splitAt (d - 1) ns
                          in if y == n then (k - 1, xs ++ (-1) : zs) else (k, xs ++ (-1) : zs) 

combination _ 0 = [[]]
combination [] _ = []
combination (x:xs) n = (map (x:) (combination xs (n - 1))) ++ (combination (xs) n)

sieve :: Mind -> (Int,Int) -> Mind
sieve (c, gs) (d, n) = (c // [(d, delete n $ (c ! d))], map fill' gs)
    where fill' (k, ns) = let (xs, y:zs) = splitAt (d - 1) ns
                          in if y == n then (k, xs ++ (-1) : zs) else (k, xs ++ y : zs) 

step :: Mind -> [Mind]
step (c, (k, ns):gs) = [foldl' fill (foldl' sieve (c, gs) (ps \\ p)) p | p <- combination ps k]
    where ps = filter ((>= 0) . snd) $ zip [1..] ns 

solve :: [Mind] -> Integer
solve (m@(c, gs):ms) | answer m = read . map intToDigit . concat $ elems c 
                     | impossible m = solve ms
                     | unique c /= [] = solve $ foldl' fill m (unique c) : ms
                     | otherwise = solve $ step (c, sort gs) ++ ms

main = print $ solve [(listArray (1, 16) $ repeat [0..10], guesses)]