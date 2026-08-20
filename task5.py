# В твоём проекте с match-3 игрой нужно проверить результаты нескольких прошедших тестов. У тебя есть файл test_results.json.json со списком тестов — у каждого есть название теста, статус ("passed" или "failed") и время выполнения в секундах.
#
# Напиши скрипт, который:
# Прочитает данные из test_results.json
# Найдёт все тесты со статусом "failed"
# Выведет их в консоль (название и время выполнения)
# Посчитает сколько всего тестов упало
# Запишет упавшие тесты в отдельный файл failed_tests.json
# Дополнительно (по желанию): допишет в лог-файл test_run.log строку вида "Тестов упало: 2" — не перезаписывая предыдущие записи
#
# Создай сначала сам файл test_results.json.json с 5-6 тестами (придумай названия, статусы и время сама), а потом напиши скрипт.

import json

with open("test_results.json","r") as f:
    results = json.load(f)

counter_failed = 0
list_failed = []
for i in results:
    if i["status"] == "failed":
        counter_failed += 1
        list_failed.append(i)
        print(i["test_case"],i["time"])

with open("failed_tests.json", "w") as f:
    json.dump(list_failed,f)

with open("test_run.log","a") as f:
    f.write(f"Тестов упало: {counter_failed}")
    
