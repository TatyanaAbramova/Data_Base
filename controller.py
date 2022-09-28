import knot
import r_w_file
import view

def start():
    path_txt = input('Название файла с которым вы хотите работать: ')
    data = r_w_file.read_file(f'{path_txt}')
    number = ''
    while (number != '6'):
        number = view.get_request()
        knot.init(data, path_txt)
        knot.distribution(number)
        print()






