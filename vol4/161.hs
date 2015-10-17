import Data.Array.Unboxed
import qualified Data.Map as M

data Triomino = N | W | S | E | V | H
type Board = UArray Int Bool
type Memo = M.Map Board Integer

h = 12
w = 9

memorize f x y memo = case M.lookup x memo of
                           Just fx -> (fx, memo)
                           Nothing -> let (fx, memo') = f x y memo
                                   in (fx, if fx > 1 then M.insert x fx memo' else memo')

inBoard :: Int -> Triomino -> Bool
inBoard x t = case t of
                W -> x `div` w < h - 1 && x `mod` w > 0
                V -> x `div` w < h - 2
                H -> x `mod` w < w - 2
                _ -> x `div` w < h - 1 && x `mod` w < w - 1

area x t = let ys = case t of
                        N -> [0, w, w + 1]
                        W -> [0, w, w - 1]
                        S -> [0, w + 1, 1]
                        E -> [0, w, 1]
                        V -> [0, w, 2 * w]
                        H -> [0, 1, 2]
        in zipWith (+) ys $ repeat x

canPut :: Board -> Int -> Triomino -> Bool
canPut b x t = if inBoard x t == False then False
               else all (not . (b !)) $ area x t

solve :: Board -> Int -> Memo -> (Integer, Memo)
solve b x memo | x == h * w = (1, memo)
               | b ! x = memorize solve b (x + 1) memo
               | otherwise = foldl next (0, memo) $ filter (canPut b x) [N, W, S, E, V, H]
                where next (c, m) t = let (c', m') = memorize solve (b // [(y, True) | y <- area x t]) x m
                                      in (c + c', m')

main = print . fst $ solve board 0 M.empty
    where board = listArray (0, h * w - 1) . repeat $ False