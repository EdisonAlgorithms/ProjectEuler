import Text.Printf

func 0 0 0 1 = 0
func 0 0 1 0 = 1
func 0 1 0 0 = 1 + func 0 0 1 1
func 1 0 0 0 = 1 + func 0 1 1 1
func a b c d = (pickA + pickB + pickC + pickD) / (a + b + c + d)
        where 
        pickA | a > 0 = a * func (a - 1) (b + 1) (c + 1) (d + 1)
              | otherwise = 0
        pickB | b > 0 = b * func a (b - 1) (c + 1) (d + 1)
              | otherwise = 0
        pickC | c > 0 = c * func a b (c - 1) (d + 1)
              | otherwise = 0
        pickD | d > 0 = d * func a b c (d - 1)
              | otherwise = 0

main = do
    printf "%.6f\n" $ (func 1 1 1 1 :: Float)
