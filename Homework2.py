dict_list = {}
len_list = []
with open ('1.txt', encoding='utf-8') as file_one:
    lines_one = file_one.readlines()
    length_one = len(lines_one)

with open ('2.txt', encoding='utf-8') as file_two:
    lines_two = file_two.readlines()
    length_two = len(lines_two)

with open ('3.txt', encoding='utf-8') as file_three:
    lines_three = file_three.readlines()
    length_three = len(lines_three)

len_list.append(length_one)
len_list.append(length_two)
len_list.append(length_three)
new_list = sorted(len_list)
# print(new_list)

dict_list ['1.txt'] = length_one
dict_list ['2.txt'] = length_two
dict_list ['3.txt'] = length_three
# print(dict_list)

with open ('finish.txt', 'a') as file_fourth:
    for all in new_list:
        for key, value in dict_list.items():
            if value == all:
                file_fourth.write(f'{key} \n')
                file_fourth.write(f'{str(all)} \n')
                with open (key, encoding='utf-8') as some_file:
                    lines = some_file.readlines()
                    for line in lines:
                        file_fourth.write(f'{str(line)} \n')

    
