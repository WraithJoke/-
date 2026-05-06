import sqlite3
import csv

connection = sqlite3.connect("medcentr.db")
cursor = connection.cursor()
cursor.execute("PRAGMA foreign_keys = ON")

cursor.execute("""DROP TABLE IF EXISTS clients""")
cursor.execute("""DROP TABLE IF EXISTS doctors""")
cursor.execute("""DROP TABLE IF EXISTS uslugi""")

cursor.execute("""CREATE TABLE clients(
id INTEGER PRIMARY KEY AUTOINCREMENT,
clientname TEXT NOT NULL,
age INTEGER NOT NULL,
gender TEXT NOT NULL,
usluga TEXT
)
""")

cursor.execute("""CREATE TABLE doctors(
id INTEGER PRIMARY KEY AUTOINCREMENT,
doctorname TEXT NOT NULL,
staj INTEGER NOT NULL,
dolgnost TEXT NOT NULL,
obrazovanie TEXT NOT NULL
)
""")

cursor.execute(""" CREATE TABLE uslugi(
id INTEGER PRIMARY KEY AUTOINCREMENT,
usluganame TEXT NOT NULL,
price INTEGER NOT NULL,
kolvo INTEGER NOT NULL
)
""")


print("Введите имя")
clientname = input()
print("Введите возраст")
age = int(input())
print("Введите пол")
gender = input()
print("Введите услугу")
usluga = input()

cursor.execute(""" 
INSERT INTO clients (clientname, age, gender, usluga)
VALUES (?,?,?,?)
""", (clientname, age, gender, usluga))

print("Введите цену")
price = int(input())
print("Введите количество")
kolvo = int(input())


cursor.execute("""
INSERT INTO uslugi (usluganame, price, kolvo)
VALUES (?,?,?)
""", (usluga, price, kolvo))


cursor.execute("""
INSERT INTO clients (clientname, age, gender, usluga)
VALUES ("Михаил", 22, "М", "Приём терапевта")
""")

cursor.execute("""
INSERT INTO doctors (doctorname, staj, dolgnost, obrazovanie)
VALUES ("Краснов Александр Дмитриевич", 15, "Терапевт", "Высшее") 
""")

cursor.execute("""
INSERT INTO clients (clientname, age, gender, usluga)
VALUES ("Марк", 19, "М", "УЗИ")
""")

cursor.execute("""
INSERT INTO clients (clientname, age, gender, usluga)
VALUES ("Кирилл", 24, "М", "ЭКГ")
""")

cursor.execute("""
INSERT INTO clients (clientname, age, gender, usluga)
VALUES ("Екатерина", 20, "Ж", "Анализ крови")
""")

clients_array = [
    ("Анна", 25, "ж", None), ("Дмитрий", 19, "м", None), ("Елена", 34, "ж", None),
    ("Илья", 42, "м", None), ("Татьяна", 28, "ж", None),
    ("Роман", 21, "м", None), ("Виктория", 18, "ж", None), ("Кирилл", 31, "м", None),
    ("Наталья", 27, "ж", None), ("Арсений", 16, "м", None),
    ("Марина", 45, "ж", None), ("Олег", 36, "м", None), ("Полина", 23, "ж", None),
    ("Степан", 24, "м", None), ("Алина", 29, "ж", None),
    ("Валерий", 52, "м", None), ("Екатерина", 30, "ж", None), ("Станислав", 38, "м", None),
    ("Ирина", 40, "ж", None), ("Руслан", 26, "м", None),
    ("Светлана", 33, "ж", None), ("Александр", 22, "м", None), ("Юлия", 29, "ж", None),
    ("Владимир", 47, "м", None), ("Анастасия", 20, "ж", None),
    ("Артём", 23, "м", None), ("Дарья", 26, "ж", None), ("Максим", 44, "м", None),
    ("Ольга", 31, "ж", None), ("Сергей", 28, "м", None),
    ("Ксения", 32, "ж", None), ("Глеб", 20, "м", None), ("Вероника", 27, "ж", None),
    ("Матвей", 18, "м", None), ("Елизавета", 35, "ж", None),
    ("Данила", 22, "м", None), ("Василиса", 24, "ж", None), ("Захар", 37, "м", None),
    ("Ульяна", 21, "ж", None), ("Егор", 25, "м", None),
]

cursor.executemany("""
INSERT INTO clients (clientname, age, gender, usluga)
VALUES (?,?,?,?)
""", clients_array)

doctors_array = [
    ("Алексей Иванович Иванов", 25, "Хирург", "Высшее"),
    ("Мария Петровна Петрова", 18, "Терапевт", "Высшее"),
    ("Дмитрий Сергеевич Сидоров", 12, "Кардиолог", "Высшее"),
    ("Елена Васильевна Васильева", 30, "Невролог", "Высшее"),
    ("Андрей Владимирович Смирнов", 8, "Педиатр", "Высшее"),
    ("Ольга Дмитриевна Кузнецова", 22, "Офтальмолог", "Высшее"),
    ("Игорь Александрович Попов", 15, "Стоматолог", "Высшее"),
    ("Наталья Михайловна Соколова", 10, "Дерматолог", "Высшее"),
    ("Владимир Павлович Лебедев", 35, "Эндокринолог", "Высшее"),
    ("Татьяна Алексеевна Новикова", 7, "Гинеколог", "Высшее"),
    ("Сергей Андреевич Фёдоров", 20, "Уролог", "Высшее"),
    ("Анна Игоревна Морозова", 14, "Рентгенолог", "Высшее"),
    ("Павел Евгеньевич Волков", 28, "Анестезиолог", "Высшее"),
    ("Юлия Викторовна Козлова", 9, "ЛОР", "Высшее"),
    ("Михаил Борисович Егоров", 32, "Онколог", "Высшее"),
    ("Екатерина Николаевна Зайцева", 6, "Травматолог", "Высшее"),
    ("Александр Валерьевич Борисов", 17, "Реаниматолог", "Среднее специальное"),
    ("Светлана Геннадьевна Виноградова", 40, "Психиатр", "Высшее"),
    ("Роман Денисович Беляев", 4, "Интерн", "Высшее"),
    ("Виктория Олеговна Орлова", 11, "Венеролог", "Высшее"),
    ("Константин Юрьевич Макаров", 16, "Гастроэнтеролог", "Высшее"),
]

cursor.executemany("""
INSERT INTO doctors (doctorname, staj, dolgnost, obrazovanie)
VALUES(?,?,?,?)
""", doctors_array)

uslugi_array = [
    ("Приём терапевта", 1500, 30),
    ("УЗИ брюшной полости", 2500, 25),
    ("ЭКГ", 1200, 40),
    ("Общий анализ крови", 800, 50),
    ("МРТ одного отдела", 4500, 15),
    ("КТ одного отдела", 4000, 18),
    ("Консультация кардиолога", 2000, 20),
    ("Вакцинация", 1000, 60),
    ("Флюорография", 900, 35),
    ("Стоматологическая чистка", 3500, 22),
    ("Эндоскопия желудка", 3800, 12),
    ("Справка для бассейна", 500, 45),
    ("Гинекологический осмотр", 1800, 28),
    ("Анализ на гормоны", 1700, 32),
    ("Хирургическое удаление", 5500, 10),
    ("Лазерная коррекция зрения", 35000, 5),
    ("Сеанс массажа", 2500, 18),
    ("Физиотерапия", 1300, 24),
    ("Капельница", 2200, 15),
    ("Вызов врача на дом", 3000, 8),
    ("Тест на COVID-19", 1200, 35),
    ("Эхокардиография", 3200, 14),
    ("Аллергопроба", 1100, 26),
    ("Холтер ЭКГ", 2900, 11),
    ("Справка в ГИБДД", 700, 42),
    ("Диспансеризация", 3500, 19),
    ("Биохимия крови", 950, 38),
    ("Перевязка", 600, 55),
    ("Медицинская книжка", 2500, 20),
    ("Телемедицинская консультация", 1000, 44),
]

cursor.executemany("""
INSERT INTO uslugi (usluganame, price, kolvo)
VALUES(?,?,?)
""", uslugi_array)

connection.commit()
connection.close()