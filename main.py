class Restaurant:
    def __init__(self, name, tables):
        self.name = name
        self.__tables = tables

    def get_tables(self):
        return self.__tables

    def set_tables(self, new_tables):
        self.__tables = new_tables


r1 = Restaurant('Oqtepa Lavash', 25)

print(r1.name)
print(r1.get_tables())

r1.set_tables(40)

print(r1.get_tables())
