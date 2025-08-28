import sys

# Kiểm tra nếu có truyền tham số
if len(sys.argv) > 1:
    # sys.argv[0] là tên file, nên chuỗi bắt đầu từ sys.argv[1]
    chuoi = " ".join(sys.argv[1:])
    print("Chuỗi bạn nhập là:", chuoi)
else:
    print("Bạn chưa nhập chuỗi từ tham số dòng lệnh!")