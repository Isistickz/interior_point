import numpy as np
import Interior_Point


def main():
    C = np.array(list(map(float, input("Enter the coefficients of the objective function:\n").split())))

    A = []

    num_of_constraints = int(input("Enter the number of constraints: \n"))

    print("Enter the coefficients of variables in the constraints: ")

    for i in range(num_of_constraints):
        A.append(list(map(float, input().split())))

    A = np.array(A)

    print("Enter the right hand side of the constraints:")
    b = np.array(list(map(float, input().split())))

    X = np.array(list(map(float, input("Enter the initial trial point for the Interior point algorithm:\n").split())))

    approximation_accuracy = int(input("Enter the approximation accuracy:\n"))

    alpha = float(input("Enter the alpha: \n"))

    Interior_Point.Interior_Point_Solver(A, b, C, X, alpha, approximation_accuracy)

if __name__ == "__main__":
    main()