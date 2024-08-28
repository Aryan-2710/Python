test_list = [[5, 6], [4, 7, 10, 17]]

output = []
for sub_list in test_list:
    for element in sub_list:
        output.append((element,))
        
print(output)