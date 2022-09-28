
def output_all(source):
    for i in source:
        print(f'{i} {source[i]["name"]} {source[i]["surname"]} {source[i]["class"]}', end='')
        print()

def sort_num_class(data):
    a = input('Введите номер класса: ')
    sup_str = ''
    file = open(data, 'r')
    for line in file:
        arr = line.split()
        if arr[3] == a:
            sup_str += (f'{arr[0]} {arr[1]} {arr[2]} \n')
    if (sup_str == ''): return 'В этом классе нет учеников'
    else: return sup_str

def sort_abc(source):
    result = []
    sup_str = ''
    for i in source:
        result.append(f'{source[i]["surname"]} {source[i]["name"]} id - {i}')
    result.sort()
    for i in result:
        sup_str += f'{i} \n'
    return sup_str


# Дополнительный метод для сортировки по классу, работает с переменной, хранящей таблицу
def sort_class(source):
    num_class = input('Введите номер класса: ')
    sup_str =''
    for i in source:
        if (source[i]["class"] == str(num_class)):
            sup_str += (f'{i} {source[i]["surname"]} {source[i]["name"]} - {source[i]["class"]} \n')
    if (sup_str == ''): return 'В этом классе нет учеников'
    else: return sup_str
