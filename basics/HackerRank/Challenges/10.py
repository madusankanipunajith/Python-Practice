from collections import Counter

name = list(str(input()))
name_count = Counter(name)
dict_name = dict(name_count)
# print(dict_name)
dict_name_key = sorted(dict_name.items())
final_dict_name = sorted(dict_name_key, key=lambda x: x[1], reverse=True)
print(dict_name_key)
# print(final_dict_name)

for i in range(3):
    print(final_dict_name[i][0], final_dict_name[i][1])



