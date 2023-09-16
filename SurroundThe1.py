def SurroundThe1(arr):

    out = 0
    num = 0
    m = len(arr)
    n = len(arr[0])
    for x in range(m):
        for y in range(n):
            if arr[x][y] == 1:
                if m == 1:
                    if n == 1:
                        out = 0
                    else:
                        if arr[x][y - 1] == 0:
                            num += 1
                        if arr[x][y + 1] == 0:
                            num += 1
                elif n == 1:
                    if arr[x - 1][y] == 0:
                        num += 1
                    if arr[x + 1][y] == 0:
                        num += 1
                elif x == 0:
                    if y == 0:
                        if arr[x][y + 1] == 0:
                            num += 1
                        if arr[x + 1][y] == 0:
                            num += 1
                        if arr[x + 1][y + 1] == 0:
                            num += 1
                    elif y == n - 1:
                        if arr[x][y - 1] == 0:
                            num += 1
                        if arr[x + 1][y - 1] == 0:
                            num += 1
                        if arr[x + 1][y] == 0:
                            num += 1
                    else:
                        if arr[x][y - 1] == 0:
                            num += 1
                        if arr[x][y + 1] == 0:
                            num += 1
                        for i in range(3):
                            if arr[x + 1][y - 1 + i] == 0:
                                num += 1
                elif x == m - 1:
                    if y == 0:
                        if arr[x][y + 1] == 0:
                            num += 1
                        if arr[x - 1][y] == 0:
                            num += 1
                        if arr[x - 1][y + 1] == 0:
                            num += 1
                    elif y == n - 1:
                        if arr[x][y - 1] == 0:
                            num += 1
                        if arr[x - 1][y - 1] == 0:
                            num += 1
                        if arr[x - 1][y] == 0:
                            num += 1
                    else:
                        if arr[x][y - 1] == 0:
                            num += 1
                        if arr[x][y + 1] == 0:
                            num += 1
                        for i in range(3):
                            if arr[x - 1][y - 1 + i] == 0:
                                num += 1
                else:
                    if y == 0:
                        for i in range(3):
                            if arr[x - 1 + i][y + 1] == 0:
                                num += 1
                        if arr[x - 1][y] == 0:
                            num += 1
                        if arr[x + 1][y] == 0:
                            num += 1
                    elif y == n - 1:
                        for i in range(3):
                            if arr[x - 1 + i][y - 1] == 0:
                                num += 1
                        if arr[x - 1][y] == 0:
                            num += 1
                        if arr[x + 1][y] == 0:
                            num += 1
                    else:
                        if arr[x][y - 1] == 0:
                            num += 1
                        if arr[x][y + 1] == 0:
                            num += 1
                        for i in range(3):
                            if arr[x - 1][y - 1 + i] == 0:
                                num += 1
                        for i in range(3):
                            if arr[x + 1][y - 1 + i] == 0:
                                num += 1
                if num%2 == 0 and num != 0:
                    out += 1
                num = 0
    return out

print(SurroundThe1([[1, 0, 0], [1, 1, 0], [0, 1, 0]]))
print(SurroundThe1([[1]]))