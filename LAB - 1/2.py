import keyword 

all_keywords = keyword.kwlist
print("All Python Keywords : ")
i = 1 
for word in all_keywords:
    print("\t\t\t" + str(i) + ". " + word)
    i += 1