string = input("Enter the string : ")
result = {}  

for char in string:
    if char in result:
        result[char] += 1  
    else:
        result[char] = 1 
 
print(result)
