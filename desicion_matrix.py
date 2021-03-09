import random


def gather(c_l, i_l):
    """
    Сбор первоначальной информации по кол-ву альтернатив и их критериев для дальнейшей
    тестовой генерации сценария расчета метода
    :param c_l: кол-во альтернатив
    :param i_l: кол-во критериев
    :return: массив аттрибутов, критериев и положительности аттрибутов
    """
    alternatives = ["A" + str(i) for i in range(1, c_l + 1)]
    indicators = ["K" + str(i) for i in range(1, i_l + 1)]
    positiveness = [random.randint(0, 1) for i in range(1, i_l + 1)]
    attr = [alternatives, indicators, positiveness]
    return attr


def d_matrix(attr):
    """
    Создание множества Паретто из полученной таблицы (матрицы выбора)
    :param attr: массив аттрибутов, критериев и положительности аттрибутов
    :return: матрица выбора
    """
    print("\nМножество Паретто: ")
    v_table = []
    for a in attr[1]:
        row = []
        for k in attr[0]:
            row.append(random.choice(range(2000, 9000)))
        v_table.append(row)
        print(f"{a} | {row}")
    return v_table


def expert(attr, n):
    """
    рандомное заполнение экспертной оценки важности критериев (для тестов)
    :param attr: массив аттрибутов, критериев и положительности аттрибутов
    :param n: количество экспертных оценок
    :return: веса для каждого критерия с учетом оценки всех экспертов
    """
    print("\nЭкспертные оценки: ")
    weights_table = []
    table = []
    for a in range(n):
        row = []
        for k in attr[1]:
            row.append(random.choice(range(1, 11)))
        table.append(row)
        print(f"{a + 1}-й эксперт | {row}")
    summ = 0
    print("\nВеса:")
    for a in range(n):
        summ += sum(table[a])
    for k in range(len(attr[1])):
        column_sum = 0
        for a in range(n):
            column_sum += table[a][k]
        column_sum = round(column_sum / summ, 2)
        weights_table.append(column_sum)
        print(f"V{k + 1} | {column_sum}")
    return weights_table
