import threading
from random import randint
from time import  sleep
from queue import Queue
class Table:
    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest

class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self._name = name

    def run(self):
        sleep(randint(3, 10))

class Cafe:
    def __init__(self, *tables):
        self.table = tables
        self.queue = Queue()

    def guest_arrival(self, *guests):
        c = 0
        for i in range(len(self.table)):
            self.table[i].guest = guests[i]
            guests[i].start()
            print(f"{guests[i]._name} сел(-а) за стол номер {self.table[i].number}")
            c += 1
        if c < len(guests):
            for g in range(c, len(guests)):
                self.queue.put(guests[g])
                print(f"{guests[g]._name} в очереди")

    def discuss_guests(self):
        while not self.queue.empty() or any([table.guest for table in self.table]):
            for table in self.table:
                if table.guest is not None and not table.guest.is_alive():
                    print(f'{table.guest._name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None
                if not self.queue.empty() and table.guest is None:
                    table.guest = self.queue.get()
                    print(f'{table.guest._name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                    table.guest.start()








# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Viktoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()