class NhanVien:
    def __init__(self, ma_nv, ho_ten, Luong):
        self.ma_nv = ma_nv
        self.ho_ten = ho_ten
        self.Luong = Luong
        def get_thu_nhap(self):
            return self.Luong
        def __str__(self):
            return f"{self.ma_nv :<10} /| {self.ho_ten :<25} /| {self.Luong :>25}"
class TiepThi(NhanVien):
    def __init__(self, ma_nv, ho_ten , Luong , doanh_so , hoa_hong):
                super ().__init__(ma_nv, ho_ten , Luong)
                self.ho_ten = ho_ten
                self.doanh_so = doanh_so
                self.hoa_hong = hoa_hong
    def get_thu_nhap(self):
                return self.Luong + self.doanh_so *  self.hoa_hong
class TruongPhong(NhanVien):
    def __init__(self , ma_nv , ho_ten , Luong , phu_cap):
            super ().__init__(ma_nv , ho_ten , Luong)
            self . phu_cap = phu_cap
    def get_thu_nhap(self):
            return self .Luong + self.phu_cap
class QuanLyNhanVien(NhanVien):
      def __init__(self, ma_nv, ho_ten, Luong):
            super().__init__(ma_nv, ho_ten, Luong)
            self.ds_nv=[]
            def them_nhan_vien(self, nhan_vien):
                self.ds_nv.append(nhan_vien)
            def get_thu_nhap(self):
                return sum(nv.get_thu_nhap() for nv in self.ds_nv)
            def hien_thi_danh_sach(self):
                print(f"{'Mã NV':<10} | {'Họ tên':<25} | {'Thu nhập':>15}")
                print("-" * 55)
                for nv in self.ds_nv:
                    print(nv)
class NhanVien:
    def __init__(self, ma_nv, ho_ten, Luong):
        self.ma_nv = ma_nv
        self.ho_ten = ho_ten
        self.Luong = Luong
    def get_thu_nhap(self):
        return self.Luong
    def __str__(self):
        return f"{self.ma_nv :<10} | {self.ho_ten :<25} | {self.Luong :>15,.0f}"
class TiepThi(NhanVien):
    def __init__(self, ma_nv, ho_ten , Luong , doanh_so , hoa_hong):
        super ().__init__(ma_nv, ho_ten , Luong)
        self.doanh_so = doanh_so
        self.hoa_hong = hoa_hong
    def get_thu_nhap(self):
        return self.Luong + self.doanh_so *  self.hoa_hong
class TruongPhong(NhanVien):
    def __init__(self , ma_nv , ho_ten , Luong , phu_cap):
        super ().__init__(ma_nv , ho_ten , Luong)
        self.phu_cap = phu_cap
    def get_thu_nhap(self):
        return self.Luong + self.phu_cap
class QuanLyNhanVien:
    def __init__(self):
        self.ds_nv=[]
    def them_nhan_vien(self, nhan_vien):
        self.ds_nv.append(nhan_vien)
    def get_thu_nhap(self):
        return sum(nv.get_thu_nhap() for nv in self.ds_nv)
    def hien_thi_danh_sach(self):
        print(f"{'Mã NV':<10} | {'Họ tên':<25} | {'Thu nhập':>15}")
        print("-" * 55)
        for nv in self.ds_nv:
            print(f"{nv.ma_nv :<10} | {nv.ho_ten :<25} | {nv.get_thu_nhap() :>15,.0f}")
    def xuat_danh_sach(self):
        print(f"{'Mã NV':<10} | {'Họ tên':<25} | {'Lương':>15}")
        print("-" * 55)
        for nv in self.ds_nv:
            print(nv)
        print("-" * 55)
        def xuat_danh_sach(self):
                print(f"{'Mã NV':<10} | {'Họ tên':<25} | {'Lương':>15}")
                print("-" * 55)
        for nv in self.ds_nv:
                print(nv)
                print("-" * 55)
    
            
      
