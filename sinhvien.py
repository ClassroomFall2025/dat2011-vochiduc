class SinhVienPoly:
    def __init__(self, TenSinhVien, nganh):
        self.TenSinhVien = TenSinhVien
        self.nganh = nganh

    def get_diem(self):
        return 0

    def get_hoc_luc(self):
        diem = self.get_diem()
        if diem < 5:
            return "Yếu"
        elif diem < 7:
            return "Trung bình"
        elif diem < 8:
            return "Khá"
        elif diem < 9:
            return "Giỏi"
        else:
            return "Xuất sắc"

    def xuat(self):
        print(f"Họ tên: {self.TenSinhVien}")
        print(f"Ngành: {self.nganh}")
        print(f"Điểm: {self.get_diem():.2f}")
        print(f"Học lực: {self.get_hoc_luc()}")
        print("-" * 30)


class SinhVienIT(SinhVienPoly):
    def __init__(self, TenSinhVien, java, html, css):
        super().__init__(TenSinhVien, "IT")
        self.java = java
        self.html = html
        self.css = css

    def get_diem(self):
        return (2 * self.java + self.html + self.css) / 4

class SinhVienBiz(SinhVienPoly):
    def __init__(self, TenSinhVien, marketing, sales):
        super().__init__(TenSinhVien, "Biz")
        self.marketing = marketing
        self.sales = sales

    def get_diem(self):
        return (2 * self.marketing + self.sales) / 3


class QuanLySinhVien:
    def __init__(self):
        self.danh_sach = []

    def nhap_sinh_vien(self):
        while True:
            loai = input("Nhập loại sinh viên (IT/Biz, hoặc 0 để dừng): ").strip().lower()
            if loai == "0":
                break

            ten = input("Nhập tên sinh viên: ")

            if loai == "it":
                java = float(input("Điểm Java: "))
                html = float(input("Điểm HTML: "))
                css = float(input("Điểm CSS: "))
                sv = SinhVienIT(ten, java, html, css)
            elif loai == "biz":
                marketing = float(input("Điểm Marketing: "))
                sales = float(input("Điểm Sales: "))
                sv = SinhVienBiz(ten, marketing, sales)
            else:
                print(" Loại sinh viên không hợp lệ!")
                continue

            self.danh_sach.append(sv)
            print(" Đã thêm sinh viên thành công!")

    def xuat_ds(self):
        if not self.danh_sach:
            print("Danh sách trống.")
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
        from sinhvien import QuanLySinhVien

ql = QuanLySinhVien()

menu = {
    "1": "Nhập danh sách sinh viên",
    "2": "Xuất thông tin danh sách sinh viên",
    "3": "Xuất danh sách sinh viên có học lực giỏi",
    "4": "Sắp xếp danh sách sinh viên theo điểm",
    "5": "Kết thúc"
}

while True:
    print("\n===== MENU QUẢN LÝ SINH VIÊN =====")
    for k, v in menu.items():
        print(f"{k}. {v}")

    lua_chon = input("Nhập lựa chọn: ")

    match lua_chon:
        case "1":
            ql.nhap_sinh_vien()
        case "2":
            ql.xuat_ds()
        case "3":
            ql.xuat_sv_gioi()
        case "4":
            ql.sap_xep_theo_diem()
        case "5":
            print("Kết thúc chương trình.")
            break
        case _:
            print(" Lựa chọn không hợp lệ, vui lòng nhập lại.")
            print([sv.TenSinhVien for sv in ql.danh_sach])