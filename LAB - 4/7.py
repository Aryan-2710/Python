N = int(input("Enter the no. of inputs : "))
result = []
for i in range(N):
    A = input().split(",")
    result.append(A)
    
result.sort()
answer = []
for sub_list in result:
    sub_list = tuple(sub_list)
    answer.append(sub_list)

print()
print(answer)


