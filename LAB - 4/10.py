tuple_list = [(15, 6), (16, 7), (16, 8), (16, 10), (17, 13)]

dict_ = {}
for item in tuple_list:
    if item[0] not in dict_:
        dict_[item[0]] = list(item)
    else:
        dict_[item[0]].extend(item[1:])

result_list = []
for values in dict_.values():
    result_list.append(tuple(values))

print(result_list)
