# Проект базы данных для медицинского центра
## Описание
**Проект базы данных медицинского центра, написанный на SQLite**

## Структуры базы данных

**Таблица clients (клиенты)**

| Поле | Тип | Описание |
|------|-----|----------|
| id | INTEGER | Идентификатор клиента |
| clientname | TEXT | Имя клиента |
| age | INTEGER | Возраст клиента |
| gender | TEXT | Пол клиента |
| usluga | TEXT | Название услуги |

**Таблица doctors (врачи)**

| Поле | Тип | Описание |
|------|-----|----------|
| id | INTEGER | Идентификатор врача |
| doctorname | TEXT | Имя врача |
| staj | INTEGER | Стаж работы |
| dolgnost | TEXT | Должность |
| obrazovanie | TEXT | Образование |

**Таблица uslugi (услуги)**

| Поле | Тип | Описание |
|------|-----|----------|
| id | INTEGER | Идентификатор услуги |
| usluganame | TEXT | Название услуги |
| price | INTEGER | Цена |
| kolvo | INTEGER | Количество |

## Скриншоты

> Таблица clients

<img width="1268" height="889" alt="image" src="https://github.com/user-attachments/assets/83b31e4a-8013-4206-98c5-dfedd92aabf1" />


> Таблица doctors

<img width="1267" height="881" alt="image" src="https://github.com/user-attachments/assets/a1855b4d-f54b-4d98-ae72-972378f358e2" />


> Таблица uslugi
<img width="1293" height="902" alt="image" src="https://github.com/user-attachments/assets/da62c3a5-fbf0-43a2-9d6a-324a7170da94" />
