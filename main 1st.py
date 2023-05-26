"""a = input('enter your name:')
print('my name is ' , a)
a = input('enter you 1st number')
b = input('enter you 2st number')
print(int(a)+int(b))

name = 'waheed'
print (name[-4:-2])
print (name[1])
print (name.replace('waheed','champ'))
print (len(name.center(50)))
for char in name:
    print(char)
nc = 'waheed ho tar ma to kon ha ma be aya aja to be ma '
print(nc.find('ho'))
a = int(input('enter your age: '))
print('your age is :  ' , a)

print(a==18)
print(a<18)
print(a>18)
print(a<=18)
print(a!=8)

if(a>18):
    print('you can drive')
else:
    print('you can drive')
    
x = int(input('enter the value of x'))
match x:
       # if x is 0    
    case 0:
           print('x is zero')
    case 4:
            print('x is 4')

for i in range(3):
    print(i)
    
i = 0 
while(i<39):
    i = int(input('Enter your number'))
     int(i)
print('done with loop') 

count = 5
while (count > 0):
    print(count)
    count = count -1
    
colors = ['Red', 'Green', 'Blue', 'Yellow']
for color in colors:
    print(color)
    for i in color:
        print(i)
        
for k in range(1 , 20000):
    print(k)
"""
# def average(a=9, b=1):
#     print('The average is', (a+b)/2)
    
# average(a=1 ,b=65)
# def averages(*numbers):
    
#     sum= 0
#     for i in numbers:
#         sum= sum + i
#     print('Average is :' , sum/len(numbers))
        
# averages(6,7,3,4,5)
# def square(n):
#     print(n**2)
# square(98)

# def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n * factorial(n-1)
# print(factorial(3))
# print(factorial(2))
# print(factorial(8))
# print(factorial(6))
# s1 = {1,2,5,6}
# s2 = {3,6,7,}
# print(s1.union(s2))
# s1.update(s2)
# print(s1,s2)

# dic = {
#     "Waheed": "Human being" ,
#     "Spoon" : "Object"    
# }

# print(dic['Waheed'])

# dic.clear()
# for i in range(5):
#     print(i)
# else:
#     print("Sorry no i")

# a = input("Enter the number: ")
# print(f"Multipliciation table of {a} is:")

# for i in range(1, 11):
#     print(f"{int(a)} X {i} = {int(a)*i}")
# except :
#     print(e)
    
# print ("Some imp lines of code")
# print("End of program")
# a = int(input("Enter any value between  5 and 8"))
# if (a<5 or a>8):
#     raise ValueError("Value should be between 5 and 8")
# a = 330
# b = 3303
# print("A") if a > b else print("=") if a==b else print("B")
