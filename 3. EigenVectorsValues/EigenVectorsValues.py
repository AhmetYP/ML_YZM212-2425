import time
import numpy as np

# Özdeğerleri manuel olarak hesaplama için gerekli fonksiyonlar
def get_dimensions(matrix):
    return [len(matrix), len(matrix[0])]

def find_determinant(matrix, excluded=1):
    dimensions = get_dimensions(matrix)
    if dimensions == [2, 2]:
        return excluded * ((matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0]))
    else:
        new_matrices = []
        excluded = []
        exclude_row = 0
        for exclude_column in range(dimensions[1]):
            tmp = []
            excluded.append(matrix[exclude_row][exclude_column])
            for row in range(1, dimensions[0]):
                tmp_row = []
                for column in range(dimensions[1]):
                    if (row != exclude_row) and (column != exclude_column):
                        tmp_row.append(matrix[row][column])
                tmp.append(tmp_row)
            new_matrices.append(tmp)
        determinants = [find_determinant(new_matrices[j], excluded[j]) for j in range(len(new_matrices))]
        determinant = 0
        for i in range(len(determinants)):
            determinant += ((-1) ** i) * determinants[i]
        return determinant

def list_multiply(list1, list2):
    result = [0 for _ in range(len(list1) + len(list2) - 1)]
    for i in range(len(list1)):
        for j in range(len(list2)):
            result[i + j] += list1[i] * list2[j]
    return result

def list_add(list1, list2, sub=1):
    return [i + (sub * j) for i, j in zip(list1, list2)]

def determinant_equation(matrix, excluded=[1, 0]):
    dimensions = get_dimensions(matrix)
    if dimensions == [2, 2]:
        tmp = list_add(list_multiply(matrix[0][0], matrix[1][1]), list_multiply(matrix[0][1], matrix[1][0]), sub=-1)
        return list_multiply(tmp, excluded)
    else:
        new_matrices = []
        excluded = []
        exclude_row = 0
        for exclude_column in range(dimensions[1]):
            tmp = []
            excluded.append(matrix[exclude_row][exclude_column])
            for row in range(1, dimensions[0]):
                tmp_row = []
                for column in range(dimensions[1]):
                    if (row != exclude_row) and (column != exclude_column):
                        tmp_row.append(matrix[row][column])
                tmp.append(tmp_row)
            new_matrices.append(tmp)
        determinant_equations = [determinant_equation(new_matrices[j], excluded[j]) for j in range(len(new_matrices))]
        dt_equation = [sum(i) for i in zip(*determinant_equations)]
        return dt_equation

def identity_matrix(dimensions):
    matrix = [[0 for j in range(dimensions[1])] for i in range(dimensions[0])]
    for i in range(dimensions[0]):
        matrix[i][i] = 1
    return matrix

def characteristic_equation(matrix):
    dimensions = get_dimensions(matrix)
    return [[[a, -b] for a, b in zip(i, j)] for i, j in zip(matrix, identity_matrix(dimensions))]

def find_eigenvalues(matrix):
    dt_equation = determinant_equation(characteristic_equation(matrix))
    return np.roots(dt_equation[::-1])

# Ana program güncellenmiş hali
if __name__ == "__main__":
    A = [[6, 1, -1],
         [0, 7, 0],
         [3, -1, 2]]

    # Manuel hesaplama için süre ölçümü
    start_time_custom = time.time()
    custom_eigenvalues = find_eigenvalues(A)
    end_time_custom = time.time()
    custom_duration = end_time_custom - start_time_custom

    # NumPy hesaplama için süre ölçümü
    start_time_numpy = time.time()
    numpy_eigenvalues, _ = np.linalg.eig(A)
    end_time_numpy = time.time()
    numpy_duration = end_time_numpy - start_time_numpy

    # Sonuçlar
    print("Özdeğerler (manuel hesaplama):", custom_eigenvalues)
    print("Hesaplama süresi (manuel):", custom_duration, "saniye")

    print("Özdeğerler (NumPy):", numpy_eigenvalues)
    print("Hesaplama süresi (NumPy):", numpy_duration, "saniye")
