
# 1.  reverse of a string
# company = "cybrosys"
# reverse ="". join(reversed(company))
# print(reverse)
# ---------------------------------------------------------------
# 2. To check the number is prime or not

# num = int(input("Enter a number : "))
# if num <= 0:
#     print("Number is not a prime number")
# for i in range(2,int(num**0.5),+1):
#     if i % 2 ==0:
#         print("number is not a prime number")
#         break
# else:
#     print("it is a prime number")
# -----------------------------------------------------------
# 3 . fibonacci series up to n

# n = int(input("Enter the number of terms: "))

# a, b = 0, 1
# count = 0

# if n <= 0:
#     print("Please enter a positive integer")
# elif n == 1:
#     print("Fibonacci sequence:")
#     print(a)
# else:
#     print("Fibonacci sequence:")
#     while count < n:
#         print(a, end=" ")
#         a, b = b, a + b
#         count += 1
# --------------------------------------------------
# 4. check if a string is palindrome

# string = input("enter a string : ")

# reversed_string = "".join(reversed(string))

# if string == reversed_string :

#     print(reversed_string ,"is palimdrome")

# else:

#     print("it is not palindome")

# ----------------------------------------------------

# 5. count frequency of character in a string
string = "bvvdhhhdds"
freq = {}

for word in string:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print(freq) 