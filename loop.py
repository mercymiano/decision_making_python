#if statement
x = 5
y = 7
if (x < y):
   print ("x is less")
print("y is greater")

#prompting a number and decicing if it is an even or odd number
print ("enter a number")
a = int(input())
if  a % 2 == 0:
    print("is an even number")
else:
    print("is an odd number")

 # Grading system
print("enter marks")
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

total = a+b+c+d+e
avg = (a+b+c+d+e)/5
print ( total)
print ( avg)

if avg >= 70 and avg <=100:
    print("Grade A")
elif avg >= 60 and avg <=69:
    print("Grade B")
elif avg >=50 and avg <=59:
    print("Grade c")
elif avg >=40 and avg <= 49:
    print("Grade D") 
else:
    print('Grade E')           

   
 


