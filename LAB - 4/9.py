string = list(input().split())

string.sort()

result = {}

for char in string:
    if(char not in result):
        result[char] = 1 
    else:
        result[char] += 1 
        
for char in result:
    print(f"{char} : {result[char]}")