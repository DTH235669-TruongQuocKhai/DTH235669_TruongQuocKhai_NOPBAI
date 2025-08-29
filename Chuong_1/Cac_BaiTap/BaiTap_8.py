rows = 4   # số dòng
cols = 5   # số cột

for i in range(rows):
    for j in range(cols):
        # In * ở dòng đầu, dòng cuối, cột đầu, cột cuối
        if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()