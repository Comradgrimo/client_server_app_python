# Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных данных из файлов
# info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV.
import re
import csv
import json
import datetime
import yaml

def get_data():
    strings  = ['Изготовитель системы',  'Название ОС', 'Код продукта', 'Тип системы']
    os_prod_list =[]
    os_name_list =[]
    os_code_list =[]
    os_type_list =[]
    for i in range(3):
        with open(f'info_{i+1}.txt', encoding='windows-1251') as f:
            # print(f)
            for i in f:
                # print(i)
                for string in strings:
                    match = re.search(string, i)
                    # re.split(r'y', 'Analytics')
                    # result = re.findall(r'\w+$', string)
                    if match:
                        if string == strings [0]:
                            os_prod_list.append((re.search(r'\w+$', i)).group(0))
                        if string == strings [1]:
                            os_name_list.append((re.search(r'\w+\W+\w+\W+\w+\W+\w+\W+$', i)).group(0))
                        if string == strings [2]:
                            os_code_list.append((re.search(r'\w+\W+\w+\W+\w+\W+\w+\W+$', i)).group(0))
                        if string == strings [3]:
                            os_type_list.append((re.search(r'\w+\W+\w+\W+\w+\W+$', i)).group(0))
    os_name_list = [line.rstrip() for line in os_name_list]
    os_code_list = [line.rstrip() for line in os_code_list]
    os_type_list = [line.rstrip() for line in os_type_list]
    main_data=[]
    print(strings)
    print(os_prod_list)
    # print(os_name_list)
    # print(os_code_list)
    # print(os_type_list)
    # print(main_data)
    for i in range(2):
        main_data[i] = [strings,os_prod_list[i],os_name_list[i],os_code_list[i],os_type_list[i] ]
    return main_data
# get_data()
# data = [['hostname', 'vendor', 'model', 'location'],
#         ['kp1', 'Cisco', '2960', 'Moscow, str'],
#         ['kp2', 'Cisco', '2960', 'Novosibirsk, str'],
#         ['kp3', 'Cisco', '2960', 'Kazan, str'],
#         ['kp4', 'Cisco', '2960', 'Tomsk, str']]
def write_to_csv():
    foo = get_data()
    with open('report.csv', 'w') as f_n:
        f_n_writer = csv.writer(f_n, quoting=csv.QUOTE_NONNUMERIC)
        for row in foo:
            f_n_writer.writerow(row)

    with open('report.csv') as f_n:
        print(f_n.read())

write_to_csv()

# Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах. Написать
# скрипт, автоматизирующий его заполнение данными

def write_order_to_json(item, quantity, price, buyer,date):
    dict_to_json = {
        'item': item,
        "quantity": quantity,
        "price": price,
        "buyer": buyer,
        "date": date
    }
    with open('orders.json', 'w') as f_n:
        json.dump(dict_to_json, f_n, sort_keys=True, indent=2, ensure_ascii=False)

    with open('orders.json') as f_n:
        print(f_n.read())

now = datetime.datetime.today().strftime("%m/%d/%Y")
write_order_to_json('Булка',10,30,'Иванов',now)

# Задание на закрепление знаний по модулю yaml. Написать скрипт, автоматизирующий сохранение данных в файле YAML-формата
def write_to_yaml():
    my_dist = {
        1: ['test'],
        2: 10,
        3: {'©': ['test','test'],'€':2,'®':3}
    }
    # print(my_dist)
    with open('file.yaml', 'w') as f_n:
        yaml.dump(my_dist, f_n, default_flow_style=False, allow_unicode = True)

    with open('file.yaml') as f_n:
        print(f_n.read())

write_to_yaml()