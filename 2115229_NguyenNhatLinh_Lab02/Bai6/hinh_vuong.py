from hinh_chu_nhat import HinhChuNhat

class HinhVuong(HinhChuNhat):
    def __init__(self, cd: float) -> None:
        super().__init__(cd, dai = 0)

    def tinhDienTich(self):
        return super().tinhDienTich() + self._canh * self._canh
    
    def __str__(self) -> str:
        return f"{self._canh}\t{self.tinhDienTich()}"