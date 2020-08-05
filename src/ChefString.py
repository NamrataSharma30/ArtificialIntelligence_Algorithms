number_of_pairs = 0
str_list_of_lists = []
str_list = []
temp = 0
T = int(input())
for _ in range(T):
    str_ = list(input().split("\n"))
    str_list_of_lists.append(str_)

for i in range(len(str_list_of_lists)):
    str_list = str_list_of_lists[i]
    current_str_length = len(str_list[0])
    if temp < i:
        number_of_pairs = 0
    for j in range(current_str_length):
        temp = i
        if str_list[0][j] == 'x' and str_list[0][j+1] == 'y':
            number_of_pairs = number_of_pairs + 1
    print(number_of_pairs)
