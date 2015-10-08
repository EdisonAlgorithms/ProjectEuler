factorial n = product [1..toInteger n]

fallingFactorial x n = product [x - i | i <- [0..fromIntegral n - 1]]

combination n k = fallingFactorial n k `div` factorial k

coe 2 = 1
coe n = 2 * (coe (n - 1)) + n - 1

solve = maximum [func n | n <- [2..26]]
    where func x = (coe x) * (combination 26 x)

main = do
    print solve
