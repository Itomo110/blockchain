import numpy as np
def trace_matrix(matrix):
    t_matrix = matrix.T
    return t_matrix

def distributed_share(t_matrix,participant:list):
    dict_share = {}
    for i in range(4):
        dict_share[participant[i]] = t_matrix[i]
    return dict_share

def main():
#input
    m = np.array([[1,0,0,1],
                 [0,0,0,0],
                 [0,0,0,0],
                 [0,0,0,0] ])

    participant_list = ["A","B","C","D"]

    print(distributed_share(trace_matrix(m),participant_list))

if __name__ == "__main__":
    main()


