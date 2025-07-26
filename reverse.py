
# 1.  reverse of a string
# company = "cybrosys"
# reverse ="". join(reversed(company))
# print(reverse)

# 2. To check the number is prime or not

num = int(input("Enter a number : "))
if num <= 0:
    print("Number is not a prime number")
for i in range(2,int(num**0.5),+1):
    if i % 2 ==0:
        print("number is not a prime number")
        break
else:
    print("it is a prime number")