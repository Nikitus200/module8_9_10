from threading import Thread
from time import sleep
class Knight(Thread):
    def __init__(self, name, power):
        self.name_ = name
        self.power_ = int(power)
        super().__init__()

    def run(self):
        print(f"{self.name_}, на нас напали!")
        self.c = 0
        self.enemys = 100
        while True:
            self.enemys -= self.power_
            sleep(1)
            if self.enemys < 0:
                print(f"{self.name_} одержал победу спустя {self.c} дней(дня)!")
                break
            else:
                self.c += 1
                print(f"{self.name_} сражается {self.c} дней(дня, день)..., осталось {self.enemys} воинов.")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
print("Все битвы закончились!")


