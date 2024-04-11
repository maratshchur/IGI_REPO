from tasks.task5.initializer import generate_random_int
from tasks.task5.models import ModificatedMatrix

def task5():
    n = generate_random_int()
    m = generate_random_int()
    matrix_1 = ModificatedMatrix(n,m)
    
    print("Original matrix:")
    print(matrix_1)

    print("Max element: ", matrix_1.find_max_abs())
    matrix_1.divide_matrix_on_max_abs_element()

    print("New matrix: ")
    print(matrix_1)
    
    variance_1 = matrix_1.numpy_variance()
    variance_2 = matrix_1.variance()
    print("Variance of matrix (standart function): {:.2f}".format(variance_1))
    print("Variance of matrix (my function): {:.2f}".format(variance_2))
    
    mean_value = matrix_1.numpy_mean()
    print("Mean value:", mean_value)

    # median_value = np.median(matrix_2)
    # print("Median:", median_value)

    # corr_matrix = np.corrcoef(matrix_2)
    # print("Correlation matrix:")
    # print(corr_matrix)

    std_value = matrix_1.numpy_std()
    print("Standard deviation:", std_value)