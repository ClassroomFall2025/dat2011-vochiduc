class sanpham:
    def __init__(self, ten_san_pham, gia, Giam_gia):
        self.__ten_san_pham = ten_san_pham
        self.__gia = gia
        self.__Giam_gia = Giam_gia

    # def doc_giam_gia(self):
    #     return self.__Giam_gia
    # def ghi_giam_gia(self,giam_gia_moi):
    #     self.__Giam_gia = giam_gia_moi
    def get_ten_sp(self):
        return self.__ten_san_pham
    def set_ten_sp(self, ten_sp):
        self.__ten_san_pham = ten_sp
    def get_gia_sp(self):
        return self.__gia
    def set_gia_sp(self, gia_sp):
        self.__gia = gia_sp
    def get_giam_gia(self):     
        return self.__Giam_gia
    def set_giam_gia(self, giam_gia):
        self.__Giam_gia = giam_gia
    def thue_nhap_khau(self):
        return self.gia * 0.1
    def nhap_thong_tin(self):
        self.ten_san_pham=input(" ten san pham:")
        self.gia=float(input("gia san pham:"))
        self.__Giam_gia=float(input("giam gia:"))
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
    def _str_(self):
        return(f"sản phẩm {self.ten_san_pham} có giá {self.gia} được giảm giá hết {self.giam_gia} và thuế nhập khẩu {self.thue_nhap_khau()}")