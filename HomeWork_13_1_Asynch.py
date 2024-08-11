import asyncio

# Эта асинхронная функция, принимает два параметра: имя силача и его сила
async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования')
    for i in range(1, 6): # в цикле от 1 до 5 (включительно) происходит "поднятие шаров"
        await asyncio.sleep(1 / power) # создает задержку, обратно пропорциональную силе силача
        print(f'Силач {name} поднял {i} шар')
    print(f'Силач {name} закончил соревнования')

# Эта асинхронная функция, создаёт три задачи, каждая из которых вызывает start_strongman с разными параметрами
async def start_tournament():
    tasks = [
        asyncio.create_task(start_strongman('Pasha', 3)),
        asyncio.create_task(start_strongman('Denis', 4)),
        asyncio.create_task(start_strongman('Apollon', 5))
    ]
    await asyncio.gather(*tasks) # запускает все задачи одновременно и ожидает их завершения.

asyncio.run(start_tournament()) # запускает асинхронную функцию в событийном цикле.