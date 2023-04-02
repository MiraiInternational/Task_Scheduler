"""
Класс, представляющий задачу
Свойства:

* title (str): Название задачи
* description (str): Описание задачи
* priority (int): Приоритет задачи (от 1 до 5).
* due_date (date): Дата выполнения задачи.
* completed (bool): Состояние выполнения задачи.
"""
class Task:
    title = ""
    description = ""
    priority = 0
    due_date = ""
    completed = False
    def __init__(self, title, description, priority, due_date):
        """
        Создает новую задачу с заданными свойствами
        """
        return 0

    def complete(self):
        """
        Отмечает задачу как выполненную.
        """
        return 0

    def __str__(self):
        """
        Возвращает строковое представление задачи.
        """
        return 0