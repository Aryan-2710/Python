for num in range(1,20):
    count = 0
    for i in range(1,num//2+1):
        if(num % i == 0):
            count += 1 
    if(count == 1):
        print(num, end = " ")