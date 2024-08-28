binary_num = list(map(int, input().split(",")))

result = []
for num in binary_num:
    num = str(num)
    int_val = int(num,2)
    if(int_val % 5 == 0):
        result.append(num)
        
print(", ".join(str(value) for value in result))