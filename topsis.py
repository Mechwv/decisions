def calculate(info, matrix, weights):
    """
    The Technique for Order of Preference by Similarity to Ideal Solution
    TOPSIS is a multi-criteria decision analysis method
    """
    print("\n\n -------- МЕТОД TOPSIS -------- \n")
    A_plus = []
    A_minus = []

    for i in range(len(info[0])):
        summ = 0

        for j in range(len(info[1])):
            summ += matrix[j][i] ** 2

        summ = summ ** 0.5

        row_best = 0
        row_worst = 100
        for j in range(len(info[1])):
            matrix[j][i] /= summ
            matrix[j][i] *= weights[i]
            if matrix[j][i] > row_best:
                row_best = matrix[j][i]
            if matrix[j][i] < row_worst:
                row_worst = matrix[j][i]

        if info[2][i]:
            A_plus.append(row_best)
            A_minus.append(row_worst)
        else:
            A_plus.append(row_worst)
            A_minus.append(row_best)

    S_plus = []
    S_minus = []
    print("Preparing matrix for determining solution: \n")
    for i in range(len(info[1])):
        summ_plus = 0
        summ_minus = 0

        row = []
        for j in range(len(info[0])):
            row.append(round(matrix[i][j], 5))
            summ_plus += (matrix[i][j] - A_plus[j]) ** 2
            summ_minus += (matrix[i][j] - A_minus[j]) ** 2

        print(f"A{i + 1} | {row}")

        summ_plus = summ_plus ** 0.5
        summ_minus = summ_minus ** 0.5

        S_plus.append(summ_plus)
        S_minus.append(summ_minus)
    C = []
    print("\nRelative closeness to the ideal solution: \n")
    for i in range(len(S_plus)):
        C.append(S_minus[i] / (S_plus[i] + S_minus[i]))
        print(f"A{i} => {C[i]}")
    maxx = max(C)
    minn = min(C)
    print(f"\nBest: A{C.index(maxx)}")
    print(f"Worst: A{C.index(minn)}")
