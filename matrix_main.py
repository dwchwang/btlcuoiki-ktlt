# Name: Nguyễn Đức Bảo Hoàng
# Student ID: 20227116
# Class: KTLT-150328
# Project: Chủ đề 1 - Xây dựng "thư viện/tiện ích" về ma trận cho phép thực hiện các chức năng
# Date: 03/06/2024

from matrix_lib import Matrix

def main():
    matrix = Matrix()

    while True:
        print("--------------" + "CHUONG TRINH MA TRAN" + "--------------")
        print("Chọn thao tác:")
        print("1. Nhập ma trận từ bàn phím")
        print("2. Nhập ma trận từ file")
        print("3. Nhân ma trận với 1 số")
        print("4. Tính ma trận chuyển vị")
        print("5. Tính ma trận nghịch đảo")
        print("6. Cộng 2 ma trận")
        print("7. Thoát")
        print("------------------------------------------------")

        choice = input("Lựa chọn của bạn: ")

        if choice == '1':
            matrix.input_matrix()
            print("Ma trận đã nhập:")
            matrix.print_matrix()
            matrix.save_to_file("Ma trận ban đầu: ")

        elif choice == '2':
            matrix.input_from_file()
            print("Ma trận đã đọc từ file:")
            matrix.print_matrix()
            matrix.save_to_file("Ma trận ban đầu: ")

        elif choice == '3':
            scalar = float(input("Nhập số để nhân với ma trận: "))
            result = matrix.multiply_by_scalar(scalar)
            print("Kết quả của phép nhân:")
            result.print_matrix()
            result.save_to_file("Ma trận sau khi nhân với " + str(scalar) + ":")

        elif choice == '4':
            result = matrix.transpose()
            print("Ma trận chuyển vị:")
            result.print_matrix()
            result.save_to_file("Ma trận chuyển vị: ")

        elif choice == '5':
            try:
                result = matrix.invert()
                print("Ma trận nghịch đảo:")
                result.print_matrix()
                result.save_to_file("Ma trận nghịch đảo: ")
            except ValueError as e:
                print(f"Lỗi: {e}")

        elif choice == '6':
            print("Nhập ma trận thứ hai:")
            matrix2 = Matrix()
            matrix2.input_matrix()
            print("Ma trận thứ hai:")
            matrix2.print_matrix()
            try:
                result = matrix.add(matrix2)
                print("Kết quả của phép cộng:")
                result.print_matrix()
                result.save_to_file("Tổng hai ma trận: ")
            except ValueError as e:
                print(f"Lỗi: {e}")

        elif choice == '7':
            print("Các kết quả của Ma trận đã được lưu vào File output.txt.\nThoát chương trình!!!")
            break

        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn lại.")

if __name__ == "__main__":
    main()
