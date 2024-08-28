C, H = 50, 30 
d_list = list(map(int, input().split(",")))
result = []
for D in d_list:
    Q = ((2 * C * D ) / H ) ** 0.5
    result.append(round(Q))
    
print(", ".join(str(num) for num in result))
