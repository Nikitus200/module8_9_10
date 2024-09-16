def discuss_guests(self):
    c = 0
    for i in self.table:
        if i.guest is None:
            pass
        else:
            c += 1
    # Снизу ошибочный участок нужно исправить
    while self.queue.empty() == False and c >= 1:
        c = 0
        for i in self.table:
            if i.guest is None:
                pass
            elif i.guest.is_alive() == False:
                print(f"{i.guest._name} покушал(-а) и ушёл(ушла)")
                print(f"Стол номер {i.number} свободен")
                i.guest = None
                if self.queue.empty() == False:
                    i.guest = self.queue.get()
                    print(f"{i.guest._name} вышел(-ла) из очереди и сел(-а) за стол номер {i.number}")
                    i.guest.start()
                    c += 1