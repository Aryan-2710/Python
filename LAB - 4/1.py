numbers = list(map(int, input().split()))
factorials = []
for num in numbers:
    result = 1
    while(num > 1):
        result *= num 
        num -= 1 
    factorials.append(result)
    
print(", ".join(str(n) for n in factorials))
