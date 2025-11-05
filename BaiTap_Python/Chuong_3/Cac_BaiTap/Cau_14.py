a = 0
while a < 100:
    b = 0
    while b < 40:
        if (a + b) % 2 == 0:
            print('*', end=' ')
        b += 1
    print()
    a += 1

#Tổng số dòng: 100 (a từ 0 đến 99)
#Mỗi dòng có 40 cột (b từ 0 đến 39)
#Với mỗi cặp (a, b), nếu (a + b) chẵn thì in ra *
#Trong 40 số liên tiếp, số lượng số chẵn và lẻ là như nhau (20 số chẵn, 20 số lẻ).
#Vậy mỗi dòng sẽ in ra 20 dấu *.
#Tổng số dòng là 100, nên tổng số dấu * là:
#100 dòng × 20 dấu * mỗi dòng = 2000 dấu *