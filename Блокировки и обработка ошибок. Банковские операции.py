
import threading
import random
import time

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for _ in range(100):
            amount = random.randint(50, 500)
            self.lock.acquire()  # Захват замка
            self.balance += amount
            print(f'Пополнение: {amount}. Баланс: {self.balance}')
            self.lock.release()  # Освобождение замка
            time.sleep(0.001)

    def take(self):
        for _ in range(100):
            amount = random.randint(50, 500)
            print(f'Запрос на {amount}')
            self.lock.acquire()  # Захват замка
            if amount <= self.balance:
                self.balance -= amount
                print(f'Снятие: {amount}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
            self.lock.release()  # Освобождение замка
            time.sleep(0.001)

bk = Bank()

# Создание потоков
thread1 = threading.Thread(target=bk.deposit)
thread2 = threading.Thread(target=bk.take)

# Запуск потоков
thread1.start()
thread2.start()

# Ожидание завершения потоков
thread1.join()
thread2.join()

# Итоговый баланс
print(f'Итоговый баланс: {bk.balance}')
