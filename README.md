# Task_Scheduler
Планеровщик задач - это инструмент управления задачами, который помогает пользователям создавать, управлять и отслеживать свои задачи и проекты.

Вы можете использовать планер задач для следующих целей:

- Создать задачи
- Определить сроки выполнения задач
- Управлять приоритетом задач
- Добавить описание и комментарии к задачам
- Установить напоминания о задачах
- Отслеживать прогресс выполнения задач

Документация разработчика
--
Планеровщик задач - это веб-приложение, созданное с использованием фреймворка Django.

Для запуска планера задач на локальном компьютере необходимо выполнить следующие шаги:

1. Склонировать репозиторий:

```git clone https://github.com/MiraiInternational/Task_Scheduler.git```

2. Установить зависимости:

```pip install -r requirements.txt```

3. Создать и применить миграции базы данных:

```python manage.py makemigrations```

```python manage.py migrate```

4. Создать суперпользователя:

```python manage.py createsuperuser```

5. Запустить сервер:

```python manage.py runserver```

После запуска сервера можно открыть приложение в браузере по адресу http://localhost:8000/.
