# Name: Nguyễn Đức Bảo Hoàng
# Student ID: 20227116
# Class: KTLT-150328
# Project: Chủ đề 1 - Xây dựng "thư viện/tiện ích" về ma trận cho phép thực hiện các chức năng
# Date: 03/06/2024

import os

class Matrix:
    file_reset = False  # Biến lớp để theo dõi nếu tệp đã được đặt lại
    # Hàm khởi tạo kết quả ban đầu
    def __init__(self, data=None):
        self.data = data or []
        if not Matrix.file_reset:
            self.reset_file()
            Matrix.file_reset = True

    # Hàm nhập ma trận từ bàn phím và đảm bảo giá trị là hợp lệ
    def input_matrix(self):
        while True:
            try:
                rows = int(input("Nhập số hàng của ma trận: "))
                cols = int(input("Nhập số cột của ma trận: "))
                if rows <= 0 or cols <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Số hàng và số cột phải là các số nguyên dương. Vui lòng nhập lại.")

        print("Nhập các phần tử của ma trận:")
        self.data = []
        for i in range(rows):
            row = []
            for j in range(cols):
                while True:
                    try:
                        element = float(input(f"Phần tử ({i+1}, {j+1}): "))
                        row.append(element)
                        break
                    except ValueError:
                        print("Giá trị phải là một số. Vui lòng nhập lại.")
            self.data.append(row)

    # Hàm nhập ma trận từ file và đảm bảo nội dung file hợp lệ
    def input_from_file(self):
        filename = os.path.join(os.path.dirname(__file__), 'input.txt')
        with open(filename, 'r') as file:
            self.data = []
            for line in file:
                cleaned_line = line.strip().replace('\u200b', '')  # Xóa các khoảng trắng không độ rộng và xóa khoảng trắng
                if cleaned_line:  # Đảm bảo dòng không trống
                    try:
                        row = list(map(float, cleaned_line.split()))
                        self.data.append(row)
                    except ValueError:
                        print("File chứa ký tự không hợp lệ. Vui lòng kiểm tra lại nội dung file.")
                        self.data = []
                        break

    # Hàm đặt lại file trước khi ghi
    def reset_file(self):
        filename = os.path.join(os.path.dirname(__file__), 'output.txt')
        open(filename, 'w').close()  # Mở file ở chế độ ghi để xóa nội dung file

    # Hàm ghi kết quả ra file
    def save_to_file(self, operation_name=""):
        filename = os.path.join(os.path.dirname(__file__), 'output.txt')
        with open(filename, 'a') as file:
            if operation_name:
                file.write(f"{operation_name}\n")
            for row in self.data:
                file.write(' '.join(map(str, row)) + '\n')
            if operation_name:
                file.write('\n')

    # Hàm hiển thị ma trận ra màn hình
    def print_matrix(self):
        for row in self.data:
            print(' '.join(map(str, row)))

    # Hàm kiểm tra ma trận có vuông hay không
    def is_square(self):
        return all(len(row) == len(self.data) for row in self.data)

    # Hàm thực hiện chức năng nhân ma trận với một số nguyên được nhập từ bàn phím  
    def multiply_by_scalar(self, scalar):
        result = Matrix([[element * scalar for element in row] for row in self.data])
        return result

    # Hàm thực hiện chức năng tính ma trận chuyển vị
    def transpose(self):
        result = Matrix([[self.data[j][i] for j in range(len(self.data))] for i in range(len(self.data[0]))])
        return result

    # Hàm tính định thức của ma trận
    def determinant(self):
        
        if not self.is_square():
            raise ValueError("Chỉ có thể tính định thức của ma trận vuông.")
        if len(self.data) == 1:
            return self.data[0][0]
        if len(self.data) == 2:
            return self.data[0][0] * self.data[1][1] - self.data[0][1] * self.data[1][0]
        det = 0
        for c in range(len(self.data)):
            det += ((-1) ** c) * self.data[0][c] * Matrix(minor(self.data, 0, c)).determinant()
        return det

    # Hàm thực hiện chức năng tính ma trận nghịch đảo
    def invert(self):
        if not self.is_square():
            raise ValueError("Chỉ có thể tính ma trận nghịch đảo của ma trận vuông.")
        det = self.determinant()
        if (det == 0):
            raise ValueError("Ma trận không có ma trận nghịch đảo (Do định thức bằng 0).")
        cofactors = cofactor(self.data)
        cofactors = Matrix(cofactors).transpose().data
        for r in range(len(cofactors)):
            for c in range(len(cofactors[0])):
                cofactors[r][c] = cofactors[r][c] / det
        return Matrix(cofactors)

    # Hàm thực hiện chức năng cộng hai ma trận với ma trận thứ 2 được nhập từ bàn phím
    def add(self, other):
        if len(self.data) != len(other.data) or len(self.data[0]) != len(other.data[0]):
            raise ValueError("Hai ma trận phải cùng kích thước để cộng.")
        return Matrix([[self.data[i][j] + other.data[i][j] for j in range(len(self.data[0]))] for i in range(len(self.data))])

# Hàm này tính ma trận con bằng cách bỏ đi hàng i và cột j của ma trận gốc
def minor(matrix, i, j):
    return [row[:j] + row[j+1:] for row in (matrix[:i] + matrix[i+1:])]

# Hàm này tính ma trận phụ đại số (cofactor matrix)
def cofactor(matrix):
    cofactors = []
    for r in range(len(matrix)):
        cofactorRow = []
        for c in range(len(matrix)):
            minor_det = Matrix(minor(matrix, r, c)).determinant()
            cofactorRow.append(((-1) ** (r + c)) * minor_det)
        cofactors.append(cofactorRow)
    return cofactors
