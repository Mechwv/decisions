def calculate(info, matrix, weights):
    print("\n\n -------- МЕТОД SAW -------- \n")
    row = 0
    best_sum = 0
    for i in range(len(info[0])):
        summ = 0
        for j in range(len(info[1])):
            summ += matrix[j][i] * weights[j]
        print(f"Сумма для A{i+1}: {round(summ, 2)}")
        if summ > best_sum:
            best_sum = summ
            row = i
    print(f"\nЛучшая альтернатива: {info[0][row]}")