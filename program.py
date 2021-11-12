try:
    from include.main import Manager as main
    # Конфигурируем программу добавляя задачи в список
    # В каждой задаче настраиваем ввод, вывод, исполняющую функцию и тип ожидаемых данных от пользователя
    # Последовательноть выволнения задач будет в соответствии со списком tasks 
    # Если необходимо, то список задач можно сортировать, так как номера задач весьма условны
    tasks = list()
    
    try:
        from tasks.task1 import Task as task1
        # tasks.append(task1()())
    except ImportError:
        pass

    try:
        from tasks.task2 import Task as task2
        # tasks.append(task2()())
    except ImportError:
        pass

    try:
        from tasks.task3 import Task as task3
        # tasks.append(task3()())
    except ImportError:
        pass

    try:
        from tasks.task4 import Task as task4
        # tasks.append(task4()())
    except ImportError:
        pass

    try:
        from tasks.task5 import Task as task5
        # tasks.append(task5()())
    except ImportError:
        pass

    try:
        from tasks.task6 import Task as task6
        # tasks.append(task6()())
    except ImportError:
        pass

    try:
        from tasks.task7 import Task as task7
        # tasks.append(task7()())
    except ImportError:
        pass    

    main()(tasks)
except ImportError:
    print("import error!")
