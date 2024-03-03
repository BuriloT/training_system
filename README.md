# Построение системы для обучения
## Описание проекта
Этот проект представляет собой систему для обучения, включающую в себя архитектуру базы данных и API для работы с продуктами, уроками и группами пользователей.

Построение архитектуры
1. Создание сущности "Продукт"
Продукт содержит информацию о создателе (авторе/преподавателе), названии, дате и времени старта, стоимости.
2. Определение доступа пользователя к продукту
Механизм определения доступа пользователя к продукту реализован.
3. Создание сущности "Урок"
Урок привязан к одному продукту и содержит базовую информацию: название и ссылка на видео.
4. Создание сущности "Группа"
Группа привязана к продукту и содержит информацию о учениках, названии группы, и минимальном/максимальном количестве участников.
Написание запросов и реализация логики распределения

## Инструкции по запуску проекта
Клонировать репозиторий:
```
git clone https://github.com/yourusername/training_system.git
cd training_system
```
Создать виртуальное окружение и активировать его:
```
python -m venv venv
source venv/bin/activate  # для Linux/Mac
venv\Scripts\activate  # для Windows
```
Установить зависимости:
```
pip install -r requirements.txt
```
Применить миграции:
```
python manage.py migrate
```
Запустить сервер разработки:
```
python manage.py runserver
```
