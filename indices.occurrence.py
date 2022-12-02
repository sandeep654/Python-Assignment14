#Write a Python script to print indices of all occurrences of a given element in a given list
Li=[eval(x) for x in input("Enter a list").split(',')]
element=int(input("Enter element number: "))
index=0
while index<len(Li):
    if Li[index]==element:
        print(index,end=' ')
    index+=1
print(Li)