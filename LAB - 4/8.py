x, y = 0, 0 

N = int(input("Enter the steps : "))

for i in range(N):
    steps = input().split()
    if(steps[0] == "UP"):
        y +=  int(steps[1])
    elif(steps[0] == "DOWN"):
        y -=  int(steps[1]) 
    elif(steps[0] == "LEFT"):
        x  -=  int(steps[1]) 
    else:
        x +=  int(steps[1]) 

new_x , new_y = x , y 

distance =  (new_x ** 2 + new_y ** 2) ** 0.5 

print("\nDistance from origin :",round(distance))

