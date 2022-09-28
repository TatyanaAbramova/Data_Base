data = {
    0: {'name': 'Ilya', 'surname': 'Aleksandrov', 'birthday': '01.11.2001', 'class': '11'},
    1: {'name': 'Sasha', 'surname': 'Pavlov', 'birthday': '02.05.2001', 'class': '11'},
    2: {'name': 'Kolya', 'surname': 'Petrov', 'birthday': '16.06.2001', 'class': '11'},
    3: {'name': 'Marina', 'surname': 'Lanova', 'birthday': '24.10.2001', 'class': '10'}
}

# _________________________сортировка по алфавиту без метода___________________________


sorted_keys = sorted(data, key=lambda x: (data[x]['surname']))


for i in sorted_keys:
    sorted_keys = dict.fromkeys(sorted_keys)
    
    print(data[i])

#__________________Вывод учеников определенного класса_________________________________________________________


n = '11'  # 


def sotr_value(data):
    new_dict = {key: value for key,
                value in data.items() if value['class'] == n}
    return new_dict


print(sotr_value(data))


