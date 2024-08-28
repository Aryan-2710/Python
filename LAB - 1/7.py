str1 = input("Enter the 1st string : ")
str2 = input("Enter the 2nd string : ")

res1 = str2[:2] + str1[2:]
res2 = str1[:2] + str2[2:]

print("Result : " + res1 + " " + res2)