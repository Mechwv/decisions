def calculate(info, matrix, weights):
    """
    The Technique for Order of Preference by Similarity to Ideal Solution
    TOPSIS is a multi-criteria decision analysis method
    """
    print("\n\n -------- МЕТОД TOPSIS -------- \n")
    A_plus = []
    A_minus = []

    # Construct the Normalized Decision Matrix
    for i in range(len(info[1])):
        summ = 0

        for j in range(len(info[0])):
            summ += matrix[i][j] ** 2

        summ = summ ** 0.5

        # Construct the Weighted Normalized Decision Matrix
        row_best = 0
        row_worst = 100
        for j in range(len(info[0])):
            matrix[i][j] /= summ
            matrix[i][j] *= weights[i]
            if matrix[i][j] > row_best:
                row_best = matrix[i][j]
            if matrix[i][j] < row_worst:
                row_worst = matrix[i][j]

        # Determine Ideal and Negative-Ideal Solutions
        if info[2][i]:
            A_plus.append(row_best)
            A_minus.append(row_worst)
        else:
            A_plus.append(row_worst)
            A_minus.append(row_best)

    # Calculate the Separation Measure:
    S_plus = []
    S_minus = []
    print("Preparing matrix for determining solution: \n")
    for i in range(len(info[0])):
        summ_plus = 0
        summ_minus = 0

        row = []
        for j in range(len(info[1])):
            row.append(round(matrix[j][i], 5))
            summ_plus += (matrix[j][i] - A_plus[j]) ** 2
            summ_minus += (matrix[j][i] - A_minus[j]) ** 2

        print(f"A{i + 1} | {row}")

        summ_plus = summ_plus ** 0.5
        summ_minus = summ_minus ** 0.5

        S_plus.append(summ_plus)
        S_minus.append(summ_minus)

    # Calculate the Relative Closeness to the Ideal Solution
    C = []
    print("\nRelative closeness to the ideal solution: \n")
    for i in range(len(S_plus)):
        C.append(S_minus[i] / (S_plus[i] + S_minus[i]))
        print(f"A{i+1} => {C[i]}")
    maxx = max(C)
    minn = min(C)
    print(f"\nBest: A{C.index(maxx)+1}")
    print(f"Worst: A{C.index(minn)+1}")
