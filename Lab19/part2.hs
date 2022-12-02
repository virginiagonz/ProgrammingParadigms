myLength :: (Num b) => [a] -> b
myLength [] =  0
myLength (_:n) = 1 + myLength n


gradeFinder :: (RealFloat a) => a -> a -> String
gradeFinder a b
   | (a + b) / 2 >= 90 = "A"
   | (a + b) / 2 >= 80 = "B"
   | (a + b) / 2 >= 60 = "C"
   | otherwise = "F"

main = do
   
   print (myLength list2)    
   print (gradeFinder 95 45)
   print (gradeFinder 25 87)
   print (gradeFinder 75 99)
   
   
   
   let list2 = [1,2,3,4]
   
   