num = input("Enter a value : ")
num_reverse = num[::-1]

if(num == num_reverse):
    print("Palindrome")
else:
    print("Not a palindrome")
    
num_list = list(num)
num_set = set(num)

for char in num_set:
    print(str(char) + " appears " + str(num_list.count(char)) + " times")