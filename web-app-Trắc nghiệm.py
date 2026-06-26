
import streamlit as st

# Danh sách câu hỏi
cac_cau_hoi = [
    {
        "cau_hoi": "Ai là người có thẩm quyền ký phát hành vận đơn đường biển:",
        "goi_y": ["A. Chủ hàng", "B. Thuyền trưởng hoặc thuyền phó thuyền trưởng", "C. Hãng tàu hoặc đại lý hãng tàu", "D. B và C đều đúng"],
        "dap_an_dung": "D"
    },
    {
        "cau_hoi": "Nội dung nào sau đây KHÔNG là chức năng của vận đơn đường biển:",
        "goi_y": ["A. Là chứng từ bảo hiểm", "B. Bằng chứng về việc người vận chuyển đã nhận hàng hóa với số lượng, chủng loại, tình trạng như được ghi trong vận đơn để vận chuyển đến nơi trả hàng", "C. Bằng chứng về sở hữu hàng hóa", "D. Bằng chứng của hợp đồng vận chuyển hàng hóa bằng đường biển"],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Người giao nhận có thể đóng những vai trò nào sau đây?",
        "goi_y": ["A. Người chuyên chở", "B.Đại lý của người chuyên chở hoặc của người gửi hàng, người gom hàng", "C. Môi giới hải quan", "D. Tất cả các đáp án đều đúng"],
        "dap_an_dung": "D"
    },
    {
        "cau_hoi": "LO-LO charge là gì?",
        "goi_y": ["A. Phí nâng hạ container", "B.Phí xếp dỡ tại cảng (từ cảng lên tàu hoặc từ tàu xuống cảng)", "C.Phí vệ sinh container", "D. Phụ phí nhiên liệu"],
        "dap_an_dung": "B"
    },
    {
        "cau_hoi": "EIR là gì?",
        "goi_y": ["A. Phiếu giao nhận container", "B.Phiếu xác nhận khối lượng toàn bộ container", "C.Giấy chứng nhận xuất xứ hàng hóa", "D. Lệnh giao hàng"],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Nội dung nào sau đây là trách nhiệm của người giao nhận khi thuê một người xuất khẩu (điều kiện giao hàng CFR)?",
        "goi_y": ["A. Giám sát toàn bộ hành trình vận chuyển hàng hóa đến khi cấp chứng từ nhập khẩu", "B.Đưa hàng hóa ra cảng và làm thủ tục thông quan xuất khẩu", "C.Thuê phương tiện vận chuyển", "D. Tất cả các đáp án đều đúng"],
        "dap_an_dung": "D"
    },
    {
        "cau_hoi": "Nội dung nào sau đây KHÔNG có trên vận đơn hàng không?",
        "goi_y": ["A. Thông tin về cước phí", "B.Mô tả khái quát về hàng hóa", "C.Số lượng bản gốc vận đơn ghi bằng số và bằng chữ", "D. Sân bay đi và sân bay đến"],
        "dap_an_dung": "C"
    },
    {
        "cau_hoi": "Trong phương thức nhờ thu kèm chứng từ (Documentary Collection), ngân hàng nhờ thu KHÔNG có trách nhiệm nào sau đây?",
        "goi_y": ["A. Kiểm tra tính đầy đủ của chứng từ (số loại chứng từ, số lượng mỗi loại, bản gốc, bản sao)", "B.Thực hiện đúng chỉ thị trong Đơn yêu cầu nhờ thu", "C.Kiểm tra tính chân thật của bộ chứng từ nhờ thu (chữ ký)", "D. Kiểm tra, đối chiếu nội dung các chứng từ"],
        "dap_an_dung": "D"
    },
    {
        "cau_hoi": "Trên booking: 'Closing time (cut-off time)' có ý nghĩa là gì?",
        "goi_y": ["A. Thời hạn cuối cùng mà người gửi hàng hoàn tất thủ tục để cho cảng bốc xếp container lên tàu", "B.Thời hạn cuối cùng mà người gửi hàng phải gửi SI cho hãng tàu để hãng tàu làm B/L", "C.Không đáp án nào đúng", "D. Thời hạn cuối cùng mà người gửi hàng phải gửi VGM cho hãng tàu"],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Phương thức vận tải nào là phù hợp nhất để vận chuyển Bắc – Nam loại hàng cồng kềnh, khối lượng lớn, giá trị thấp, lưu thông (như vật liệu xây dựng, than đá...)?",
        "goi_y": ["A. Đường ô tô", "B.Đường sắt", "C.Đường thủy nội địa", "D. Đường hàng không"],
        "dap_an_dung": "B"
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