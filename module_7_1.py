from operator import concat
from pprint import pprint

class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
       file = open(self.__file_name, 'r')
       rezult = file.read()
       file.close()
       return rezult

    def add(self, *products):
        file = self.get_products()

        for value in products:
            if (value.name in str(file)):
                print(f'Продукт {value.name} уже есть в магазине')
            else:
                file2 = open(self.__file_name, 'a')
                file2.write(value.__str__() + '\n')
                file2.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())



