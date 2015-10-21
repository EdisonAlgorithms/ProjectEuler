solve x y 
    | y == 0 = []
    | x < y = solve y x
    | r == 0 && q /= 1 && y /= 1  = (q - 1) : solve y y
    | otherwise = q : solve y r
    where (q, r) = x `divMod` y



main :: IO ()
main = do
    print . reverse $ solve 123456789 987654321
    print $ solve 13 17
