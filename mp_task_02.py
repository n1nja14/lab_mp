import asyncio
import threading
import time
import multiprocessing
import math

# Функции для АТ-02

# запускать с n = 700004
def fibonacci(n):  # содержимое функции не менять
    """Возвращает последнюю цифру n-е числа Фибоначчи."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    print(f'fibonacci = {b % 10}')


# запускать с f, a, b, n равными соответственно math.sin, 0, math.pi, 20000000
def trapezoidal_rule(f, a, b, n):  # содержимое функции не менять
    """Вычисляет определенный интеграл функции f от a до b методом трапеций с n шагами."""
    h = (b - a) / n
    integral = (f(a) + f(b)) / 2.0
    for i in range(1, n):
        integral += f(a + i * h)
    print(f'trapezoidal_rule = {integral * h}')


def sequence():
    start_time = time.time()
    fibonacci(700004)
    trapezoidal_rule(math.sin, 0, math.pi, 20000000)
    end_time = time.time()
    print(f'sequence time: {end_time - start_time: 0.2f} \n')

def threads():
    start_time = time.time()
    thread1 = threading.Thread(target=fibonacci, args=(700004,))
    thread2 = threading.Thread(target=trapezoidal_rule, args=(math.sin, 0, math.pi, 20000000,))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    end_time = time.time()
    print(f'threads time: {end_time - start_time: 0.2f} \n')

def processes():
    start_time = time.time()
    process1 = multiprocessing.Process(target=fibonacci, args=(700004,))
    process2 = multiprocessing.Process(target=trapezoidal_rule, args=(math.sin, 0, math.pi, 20000000,))
    process1.start()
    process2.start()
    process1.join()
    process2.join()
    end_time = time.time()
    print(f'processes time: {end_time - start_time: 0.2f} \n')

async def calculate_fibonacci(n):
    return fibonacci(n)

async def calculate_trapezoidal_rule(*args):
    return trapezoidal_rule(*args)

async def async_():
    start_time = time.time()
    tasks = [asyncio.create_task(calculate_fibonacci(700004)), asyncio.create_task(calculate_trapezoidal_rule(math.sin, 0, math.pi, 20000000))]
    await asyncio.gather(*tasks)
    end_time = time.time()
    print(f'async_ time: {end_time - start_time: 0.2f} \n')

if __name__ == '__main__':
    # sequence()
    # threads()
    # processes()
    asyncio.run(async_())
    """
        Результатом должно стать (знаки вопроса заменятся на ваше время выполнения):
        
        fibonacci = 3
        trapezoidal_rule = 2.000000000000087
        sequence time:  5.46 
        
        fibonacci = 3
        trapezoidal_rule = 2.000000000000087
        threads time:  5.19 
        
        fibonacci = 3
        trapezoidal_rule = 2.000000000000087
        processes time:  3.52 
    """
