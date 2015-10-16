{--
    1. The number of m such that m ^ e mod p == m mod p is:
        gcd(e - 1, p - 1) + 1
    2. The number of m such that m ^ e mod n == m mod n is:
        (gcd(e - 1, p - 1) + 1) * (gcd(e - 1, q -  1) + 1)
--}
solve p q = sum [e | e <- [3, 5..phi - 1], gcd e phi == 1,
                    gcd (e - 1) (p - 1) == 2, gcd (e - 1) (q - 1) == 2]
    where phi = (p - 1) * (q - 1)

main = do
    print $ solve 1009 3643
