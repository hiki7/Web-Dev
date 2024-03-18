def or_value (first_num, second_num):
    if first_num or second_num:
        return 1
    return 0

first_num = int(input())
second_num = int(input())

print(or_value(first_num, second_num))