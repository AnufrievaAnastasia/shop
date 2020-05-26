from main import *

print('Добавьте товар в корзину \n'
      'Если вы хотите остановить запись, введите:  "EXIT" \n'
      'Вводите данные по образцу:\n'
      'Название, артикул, категория товара,цвет, количество, цена за штуку ')

key = True
key_2 = True
amount = []
articles = []
while key:
    try:
        number = input('Введите номер товара: ')
        name, article_number, category, color, quantity, price = input('Введите данные о товаре: \n').split(',')

        info = Goods(name, article_number, category, color, quantity, price)
        amount.append(float(info.vat()))
        articles.append(article_number)
        my_file = open("information3.txt", "a")
        my_file.write(str(number))
        my_file.write(str(info))

    except ValueError:
        print('Запись завершена.')
        key = False

while key_2:
    remove = input('Если Вы хотите удалить какой нибудь товар введите: ДА')
    if remove == 'ДА':
        article = input('Введите артикул товара: ')
        info_2 = Shop(amount, "information3.txt", articles)
        info_2.articlee = article

    else:
        key_2 = False
        info_2 = Shop(amount, "information3.txt", articles)
        my_file.write(str(info_2))