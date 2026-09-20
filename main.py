""" Приложение Task Manager

    =============================================================
    консольное приложение - менеджер управления заметок,
    пользователь может создать заметку, редактировать,
    посмотреть все заметки или удалить выбранную.
    =============================================================

    version app 0.0.4
    v(0.0.1)
    разработан цикл приложения - структурное программирование

    v(0.0.2)
    внедрен  i/o функционал для ввода заметки

    v(0.0.3)
    разработаны функции для цикла - функциональное программирование

    v(0.0.4)
    добавлены проверки и подтверждения

    v(0.0.5)
    созданы методы сохранения и загрузки - файловые сохранения
"""

is_running = True
collection = []
print("Приветствуем вас в приложении  TASK MANAGER")


def show_list(collection_list: list):
    print("-" * 30)
    for i, j in enumerate(collection_list):
        print(i + 1, j.strip('\n'))
    print("-" * 30)


def check_confirm(check_funk: int):
    check_task = int(input('введите номер задачи: '))
    if (check_task <= len(collection)):
        if(check_funk == 1):
            print("Введите да/нет или yes/no")
            confirm_edit = input(f'вы точно хотите редактировать задачу {check_task}')
            if (confirm_edit.startswith('y') or confirm_edit.startswith('д')):
                edit_name = input("новое имя задачи: ")
                collection[check_task - 1] = edit_name
                print(f"заметка {check_task} теперь называется {edit_name}")
            else:
                print("отмена редактирования!")
        elif(check_funk == 2):
            print("Введите да/нет или yes/no")
            confirm_delete = input(f'вы точно хотите удалить задачу {check_task}')
            if (confirm_delete.startswith('y') or confirm_delete.__str__().startswith('д')):
                print(f"заметка {check_task} удалена")
                collection.pop(check_task - 1)
            else:
                print("отмена удаления!")
    else:
        print(f"заметка {check_task} не найдена в списке")
        print(f"всего{len(collection)} заметок в списке")


def save_file(tasks):
    print(tasks)
    name = 'saves.txt'
    file = open(name, 'w', encoding="utf-8")
    for task in tasks:
        file.write(f"{task}\n")
    file.close()


def load_file():
    name = 'saves.txt'
    file = open(name, 'r', encoding="utf-8")
    tasks = []
    for line in file:
        print(line.strip('\n'))
        tasks.append(line.strip('\r'))
    print(tasks)
    file.close()
    return tasks


def main(is_run):
    while is_run:
        print('1 - посмотреть задачи'
              '\n2 - добавить задачу'
              '\n3 - редактировать задачу'
              '\n4 - удалить задачу'
              '\n5 - выход')
        choice_user = input("введите команду: ")

        match choice_user:
            case "1":
                show_list(collection_list=collection)
                input("Нажмите 'ENTER' для продолжения")
            case "2":
                task_name = input('введите название задачи: ')
                collection.append(task_name)
                save_file(collection)
            case "3":
                show_list(collection_list=collection)
                check_confirm(1)    #редактируем = 1 - атрибут
            case "4":
                show_list(collection_list=collection)
                check_confirm(2)    #удаляем = 2 - атрибут
            case "5":
                print("отключение...")
                is_run = False
            case _:
                print('неверная команда')


if __name__ == "__main__":
    collection = load_file()
    main(is_running)



