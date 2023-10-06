from hinh_hoc import HinhHoc
from hinh_tron import HinhTron
from hinh_chu_nhat import HinhChuNhat
from hinh_vuong import HinhVuong
from ds_hinh_hoc import DanhSachHinhHoc
from loai_hinh import LoaiHinh

hv = HinhVuong(5)
hv1 = HinhVuong(2)
hcn = HinhChuNhat(3,2)
hcn1 = HinhChuNhat(4.1,2.2)
ht = HinhTron(4)
ht1 = HinhTron(2)

ds = DanhSachHinhHoc()
dsMoi = DanhSachHinhHoc()
kieu = LoaiHinh

ds.themHinhHoc(hv)
ds.themHinhHoc(hv1)
ds.themHinhHoc(hcn)
ds.themHinhHoc(hcn1)
ds.themHinhHoc(ht)
ds.themHinhHoc(ht1)


# dsMoi = ds.timHinhCoDienTichLonNhat()
# dsMoi.Xuat()

# dsMoi = ds.timHinhCoDienTichNhoNhat()
# dsMoi.Xuat()

# dsMoi = ds.timHinhTronNhoNhat()
# dsMoi.Xuat()

# ds.sapGiamTheoDienTich()
# ds.Xuat()

# a = ds.DemSoLuongHinh(kieu.TatCa.value)
# print(a)

# a = ds.tinhTongDienTich()
# print(a)

# dsMoi = ds.timHinhCoDienTichLonNhatTheoLoai(kieu.HinhTron.value)
# dsMoi.Xuat()

# a = ds.timVTCuaHinh(ht) + 1
# ds.Xuat()

# ds.xoaHinhTaiViTri(1)
# ds.Xuat()

# dsMoi = ds.timHinhTheoDienTich(25)
# dsMoi.Xuat()

# ds.xoaHinh(hv)
# ds.xoaHinh(hv1)
# ds.xoaHinh(ht1)
# ds.Xuat()

# ds.xoaHinhTheoLoai(kieu.HinhVuong.value)
# ds.Xuat()

# ds.xuatHinhTheoChieuTangGiam(kieu.HinhTron.value, True)
# ds.xuatHinhTheoChieuTangGiam(kieu.HinhVuong.value, True)
# ds.Xuat()

a = ds.tinhTongDienTichTheoHinh(kieu.HinhTron.value)
print(a)

