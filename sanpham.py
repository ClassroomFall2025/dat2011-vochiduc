class SanPham:
    def __init__(self, tensp, gia, giam_gia=0):
        self.__tensp = tensp
        self.__gia = gia
        self.__giam_gia = giam_gia

    def get_ten(self):
        return self.__tensp

    def get_ten(self, ten_sp):
        self.__tensp = ten_sp

    def get_gia(self):
        return self.__gia
    
    def set_gia(self, gia_sp):
        self.__gia = gia_sp

    def get_giam_gia(self):
        return self.__giam_gia

    def get_giam_gia(self, giam_gia_sp):
         self.__giam_gia = giam_gia_sp

    def thue_nhap_khau(self):
        return self.__gia * 0.1
    
    def nhap_thong_tin(self):
        self.__tensp = input("Nhập tên sản phẩm: ")
        self.__gia = float(input("Nhập giá sản phẩm: "))
        self.__giam_gia = float(input("Nhập giảm giá sản phẩm (%): "))

    def xuat_thong_tin(self):
        print(f"Tên sản phẩm: {self.__tensp}")
        print(f"Giá sản phẩm: {self.__gia}")
        print(f"Giảm giá: {self.__giam_gia}%")
        print(f"Thuế nhập khẩu: {self.thue_nhap_khau()}")

    def __init__(self, ten_san_pham, gia, giam_gia):
        self.ten_san_pham = ten_san_pham
        self.gia = gia
        self.giam_gia = giam_gia

    def nhap_thong_tin(self):
        self.ten_san_pham = input("tên sản phẩm")
        self.gia = float(input('GIÁ'))
        self.giam_gia = float(input("giảm giá:"))
    def thue_nhap_khau(self):
        return self.gia * 0.1
    def xuat_thong_tin(self):
        print(f"sản phẩm {self.ten_san_pham} có giá {self.gia} được giảm giá hết {self.giam_gia} và thuế nhập khẩu {self.thue_nhap_khau()}")
    def __str__(self):
        return(f"sản phẩm {self.ten_san_pham} có giá {self.gia} được giảm giá hết {self.giam_gia} và thuế nhập khẩu {self.thue_nhap_khau()}")