class SinhVienPoly:
    def __init__(self, TenSinhVien, nganh):
        self.ho_ten = TenSinhVien
        self.nganh_hoc = nganh

    def get_diem(self):
        pass

    def get_hoc_luc(self):
        if self.get_diem() >= 9 and self.get_diem() <= 10:
            hoc_luc = "Xuất sắc"
        elif self.get_diem() >= 8:
            hoc_luc = "Giỏi"
        elif self.get_diem() >= 7:
            hoc_luc = "Khá"
        elif self.get_diem() >= 5:
            hoc_luc = "Trung bình"
        elif self.get_diem() >= 0:
            hoc_luc = "Yếu"
        else:
            print("diem khong hop le")
        return hoc_luc

    def __str__(self):
        return f"({self.ho_ten}, {self.nganh_hoc}, {self.get_diem()}, {self.get_hoc_luc()})"
    def xuat(self):
        print(f"{self.ho_ten}, {self.nganh_hoc}, {self.get_diem()}, {self.get_hoc_luc()})")


class SinhVienIT(SinhVienPoly):
    def __init__(self, TenSinhVien, nganh_hoc, java, html, css):
        super().__init__(TenSinhVien, nganh_hoc)
        self.java = java
        self.html = html
        self.css = css

    def get_diem(self):
        return (2 * self.java + self.html + self.css) / 4

class SinhVienBiz(SinhVienPoly):
    def __init__(self, TenSinhVien, nganh_hoc, marketing, sales):
        super().__init__(TenSinhVien, nganh_hoc)
        self.marketing = marketing
        self.sales = sales

    def get_diem(self):
        return (2 * self.marketing + self.sales) / 3