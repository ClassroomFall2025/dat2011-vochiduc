class hinh:
    def __init__(self, dai, rong):
        self.dai = dai
        self.rong = rong
    def tinh_chu_vi(self):
        return (self.dai + self.rong) * 2
    def tinh_dien_tich(self):
        return self.dai * self.rong

    def xuat(self):
        print(f"chiều dài hình chữ nhật :{self.dai}")
        print(f"chiều rộng hình chữ nhật :{self.rong}")
        print(f"chu vi hình chữ nhật :{self.tinh_chu_vi()}")
        print(f"diện tích hình chữ nhật :{self.tinh_dien_tich()}")
        

class hinhvuong (hinh):
    def __init__(self, canh):
        self.canh = canh
        super().__init__(self.canh, self.canh)
        
    def xuat(self):
        print(f"cạnh hình vuông :{self.canh}")
        print(f"chu vi hình vuông :{self.tinh_chu_vi()}")
        print(f"diện tích hình vuông :{self.tinh_dien_tich()}") 
    