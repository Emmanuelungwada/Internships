#!/usr/bin/env python
# coding: utf-8

# MACHINE LEARNING
# ANSWERS TO THE QUESTIONS ARE SHOWN BELOW:
# 
# 1.	A) Least Square Error
# 2.	A) Linear regression is sensitive to outliers 
# 3.	B) Negative 
# 4.	C) Both of them
# 5.	A) High bias and high variance 
# 6.	A) Descriptive model 
# 7.	D) Regularization 
# 8.	A) Cross validation
# 9.	C) Sensitivity and Specificity
# 10.	A) True 
# 11.	B) Apply PCA to project high dimensional data 
# 12.	B) It becomes slow when number of features is very large. 
#                 C) We need to iterate.
# 
# 
# 
# 
# B SECTION
# 13.	Explain the term regularization? 
# Answer:
# Regularization refers to strategies which are used to calibrate machine learning models to limit the adjusted loss feature and save you overfitting or underfitting.  Also, regularization in machine learning, refers to a set of techniques that help the machine to learn more than just memorize.
# 
# 14.	Which particular algorithms are used for regularization?
# Answer:
# 
# There are three main regularization techniques, namely: Ridge Regression (L2 Norm) Lasso (L1 Norm) Dropout.
# 
# 15.	Explain the term error present in linear regression equation? 
# 
# 
# The error time period is the distinction among the expected rate at a specific time and the price that changed into simply observed.
# 
# 

# In[ ]:





# In[ ]:





# # PYTHON – WORKSHEET 1
#       ANSWERS
# 
# 1.	C) % 
# 2.	B) 0 
# 3.	C) 24 
# 4.	A) 2 
# 5.	D) 6 
# 6.	B) It encloses the lines of code which will be executed if any error occurs while executing the lines of code in 
# the try block. 
# 7.	A) It is used to raise an exception.
# 8.	C) in defining a generator
# 9.	B) 1abc 
#     C) abc2
# 10.	A) yield
# 	B) raise
# 

# # Programming questions.
#       ANSWERS

# 11. 
# 
# #Factorials are a higher level math operation that can be difficult to 
# digest all in one go. The best solution in programming problems like this,
# is to break down one large task into smaller tasks#
# 

# In[12]:


import math
math.factorial(10)


# In[11]:


def factorial(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact


# In[ ]:





# Question 12.
# Write a python program to find whether a number is prime or composite

# In[ ]:


n=int(input())
for m in range(1,n):
       
    if n==6*m+1 or n==6*m-1:
        print("Cannot be determined")
    else:
        print("Composite number")
    break


# In[ ]:





# # OR

# In[ ]:


def prime(x):
    """To generate prime number"""
    a = x // 2 + 1
    for i in range(2, x):
        if x % i == 0:
            return False
        elif i == a:
            return True


def gap(p, q, m):
    """To generate gap in between two prime numbers"""
"""p is the difference,q is the lower limit where the list of numbers in between which prime is filtered,m is the upper limit"""
    b = []
    a = b.append
    c = prime
    q = (q // 2) * 2 + 1
    for i in range(q, m + 1, 2):
        if c(i) == True:
            a(i)
            if len(b) > 1:
                if b[-1] - b[-2] == p:
                    return [b[-2], b[-1]]


# Question 13
# Write a python program to check whether a given string is palindrome or not

# In[ ]:


# function to check string is
# palindrome or not
def isPalindrome(str):
 
    # Run loop from 0 to len/2
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True
 
# main function
s = "malayalam"
ans = isPalindrome(s)
 
if (ans):
    print("Yes")
else:
    print("No")


# In[ ]:





# Question 14.
# Write a Python program to get the third side of right-angled triangle from two 
# given sides

# In[ ]:


def pythagoras(opposite_side,adjacent_side,hypotenuse):
        if opposite_side == str("x"):
            return ("Opposite = " + str(((hypotenuse**2) - (adjacent_side**2))**0.5))
        elif adjacent_side == str("x"):
            return ("Adjacent = " + str(((hypotenuse**2) - (opposite_side**2))**0.5))
        elif hypotenuse == str("x"):
            return ("Hypotenuse = " + str(((opposite_side**2) + (adjacent_side**2))**0.5))
        else:
            return "You know the answer!"
    
print(pythagoras(3,4,'x'))
print(pythagoras(3,'x',5))
print(pythagoras('x',4,5))
print(pythagoras(3,4,5))


# In[ ]:





# Question 15.
#  Write a python program to print the frequency of each of the characters present in a given string.

# In[ ]:


def most_common_letter():
    string = str(input())
    letters = set(string)
    if " " in letters:         # If you want to count spaces too, ignore this if-statement
        letters.remove(" ")
    max_count = 0
    freq_letter = []
    for letter in letters:
        count = 0
        for char in string:
            if char == letter:
                count += 1
        if count == max_count:
            max_count = count
            freq_letter.append(letter)
        if count > max_count:
            max_count = count
            freq_letter.clear()
            freq_letter.append(letter)
    return freq_letter, max_count


# In[ ]:





# # STATISTICS WORKSHEET-1

# 1. a) True
# 2. a) Central Limit Theorem
# 3. b) Modeling bounded count data
# 4. c) The square of a standard normal random variable follows what is called chi-squared 
#       distribution
# 5. c) Poisson
# 6. b) False
# 7. b) Hypothesis
# 8. a) 0
# 9. d) None of the mentioned
# 
# 
# 

# # SECTION 2
# 
#         ANSWERS
# 
# 10. 
# 
# Is a probability distribution that is symmetric about the mean, showing that data near the mean are more frequent in occurrence than data far from the mean.
# 
# Also, A normal distribution is an arrangement of a data set in which most values cluster in the middle of the range and the rest taper off symmetrically toward either extreme.
# 
# 11. 
# 
# -Deletions. Pairwise Deletion. Listwise Deletion/ Dropping rows. Dropping complete columns.
# -Basic Imputation Techniques. Imputation with a constant value. Imputation using the statistics (mean, median, mode)
# -K-Nearest Neighbor Imputation.
# 
# 
# I recommend the following tecnique:
# 
# Cold deck imputation.
# Regression imputation. 
# Stochastic regression imputation.
# 
# 12. 
# A/B testing, also known as split testing, refers to a randomized experimentation process wherein two or more versions of a variable.
# 
# 13. 
# Mean imputation is typically considered terrible practice since it ignores feature correlation.
# 
# 14.
# Linear regression attempts to model the relationship between two variables by fitting a linear equation to observed data.
# 
# 15.
# There are three real branches of statistics: data collection, descriptive statistics and inferential statistics.

# In[ ]:




