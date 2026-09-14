"""
    Точка входа в приложение Task Manager
    version 0.0.4
    --- description ---
    проложение может сохранять задачи,
    редактировать, выдает список задач
    и может удалять задачу.
"""

is_running = True
collection = ["task 1", "task 2"] # list

print("Добро пожаловать!")
while is_running:
    print("1 - посмотреть задачи \n"
          "2 - добавить задачу \n"
          "3 - редактирование задачи \n"
          "4 - удаление задачи \n"
          "5 - выход")

    choice_user = input("Введите свой выбор")
    match str(choice_user):
        case '1':
            for i, j in enumerate(collection):
                print(i + 1, j)
        case '2':
            add_task = input("Введите имя задачи для добавления")
            collection.append(add_task)
        case '3':
            for i, j in enumerate(collection):
                print(i + 1, j)
            select_task = int(input("Введите номер задачи"))
            edit_task = input("Введите новое имя задачи для редактирования")
            collection[select_task - 1] = edit_task
        case '4':
            for i, j in enumerate(collection):
                print(i + 1, j)
            delete_task = int(input("Введите номер задачи для удаления"))
            collection.pop(delete_task - 1)
        case '5':
            is_running = False
            print("До свидания!")
        case _:
            print("Такого пункта нет!")
