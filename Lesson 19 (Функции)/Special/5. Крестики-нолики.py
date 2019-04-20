def tic_tac_toe(field):
    matrix = [i for i in field if i != ' ' and i != '\n']

    for i in range(3):
        if matrix[i][0] == matrix[i][1] == matrix[i][2] == 'x':
            print("x win")
            return
        if matrix[0][i] == matrix[1][i] == matrix[2][i] == 'x':
            print("x win")
            return
        if matrix[0][0] == matrix[1][1] == matrix[2][2] == 'x':
            print("x win")
            return
        if matrix[0][2] == matrix[1][1] == matrix[2][0] == 'x':
            print("x win")
            return

        if matrix[i][0] == matrix[i][1] == matrix[i][2] == '0':
            print("0 win")
            return
        if matrix[0][i] == matrix[1][i] == matrix[2][i] == '0':
            print("0 win")
            return
        if matrix[0][0] == matrix[1][1] == matrix[2][2] == '0':
            print("0 win")
            return
        if matrix[0][2] == matrix[1][1] == matrix[2][0] == '0':
            print("0 win")
            return
    print("draw")
