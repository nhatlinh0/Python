from hinh_hoc import HinhHoc

class HinhChuNhat(HinhHoc):
    def __init__(self, cd: float, dai: float) -> None:
        super().__init__(cd)
        self.__dai = dai 

    @property
    def ChieuDai(self):
        return self.__dai
    
    @property
    def ChieuRong(self):
        return self._canh
    
    def tinhDienTich(self):
        return super().tinhDienTich() + self._canh * self.__dai
    
    def __str__(self) -> str:
        return f"{self.__dai}\t{self._canh}\t{self.tinhDienTich()}"