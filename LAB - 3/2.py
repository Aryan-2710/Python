Aryan = input("Enter the birthdate: ")
Raj = input("Enter the birthdate: ")

result1 =  Aryan.split("-")
result2 = Raj.split("-")

Aryan = {
"Year" : result1[2],
"Month": result1[1],
"Date" : result1[0]
}

Raj = {
"Year": result2[2],
"Month": result2[1],
"Date" : result2[0]
}

print("Aryan is born on :",Aryan) 
print("Raj is born on ",Raj)
print()
print("Aryan turns ",2024-int(Aryan [ "Year"])," years on the date",Aryan [ "Date"],Aryan [ "Month"],2024)
print("Raj turns ",2024-int(Raj["Year"])," years on the date",Raj["Date"],Raj["Month"],2024)