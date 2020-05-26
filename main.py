class Goods:
    def __init__(self, name, article_number, category, color, quantity, price):
        self.name = name
        self.article_number = article_number
        self.category = category
        self.color = color
        self.quantity = quantity
        self.__price = price

    def color_info(self):
        colors = {'красный': 'red', ' жёлтый': 'yellow', 'синий': 'blue', 'зелёный': 'green', 'коричневый': 'brown',
                  'чёрный': 'black', 'белый': 'white', 'фиолетовый': 'purple'}

        if self.color not in colors.keys():
            return 'Цвет введен неправильно или не указан'
        else:
            return self.color

    def amount(self):
        return int(self.quantity) * int(self.__price)

    def vat(self):
        return str(int(self.amount()) + (int(self.amount()) / 100 * 10))

    def __str__(self):

        s = '\n' + '| 1. | Название товара        | ' + self.name + '\n'
        s += '| 2. | Артикл                 | ' + self.article_number + '\n'
        s += '| 3. | Категория товара       | ' + self.category + '\n'
        s += '| 4. | Цвет                   | ' + self.color_info() + '\n'
        s += '| 5. | Количество             | ' + self.quantity + '\n'
        s += '| 6. | Цена  1x               | ' + self.__price + '\n'
        s += '| 6. | Цена за указ. кол - во | ' + str(self.amount()) + '\n'
        s += '| 7. | Цена c учетом НДС      | ' + self.vat() + '\n'

        return s

    def __repr__(self):
        return self.__str__()

class Shop:
    @staticmethod
    def count(x):
        summ = 0
        for i in x:
            summ += i
        return summ

    def __init__(self, amount,  file_name, articles):
        self.amount = amount
        self.file_name = file_name
        self.sum_amount = Shop.count(self.amount)
        self.articles = articles
        self.__articlee = None

    article = property()

    @article.setter
    def article(self, value):
        if isinstance(value, str):
            self.__articlee = value
        else:
            raise (ValueError)

    @article.getter
    def article(self):
        if self.__articlee in self.articles:
            index = self.articles.index(self.__articlee)
            self.articles.remove(self.__articlee)
            self.amount.pop(int(index))
            f = open(self.file_name, "r")
            lines = f.readlines()
            f.close()
            f = open(self.file_name, "w")
            for line in lines:
                if line != '| 2. | Артикл                 | ' + self.__articlee + '\n':
                    f.write(line)
        else:
            return 'Артикл не найден\n'



    def __str__(self):
        s = 'Текущая стоимость покупки {}'.format(self.sum_amount)
        return s


    def __repr__(self):
        return self.__str__()