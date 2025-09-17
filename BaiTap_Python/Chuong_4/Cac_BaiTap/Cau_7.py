from math import sqrt, pow
def DoDai (xA, xB, yA, yB):
    return sqrt(pow((xB-xA),2)+pow((yB-yA),2))
xA =int (input("Nhập tọa độ xA: "))
xB =int (input("Nhập tọa độ xB: "))
yA =int (input("Nhập tọa độ yA: "))
yB =int (input("Nhập tọa độ yB: "))
print ("Độ dài AB là: ", DoDai(xA, xB, yA, yB))