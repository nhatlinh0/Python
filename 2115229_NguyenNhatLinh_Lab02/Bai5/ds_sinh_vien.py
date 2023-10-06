from sinh_vien import SinhVien
from sinh_vien_chinh_quy import SinhVienChinhQuy
from sinh_vien_phi_chinh_quy import SinhVienPhiCQ
from datetime import datetime

class DanhSachSv:
    def __init__(self) -> None:
        self.dssv = []

    def themSV(self, sv :SinhVien):
        self.dssv.append(sv)

    def xuat(self):
        for sv in self.dssv:
            print(sv)
    
    def timSVTheoMs(self, ms: str):
        for i in range(len(self.dssv)):
            if(self.dssv[i].mssv == ms):
                return i
        else:
            return -1
    
    def timSvTheoLoai(self, loai: str):
        if loai == "chinhquy":
            return [sv for sv in self.dssv if isinstance(sv, SinhVienChinhQuy)]
        return [sv for sv in self.dssv if isinstance(sv, SinhVienPhiCQ)]

    def timSvDiemRLTren80(self):
        return [sv for sv in self.dssv if isinstance(sv, SinhVienChinhQuy) and sv.diemRL > 80]

    def timSvCaoDang(self, date):
        arr = []
        for sv in self.dssv:
            if(isinstance(sv, SinhVienPhiCQ) and sv._ngaySinh < date and sv.trinhDo == "Cao đẳng"):
                arr.append(sv)
        return arr

