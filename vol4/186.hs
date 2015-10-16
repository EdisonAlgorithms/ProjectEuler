{-# LANGUAGE BangPatterns #-}
import Control.Monad.ST (ST, runST)
import Control.Monad (when, liftM)
import Data.Array.ST (STUArray, newArray, readArray, writeArray)

lagFib :: [Integer]
lagFib = [(100003 - 200003 * k + 300007 * k ^ 3) `mod` 1000000 | k <- [1..55]] ++ zipWith modAdd lagFib (drop 31 lagFib)
    where modAdd x y = (x + y) `mod` 1000000

data UnionFind s = U {root :: STUArray s Int Int, rank :: STUArray s Int Int}

unionFind :: Int -> ST s (UnionFind s)
unionFind n = do
    root' <- newArray (0, n - 1) $ -1
    rank' <- newArray (0, n - 1) $ 0
    return $ U root' rank'

find :: UnionFind s -> Int -> ST s Int
find u x = do
    r <- readArray (root u) x
    if r < 0 then return x
    else do
        s <- find u r
        writeArray (root u) x s
        return s

size :: UnionFind s -> Int -> ST s Int
size u x = find u x >>= liftM negate . readArray (root u)

union :: UnionFind s -> Int -> Int -> ST s ()
union u x y = do
    rootX <- find u x
    rootY <- find u y
    sizeX <- readArray (root u) rootX
    sizeY <- readArray (root u) rootY
    rankX <- readArray (rank u) rootX
    rankY <- readArray (rank u) rootY
    case compare rankX rankY of
        GT -> writeArray (root u) rootY rootX >> writeArray (root u) rootX (sizeX + sizeY)
        LT -> writeArray (root u) rootX rootY >> writeArray (root u) rootY (sizeX + sizeY)
        EQ -> when (rootX /= rootY) $ do
                writeArray (root u) rootY rootX
                writeArray (root u) rootX (sizeX + sizeY)
                writeArray (rank u) rootX (rankX + 1)

solve :: Int
solve = runST $ do
            u <- unionFind (10 ^ 6)
            let call !c (a:b:cs)
                    | a == b = call c cs
                    | otherwise = do 
                        s <- size u 524287
                        if s >= 990000 then return c
                        else union u a b >> call (c + 1) cs
            call 0 . map fromInteger $ lagFib

main :: IO ()
main = print solve