# Дана "грязная" строка:
# raw_data = "  login_test : FAILED  "
# Нужно привести её к чистому виду, требования:
# итоговая строка должна собираться из очищенных от лишних пробелов частей (никаких пробелов вокруг login_test и FAILED в финальном выводе быть не должно)
# разделитель между частями меняется с ":" на " -> "
# если статус теста — "FAILED", должна дополнительно вывестись строка "Тест провалился"

raw_data = "  login_test : FAILED  "
clean_data = raw_data.replace(" ","")
clean_data = clean_data.replace(":","->")
print(clean_data)
if "FAILED" in clean_data:
    print("Тест провалился")

print("-"*80)
# Дана "грязная" строка:
# raw_filename = "  Test_Report#Checkout#PASSED.log  "
#
# Нужно привести её к виду:
# Итог: Checkout -> PASSED
# Файл в порядке
#
# Требования: строка изначально содержит лишние пробелы по краям и разделяется символом "#" на три части, из которых для финального результата нужны только вторая и третья (третья часть — с "мусорным" расширением .log, которое нужно удалить); финальные две части склеиваются через " -> "; дополнительно нужно вывести сообщение в зависимости от того, равен ли итоговый статус "PASSED" или нет.
# Используй strip(), split(), replace(), join(), == или in.

raw_filename = "  Test_Report#Checkout#PASSED.log  "
raw_filename = raw_filename.strip()
parts = raw_filename.split("#")
part1, part2 = parts[1], parts[2]
part2 = part2.replace(".log","")
result = f"{part1} -> {part2}"
print(result)
if "PASSED" in result:
    print("Файл в порядке")