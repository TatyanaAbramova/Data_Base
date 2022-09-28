import r_w_file
import action_table

def init(source_tabl,path_tabl):
    global source
    source = source_tabl
    global path
    path = path_tabl

def distribution(key_func):
    if (key_func == '1'): action_table.output_all(source)
    elif (key_func == '2'): r_w_file.append_info(source,path)
    elif (key_func == '3'): r_w_file.del_info(source, path)
    elif (key_func == '4'): print(action_table.sort_num_class(path))
    elif (key_func == '5'): print(action_table.sort_abc(source))
    elif (key_func == '6'): print('Всего хорошего!')
    else: print('Введите корректное число')




