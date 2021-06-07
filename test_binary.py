def find_elem_matrix_bool(m1, value):
    found = False
    row = 0
    col = len(m1[0]) -1
    count = 0
    while row < len(m1) and col >= 0:
        count += 1
        if m1[row][col] == value:
            found = True
            break
        elif m1[row][col] > value:
            col -= 1
        else:
            row += 1
    return found, count

def searching_in_a_mat(m1, value):
    rows = len(m1)
    cols = len(m1[0])
    lo = 0
    hi = rows * cols
    while lo < hi:
        mid = (lo + hi) // 2
        row = mid // cols
        col = mid % cols
        v = m1[row][col]
        if v == value:
            return True
        elif v > value:
            hi = mid
        else:
            lo = mid + 1
    return False

def find_sqrt_bin_search(n, error=0.001):
    lower = n < 1 and n or 1
    upper = n < 1 and 1 or n
    mid = lower + (upper - lower) / 2.0
    square = mid * mid
    while abs(square - n) > error:
        if square < n:
            lower = mid
        else:

            upper = mid
        mid = lower + (upper - lower) / 2.0
        square = mid * mid
    return mid





def test_searching_in_a():
    a = [[1, 3, 5], [7, 9, 11], [13, 15, 17]]
    print(searching_in_a_mat(a, 13))

if __name__ == '__main__':
    mat = [[1,2,8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]
    print(find_elem_matrix_bool(mat, 8))
    test_searching_in_a()
    a = 2
    b = 9
    print(find_sqrt_bin_search(a))