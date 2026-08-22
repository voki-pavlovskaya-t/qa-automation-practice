# Напиши функцию use_potion(player_health, max_health), которая:
# увеличивает player_health на 20
# если получилось больше max_health — здоровье не должно превышать максимум
# возвращает итоговое здоровье
#
# Добавь логирование:
# INFO — когда зелье использовано и здоровье увеличилось
# WARNING — если здоровье уже было на максимуме, и зелье фактически бесполезно
#
# Настрой basicConfig так, чтобы в файл не попадали обычные INFO-сообщения, только WARNING и выше.
# Напиши также два теста: один — когда зелье реально помогает, второй — когда здоровье уже максимальное.

import logging

logging.basicConfig(
    level=logging.WARNING,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def use_potion(player_health, max_health):
    if player_health >= max_health:
        logging.warning("Зелье использовано впустую, здоровье уже на максимуме")
        return player_health

    new_health = player_health + 20
    if new_health > max_health:
        new_health = max_health

    logging.info(f"Зелье использовано, здоровье увеличено до {new_health}")
    return new_health

def test_potion_heals():
    result = use_potion(50, 100)
    assert result == 70

def test_potion_useless_at_max():
    result = use_potion(100, 100)
    assert result == 100

