-- Problem 1: Modify isGodzilla from today's lecture to isNum where the function 
-- accepts integer as an input parameter and outputs True if this integer matches 
-- the number in the function.
isNum :: Int -> Bool
isNum 5 = True
isNum x = False

-- Problem 2: Write a function fibList that uses the fib function from today's lecture. 
-- fibList accepts a number n as parameter and outputs a list of the numbers in the
-- Fibonacci series up to n. Note that fibList will use a list comprehension involving fib.
fib :: Int -> Int
-- two base cases
fib 0 = 0
fib 1 = 1
-- recursive call
fib n = fib (n-1) + fib (n - 2)
-- fibList using fib in a list comprehension
fibList :: Int-> [Int]
fibList n = map fib[1..n]


-- Problem 3: Write a function justHighScores that takes the list generated as output 
-- of the gradeBook function and returns a list of students who score >= 95. 
-- Please use the isHighScorer function from today's lecture in justHighScores. 
-- You will also have to implement the gradeBook function discussed in class today.
students = ["Andy", "Beatrice", "Carlos", "David", "Eunice"]
grades = [95, 92, 83, 95, 81]
-- create a tuple of students and grades
gradebook ss gs = zip students grades
-- obtain the tuple with the high grade
isHighScorer :: (Ord a, Integral a)=>([Char], a) -> Bool 
isHighScorer (n, g) = g >= 95
-- lists all tuples with high scores
justHighScores :: (Ord a, Integral a)=>[([Char], a)] -> [([Char], a)]
justHighScores ss = [s | s <- ss, isHighScorer s]


-- Problem 4: Modify the function lastElement from today's lecture to getSecondLast. 
-- The function getSecondLast returns the second last element from a list. The list
--  may have numbers or characters.
-- if the list is empty then return error
lastElement [] = error "Called last on empty list"
-- if there are only two elements left in the list then return second to last
lastElement (x:y:[]) = x
-- while there are more than 2 elements, recurse until two items are left in the list
lastElement (x:xs) = lastElement xs

