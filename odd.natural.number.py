#Write a Python script to create a list of first N odd natural numbers.
num=int(input("Enter N number: "))
l1=[x for x in range(1,num*2,2)]
print(l1)