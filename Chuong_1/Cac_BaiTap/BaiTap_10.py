def in_cay_thong():
    # Số lượng dấu * ở mỗi dòng
    so_luong_sao = [1, 3, 7, 3, 5, 11]

    # In cây thông
    for sao in so_luong_sao:
        # In khoảng trắng ở đầu dòng
        print(" " * ((max(so_luong_sao) - sao) // 2), end="")
        # In dấu sao
        print("*" * sao)

    # Thêm khoảng trắng giữa hai dấu * ở 2 hàng cuối
    print(" " * ((max(so_luong_sao) - 2) // 2), end="")
    print("* *")
    print(" " * ((max(so_luong_sao) - 2) // 2), end="")
    print("* *")

# Gọi hàm để in cây thông
in_cay_thong()