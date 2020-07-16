import os
from bs4 import BeautifulSoup


my_dir = os.path.dirname(__file__)
file = open(my_dir + '/words.xml')

soup = BeautifulSoup(file, 'html.parser')

words = []

for t in soup.find_all('title'):
    title = t.text.strip()
    word = title.split(' ')[0]
    if len(word) < 2: continue
    words.append(word)

def search(query):
    for s in soup.select('section > section'):
        title = s.find('title').text.strip()
        if query.title() in title:
            for p in s.select('p'):
                    print(p.text)
            print()
        else:
            continue

def start_search():
    while True:
        query = input('Введите слово для поиска: ')
        if query == 'q':
            print('До свидания!')
            break
        search(query)

try:
    print('Добро пожаловать в Словарь!')
    q = input('Начать поиск (1) или смотреть слова (2): ')

    if q == '1':
        start_search()
    elif q == '2':
        print('Список слов')
        print(' '.join(words))
        start_search()
    else: print('Неверный ввод')
except KeyboardInterrupt:
    print('Прервано пользователем')
