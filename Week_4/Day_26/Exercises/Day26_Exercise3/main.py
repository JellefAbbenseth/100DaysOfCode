def return_int_list(string_list):
    numbers = []
    for item in string_list:
        numbers.append(int(item.strip("\n")))
    return numbers


with open("file1.txt") as file1:
    list1 = file1.readlines()
    list1 = return_int_list(list1)

with open("file2.txt") as file2:
    list2 = file2.readlines()
    list2 = return_int_list(list2)

# print(list1)
# print(list2)

result = [num for num in list1 if num in list2]
# Better Solution:
# result = [int(num) for num in list1 if num in list2]

# Write your code above 👆

print(result)
