import qualified Data.Map as M

data StepState = StepState {
                    minDigit :: Int,
                    maxDigit :: Int, 
                    lastDigit :: Int
                 } deriving (Show, Eq, Ord)

up, down :: StepState -> StepState
up (StepState a b c) = StepState a (max b $ c + 1) (c + 1)
down (StepState a b c) = StepState (min a $ (c - 1)) b (c - 1)

next :: M.Map StepState Integer -> M.Map StepState Integer
next m = M.unionWith (+) (next' up m) (next' down m)
    where next' f = M.filterWithKey (\(StepState _ _ c) _ -> c >= 0 && c <= 9) . M.mapKeysWith (+) f

count :: M.Map StepState Integer -> Integer
count = M.fold (+) 0 . M.filterWithKey (\(StepState a b _) _  -> a == 0 && b == 9)
    
solve :: Int -> Integer
solve n = sum . map count . take n . iterate next . M.fromList $ [(StepState d d d, 1) | d <- [1..9]]

main = do
    print $ solve 40
