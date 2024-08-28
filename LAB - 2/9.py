m1 = int(input("Enter marks for t1 : "))
m2 = int(input("Enter marks for t2 : "))
m3 = int(input("Enter marks for t3 : "))

marks = sorted([m1,m2,m3])

avg = (marks[1] + marks[2]) / 2

print("Avg of best two test marks out of three test's marks is :",avg)