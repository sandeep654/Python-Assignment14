#Write a Python script to find the greatest number in a given list of numbers.
x=[10,87,80,90,67,1001]
greatest_number=x[0]
for e in x:
    if e>greatest_number:
        greatest_number=e
print(greatest_number)