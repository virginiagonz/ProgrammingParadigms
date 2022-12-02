-- 
myLength :: [a] -> Int -- function type
myLength [] =  0 -- base case
myLength (x:_) = 1 + myLength xs -- recursion case

main = do
    print(myLength [2,3,4,5,6,7])
    print(myLength [])