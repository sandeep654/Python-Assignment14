#Write a Python script to create a list of first N even natural numbers.
num=int(input("Enter N number: "))
l1=[x for x in range(2,(num*2)+1,2)]
print(l1)