import numpy as np

alternatives = []
indicators = []
positiveness = []
v_table = []
weights_table = []
soglasie_table = []
nesoglasie_table = []
matrix = None


def _dimensionless():
    """
    Приведение оценок альтернатив к безмерному виду путем выбирания наилучшего по критерию
    и нормализации относительно него
    """
    print("\nБезмерные оценки: ")
    global matrix
    for k in range(len(indicators)):
        if positiveness[k]:
            m = min(v_table[k])
            for a in range(len(alternatives)):
                v_table[k][a] = round(m / v_table[k][a], 2)
        else:
            m = max(v_table[k])
            for a in range(len(alternatives)):
                v_table[k][a] = round(v_table[k][a] / m, 2)
        print(f"K{k + 1} | {v_table[k]}")
    matrix = np.array(v_table)


def __s_index(a, b):
    """
    сравнение и расчет того, какие элементы из 1-го слобца больше противоположных во втором по правилам согласия
    :param a: столбец 1
    :param b: столбец 2
    :return: какие элементы из 1-го слобца больше противоположных во втором
    """
    c = list(np.greater_equal(a, b))
    summ = 0
    for i in range(len(c)):
        if c[i]:
            summ += weights_table[i]
    return summ


def _soglasie():
    """
    Создание матрицы согласия
    """
    print("\nМатрица согласия: ")
    global soglasie_table
    for i in range(len(alternatives)):
        row = []
        for j in range(len(alternatives)):
            if i != j:
                row.append(round(__s_index(matrix[:, i], matrix[:, j]), 2))
            else:
                row.append(100)
        print(f"A{i + 1} | {row} => {min(row)}")
        soglasie_table.append(min(row))


def __n_index(a, b):
    """
    сравнение и расчет того, какие элементы из 1-го слобца больше противоположных во втором по правилам несогласия
    :param a: столбец 1
    :param b: столбец 2
    :return: какие элементы из 1-го слобца больше противоположных во втором
    """
    c = list(np.less_equal(a, b))
    arr = []
    for i in range(len(c)):
        if c[i]:
            arr.append(b[i] - a[i])
    return max(arr)


def _nesoglasie():
    """
    Создание матрицы несогласия
    """
    print("\nМатрица несогласия: ")
    global soglasie_table
    for i in range(len(alternatives)):
        row = []
        for j in range(len(alternatives)):
            if i != j:
                row.append(round(__n_index(matrix[:, i], matrix[:, j]), 2))
            else:
                row.append(0)
        print(f"A{i + 1} | {row} => {max(row)}")
        nesoglasie_table.append(max(row))


def _best_alt():
    """
    выбор лучших(ей) альтернатив(ы) путем сравнения полученных выборок с
    коэффициентами C* и D*
    :return: list
    """
    print("\nВыделение лучших альтернатив:")
    C = 0.4
    D = 0.6
    C_best = []
    D_best = []
    for i in range(len(soglasie_table)):
        if soglasie_table[i] > C:
            C_best.append(alternatives[i])
        if nesoglasie_table[i] > D:
            D_best.append(alternatives[i])
    print(f"Cj>C\n{C_best}\nDj>D\n{D_best}\n")
    alt = list(set(C_best) & set(D_best))
    print(f"Chosen alternatives: {alt}")
    return alt


def calculate(attr, matrix, expert):
    """
    Пример вычисления лучшей альтернативы методом электра
    :param n_alternatives: кол-во альтернатив
    :param n_indicators: кол-во критериев для альтернатив
    :param number_of_experts: количество экспертных оценок важности критериев
    :return:
    """
    global alternatives, indicators, positiveness, v_table, weights_table
    alternatives = attr[0]
    indicators = attr[1]
    positiveness = attr[2]
    v_table = matrix
    weights_table = expert
    print("\n\n -------- МЕТОД ЭЛЕКТРА -------- ")
    _dimensionless()
    _soglasie()
    _nesoglasie()
    return _best_alt()
