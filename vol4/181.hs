import Data.Array (range)
import Data.Array.IO (IOArray, newArray, readArray, writeArray)
import Control.Monad (forM_)

b :: Int
b = 60

w :: Int
w = 40

main = do 
    g <- newArray ((0, 0), (b, w)) 0 :: IO (IOArray (Int, Int) Int)
    writeArray g (0, 0) 1
    forM_ [(i, j, k, l) | (i, j) <- tail $ range ((0, 0), (b, w)), (k, l) <- range ((i, j), (b, w))] $ \(i, j, k, l) -> readArray g (k - i, l - j) >>= \t -> readArray g (k, l) >>= writeArray g (k, l) . (+ t)
    print =<< readArray g (b, w)
