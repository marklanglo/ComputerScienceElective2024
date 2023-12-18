#==========================================
# Programmed By	: Mr. Wiedeman
# Date			: 12/11/2023
#==========================================

#====== Problem Name: Hello World =========
#     Description: Hello World is the first
# program many people will ever write. It's
# a great way to figure out how simple or
# difficult a coding language is based on how
# hard the "hello world" is for that
# language.
#
# Use the "print" function to write hello world for python.
#
# Syntax:
#        print("text string goes here")
#
#==========================================
def HelloWorld():
    
    print("Hello, World!")


#========== Problem Name: Mean ============
#     Description: The mean is the mathematical
# average of a group of numbers.  'numList'
# is a variable that holds many numbers in
# a list.  Using the below functions we want
# you to make the basic code for the mean function.
#
# Formula:
#        mean = ( sum of numbers ) / ( number of numbers )
#
#
# Hints:
#        'sum(my_number_list)' //this gives the sum of a list of numbers
#
#        'len(my_list)'        //this gives the number of things in a list
#
# Bonus:
#    If you finish this early, there is a way to complete this in 1
#    line of code.  If your's isn't already that short, see
#    if you can figure out how.
#==========================================

#Input/Output Examples:
#	Input: Mean((4, 6, 8))
#	Output: 6
#
#	Input: Mean((10, 15, 20, 25))
#	Output: 17.5
#
#	Input: Mean((-3, 0, 3, 6))
#	Output: 1.5

def Mean(num_list):
    
    return sum(num_list)/len(num_list)


#=======Problem: Count the Vowels==========
#     Description: For this problem you need
# to return the number of vowels for a given
# string.  A string is basically like a list
# but for characters (like numbers, letters,
# and symbols).
#
# Hints:
#
#        1. Here is the syntax for a list:
#            list = [ "a", "b", "c"]
#            list = [ 1, 2, 3]
#
#        2. You will need to create a variable
#        to store the number of vowels.
#
#        3. Here is the syntax for a for loop:
#
#            for element in list:    #this will make the code loop through every element in the list once
#                #code inside loop
#
#        4. Here is the syntax for a if-statement:
#
#            if condition:           #this checks the condition and will run the code below if the condition is met
#                #code inside statement
#
#
# Instructions:
#        1. Initialize your list of vowels and your "count" variable
#        2. Use a for loop to iterate through each letter in the input string,
#           and inside the loop, use an if-statement to check if the
#           lowercase version of the current letter is in the 'vowels' list:
#        3. Return the number of vowels
#        
#==========================================

# Input/Output Examples:
#   Input: CountTheVowels("Hello")
#   Output: 2
#
#   Input: CountTheVowels("Python Programming")
#   Output: 4
#
#   Input: CountTheVowels("Artificial Intelligence")
#   Output: 10

def CountTheVowels(string):
    
    vowels = ["a", "e", "i", "o", "u"]
    count = 0

    for letter in string:
        if letter.lower() in vowels:
            count += 1

    return count


#============Bonus Problems================
# These functions are challenge problems with no
# particular order in mind.  All of
# them are solvable with code and can be solved
# in many ways.  At least one function is provided
# per function that we considered could be useful
# for your solution.  We recommend you think about
# the logic of your solution before trying to write
# the code.  You should know what you want your
# code to do before you write it.

# =====Bonus Problem: Odd-Even Checker=======
# Difficulty: Easy
#
# Description: Write a function that takes an integer as input
# and returns "Even" if the number is even, and "Odd" otherwise.
#
# Hint:
#        You will need modulo (%) for this problem's solution
#
#==========================================

def OddEven(num):
    
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

#=======Bonus Problem: Reverse String=======
# Difficulty: Medium
#
# Description: Create a function that takes a string as input
# and returns the reverse of that string. For example, if the
# input is "python", the output should be "nohtyp".
#
# Relevant Python function:
#        reversed(), join()
#
#==========================================

def ReverseString(input_string):
    
    return ''.join(reversed(input_string))

#=====Bonus Problem: Prime Number Checker===
# Difficulty: Easy
#
# Description: Write a function that takes an integer as input
# and returns True if it's a prime number, and False otherwise.
# A prime number is a natural number greater than 1 that is not a
# product of two smaller natural numbers.
#
# Relevant Python function:
#        all(), range()
#
#==========================================

def IsPrime(number):
    
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# =====Bonus Problem: Sum of Digits=======
# Difficulty: Medium
#
# Description: Write a function that takes an integer as input
# and returns the sum of its digits using floor division.
#
# Example:
#    If the input is 123, the output should be 6 (1 + 2 + 3).
#
# Hint:
#        You can use modulo (%) and floor division (//) for this problem.
#
#==========================================

def SumDigits(num):
    
    sum = 0
    
    while num != 0:
        #adds ones place to sum
        sum = sum + (num % 10)
        #removes ones place from num
        num = num // 10
        
    return sum

#========Bonus Problem: Fibonacci Series====
# Difficulty: Hard
#
# Description: Create a function that generates the Fibonacci
# series up to a specified number of terms. The Fibonacci series
# is a series of numbers where each number is the sum of the two
# preceding ones, usually starting with 0 and 1.
#
# Relevant Python function:
#        yield, range()
#
#==========================================

def FibonacciSeries(n):

    #We initialize the fibonacci series to the first two values and set the index to 2
    fib_list = [0, 1]
    position_in_list = 2

    #We increment the list and add the previous two values together to append them
    while position_in_list <= n:
        fib_list.append(fib_list[position_in_list-1] + fib_list[position_in_list-2])
        position_in_list = position_in_list + 1
        
    return fib_list[n]
        

#========Bonus Problem: Word Frequency=========
# Difficulty: Hard
#
# Description: Write a function that takes a sentence as input
# and returns a dictionary containing the frequency of each word.
# Ignore case and punctuation. For example, if the input is
# "The cat in the hat, the cat is black.", the output should be
# {'the': 2, 'cat': 2, 'in': 1, 'hat': 1, 'is': 1, 'black': 1}.
#
# Relevant Python functions:
#        split(), lower(), strip()
#
#==========================================

def WordFrequency(sentence):
    # Initialize an empty dictionary to store word frequencies
    word_freq = {}

    # Split the sentence into words, remove punctuation, and convert to lowercase
    words = sentence.lower().split()

    # Remove punctuation from each word
    words = [word.strip(".,!?"')(') for word in words]

    # Count the frequency of each word
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    return word_freq

#==========================================


