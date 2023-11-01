import numpy as np

def print_array(Array):
    Array = np.round(Array, 2)
    idx = 1
    for element in Array:
        print("x_{} = {}".format(idx, element))
        idx += 1

def get_max_negative_value(Cp):
    negative_values = Cp[Cp < 0]
    max_abs_value = np.max(np.abs(negative_values))
    largest_negative = negative_values[negative_values == -max_abs_value]

    return largest_negative * -1

def calculate_accuracy(X, tempX, accuracy, C):
    n = X.shape[0]
    # print("I am in accuracy calculation, ", X.shape, " ", tempX.shape, " ", C.shape, '\n')
    X = X.reshape(n, 1)
    C = C.reshape(n, 1)
    C = np.transpose(C)
    X_norm = np.dot(C, X)
    tempX_norm = np.dot(C, tempX)

    if(abs(X_norm - tempX_norm) > accuracy):
        return True

    return False

def Interior_Point_Solver(A, B, C, X, alpha, accuracy):
    iter = 0
    while(True):
        D = np.diag(X)

        A_tilda = np.matmul(A, D)

        c_tilda = np.matmul(D, C)

        A_tilda_Tr = np.transpose(A_tilda)

        P = np.eye(len(C)) - np.matmul(A_tilda_Tr, np.matmul(np.linalg.inv(np.matmul(A_tilda, A_tilda_Tr)), A_tilda))

        C_p = np.matmul(P, c_tilda)

        v = get_max_negative_value(C_p)

        X_tilda = np.ones((1, len(C_p))) + ((alpha / v) * C_p)

        tempX = np.matmul(D, np.transpose(X_tilda))

        flag = calculate_accuracy(X, tempX, accuracy, C)

        if(flag == False):
           print("The vector of decision variables is: ", '\n')
           print_array(tempX)
           break
        else:
            print("This is the {} iteration".format(iter))
            iter += 1
            print_array(tempX)
            X = tempX
            X = np.squeeze(X)


