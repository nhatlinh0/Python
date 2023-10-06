from hinh_hoc import HinhHoc
from math import pi

class HinhTron(HinhHoc):
    def __init__(self, cd: float) -> None:
        super().__init__(cd)

    @property 
    def banKinh(self):
        return self._canh
    
    def tinhDienTich(self):
        return super().tinhDienTich() + self._canh *pi
    
    def __str__(self) -> str:
        return super().__str__()