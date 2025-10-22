class NhanVien:
    def __init__(self, ma_nv, ho_ten, luong):
        self.ma_nv = ma_nv
        self.ho_ten = ho_ten
        self.luong = luong

    def get_thu_nhap(self):
        return self.luong

    def __str__(self):
        return f"{self.ma_nv:<10} | {self.ho_ten:<25} | {self.luong:>10,.0f}"


class TiepThi(NhanVien):
    def __init__(self, ma_nv, ho_ten, luong, doanh_so, hoa_hong):
        super().__init__(ma_nv, ho_ten, luong)
        self.doanh_so = doanh_so
        self.hoa_hong = hoa_hong

    def get_thu_nhap(self):
        return self.luong + self.doanh_so * self.hoa_hong


class TruongPhong(NhanVien):
    def __init__(self, ma_nv, ho_ten, luong, phu_cap):
        super().__init__(ma_nv, ho_ten, luong)
        self.phu_cap = phu_cap

    def get_thu_nhap(self):
        return self.luong + self.phu_cap


class QuanLyNhanVien:
    def __init__(self):
        self.ds_nv = []

   
    def nhap_danh_sach(self):
        while True:
            print("\n1. Nhân viên hành chính")
            print("2. Nhân viên tiếp thị")
            print("3. Trưởng phòng")
            print("0. Thoát nhập")
            chon = input("Chọn loại nhân viên: ")

            if chon == "0":
                break

            ma_nv = input("Mã NV: ")
            ho_ten = input("Họ tên: ")
            luong = float(input("Lương: "))

            if chon == "1":
                nv = NhanVien(ma_nv, ho_ten, luong)
            elif chon == "2":
                doanh_so = float(input("Doanh số: "))
                hoa_hong = float(input("Hoa hồng (vd 0.05): "))
                nv = TiepThi(ma_nv, ho_ten, luong, doanh_so, hoa_hong)
            elif chon == "3":
                phu_cap = float(input("Phụ cấp: "))
                nv = TruongPhong(ma_nv, ho_ten, luong, phu_cap)
            else:
                print("Loại không hợp lệ!")
                continue

            self.ds_nv.append(nv)
            print(" Đã thêm:", ho_ten)

    def hien_thi_danh_sach(self):
        print(f"\n{'Mã NV':<10} | {'Họ tên':<25} | {'Thu nhập':>10}")
        print("-" * 50)
        for nv in self.ds_nv:
            print(f"{nv.ma_nv:<10} | {nv.ho_ten:<25} | {nv.get_thu_nhap():>10,.0f}")

    
    def tim_theo_ma(self):
        ma = input("Nhập mã NV cần tìm: ")
        for nv in self.ds_nv:
            if nv.ma_nv == ma:
                print(" Thông tin:", nv)
                return
        print(" Không tìm thấy!")

    
    def xoa_nhan_vien(self):
        ma = input("Nhập mã NV cần xóa: ")
        for nv in self.ds_nv:
            if nv.ma_nv == ma:
                self.ds_nv.remove(nv)
                print("🗑️ Đã xóa nhân viên:", ma)
                return
        print(" Không tìm thấy mã nhân viên!")

   
    def sap_xep_theo_ten(self):
        self.ds_nv.sort(key=lambda nv: nv.ho_ten.split()[-1])
        print(" Đã sắp xếp theo tên.")
        self.hien_thi_danh_sach()

   
    def sap_xep_theo_thu_nhap(self):
        self.ds_nv.sort(key=lambda nv: nv.get_thu_nhap(), reverse=True)
        print(" Đã sắp xếp theo thu nhập.")
        self.hien_thi_danh_sach()