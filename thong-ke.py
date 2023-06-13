import pandas as pd
import numpy as np

# Đường dẫn tới file excel
excel_file = "D:\Phân tích dữ liệu với Python\THPTQG_Full.xlsx"

# Đọc file excel
df = pd.read_excel(excel_file)
print(df)
print("----------------------------------------------------------")


# Tạo dữ liệu các năm tương ứng 2020,2021,2022
data_2020 = df[df['Năm'] == 2020]
# data_2021 = df[df['Năm'] == 2021]
# data_2022 = df[df['Năm'] == 2022]
print("Dữ liệu thí sinh đạt thang điểm tương ứng với các môn học trong năm 2020:\n", data_2020)
print("----------------------------------------------------------")


####### Dữ liệu môn học với các năm 2020,2021,2022
toan_av20 = data_2020[['Thang 0.2', 'Toán', 'Tiếng Anh']]
# toan_av21 = data_2021[['Thang 0.2', 'Toán', 'Tiếng Anh']]
# toan_av22 = data_2022[['Thang 0.2', 'Toán', 'Tiếng Anh']]
print("Dữ liệu số thí sinh đạt điểm tương ứng với môn Toán, Tiếng Anh trong năm 2020:\n",toan_av20)
print("----------------------------------------------------------")
to_hop20 = data_2020[['Thang 0.25', 'Văn', 'Lý', 'Hóa', 'Sinh', 'Sử', 'Địa', 'GDCD']]
# to_hop21 = data_2020[['Thang 0.25', 'Văn', 'Lý', 'Hóa', 'Sinh', 'Sử', 'Địa', 'GDCD']]
# to_hop22 = data_2020[['Thang 0.25', 'Văn', 'Lý', 'Hóa', 'Sinh', 'Sử', 'Địa', 'GDCD']]
print("Dữ liệu số thí sinh đạt điểm tương ứng với môn Văn-Lý-Hóa-Sinh-Sử-Địa-GDCD trong năm 2020:\n",to_hop20.dropna())
print("----------------------------------------------------------")


# Lọc dữ liệu số thí sinh đạt điểm giỏi Toán, Tiếng Anh 2020,2021,2022
toan_av_gioi_2020 = data_2020.loc[(data_2020['Thang 0.2'] >= 8), ['Thang 0.2', 'Toán', 'Tiếng Anh']]
# toan_av_2021 = data_2021.loc[(data_2021['Thang 0.2'] >= 8), ['Thang 0.2', 'Toán', 'Tiếng Anh']]
# toan_av_2022 = data_2022.loc[(data_2022['Thang 0.2'] >= 8), ['Thang 0.2', 'Toán', 'Tiếng Anh']]
print("Số lượng thí sinh đạt điểm giỏi môn Toán, Tiếng Anh trong năm 2020:\n", toan_av_gioi_2020)
print("----------------------------------------------------------")


# Lọc dữ liệu số lương thí sinh đạt điểm dưới 5 Văn, Lý, Hóa, Sinh, Sử, Địa, GDCD trong các năm 2020,2021,2022
to_hop_yeu_20 = data_2020.loc[(data_2020['Thang 0.25'] < 5), ['Thang 0.25', 'Văn', 'Lý', 'Hóa', 'Sinh', 'Sử', 'Địa', 'GDCD']]
# to_hop_yeu_2021 = data_2021.loc[(data_2021['Thang 0.25'] < 5), ['Thang 0.25', 'Văn', 'Lý', 'Hóa', 'Sinh', 'Sử', 'Địa', 'GDCD']]
# to_hop_yeu_2022 = data_2022.loc[(data_2022['Thang 0.25'] < 5), ['Thang 0.25', 'Văn', 'Lý', 'Hóa', 'Sinh', 'Sử', 'Địa', 'GDCD']]
print("Số lượng thí sinh đạt điểm dưới trung bình các môn Văn-Lý-Hóa-Sinh-Sử-Địa-GDCD trong năm 2020:\n", to_hop_yeu_20)
print("----------------------------------------------------------")



# Thống kê

## Trung bình
### Tính trung bình số thí sinh đạt điểm giỏi môn Toán, Tiếng Anh với thang điểm 0.2 trong các năm 2020,2021,2022
toan_av_gioi_2020 = toan_av_gioi_2020.drop(columns=['Thang 0.2'])
trung_binh_toan_av20 = toan_av_gioi_2020.mean(axis=0)
print("Trung bình số thí sinh đạt điểm giỏi >= 8 môn Toán, Tiếng Anh trong năm 2020 là:\n", trung_binh_toan_av20)
print("----------------------------------------------------------")
#
### Tính trung bình số thí sinh đạt điểm dưới trung bình của các môn Văn-Lý-Hóa-Sinh-Sử-Địa-GDCD của các năm 2020,2021,2022
to_hop_yeu_20 = to_hop_yeu_20.drop(columns=['Thang 0.25'])
trung_binh_tohop20 = to_hop_yeu_20.mean(axis=0)
print("Trung bình số thí sinh thi điểm dưới trung bình <= 5 của các môn Văn-Lý-Hóa-Sinh-Sử-Địa-GDCD năm 2020 là:\n", trung_binh_tohop20)
print("----------------------------------------------------------")


# Phương sai
## Tính phương sai số lượng thí sinh đạt điểm >= 8 các môn qua các năm 2020,2021,2022
toan_av_var20 = toan_av_gioi_2020.var()
print("Phương sai của số lượng thí sinh đạt điểm >= 8 của môn Toán, Tiếng Anh trong năm 2020:\n",toan_av_var20)
print("----------------------------------------------------------")
to_hop_var20 = to_hop_yeu_20.var()
print("Phương sai của số lượng thí sinh đạt điểm dưới trung bình <5 của các môn còn lại trong năm 2020:\n", to_hop_var20)
print("----------------------------------------------------------")


# Phương sai hiệu chỉnh
# Tính phương sai hiệu chỉnh số lượng thí sinh thi môn Toán, Tiếng Anh đạt điểm giỏi >=8 qua các năm 2020,2021,2022
n = len(toan_av_gioi_2020['Toán'])
mean = toan_av_gioi_2020['Toán'].mean()
pshc_toan20 = (sum((toan_av_gioi_2020['Toán'] - mean) ** 2) / n) * (n / (n - 1))

n = len(toan_av_gioi_2020['Tiếng Anh'])
mean = toan_av_gioi_2020['Tiếng Anh'].mean()
pshc_av20 = (sum((toan_av_gioi_2020['Tiếng Anh'] - mean) ** 2) / n) * (n / (n - 1))

print("Phương sai hiệu chỉnh số lượng thí sinh đạt điểm giỏi >=8 cácmôn Toán, Tiếng Anh trong năm 2020:\n" "Môn Toán là:", pshc_toan20,'\nMôn Tiếng Anh là:', pshc_av20)
print("----------------------------------------------------------")


# Độ lệch chuẩn
dlc_toan_av20 = np.std(toan_av_gioi_2020)
dlc_to_hop20 = np.std(to_hop_yeu_20)
print("Độ lệch chuẩn của số lương thí sinh đạt điểm giỏi môn Toán, Tiếng Anh:\n", dlc_toan_av20,'\nVà đạt điểm dưới trung bình <5 với các môn còn lại:\n', dlc_to_hop20)
print("----------------------------------------------------------")

# Min, max
min_20 = data_2020['Thang 0.2'].min()
max_20 = data_2020['Thang 0.2'].max()

min_so_luong_toan = data_2020.loc[df['Thang 0.2'] == min_20, 'Toán'].values[0]
max_so_luong_toan = data_2020.loc[df['Thang 0.2'] == max_20, 'Toán'].values[0]

min_so_luong_av = data_2020.loc[df['Thang 0.2'] == min_20, 'Tiếng Anh'].values[0]
max_so_luong_av = data_2020.loc[df['Thang 0.2'] == max_20, 'Tiếng Anh'].values[0]

min_so_luong_van = data_2020.loc[df['Thang 0.25'] == min_20, 'Văn'].values[0]
max_so_luong_van = data_2020.loc[df['Thang 0.25'] == max_20, 'Văn'].values[0]

min_so_luong_ly = data_2020.loc[df['Thang 0.2'] == min_20, 'Lý'].values[0]
max_so_luong_ly = data_2020.loc[df['Thang 0.2'] == max_20, 'Lý'].values[0]

min_so_luong_hoa = data_2020.loc[df['Thang 0.2'] == min_20, 'Hóa'].values[0]
max_so_luong_hoa = data_2020.loc[df['Thang 0.2'] == max_20, 'Hóa'].values[0]

min_so_luong_sinh = data_2020.loc[df['Thang 0.2'] == min_20, 'Sinh'].values[0]
max_so_luong_sinh = data_2020.loc[df['Thang 0.2'] == max_20, 'Sinh'].values[0]

min_so_luong_su = data_2020.loc[df['Thang 0.2'] == min_20, 'Sử'].values[0]
max_so_luong_su = data_2020.loc[df['Thang 0.2'] == max_20, 'Sử'].values[0]

min_so_luong_dia = data_2020.loc[df['Thang 0.2'] == min_20, 'Địa'].values[0]
max_so_luong_dia = data_2020.loc[df['Thang 0.2'] == max_20, 'Địa'].values[0]

min_so_luong_gdcd = data_2020.loc[df['Thang 0.2'] == min_20, 'GDCD'].values[0]
max_so_luong_gdcd = data_2020.loc[df['Thang 0.2'] == max_20, 'GDCD'].values[0]

print("Min và max của các môn học trong năm 2020:")
print("Môn Toán:\n",
      "-Số điểm nhỏ nhất là",min_20,"điểm có",min_so_luong_toan,"thí sinh\n",
      "-Số điểm lớn nhất là",max_20,"điểm có",max_so_luong_toan,"thí sinh\n",)
print("Môn Tiếng Anh:\n",
      "-Số điểm nhỏ nhất là",min_20,"điểm có",min_so_luong_av,"thí sinh\n",
      "-Số điểm lớn nhất là",max_20,"điểm có",max_so_luong_av,"thí sinh\n")
print("Môn Văn:\n",
      "-Số điểm nhỏ nhất là",min_20,"điểm có",min_so_luong_van,"thí sinh\n",
      "-Số điểm lớn nhất là",max_20,"điểm có",max_so_luong_van,"thí sinh\n")
print("Môn Lý:\n",
      "-Số điểm nhỏ nhất là",min_20,"điểm có",min_so_luong_ly,"thí sinh\n",
      "-Số điểm lớn nhất là",max_20,"điểm có",max_so_luong_ly,"thí sinh\n")
print("Môn Hóa:\n",
      "-Số điểm nhỏ nhất là",min_20,"điểm có",min_so_luong_hoa,"thí sinh\n",
      "-Số điểm lớn nhất là",max_20,"điểm có",max_so_luong_hoa,"thí sinh\n")
print("Môn Sinh:\n",
      "-Số điểm nhỏ nhất là",min_20,"điểm có",min_so_luong_sinh,"thí sinh\n",
      "-Số điểm lớn nhất là",max_20,"điểm có",max_so_luong_sinh,"thí sinh\n")
print("Môn Sử:\n",
      "-Số điểm nhỏ nhất là",min_20,"điểm có",min_so_luong_su,"thí sinh\n",
      "-Số điểm lớn nhất là",max_20,"điểm có",max_so_luong_su,"thí sinh\n")
print("Môn Địa:\n",
      "-Số điểm nhỏ nhất là",min_20,"điểm có",min_so_luong_dia,"thí sinh\n",
      "-Số điểm lớn nhất là",max_20,"điểm có",max_so_luong_dia,"thí sinh\n")
print("Môn GDCD:\n",
      "-Số điểm nhỏ nhất là",min_20,"điểm có",min_so_luong_gdcd,"thí sinh\n",
      "-Số điểm lớn nhất là",max_20,"điểm có",max_so_luong_gdcd,"thí sinh\n")
print("----------------------------------------------------------")


# Trung vị
trung_vi_toan_av20 = toan_av_gioi_2020.median()
print("Trung vị của số lượng thí sinh đạt được điểm giỏi >= 8 trong năm 2020 là:\n",trung_vi_toan_av20)
trung_vi_to_hop20 = to_hop_yeu_20.median()
print("Trung vị của số lượng thí sinh đạt được điểm <5 trong năm 2020 là:\n", trung_vi_to_hop20)
print("----------------------------------------------------------")

# Tứ phân vị
tu_phavi_toan20 = np.percentile(toan_av_gioi_2020['Toán'], [25, 50, 75])
tu_phavi_av20 = np.percentile(toan_av_gioi_2020['Tiếng Anh'], [25,50,75])
tu_phavi_van20 = np.percentile(to_hop_yeu_20['Văn'], [25,50,75])
tu_phavi_ly20 = np.percentile(to_hop_yeu_20['Lý'], [25,50,75])
tu_phavi_hoa20 = np.percentile(to_hop_yeu_20['Hóa'], [25,50,75])
tu_phavi_sinh20 = np.percentile(to_hop_yeu_20['Sinh'], [25,50,75])
tu_phavi_su20 = np.percentile(to_hop_yeu_20['Sử'], [25,50,75])
tu_phavi_dia20 = np.percentile(to_hop_yeu_20['Địa'], [25,50,75])
tu_phavi_gdcd20 = np.percentile(to_hop_yeu_20['GDCD'], [25,50,75])

print("Tứ phân vị của số lượng thí sinh thi môn Toán, Tiếng Anh đạt điểm giỏi >=8 trong năm 2020:\n",
      "-Toán:\n",
      "Tứ phân vị thứ nhất (25%):", tu_phavi_toan20[0],'\n',
      "Tứ phân vị thứ hai (50%) :", tu_phavi_toan20[1],'\n',
      "Tứ phân vị thứ ba (75%) :", tu_phavi_toan20[2],'\n',
      "-Tiếng Anh:\n",
      "Tứ phân vị thứ nhất (25%):", tu_phavi_av20[0], '\n',
      "Tứ phân vị thứ hai (50%) :", tu_phavi_av20[1], '\n',
      "Tứ phân vị thứ ba (75%) :", tu_phavi_av20[2], '\n',
      )
print("Tứ phân vị của số lượng thí sinh thi các môn còn lại đạt điểm dưới trung bình <5 trong năm 2020:\n",
      "-Văn:\n",
      "Tứ phân vị thứ nhất (25%):", tu_phavi_van20[0],'\n',
      "Tứ phân vị thứ hai (50%) :", tu_phavi_van20[1],'\n',
      "Tứ phân vị thứ ba (75%) :", tu_phavi_van20[2],'\n',
      "-Lý:\n",
      "Tứ phân vị thứ nhất (25%):", tu_phavi_ly20[0], '\n',
      "Tứ phân vị thứ hai (50%) :", tu_phavi_ly20[1], '\n',
      "Tứ phân vị thứ ba (75%) :", tu_phavi_ly20[2], '\n',
      "-Hóa:\n",
      "Tứ phân vị thứ nhất (25%):", tu_phavi_hoa20[0], '\n',
      "Tứ phân vị thứ hai (50%) :", tu_phavi_hoa20[1], '\n',
      "Tứ phân vị thứ ba (75%) :", tu_phavi_hoa20[2], '\n',
      "-Sinh:\n",
      "Tứ phân vị thứ nhất (25%):", tu_phavi_sinh20[0], '\n',
      "Tứ phân vị thứ hai (50%) :", tu_phavi_sinh20[1], '\n',
      "Tứ phân vị thứ ba (75%) :", tu_phavi_sinh20[2], '\n',
      "-Sử:\n",
      "Tứ phân vị thứ nhất (25%):", tu_phavi_su20[0], '\n',
      "Tứ phân vị thứ hai (50%) :", tu_phavi_su20[1], '\n',
      "Tứ phân vị thứ ba (75%) :", tu_phavi_su20[2], '\n',
      "-Địa:\n",
      "Tứ phân vị thứ nhất (25%):", tu_phavi_dia20[0], '\n',
      "Tứ phân vị thứ hai (50%) :", tu_phavi_dia20[1], '\n',
      "Tứ phân vị thứ ba (75%) :", tu_phavi_dia20[2], '\n',
      "-GDCD:\n",
      "Tứ phân vị thứ nhất (25%):", tu_phavi_gdcd20[0], '\n',
      "Tứ phân vị thứ hai (50%) :", tu_phavi_gdcd20[1], '\n',
      "Tứ phân vị thứ ba (75%) :", tu_phavi_gdcd20[2], '\n',
      )

# Bảng phân tổ
