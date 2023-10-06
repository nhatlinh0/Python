from hinh_hoc import HinhHoc
from hinh_tron import HinhTron
from hinh_chu_nhat import HinhChuNhat
from hinh_vuong import HinhVuong
from loai_hinh import LoaiHinh


class DanhSachHinhHoc:
    def __init__(self) -> None:
        self.dshh = []

    def themHinhHoc(self, hh: HinhHoc):
        self.dshh.append(hh)

    def Xuat(self):
        for hh in self.dshh:
            print(hh)
    
    def timDienTichLonNhat(self):
        max = 0
        for hh in self.dshh:
            if(hh.tinhDienTich() > max):
                max = hh.tinhDienTich()
        return max
    
    def timDienTichNhoNhat(self):
        min = self.timDienTichLonNhat()
        for hh in self.dshh:
            if(hh.tinhDienTich() < min):
                min = hh.tinhDienTich()
        return min
    
    def timHinhCoDienTichLonNhat(self):
        dsMoi = DanhSachHinhHoc()
        for hh in self.dshh:
            if(hh.tinhDienTich() == self.timDienTichLonNhat()):
                dsMoi.dshh.append(hh)
        return dsMoi
    
    def timHinhCoDienTichNhoNhat(self):
        dsMoi = DanhSachHinhHoc()
        for hh in self.dshh:
            if(hh.tinhDienTich() == self.timDienTichNhoNhat()):
                dsMoi.dshh.append(hh)
        return dsMoi
    
    def timHinhTronNhoNhat(self):
        dsMoi = DanhSachHinhHoc()
        min = self.timDienTichLonNhat()
        for hh in self.dshh:
            if isinstance(hh, HinhTron):
                if(hh.tinhDienTich() < min):
                    min = hh.tinhDienTich()

        for hh in self.dshh:
            if isinstance(hh, HinhTron):
                if(hh.tinhDienTich() == min):
                    dsMoi.dshh.append(hh)
        return dsMoi

    def sapGiamTheoDienTich(self):
        self.dshh.sort(reverse=True, key = lambda x: x.tinhDienTich())

    def DemSoLuongHinh(self, kieu: LoaiHinh):
        match(kieu):
            case 1:
                count = 0
                for hh in self.dshh:
                    count += 1  

            case 2:
                count = 0
                for hh in self.dshh:
                    if(isinstance(hh, HinhTron)):
                        count += 1

            case 3:
                count = 0
                for hh in self.dshh:
                    if(isinstance(hh, HinhVuong)):
                        count += 1       

            case 4:
                count = 0
                for hh in self.dshh:
                    if(isinstance(hh, HinhChuNhat)):
                        count += 1
            case _:
                print("You do not have any access to the code")
        return count
    
    def timHinhCoDienTichLonNhatTheoLoai(self, kieu: LoaiHinh):
        ds = DanhSachHinhHoc()
        match(kieu):
            case 1:
                ds = self.timHinhCoDienTichLonNhat()
            
            case 2:
                max = 0
                for hh in self.dshh:
                    if(hh.tinhDienTich() > max and isinstance(hh, HinhTron)):
                        max = hh.tinhDienTich()

                for hh in self.dshh:
                    if(hh.tinhDienTich() == max and isinstance(hh, HinhTron)):
                        ds.dshh.append(hh)

            case 3:
                max = 0
                for hh in self.dshh:
                    if(hh.tinhDienTich() > max and isinstance(hh, HinhVuong)):
                        max = hh.tinhDienTich()
                        
                for hh in self.dshh:
                    if(hh.tinhDienTich() == max and isinstance(hh, HinhVuong)):
                        ds.dshh.append(hh)
            
            case 4:
                max = 0
                for hh in self.dshh:
                    if(hh.tinhDienTich() > max and isinstance(hh, HinhChuNhat)):
                        max = hh.tinhDienTich()
                        
                for hh in self.dshh:
                    if(hh.tinhDienTich() == max and isinstance(hh, HinhChuNhat)):
                        ds.dshh.append(hh)
            case _:
                print("You do not have any access to the code")
        return ds
    
    def xoaHinhTheoLoai(self, kieu:LoaiHinh):
        match(kieu):
            case 1:
                for hh in self.dshh:
                    self.dshh.remove(hh)

            case 2:
                a = True
                ds = len(self.dshh)
                dsMoi = len(self.dshh)
                while(a):
                    for hh in self.dshh:
                        if (isinstance(hh, HinhTron)):
                            self.dshh.remove(hh)
                            dsMoi = len(self.dshh)
                    if(ds != dsMoi):
                        ds = dsMoi
                    else: 
                        a = False
                            

            
            case 3:
                a = True
                ds = len(self.dshh)
                dsMoi = len(self.dshh)
                while(a):
                    for hh in self.dshh:
                        if (isinstance(hh, HinhVuong)):
                            self.dshh.remove(hh)
                            dsMoi = len(self.dshh)
                    if(ds != dsMoi):
                        ds = dsMoi
                    else: 
                        a = False

            case 4:
                a = True
                ds = len(self.dshh)
                dsMoi = len(self.dshh)
                while(a):
                    for hh in self.dshh:
                        if (isinstance(hh, HinhChuNhat)):
                            self.dshh.remove(hh)
                            dsMoi = len(self.dshh)
                    if(ds != dsMoi):
                        ds = dsMoi
                    else: 
                        a = False
            
            case _:
                print("You do not have any access to the code")

    def xuatHinhTheoChieuTangGiam(self, kieu:LoaiHinh, tang: bool):
        match(kieu):
            case 1:
                self.dshh.sort(key = lambda x: x.tinhDienTich(), reverse= not(tang))
            
            case 2:
                self.dshh.sort(key = lambda x: x.tinhDienTich() if(isinstance(x, HinhTron)) else 0, reverse=not(tang))

            case 3:
                self.dshh.sort(key = lambda x: x.tinhDienTich() if(isinstance(x, HinhVuong)) else 0, reverse=not(tang))

            case 4:
                self.dshh.sort(key = lambda x: x.tinhDienTich() if(isinstance(x, HinhChuNhat)) else 0, reverse=not(tang))
            
            case _:
                print("You do not have any access to the code")
    
    def tinhTongDienTichTheoHinh(self, kieu: LoaiHinh):
        sum = 0
        match(kieu):
            case 1:
                self.tinhTongDienTich()
            
            case 2:
                for hh in self.dshh:
                    if(isinstance(hh, HinhTron)):
                        sum += hh.tinhDienTich()
            
            case 3:
                for hh in self.dshh:
                    if(isinstance(hh, HinhVuong)):
                        sum += hh.tinhDienTich()
            
            case 4:
                for hh in self.dshh:
                    if(isinstance(hh, HinhChuNhat)):
                        sum += hh.tinhDienTich()
            
            case _:
                print("You do not have any access to the code")
        return sum 
    
    def tinhTongDienTich(self):
        sum = 0 
        for hh in self.dshh:
            sum += hh.tinhDienTich()
        return sum
    
    def timVTCuaHinh(self, hh: HinhHoc):
        for i in range(len(self.dshh)):
            if(self.dshh[i]._canh == hh._canh and self.dshh[i].tinhDienTich() == hh.tinhDienTich()):
                return i
        return -1
    
    def xoaHinhTaiViTri(self, vt: int):
        if(vt < len(self.dshh)):
            self.dshh.pop(vt)
            return True
        return False

    def timHinhTheoDienTich(self, dt: float):
        dsMoi = DanhSachHinhHoc()
        for hh in self.dshh:
            if(hh.tinhDienTich() == dt):
                dsMoi.dshh.append(hh)
        return dsMoi
    
    def xoaHinh(self, hh: HinhHoc):
        for h in self.dshh:
            if(h == hh):
                self.dshh.remove(hh)
                
                
            
