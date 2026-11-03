import numpy as np
# a = np.array([1,2,3,4,5])
#print(a)                   # mang 1 chieu

#b = np.array([[1, 2, 3, 4, 5],
 #            [5, 6, 7, 8, 9]])
#print(b)                   # mang 2 chieu, 2 hang 5 cot

#print(np.zeros(4))
#print(np.ones((3, 8)))     # tao bang 3 hang 8 cot

#a = np.arange(0,21, 3)
#print(a)                   #[0, 3,6,9,..18]
#b = np.arange(5)        # [0,1,2,3,4]
#print(b)
#c = np.arange (1, 6)    #[1,2,3,4,5]
#print(c)
# Bat dau tu 0, moi lan cong them 3, dung truoc so do nen khong la 21
# tao day so theo cong thuc start, stop, step
#day so nguyen nen ket qua khong co dau cham

#d = np.linspace(0,100,5)
#print(d)
# tao 5 so chia deu tu 0 den 100

#arrange diem cuoi khong duoc lay, di moi buoc bao xa
#linspace diem cuoi duoc lay , muon bao nhieu diem

#print(np.zeros(3))
#print(np.ones((3,2)))
#print(np.arange(2, 12,3))
# tu 2 den 12 nhay moi buoc 3 buoc den truoc 12
#print(np.linspace(0,10,3))
#<details><summary> Dap an</summary>

#print(np.arange(10, 0,-2))
#print(np.zeros((2,4)))
#print(np.linspace(1,2,5))
#tao 5 so chia deu tu 0 den 100
#print(np.arange(1,6) * 10)
#nhay tu 1 den 5 moi so nhan 10

#b = np.array([[1, 2, 3],
           #   [4, 5, 6]])

#print(b[1, 2])   # 6   hàng 1, cột 2
#print(b[0, 0])   # 1    hang 0 cot o

# Slicing (kết thúc không lấy)
#a = np.array([10, 20, 30, 40, 50])
#print(a[1:4])
#print(a[:3])
#print(a[2:])
#print(a[::3])       #nhảy 3 bước một lần đến hết
#print(a[::-1])       #bước nhảy âm đi ngược, nên mảng bị đảo lại

#b = np.array([[1, 2, 3],
              #[4, 5, 6],
              #[7, 8, 9]])
#print(b[0])         # cả hàng 0
#print(b[2:2])
#print(b[:, 0])      # cả cột 0, dấu : nghĩa là tất cả
#print(b[1:,:2])

#BOOLEAN MASKING (lọc dữ liệu bằng điều kiện)
diem = np.array([5, 8, 3, 9, 6, 10])
#print(diem > 6)
#print(diem[diem > 6])       # giống cái rây lọc lại dữ liệu mà bạn cần

#print("before:", diem)
#diem[diem < 5] = 5
#print("after:", diem)

#diem_goc = np.array([5,6,3,5,7,8,10])
#diem_moi = diem_goc.copy()
#diem_moi[diem_moi < 5] = 6
#print(diem_goc)
#print(diem_moi)

#ĐỔI định dạng (reshape)
#x = np.arange(18)           # [0,1,2,3,..11]
#print(x.reshape(6, 3))
#print(x.reshape(9, 2))
#print(x.reshape(3, -1))

#Truc AXIS: tinh theo hang hay theo cot
#diem = np.array([[7, 8, 9],     # bạn An: Toán, Văn, Anh
                 #[6, 5, 10]])
#diem_tong = diem.sum()
#tong_tung_cot = diem.sum(axis=0)
#tong_tung_hang = diem.sum(axis=1)
#print(tong_tung_cot)
#print(tong_tung_hang)

#a = np.array([4, 8, 6, 2, 10])

#np.sum(a)       # 30     tổng
#np.mean(a)      # 6.0    trung bình
#np.median(a)    # 6.0    số ở giữa khi xếp thứ tự
#np.max(a)       # 10     lớn nhất
#np.min(a)       # 2      nhỏ nhất
#np.argmax(a)    # 4      VỊ TRÍ của số lớn nhất
#np.argmin(a)    # 3      vị trí của số nhỏ nhất
#np.std(a)       # độ lệch chuẩn (các số "tản mác" nhiều hay ít)

# SỐ NGẪU NHIÊN (RÚT THĂM)
#rng = np.random.default_rng(42)   # 42 là "hạt giống": cùng hạt giống thì ra cùng kết quả

#rng.random(3)               # 3 số thập phân ngẫu nhiên từ 0 đến 1
#rng.integers(1, 7, size=5)  # tung xúc xắc 5 lần (số từ 1 đến 6)
#rng.normal(0, 1, size=4)    # số ngẫu nhiên theo "hình chuông" (phân phối chuẩn)
#rng.choice([1, 2, 3], 2)    # rút ngẫu nhiên 2 phần tử
#a = np.array([1, 2, 3])
#print(a+10)
#bang = np.array([[1, 2, 3],
                 #[4, 5, 6]])
#hang = np.array([10, 20, 30])
#print(bang+hang)

#np.save('du_lieu.npy', a)
#a2 = np.load('du_lieu.npy')

#np.savetxt("bang.csv", a, delimiter=",")   # lưu dạng bảng CSV
#a2 = np.loadtxt("bang.csv", delimiter=",") # đọc lại

import pandas as pd
df = pd.DataFrame({
    "Toán": [7, 6],
    "Văn":  [8, 5],
    "Anh":  [9, 10]
}, index=["An", "Bình"])
print(df)
print(df.loc["Bình"])

toan= df["Toán"]
print(toan)
df["TB"]= df.mean(axis=1)

print(df["TB"])

#df = pd.read_csv("hoc_sinh.csv")     # đọc file CSV (như mở file Excel)

#df["TB"] = df.mean(axis=1)           # thêm cột điểm trung bình
#df[df["Toán"] >= 8]                  # lọc bạn có Toán từ 8 trở lên
#df.sort_values("Anh")                # sắp xếp theo điểm Anh
#df.groupby("Lớp")["Toán"].mean()     # điểm Toán trung bình theo từng lớp
#df.to_excel("ket_qua.xlsx")          # lưu ra file Excel

#collums là tên cột, index= là tên hàng trong pandas

#df.head(3)       # 3 hàng đầu (mặc định 5)
#df.tail(2)       # 2 hàng cuối
#df.shape         # (5, 4) → 5 hàng, 4 cột
#df.columns       # tên các cột
#df.index         # tên các hàng
#df.dtypes        # kiểu dữ liệu từng cột
#df.info()        # tóm tắt: số hàng, kiểu dữ liệu, số ô không trống
#df.describe()    # thống kê nhanh: trung bình, min, max, độ lệch chuẩn...


