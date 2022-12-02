#Write a Python script to print distinct elements along with their frequencies of
#occurrence in the list.
Li=[eval(x) for x in input("Enter a list").split(',')]
element=int(input("Enter element number: "))
index=0
s=0
while index<len(Li):
    if Li[index]==element:
        s=s+1
    index+=1
print(s)