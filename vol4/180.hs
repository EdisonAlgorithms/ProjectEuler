import Data.Ratio
import Data.List

sqrt' :: Rational -> Rational
sqrt' x = 
    let a = floor . sqrt . fromIntegral $ numerator x
        b = floor . sqrt . fromIntegral $ denominator x
        c = (a % b) ^ 2
    in if x == c then (a % b) else 0

reciprocal :: Rational -> Rational
reciprocal x 
    | x == 0 = 0
    | otherwise = denominator x % numerator x

solve = 
    let order = 35
        range = nub [a % b | b <- [1..order], a <- [1..b - 1]]
        fn2 = [[x, y, z] | x <- range, y <- range, 
                           let z = x * y * reciprocal (sqrt' (x ^ 2 + y ^ 2)), 
                           elem z range]
        fn1 = [[x, y, z] | x <- range, y <- range,
                           let z = x * y * reciprocal (x + y),
                           elem z range]
        f1  = [[x, y, z] | x <- range, y <- range, 
                           let z = x + y,
                           elem z range]
        f2  = [[x, y, z] | x <- range, y <- range,
                           let z = sqrt' (x ^ 2 + y ^ 2),
                           elem z range]
        ans = sum . nub $ map sum (fn2 ++ fn1 ++ f1 ++ f2)
    in (numerator ans + denominator ans)

main = print solve
