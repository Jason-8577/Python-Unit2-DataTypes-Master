""" homework = True

def not_movies(homework):
    if not homework:
        print("movie time")
    else:
        print("homework time, I hate russian")
not_movies(homework) """

""" a = int('5')
bill = input("How much was the bill?")
print(int(bill))  """ 

""" def factor(x,y):
    if x % y == 0:
        print(f"{y} is a factor of {x}")
factor(20,5)
 """

""" factor = input("what is the number?")
if factor == "10":
    print("1,2,5,10") """

""" def number(x):
    if x % 2 == 0:
        print(f"{x} is even")
    else:
        print(f"{x} is odd")
x=3  """

""" service = input("Was the service good?")
bills = 10
if service == "bad":
    x = bills*1
elif service == "okay":
    x = bills*1.15
elif service == "good":
    x = bills * 1.2
else:
    x = bills * 1.25
Total = x
print(Total) """


""" def greatest_factor(num1,num2):
    smaller = min(num1, num2) 
    gcf = 1
    for i in range(1, smaller + 1):
        if num1 % i == 0 and num2 % i == 0: 
            gcf = i
    return gcf
num1 = 10
num2 = 100
print("The gcf of", num1, "and", num2, "is", greatest_factor(num1,num2))     """