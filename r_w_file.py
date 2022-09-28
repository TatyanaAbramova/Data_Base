import os.path

def write_file(source, path):
    file = open(path, 'w')
    sup_str = ''
    for i in source:
        sup_str += f'{i} {source[i]["name"]} {source[i]["surname"]} {source[i]["class"]}'
        file.writelines(f'{sup_str} \n')
        sup_str = ''
    file.close()
    return source


def read_file(path):
    result = {}
    if(os.path.lexists(path)):
        file = open(path, 'r')
        for line in file:
            sup_arr = line.split()
            result[sup_arr[0]] = {'name': sup_arr[1], 'surname': sup_arr[2], 'class': sup_arr[3]}
        file.close()
    else:
        file = open(path, 'a')
        file.writelines('')
        file.close()
    return result


def append_info(source, path):
    new_name = input('Введите Имя ')
    new_surname = input('Введите Фамилию ')
    new_class = input('Введите номер класса ')
    if os.stat(path).st_size == 0: index = 0
    else:
        index_list = list(map(lambda el:int(el),source))
        index = int(max(index_list))+1
    source[index] = {'name':new_name, 'surname': new_surname, 'class' : new_class}
    write_file(source, path)
    return source


def del_info(source, path):
    index = input('Введите индекс пользователя, которого необходимо удалить: ')
    del source[index]
    write_file(source, path)
    return source