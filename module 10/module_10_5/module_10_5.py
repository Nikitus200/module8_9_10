import multiprocessing
from datetime import datetime
def read_info(name):
    all_data = []
    with open(name, "r", encoding="utf-8") as file:
        for line in file:
            all_data.append(line)


filenames = [f'./file {number}.txt' for number in range(1, 5)]

# Линейный вызов:
"""start = datetime.now()
for n in filenames:
    read_info(n)
end = datetime.now()
print(end - start)"""

# Многопроцессный вызов:
if __name__ == '__main__':
    start = datetime.now()
    with multiprocessing.Pool(processes=3) as pool:
        pool.map(read_info, filenames)
    end = datetime.now()
    print(end - start)