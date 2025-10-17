from sinhvienpoly import *
class QuanLySinhVien:
    def __init__(self):
        self.danh_sach = []

    def nhap_sinh_vien(self):
        while True:
            loai_sinh_vien = input("Nhập loại sinh viên (IT/Biz, hoặc 0 để dừng): ").strip().lower()
            if loai_sinh_vien == "0":
                print(" Dừng nhập sinh viên.")
                break

            ten_sinh_vien = input("Nhập tên sinh viên: ")

            if loai_sinh_vien == "it":
                java = float(input("Điểm Java: "))
                html = float(input("Điểm HTML: "))
                css = float(input("Điểm CSS: "))
                sv = SinhVienIT(ten_sinh_vien, loai_sinh_vien, java, html, css)
                self.danh_sach.append(sv)
            elif loai_sinh_vien == "biz":
                marketing = float(input("Điểm Marketing: "))
                sales = float(input("Điểm Sales: "))
                sv = SinhVienBiz(ten_sinh_vien, loai_sinh_vien, marketing, sales)
                self.danh_sach.append(sv)
            else:
                print(" Loại sinh viên không hợp lệ!")

        return self.danh_sach

    def xuat_ds(self):
        if not self.danh_sach:
            print(" Danh sách trống.")
            return
        print("\n=== DANH SÁCH SINH VIÊN ===")
        for sv in self.danh_sach:
            sv.xuat()

    def xuat_sv_gioi(self):
        ds_gioi = [sv for sv in self.danh_sach if sv.get_hoc_luc() == "Giỏi"]
        if not ds_gioi:
            print(" Không có sinh viên giỏi.")
            return
        print("\n=== SINH VIÊN GIỎI ===")
        for sv in ds_gioi:
            sv.xuat()

    def sap_xep_theo_diem(self):
        self.danh_sach.sort(key=lambda sv: sv.get_diem(), reverse=True)
        print(" Đã sắp xếp danh sách theo điểm giảm dần.")