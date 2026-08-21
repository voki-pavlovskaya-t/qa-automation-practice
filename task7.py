# Дан список предметов игрока:
# inventory = ["sword", "shield", "potion"]
#
# Тебе нужно написать функцию get_item(inventory, index), которая:
# Пытается вернуть предмет из inventory по индексу index.
# Если индекса не существует — не даёт программе упасть, а возвращает строку "Предмет не найден".
# Используй try/except (тип ошибки подбери сама, исходя из того, что мы разбирали).

inventory = ["sword", "shield", "potion"]

def get_item( inventory, index):
    try:
        return inventory[index]
    except IndexError:
        return "Предмет не найден"

print(get_item(inventory, 0))
print(get_item(inventory, 10))
print(get_item(inventory, 2))