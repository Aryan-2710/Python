num_list = list(map(int, input().split()))

n = len(num_list)

# mean :
mean = sum(num_list) / n 

# median : 
num_list.sort()
middle = n // 2
if(n % 2 == 0):
    median = (num_list[middle] + num_list[middle - 1]) / 2 
else:
    median = num_list[middle]
    
# mode :
largest = 0
num_set = set(num_list)
for num in num_set:
    if(num_list.count(num) >= largest):
        largest =  num_list.count(num)
        mode = num
        
print("Mean :",mean)
print("Median :",median)
print("Mode :",mode)        