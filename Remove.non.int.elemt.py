#Write a Python script to remove all non int values from a list.
l1=['110','34','67','89.9','99','100.2',"sandeep"]
y=[x for x in l1 if x.isnumeric() ]
print(y)