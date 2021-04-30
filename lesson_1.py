# 1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить тип и содержание
# соответствующих переменных. Затем с помощью онлайн-конвертера преобразовать строковые представление в формат Unicode
# и также проверить тип и содержимое переменных.
def task_1():
    words = ['разработка', 'сокет', 'декоратор']
    for i in words:
        print(i.encode('utf-8'))


task_1()
# 2. Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность кодов
# (не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.


def task_2():
    words = [b'class', b'function', b'method']
    for i in words:
        print(i)
        print(type(i))
        print(len(i))


task_2()

# 3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.


def task_3():
    words = ['attribute', 'класс', 'функция', 'type']
    for i in words:
        try:
            print(i.encode('ascii'))
        except UnicodeEncodeError:
            print('Это слово невозможно записать в байтовом виде')


task_3()
# 4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в
# байтовое и выполнить обратное преобразование (используя методы encode и decode).


def task_4():
    words = ['разработка', 'администрирование', 'protocol', 'standard']
    encode_words = []
    decode_words = []
    for i in range(len(words)):
        encode_words.append(words[i].encode('utf-8'))
        print(encode_words[i])
    for i in range(len(encode_words)):
        decode_words.append((encode_words[i].decode('utf-8')))
        print(decode_words[i])


task_4()
# 5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового в строковый тип на
# кириллице.


def task_5(foo):
    import subprocess
    i = 0
    subproc_ping = subprocess.Popen(foo, stdout=subprocess.PIPE)
    for line in subproc_ping.stdout:
        i += 1
        line = line.decode('cp866').encode('utf-8')
        print(line.decode('utf-8'))
        if i == 5:
            subproc_ping.kill()


# task_5(['ping', 'yandex.com'])
# task_5(['ping', 'youtube.com'])
# 6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет»,
# «декоратор». Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести его
# содержимое.
def task_6():
    with open('test_file.txt', 'w') as f_n:
        f_n.write('сетевое программирование\nсокет\nдекоратор')
    print(f_n)
    with open('test_file.txt', encoding='utf-8') as f_n:
        for el_str in f_n:
            print(el_str, end='')


task_6()
