# Запрашиваем имя и фамилию
first_name = input("Введите ваше имя: ")
last_name = input("Введите вашу фамилию: ")

# Создаем приветственное сообщение
hello = f"{first_name} {last_name}, приветствуем Вас на курсе 'Data Engineer с нуля до junior!' "

# Сохраняем сообщение в файл
with open("/app/result/hello.txt", "a", encoding="utf-8") as file:
    file.write(hello)

print("Cообщение для Вас сохранено в /app/result/hello.txt")