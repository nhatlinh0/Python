
class HinhHoc:
    def __init__(self, cd: float) -> None:
        self._canh = cd

    def tinhDienTich(self):
        return 0
    
    def __str__(self) -> str:
        return f"{self._canh}\t{self.tinhDienTich()}"
        