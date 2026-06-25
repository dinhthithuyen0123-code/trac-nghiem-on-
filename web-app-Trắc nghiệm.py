
import streamlit as st

# Danh sách câu hỏi
cac_cau_hoi = [
    {
        "cau_hoi": "Ngôn ngữ lập trình Python được ra mắt đầu tiên vào năm nào?",
        "goi_y": ["A. 1989", "B. 1991", "C. 1995", "D. 2000"],
        "dap_an_dung": "B"
    },
    {
        "cau_hoi": "Hàm nào dùng để xuất dữ liệu ra màn hình trong Python?",
        "goi_y": ["A. input()", "B. scanf()", "C. print()", "D. echo()"],
        "dap_an_dung": "C"
    }
]

st.title("🎯 Ứng Dụng Trắc Nghiệm Ôn Luyện")
st.write("Chọn đáp án đúng cho từng câu hỏi bên dưới:")

# Dùng session_state để lưu trữ điểm và trạng thái làm bài
if 'diem' not in st.session_state:
    st.session_state.diem = 0
if 'da_nop_bai' not in st.session_state:
    st.session_state.da_nop_bai = False

cau_tra_loi_cua_user = {}

# Hiển thị các câu hỏi dưới dạng Form
with st.form("quiz_form"):
    for i, ch in enumerate(cac_cau_hoi, 1):
        st.subheader(f"Câu {i}: {ch['cau_hoi']}")
        # Tạo các nút bấm chọn đáp án (Radio buttons)
        lua_chon = st.radio("Chọn một đáp án:", ch['goi_y'], key=f"cau_{i}")
        # Lấy ký tự đầu tiên (A, B, C, D) từ lựa chọn của người dùng
        cau_tra_loi_cua_user[i] = lua_chon[0] if lua_chon else None
        st.write("---")
        
    # Nút nộp bài
    submit = st.form_submit_button("Nộp Bài & Xem Kết Quả")

if submit:
    st.session_state.diem = 0
    st.session_state.da_nop_bai = True
    
    for i, ch in enumerate(cac_cau_hoi, 1):
        st.write(f"**Câu {i}:**")
        if cau_tra_loi_cua_user[i] == ch['dap_an_dung']:
            st.success(f"🎉 Đúng! Bạn chọn {cau_tra_loi_cua_user[i]}")
            st.session_state.diem += 1
        else:
            st.error(f"❌ Sai rồi! Bạn chọn {cau_tra_loi_cua_user[i]}. Đáp án đúng là {ch['dap_an_dung']}")
            
    # Hiển thị tổng điểm
    st.metric(label="Tổng điểm của bạn", value=f"{st.session_state.diem} / {len(cac_cau_hoi)}")