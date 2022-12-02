takeFromList :: [a] -> Int -> a
takeFromList xs a = xs !! a

getArea :: Int -> Int -> Int
getArea x y = x * y

getList :: Int -> [Int]
getList a = [1..a]

isSqrtEq a b c = c == sqrt(a^2 + b^2)

isPythagorean a b c = isSqrtEq a b c || isSqrtEq a c b || isSqrtEq b c a

factorial n = product [1..n]

stooges n =  take n (cycle ["Moe", "Larry", "Shemp"])
slaps list n = ["slap " ++ stooge | stooge <- stooges n]

main = do
   print (takeFromList [1,2,3,4,5] 3)
   print (getArea 10 20)
   print (getList 11)
   print (isSqrtEq 4 5 6)
   print (isPythagorean 3 4 5)
   print(factorial 5)
   print(slaps (stooges 5) 5)
  


