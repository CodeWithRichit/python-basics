#Task 1,Check if a number is even or odd
Num=int(input("Number: "))
if (Num%2==0):
    print(Num,"is even")
else:
    print(Num,"is odd")
print("Thank you")
#Task 2,Sum of integers from 1 to 50 using a loop
total=0
for i in range(1,51):
    total+=i
    print("Sum of numbers from 1 to 50 is: ",total)
