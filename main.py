import electra
import saw
import topsis
import desicion_matrix

if __name__ == "__main__":
    info = desicion_matrix.gather(5, 8)
    matrix = desicion_matrix.d_matrix(info)
    expert = desicion_matrix.expert(info, 3)
    # saw.calculate(info, matrix, expert)
    # electra.calculate(info, matrix, expert)
    topsis.calculate(info, matrix, expert)
