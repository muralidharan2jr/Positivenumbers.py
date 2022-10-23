list1 = [12, -7, 5, 64, -14]
list2 = [12, 14, -95, 3]

new_nums = list(filter(lambda x: x >0, list1))
print("Positive numbers in the list1: ", new_nums)

new_nums = list(filter(lambda x: x >0, list2))
print("Positive numberd in the list2: ", new_nums)