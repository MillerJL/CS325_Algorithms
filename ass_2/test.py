distance(i, j)
    return ceil(hypot(|i[0] - j[0]|, |i[1] - j[1]|))

J(P, Q, l)
    m <-- len(P) # rows
    n <-- len(Q) # columns
    truthTable <-- [m] * n # Boolean 2D list initialized to False

    for i in 1...m
        for j in 1...n
            if validMove(i, j, truthTable) and distance(P[i], Q[j]) <= leash
                lastTrue = [i,j]
                truthTable[i][j] <-- True
            else
                if lastTrue[0] = (i - 1) and lastTrue[1] > j # row above has T in column to the right of j
                    j <-- lastTrue[1]
                    continue
                else
                    break
        if lastTrue[0] < (i) # Checks to see if there is any T in the current row, if not then there is no viable path
            break

    return truthTable[m][n] # Will be False if there is no viable path, will be true if there is

validMove(i, j, truthTable)
    valid <-- False

    if truthTable[i - 1][j] # if value to left is true
        valid <-- True
    if truthTable[i][j - 1] # if value above is true
        valid <-- True
    if truthTable[i - 1][j - 1] # if value diagonal is true
        valid <-- True

    return valid

bestLeash(L, P, Q)
    i <-- 0
    leash <-- False
    L_length <-- len(L)

    while(L_length >= 1)
        L_length <-- len(L)
        i <-- ceil(L_length / 2)
        result <-- Jump(P, Q, L[i])

        if result = False:
            L <-- L[i...L_length]
        else:
            leash <-- L[i]
            L <-- L[0...i]
        L_length <-- (L_length - len(L))
