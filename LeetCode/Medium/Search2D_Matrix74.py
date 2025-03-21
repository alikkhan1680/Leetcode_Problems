# Search a 2D Matrix  74

def searchMatrix(matrix, target):
    if not matrix or not matrix[0]:  # Matritsa bo'sh bo‘lsa
        return False

    m, n = len(matrix), len(matrix[0])  # Matritsaning o‘lchami (qator, ustun)
    left, right = 0, m * n - 1  # 1D indeks sifatida chegaralarni belgilaymiz

    while left <= right:
        mid = (left + right) // 2  # O‘rta indeksni topamiz
        row, col = divmod(mid, n)  # 2D indeksga o'tkazamiz
        mid_value = matrix[row][col]  # O‘rtadagi qiymatni olamiz

        if mid_value == target:
            return True
        elif mid_value < target:
            left = mid + 1  # O‘ng tomonga siljamiz
        else:
            right = mid - 1  # Chap tomonga siljamiz

    return False  # Agar topilmasa False qaytaramiz

# Test misollar
matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]

print(searchMatrix(matrix, 3))  # True
print(searchMatrix(matrix, 13)) # False






