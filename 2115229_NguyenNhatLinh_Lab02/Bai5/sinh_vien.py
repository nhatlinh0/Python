from datetime import datetime

class SinhVien:
    truong = "Đại học Đà Lạt"
    def __init__(self, maSo, hoTen, ngaySinh) -> None:
        self._maSo = maSo
        self._hoTen = hoTen
        self._ngaySinh = ngaySinh
    
    @property
    def hoTen(self):
        return self._hoTen
    
    @hoTen.setter
    def hoTen(self, hoTen : str):
        self._hoTen = hoTen

    @property
    def mssv(self):
        return self._maSo
    
    @hoTen.setter
    def mssv(self, ms : str):
        if(self.ktMsHopLe(ms)):
            self._maSo = ms
    
    @property 
    def ngaySinh(self):
        return self._ngaySinh
    
    @staticmethod
    def ktMsHopLe(mssv : int):
        return len(str(mssv)) == 7
    
    def __str__(self) -> str:
        return f"{self._maSo}\t{self._hoTen}\t{self._ngaySinh}"
    
    
    