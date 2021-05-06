# Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных данных из файлов
# info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV.
import re
import csv
import json
import datetime
import yaml


def get_data():
    strings = ['Изготовитель системы',
               'Название ОС', 'Код продукта', 'Тип системы']
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    main_data = [strings]
    for i in range(3):
        with open(f'info_{i+1}.txt', encoding='windows-1251') as f:
            for line in f:
                match1 = re.search(strings[0], line)
                match2 = re.search(strings[1], line)
                match3 = re.search(strings[2], line)
                match4 = re.search(strings[3], line)
                if match1:
                    result = (re.search(r'\w+$', line)).group(0)
                    os_prod_list.append(result.rstrip())
                if match2:
                    result = (
                        re.search(r'\w+\W+\w+\W+\w+\W+\w+\W+$', line)).group(0)
                    os_name_list.append(result.rstrip())
                if match3:
                    result = (
                        re.search(r'\w+\W+\w+\W+\w+\W+\w+\W+$', line)).group(0)
                    os_code_list.append(result.rstrip())
                if match4:
                    result = (re.search(r'\w+\W+\w+\W+\w+\W+$', line)).group(0)
                    os_type_list.append(result.rstrip())
    for i in range(2):
        main_data.append([os_prod_list[i], os_name_list[i],
                         os_code_list[i], os_type_list[i]])
    return main_data


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


def write_order_to_json(item, quantity, price, buyer, date):
    dict_to_json = {
        'item': item,
        'quantity': quantity,
        'price': price,
        'buyer': buyer,
        'date': date
    }
    with open('orders.json', 'w') as f_n:
        json.dump(dict_to_json, f_n, sort_keys=True,
                  indent=2, ensure_ascii=False)

    with open('orders.json') as f_n:
        print(f_n.read())


now = datetime.datetime.today().strftime('%m/%d/%Y')
write_order_to_json('Булка', 10, 30, 'Иванов', now)

# Задание на закрепление знаний по модулю yaml. Написать скрипт, автоматизирующий сохранение данных в файле YAML-формата


def write_to_yaml():
    my_dist = {
        1: ['test'],
        2: 10,
        3: {'©': ['test', 'test'], '€': 2, '®': 3}
    }
    # print(my_dist)
    with open('file.yaml', 'w') as f_n:
        yaml.dump(my_dist, f_n, default_flow_style=False, allow_unicode=True)

    with open('file.yaml') as f_n:
        print(f_n.read())


write_to_yaml()
