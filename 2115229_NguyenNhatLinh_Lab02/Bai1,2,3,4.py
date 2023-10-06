import datetime

class SinhVien:
    truong = "Đại học Đà Lạt"
    
    def __init__(self, maSo: int, hoTen: str, ngaySinh: datetime) -> None: 
        self.__maSo = maSo
        self.__hoTen = hoTen
        self.__ngaySinh = ngaySinh

    @property 
    def maSo(self):
        return self.__maSo
    
    @maSo.setter 
    def maSo(self, maso):
        if self.laMaSoHopLe(maso):
            self.__maSo = maso

    @staticmethod
    def laMaSoHopLe(maso: int):
        return len(str(maso)) == 7

    @classmethod
    def doiTenTruong(self, tenmoi):
        self.truong = tenmoi

    def __str__(self) -> str:
        return f"{self.maSo}\t{self.hoTen}\t{self.ngaySinh}"
    
    def xuat(self):
        print(f"{self.maSo}\t{self.hoTen}\t{self.ngaySinh}")

class DanhSachSv:
    def __init__(self) -> None:
        self.dssv = []
    
    def themSinhVien(self, sv: SinhVien):
        self.dssv.append(sv)

    def xuat(self):
        for sv in self.dssv:
            print(sv)
    
    def timSvTheoMssv(self, mssv: int):
        return [sv for sv in self.dssv if sv.mssv == mssv] 
    
    def timVTSvTheoMssv(self, mssv: int):
        for i in range(len(self.dssv)):
            if self.dssv[i].mssv == mssv:
                return i
        return -1
    
    def xoaSvTheoMssv(self, maSo: int) -> bool:
        vt = self.timVTSvTheoMssv(maSo)
        if vt != -1:
            del self.dssv[vt] 
            return True
        else: 
            return False
    
    def timSvTheoTen(self, ten: str):
        for sv in self.dssv:
            n = sv.hoTen.split()
            length = len(n) - 1 
            if(sv.hoTen.split()[length] == ten):
                return 1
        return -1



    def timSvSinhTruocNgay(self, ngay: datetime):
        for sv in self.dssv:
            if(sv.__ngaySinh < ngay):
                return 1
        return -1

    @staticmethod
    def DocFile(filename: str):
        f = open("filename","r")
        print(f.read())

    def sapXepDssvTangTheoHo(self):
        for i in range(len(self.dssv-1)):
            for j in range(i, len(self.dssv)):
                if(self.dssv[i].hoTen.split()[0] > self.dssv[j].hoTen.split()[0]):
                    temp =  self.dssv[i]
                    self.dssv[i] = self.dssv[j]
                    self.dssv[j] = temp
    
    def sapXepDssvGiamTheoHo(self):
        for i in range(len(self.dssv-1)):
            for j in range(i, len(self.dssv)):
                if(self.dssv[i].hoTen.split()[0] < self.dssv[j].hoTen.split()[0]):
                    temp =  self.dssv[i]
                    self.dssv[i] = self.dssv[j]
                    self.dssv[j] = temp

class PhanSo:
     
    def __init__(self, tu = None, mau = None) -> None:
        if (mau is None):
            self.__tu = tu
            self.__mau = 1
        elif (tu is None and mau is None):
            self.__tu 
            self.__mau
        else:
            self.__tu = tu
            self.__mau = mau

    @property 
    def tu(self):
        return self.__tu
    
    @tu.setter
    def tu(self, value):
        self.__tu = value

    @property
    def mau(self):
        return self.__mau

    @mau.setter 
    def mau(self, value):
        if(value != 0 ):
            self.__mau = value
        else:
            raise ValueError("Mẫu phải khác 0")

    def tim_ucln(self, a,b):
        while b:
            a, b = b, a % b
        return a

    def rutGon(self):
        ucln = self.tim_ucln(self.__tu, self.__mau)
        self.__tu = self.__tu // ucln
        self.__mau = self.__mau // ucln

    def __add__(self, ps):
        tuso = self.__tu * ps.__mau + self.__mau * ps.__tu
        mauso = self.__mau * ps.__mau
        kq =  PhanSo(tuso, mauso)
        kq.rutGon()
        return kq


    def __sub__(self, ps ):
        tuso = self.__tu * ps.__mau - self.__mau * ps.__tu
        mauso = self.__mau * ps.__mau
        kq =  PhanSo(tuso, mauso)
        kq.rutGon()
        return kq

    def __mul__(self, ps ):
        tuso = self.__tu * ps.__tu
        mauso = self.__mau * ps.__mau
        kq = PhanSo(tuso, mauso)
        kq.rutGon()
        return kq

    def __truediv__(self, ps):
        tuso =  self.__tu  * ps.__mau
        mauso = self.__mau * ps.__tu
        kq =  PhanSo(tuso, mauso)
        kq.rutGon()
        return kq
    
    def value(self, tu, mau):
        return float(tu/mau)
        
    
    def __str__(self) -> str:
        return f"{self.__tu} / {self.__mau}"

class DanhSachPhanSo:
    def __init__(self) -> None:
        self.dsPhanSo = []

    def DemSoAm(self):
        count = 0
        for ps in self.dsPhanSo:
            if (not((ps.tu < 0 and ps.mau < 0) or (ps.tu > 0 and ps.mau > 0))):
                count += 1
        return count
    
    def TimPhanSoDuongNhoNhat(self):
        min = None
        for ps in self.dsPhanSo:
            if(ps.tu < 0 and ps.mau < 0) or (ps.tu >= 0 and ps.mau >= 0):
                min = ps.value
        return min

    def TimVTPhanSo(self, ps):
        for i in range(0, len(self.dsPhanSo)):
            if (self.dsPhanSo[i].value == ps.value):
                print(i + " ")
    
    def TongPhanSoAm(self):
        sum = 0
        for ps in self.dsPhanSo:
            if (not((ps.tu < 0 and ps.mau < 0) or (ps.tu > 0 and ps.mau > 0))):
                sum += ps.value
        return sum
    
    def XoaPhanSo(self, ps):
        for i in range(0, len(self.dsPhanSo)):
            if(self.dsPhanSo[i].value == ps.value):
                self.dsPhanSo.pop(i)

    def XoaPhanSoCoTu(self, tu):
        for i in range(0, len(self.dsPhanSo)):
            if(self.dsPhanSo[i].tu == tu):
                self.dsPhanSo.pop(i)
    
    def SapXepPhanSoTang(self):
        for i in range(len(self.dsPhanSo-1)):
            for j in range(i, len(self.dsPhanSo)):
                if(self.dsPhanSo[i] > self.dsPhanSo[j]):
                    temp =  self.dsPhanSo[i]
                    self.dsPhanSo[i] = self.dsPhanSo[j]
                    self.dsPhanSo[j] = temp

    def SapXepPhanSoGiam(self):
        for i in range(len(self.dsPhanSo-1)):
            for j in range(i, len(self.dsPhanSo)):
                if(self.dsPhanSo[i] < self.dsPhanSo[j]):
                    temp =  self.dsPhanSo[i]
                    self.dsPhanSo[i] = self.dsPhanSo[j]
                    self.dsPhanSo[j] = temp

    def SapXepPhanSoTangTheoTu(self):
        for i in range(len(self.dsPhanSo-1)):
            for j in range(i, len(self.dsPhanSo)):
                if(self.dsPhanSo[i].tu > self.dsPhanSo[j].tu):
                    temp =  self.dsPhanSo[i]
                    self.dsPhanSo[i] = self.dsPhanSo[j]
                    self.dsPhanSo[j] = temp

    def SapXepPhanSoTangTheoMau(self):
        for i in range(len(self.dsPhanSo-1)):
            for j in range(i, len(self.dsPhanSo)):
                if(self.dsPhanSo[i].mau > self.dsPhanSo[j].mau):
                    temp =  self.dsPhanSo[i]
                    self.dsPhanSo[i] = self.dsPhanSo[j]
                    self.dsPhanSo[j] = temp
                  
    def SapXepPhanSoGiamTheoTu(self):
        for i in range(len(self.dsPhanSo-1)):
            for j in range(i, len(self.dsPhanSo)):
                if(self.dsPhanSo[i].tu < self.dsPhanSo[j].tu):
                    temp =  self.dsPhanSo[i]
                    self.dsPhanSo[i] = self.dsPhanSo[j]
                    self.dsPhanSo[j] = temp
    
    def SapXepPhanSoGiamTheoMau(self):
        for i in range(len(self.dsPhanSo-1)):
            for j in range(i, len(self.dsPhanSo)):
                if(self.dsPhanSo[i].mau < self.dsPhanSo[j].mau):
                    temp =  self.dsPhanSo[i]
                    self.dsPhanSo[i] = self.dsPhanSo[j]
                    self.dsPhanSo[j] = temp


