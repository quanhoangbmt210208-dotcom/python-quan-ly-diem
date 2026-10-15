
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Quản lý điểm sinh viên", layout="wide")

st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

data = {
    "Ho_ten": ["An", "Binh", "Chi", "Dung", "Ha",
               "Lan", "Minh", "Nam", "Phuc", "Trang"],
    "Chuyen_can": [8, 9, 7, 10, 8, 6, 9, 7, 8, 10],
    "Giua_ky": [7, 8, 6, 9, 8, 5, 9, 7, 8, 9],
    "Cuoi_ky": [8, 9, 7, 10, 8, 6, 9, 8, 7, 10]
}

df = pd.DataFrame(data)

df["Tong_ket"] = (
    df["Chuyen_can"] * 0.2
    + df["Giua_ky"] * 0.3
    + df["Cuoi_ky"] * 0.5
)

def xep_loai(diem):
    if diem >= 8.5:
        return "Giỏi"
    elif diem >= 7:
        return "Khá"
    elif diem >= 5:
        return "Trung bình"
    return "Yếu"

df["Xep_loai"] = df["Tong_ket"].apply(xep_loai)

st.subheader("1. Bảng điểm sinh viên")
st.dataframe(df.round(2), use_container_width=True)

st.subheader("2. Thống kê")
st.write("Điểm trung bình lớp:", round(df["Tong_ket"].mean(), 2))

cao_nhat = df.loc[df["Tong_ket"].idxmax()]
thap_nhat = df.loc[df["Tong_ket"].idxmin()]

st.write("Điểm cao nhất:", cao_nhat["Ho_ten"], "-", round(cao_nhat["Tong_ket"], 2))
st.write("Điểm thấp nhất:", thap_nhat["Ho_ten"], "-", round(thap_nhat["Tong_ket"], 2))
st.write("Số sinh viên đạt từ 5 điểm:", int((df["Tong_ket"] >= 5).sum()))

st.subheader("3. Tra cứu sinh viên")
ten = st.selectbox("Chọn sinh viên", df["Ho_ten"])
sv = df[df["Ho_ten"] == ten].iloc[0]

st.write("Điểm chuyên cần:", sv["Chuyen_can"])
st.write("Điểm giữa kỳ:", sv["Giua_ky"])
st.write("Điểm cuối kỳ:", sv["Cuoi_ky"])
st.write("Điểm tổng kết:", round(sv["Tong_ket"], 2))
st.write("Xếp loại:", sv["Xep_loai"])

st.subheader("4. Biểu đồ điểm tổng kết")
fig, ax = plt.subplots(figsize=(8, 5))
ax.barh(df["Ho_ten"], df["Tong_ket"])
ax.set_xlabel("Điểm tổng kết")
ax.set_ylabel("Họ tên sinh viên")
ax.set_xlim(0, 10)
ax.set_title("Điểm tổng kết của 10 sinh viên")
fig.tight_layout()
st.pyplot(fig)
plt.close(fig)

st.markdown("---")
st.caption("Người tạo: [NGUYỄN HOÀNG QUÂN] | MSSV: [066208017381]")
