import streamlit as st
import os
st.set_page_config(
    page_title="Trắc Nghiệm Giao Nhận Hàng Hóa & Vận Tải Biển - Ôn Thi Logistics",
    page_icon="🎯",
    layout="centered"
)
# 1. Hàm tự động đếm và lưu lượt truy cập vào file text
def dem_luot_truy_cap():
    file_name = "luot_truy_cap.txt"
    # Nếu file chưa tồn tại thì tạo mới với số 0
    if not os.path.exists(file_name):
        with open(file_name, "w") as f:
            f.write("0")
            
    # Đọc số lượt hiện tại, tăng lên 1 và ghi lại
    with open(file_name, "r") as f:
        luot = int(f.read().strip())
    luot += 1
    with open(file_name, "w") as f:
        f.write(str(luot))
    return luot
# Gọi hàm đếm lượt truy cập ngay khi mở trang web
if 'da_dem' not in st.session_state:
    st.session_state['da_dem'] = True
    tong_luot = dem_luot_truy_cap()
else:
    # Nếu chỉ F5 hoặc đổi chương thì giữ nguyên số cũ, không đếm tăng lên
    if os.path.exists("luot_truy_cap.txt"):
        with open("luot_truy_cap.txt", "r") as f:
            tong_luot = int(f.read().strip())
    else:
        tong_luot = 1
# --- BẮT ĐẦU GIAO DIỆN WEB ---
st.title("Ôn Luyện Trắc Nghiệm Giao Nhận")
st.write("""
Chào mừng bạn đến với hệ thống **ôn thi trắc nghiệm logistics** trực tuyến. 
Tại đây tổng hợp các câu hỏi bài tập về **giao nhận hàng hóa quốc tế**, **vận tải đường biển**, 
quy trình xuất nhập khẩu và các nghiệp vụ cảng biển mới nhất giúp bạn ôn tập hiệu quả.
""")
# 2. Tạo thanh menu chọn chương ở bên trái màn hình (Sidebar)
chuong_da_chon = st.sidebar.selectbox(
    "📚 Chọn Chương Ôn Tập:",
    ["Chương 1: Tổng quan về giao nhận hàng hóa", "Chương 2: Giao nhận bằng đường biển", "Chương 8.1: Thanh toán quốc tế", "Chương 8.2: Thanh toán quốc tế", "Chương 8.3: Thanh toán quốc tế", "Chương 8.4: Thanh toán quốc tế", "Câu hỏi hỗn hợp", "Đề 1","Đề 2", "Đề 3", "Đề 4", "Đề 5", "Đề 6"]
)
# Hiển thị số lượt truy cập nhỏ ở góc dưới sidebar để bạn theo dõi
st.sidebar.write(f"📊 **Tổng số lượt truy cập:** {tong_luot}")
# 3. Thiết lập kho câu hỏi cho từng chương
if chuong_da_chon == "Chương 1: Tổng quan về giao nhận hàng hóa":
    cac_cau_hoi = [
        {
        "cau_hoi": "Theo FIATA, dịch vụ giao nhận bao gồm hoạt động nào sau đây?",
        "goi_y": [
            "A.Chỉ vận chuyển hàng hóa",
            "B.Chỉ lưu kho hàng hóa",
            "C.Vận chuyển, lưu kho, đóng gói, phân phối và các dịch vụ liên quan",
            "D.Chỉ làm thủ tục hải quan"
        ],
        "dap_an_dung": "C"
    },
    {
        "cau_hoi": "FIATA là tên viết tắt của tổ chức nào?",
        "goi_y": [
            "A.Hiệp hội Logistics Việt Nam",
            "B.Liên đoàn các Hiệp hội Giao nhận Vận tải Quốc tế",
            "C.Tổ chức Hải quan Thế giới",
            "D.Hiệp hội Chủ tàu"
        ],
        "dap_an_dung": "B"
    },
    {
        "cau_hoi": "Theo Luật Thương mại 2005, dịch vụ logistics là hoạt động nhằm mục đích gì?",
        "goi_y": [
            "A.Từ thiện",
            "B.Hưởng thù lao",
            "C.Hỗ trợ Nhà nước",
            "D.Không vì lợi nhuận"
        ],
        "dap_an_dung": "B"
    },
    {
        "cau_hoi": "Giai đoạn đầu tiên trong quá trình phát triển của Logistics là gì?",
        "goi_y": [
            "A.Quản trị chuỗi cung ứng",
            "B.Phân phối vật chất",
            "C.Logistics tích hợp",
            "D.4PL"
        ],
        "dap_an_dung": "B"
    },
    {
        "cau_hoi": "SCM là viết tắt của cụm từ nào?",
        "goi_y": [
            "A.Shipping Cargo Management",
            "B.Supply Chain Management",
            "C.Sea Carrier Management",
            "D.Service Chain Model"
        ],
        "dap_an_dung": "B"
    },
    {
        "cau_hoi": "3PL là viết tắt của loại hình nào?",
        "goi_y": [
            "A.First Party Logistics",
            "B.Second Party Logistics",
            "C.Third Party Logistics",
            "D.Fourth Party Logistics"
        ],
        "dap_an_dung": "C"
    },
    {
        "cau_hoi": "Hoạt động nào thuộc giao nhận quốc tế?",
        "goi_y": [
            "A.Vận chuyển Bắc Ninh - TP.HCM",
            "B.Vận chuyển Hà Nội - Đà Nẵng",
            "C.Vận chuyển từ Việt Nam sang Singapore",
            "D.Vận chuyển nội tỉnh"
        ],
        "dap_an_dung": "C"
    },

    {
        "cau_hoi": "Theo phạm vi hoạt động, giao nhận được chia thành?",
        "goi_y": [
            "A.Đường biển và đường bộ",
            "B.Quốc tế và nội địa",
            "C.FCL và LCL",
            "D.FOB và CIF"
        ],
        "dap_an_dung": "B"
    },
    {
        "cau_hoi": "Người giao nhận thay mặt người gửi hàng có thể thực hiện công việc nào?",
        "goi_y": [
            "A.Lựa chọn phương thức vận tải",
            "B.Ký hợp đồng vận tải",
            "C.Mua bảo hiểm nếu cần",
            "D.Tất cả các đáp án trên"
        ],
        "dap_an_dung": "D"
    },
    {
        "cau_hoi": "Người giao nhận thay mặt người nhận hàng phải làm gì?",
        "goi_y": [
            "A.Làm thủ tục hải quan",
            "B.Nộp thuế",
            "C.Nhận hàng từ người chuyên chở",
            "D.Tất cả các đáp án trên"
        ],
        "dap_an_dung": "D"
    },
    {
        "cau_hoi": "Dịch vụ nào sau đây thuộc dịch vụ giao nhận đặc biệt?",
        "goi_y": [
            "A.Hàng siêu trường siêu trọng",
            "B.Hàng nguy hiểm",
            "C.Hàng dễ hư hỏng",
            "D.Tất cả các đáp án trên"
        ],
        "dap_an_dung": "D"
    },
    {
        "cau_hoi": "MTO là viết tắt của cụm từ nào?",
        "goi_y": [
            "A.Multi Trade Operator",
            "B.Multimodal Transport Operator",
            "C.Marine Transport Office",
            "D.Master Trade Operator"
        ],
        "dap_an_dung": "B"
    },
    {
        "cau_hoi": "Khi làm thủ tục hải quan thay chủ hàng, người giao nhận đóng vai trò gì?",
        "goi_y": [
            "A.Carrier",
            "B.Customs Broker",
            "C.Agent",
            "D.Shipper"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Người giao nhận gom nhiều lô hàng lẻ thành hàng nguyên container được gọi là gì?",
        "goi_y": [
            "A.Agent",
            "B.Carrier",
            "C.Cargo Consolidation",
            "D.Customs Broker"
        ],
        "dap_an_dung": "C"
    },
    {
        "cau_hoi": "Người giao nhận có thể trực tiếp ký hợp đồng vận chuyển và chịu trách nhiệm chuyên chở với vai trò gì?",
        "goi_y": [
            "A.Carrier",
            "B.Customs",
            "C.Bank",
            "D.Consignee"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Một trong những ý nghĩa của dịch vụ giao nhận ở tầm vi mô là gì?",
        "goi_y": [
            "A.Giảm chi phí vận tải",
            "B.Tăng tốc lưu thông hàng hóa",
            "C.Giúp doanh nghiệp chuyên môn hóa",
            "D.Tất cả các đáp án trên"
        ],
        "dap_an_dung": "D"
    },
    {
        "cau_hoi": "Forwarder giúp giảm chi phí vận tải nhờ khả năng nào?",
        "goi_y": [
            "A.Gom hàng lẻ",
            "B.Tìm tuyến vận tải phù hợp",
            "C.Làm việc trực tiếp với hãng tàu",
            "D.Tất cả các đáp án trên"
        ],
        "dap_an_dung": "D"
    },
    {
        "cau_hoi": "Người giao nhận có quan hệ với ngân hàng nhằm mục đích gì?",
        "goi_y": [
            "A.Thanh toán",
            "B.Vay vốn",
            "C.Đăng kiểm",
            "D.Đóng container"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "VIFFAS hiện nay đổi tên thành gì?",
        "goi_y": [
            "A.VPA",
            "B.VLA",
            "C.VCCI",
            "D.VSA"
        ],
        "dap_an_dung": "B"
    },
    {
        "cau_hoi": "Theo Luật Thương mại, hợp đồng mua bán hàng hóa quốc tế phải được lập dưới hình thức nào?",
        "goi_y": [
            "A.Bằng miệng",
            "B.Bằng văn bản hoặc hình thức có giá trị pháp lý tương đương",
            "C.Chỉ qua email",
            "D.Chỉ cần hóa đơn"
        ],
        "dap_an_dung": "B"
    },
    {
        "cau_hoi": "Đâu KHÔNG phải là rủi ro trong thương mại quốc tế?",
        "goi_y": [
            "A.Khoảng cách xa",
            "B.Khác biệt văn hóa",
            "C.Khác biệt pháp luật",
            "D.Cùng một hệ thống pháp luật"
        ],
        "dap_an_dung": "D"
    },
    {
        "cau_hoi": "CISG 1980 là công ước về?",
        "goi_y": [
            "A.Vận tải biển",
            "B.Bảo hiểm",
            "C.Hợp đồng mua bán hàng hóa quốc tế",
            "D.Hải quan"
        ],
        "dap_an_dung": "C"
    },
    {
        "cau_hoi": "Điều khoản nào sau đây KHÔNG phải là nội dung cơ bản của hợp đồng mua bán quốc tế?",
        "goi_y": [
            "A.Commodity",
            "B.Payment",
            "C.Arbitration",
            "D.Driver"
        ],
        "dap_an_dung": "D"
    },
    {
        "cau_hoi": "Incoterms quy định nội dung nào?",
        "goi_y": [
            "A.Giá bán hàng hóa",
            "B.Phân chia trách nhiệm, chi phí và rủi ro",
            "C.Thuế thu nhập",
            "D.Lãi suất ngân hàng"
        ],
        "dap_an_dung": "B"
    },
    {
        "cau_hoi": "Incoterms 2020 đã thay điều kiện DAT bằng điều kiện nào?",
        "goi_y": [
            "A.DDP",
            "B.DPU",
            "C.DAP",
            "D.CPT"
        ],
        "dap_an_dung": "B"
    },
    {
        "cau_hoi": "Điều kiện nào sau đây chỉ áp dụng cho vận tải biển và đường thủy nội địa?",
        "goi_y": [
            "A.CIP",
            "B.CPT",
            "C.FOB",
            "D.DAP"
        ],
        "dap_an_dung": "C"
    },
    {
        "cau_hoi": "Khi lựa chọn điều kiện Incoterms cần xem xét yếu tố nào?",
        "goi_y": [
            "A.Phương thức vận tải",
            "B.Khả năng mua bảo hiểm",
            "C.Phân chia chi phí và rủi ro",
            "D.Tất cả các đáp án trên"
        ],
        "dap_an_dung": "D"
    },
    {
        "cau_hoi": "Cơ sở pháp lý quan trọng điều chỉnh hoạt động logistics tại Việt Nam là?",
        "goi_y": [
            "A.Luật Thương mại 2005",
            "B.Nghị định 163/2017/NĐ-CP",
            "C.Luật Quản lý ngoại thương 2017",
            "D.Tất cả các đáp án trên"
        ],
        "dap_an_dung": "D"
    },
    {
        "cau_hoi": "Theo Incoterms 2020 có bao nhiêu điều kiện thương mại?",
        "goi_y": [
            "A.9",
            "B.10",
            "C.11",
            "D.12"
        ],
        "dap_an_dung": "C"
    }
    ]
elif chuong_da_chon == "Chương 2: Giao nhận bằng đường biển":
    cac_cau_hoi =[  
        {
        "cau_hoi": "Hiện nay vận tải biển đảm nhận khoảng bao nhiêu khối lượng hàng hóa vận chuyển quốc tế?",
        "goi_y": [
            "A.50%",
            "B.60%",
            "C.80%",
            "D.95%"
        ],
        "dap_an_dung": "C"
    },
    {
        "cau_hoi": "Ưu điểm lớn nhất của vận tải biển là gì?",
        "goi_y": [
            "A.Tốc độ nhanh",
            "B.Chi phí thấp và năng lực vận chuyển lớn",
            "C.Không phụ thuộc thời tiết",
            "D.Thời gian vận chuyển ngắn"
        ],
        "dap_an_dung": "B"
    },
    {
        "cau_hoi": "Nhược điểm lớn nhất của vận tải biển là gì?",
        "goi_y": [
            "A.Giá cước cao",
            "B.Không vận chuyển được hàng nặng",
            "C.Phụ thuộc điều kiện tự nhiên và thời gian vận chuyển dài",
            "D.Không phù hợp hàng quốc tế"
        ],
        "dap_an_dung": "C"
    },
    {
        "cau_hoi": "Yếu tố nào sau đây KHÔNG phải căn cứ lựa chọn phương thức vận tải?",
        "goi_y": [
            "A.Chi phí vận chuyển",
            "B.Điều kiện tự nhiên",
            "C.Màu sắc phương tiện",
            "D.Đặc điểm hàng hóa"
        ],
        "dap_an_dung": "C"
    },
   
    {
        "cau_hoi": "Dung tích chứa hàng bao kiện được gọi là gì?",
        "goi_y": [
            "A.Grain Space",
            "B.Bale Space",
            "C.Cargo Hold",
            "D.Net Space"
        ],
        "dap_an_dung": "B"
    },
    {
        "cau_hoi": "Dung tích chứa hàng rời được gọi là gì?",
        "goi_y": [
            "A.Bale Space",
            "B.Grain Space",
            "C.Cargo Volume",
            "D.Net Space"
        ],
        "dap_an_dung": "B"
    },
    {
        "cau_hoi": "Công thức hệ số xếp hàng của tàu là?",
        "goi_y": [
            "A.CL = DWCC/CS",
            "B.CL = CS × DWCC",
            "C.CL = CS/DWCC",
            "D.CL = DWC/CS"
        ],
        "dap_an_dung": "C"
    },
    {
        "cau_hoi": "Stowage Factor (SF) được tính bằng?",
        "goi_y": [
            "A.Trọng lượng/Thể tích",
            "B.Thể tích/Trọng lượng",
            "C.DWT/CS",
            "D.CS/DWT"
        ],
        "dap_an_dung": "B"
    },
    {
        "cau_hoi": "Hàng nặng (Deadweight cargo) có SF như thế nào?",
        "goi_y": [
            "A.> 40 c.ft/ton",
            "B.< 20 c.ft/ton",
            "C.≤ 40 c.ft/ton",
            "D.= 100 c.ft/ton"
        ],
        "dap_an_dung": "C"
    },
    {
        "cau_hoi": "Hàng nhẹ (Measurement cargo) có SF như thế nào?",
        "goi_y": [
            "A.≤ 40 c.ft/ton",
            "B.> 40 c.ft/ton",
            "C.= 40 c.ft/ton",
            "D.< 10 c.ft/ton"
        ],
        "dap_an_dung": "B"
    },
    {
        "cau_hoi": "Thuê tàu chợ (Liner) có đặc điểm nào?",
        "goi_y": [
            "A.Không có lịch trình",
            "B.Theo lịch trình cố định",
            "C.Chỉ chở hàng rời",
            "D.Chỉ chở dầu"
        ],
        "dap_an_dung": "B"
    },
    {
        "cau_hoi": "Chứng từ chính của thuê tàu chợ là gì?",
        "goi_y": [
            "A.Invoice",
            "B.Packing List",
            "C.B/L",
            "D.C/O"
        ],
        "dap_an_dung": "C"
    },
    {
        "cau_hoi": "Trong thuê tàu chợ, ai là người chuyên chở?",
        "goi_y": [
            "A.Người thuê tàu",
            "B.Chủ hàng",
            "C.Chủ tàu",
            "D.Hải quan"
        ],
        "dap_an_dung": "C"
    },
    {
        "cau_hoi": "Thuê tàu chuyến có đặc điểm nào?",
        "goi_y": [
            "A.Theo tuyến cố định",
            "B.Không theo lịch trình cố định",
            "C.Không có hợp đồng",
            "D.Không có B/L"
        ],
        "dap_an_dung": "B"
    },
     {
        "cau_hoi": "Thuê tàu chuyến một (Single Trip) là hình thức thuê tàu nào?",
        "goi_y": [
            "A.Cho nhiều chuyến liên tiếp",
            "B.Chỉ cho một chuyến vận chuyển",
            "C.Theo thời gian 1 năm",
            "D.Không giới hạn số chuyến"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Round Trip là tên tiếng Anh của hình thức thuê tàu nào?",
        "goi_y": [
            "A.Thuê tàu trần",
            "B.Thuê định hạn",
            "C.Thuê chuyến khứ hồi",
            "D.Thuê khoán"
        ],
        "dap_an_dung": "C"
    },

    {
        "cau_hoi": "Thuê chuyến khứ hồi nghĩa là gì?",
        "goi_y": [
            "A.Tàu chỉ chạy chiều đi",
            "B.Tàu thực hiện cả chuyến đi và chuyến về theo hợp đồng",
            "C.Thuê tàu theo tháng",
            "D.Thuê toàn bộ thủy thủ đoàn"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Consecutive Voyage là gì?",
        "goi_y": [
            "A.Thuê định hạn",
            "B.Thuê chuyến liên tục",
            "C.Thuê tàu trần",
            "D.Thuê khoán"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Đặc điểm của thuê chuyến liên tục là gì?",
        "goi_y": [
            "A.Chỉ vận chuyển một lần",
            "B.Thực hiện nhiều chuyến liên tiếp theo cùng hợp đồng",
            "C.Chỉ vận chuyển chiều về",
            "D.Thuê tàu theo ngày"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Thuê chuyến khứ hồi liên tục là gì?",
        "goi_y": [
            "A.Một chuyến đi duy nhất",
            "B.Nhiều chuyến đi và về liên tiếp",
            "C.Thuê tàu trong 6 tháng",
            "D.Thuê không có thủy thủ"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Thuê khoán là hình thức thuê dựa trên yếu tố nào?",
        "goi_y": [
            "A.Thời gian sử dụng tàu",
            "B.Khối lượng hàng hóa vận chuyển",
            "C.Tuổi của tàu",
            "D.Quốc tịch tàu"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Thuê định hạn (Time Charter) là gì?",
        "goi_y": [
            "A.Thuê theo số lượng hàng hóa",
            "B.Thuê trong một thời gian xác định",
            "C.Thuê một chuyến duy nhất",
            "D.Thuê theo từng container"
        ],
        "dap_an_dung": "B"
    },
    {
        "cau_hoi": "Trong thuê định hạn, căn cứ chính để tính tiền thuê là gì?",
        "goi_y": [
            "A.Số container",
            "B.Khối lượng hàng hóa",
            "C.Thời gian thuê tàu",
            "D.Khoảng cách vận chuyển"
        ],
        "dap_an_dung": "C"
    },
    {
        "cau_hoi": "Hình thức thuê nào không dựa trên thời gian thuê?",
        "goi_y": [
            "A.Time Charter",
            "B.Thuê định hạn",
            "C.Thuê khoán",
            "D.Thuê tàu 12 tháng"
        ],
        "dap_an_dung": "C"
    },
    {
        "cau_hoi": "Hợp đồng thuê tàu chuyến được gọi là gì?",
        "goi_y": [
            "A.Booking Note",
            "B.Charter Party (C/P)",
            "C.Shipping Instruction",
            "D.Invoice"
        ],
        "dap_an_dung": "B"
    },
    {
        "cau_hoi": "Trong thuê tàu chuyến, người thuê tàu có quyền gì?",
        "goi_y": [
            "A.Không được thương lượng cước",
            "B.Được tự do thỏa thuận điều khoản chuyên chở",
            "C.Phải theo biểu cước",
            "D.Không được ký hợp đồng"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Thuê tàu chuyến thường dùng để chở loại hàng nào?",
        "goi_y": [
            "A.Hàng bách hóa",
            "B.Hàng lẻ",
            "C.Hàng lỏng và hàng khối lượng lớn",
            "D.Hàng chuyển phát nhanh"
        ],
        "dap_an_dung": "C"
    },
      {
        "cau_hoi": "Nội dung nào sau đây KHÔNG phải là nội dung chủ yếu của hợp đồng thuê tàu chuyến?",
        "goi_y": [
            "A.Các bên của hợp đồng",
            "B.Quy định về hàng hóa",
            "C.Quy định về cước phí và thanh toán cước phí",
            "D.Chi phí bảo dưỡng tàu định kỳ"
        ],
        "dap_an_dung": "D"
    },

    {
        "cau_hoi": "Trong hợp đồng thuê tàu chuyến, quy định về hàng hóa bao gồm những nội dung nào?",
        "goi_y": [
            "A.Tên hàng, loại bao bì, ký mã hiệu, trọng lượng, số lượng, thể tích, tính chất nguy hiểm",
            "B.Chỉ tên hàng và trọng lượng",
            "C.Chỉ số lượng hàng",
            "D.Chỉ loại bao bì"
        ],
        "dap_an_dung": "A"
    },

    {
        "cau_hoi": "Điều khoản nào quy định thời gian tàu đến cảng để xếp hàng?",
        "goi_y": [
            "A.Quy định về con tàu và thời gian tàu đến cảng xếp hàng",
            "B.Quy định về cước phí",
            "C.Quy định về trọng tài",
            "D.Quy định về luật pháp"
        ],
        "dap_an_dung": "A"
    },
  {
        "cau_hoi": "Nguyên tắc chung về giao nhận hàng hóa là gì?",
        "goi_y": [
            "A.Nhận theo số lượng, giao theo trọng lượng",
            "B.Nhận bằng phương pháp nào thì giao bằng phương pháp ấy",
            "C.Nhận theo container, giao theo bao kiện",
            "D.Nhận theo yêu cầu của người gửi, giao theo yêu cầu của người nhận"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Nội dung nào sau đây KHÔNG phải là một phương pháp giao nhận hàng hóa?",
        "goi_y": [
            "A.Giao nhận nguyên bao kiện, bó, tấm, cây, chiếc",
            "B.Giao nhận theo nguyên hầm cặp chì",
            "C.Giao nhận theo giá trị lô hàng",
            "D.Giao nhận theo số lượng, trọng lượng, thể tích"
        ],
        "dap_an_dung": "C"
    },

    {
        "cau_hoi": "Giao nhận theo số lượng, trọng lượng, thể tích được thực hiện bằng cách nào?",
        "goi_y": [
            "A.Kiểm tra niêm phong",
            "B.Cân, đo, đong, đếm",
            "C.Chụp ảnh hàng hóa",
            "D.Kiểm tra chứng từ"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Phương pháp giao nhận nào áp dụng đối với hàng nguyên container còn nguyên niêm phong?",
        "goi_y": [
            "A.Giao nhận nguyên container cặp chì",
            "B.Giao nhận theo mớn nước của tàu",
            "C.Giao nhận theo cân, đo, đong, đếm",
            "D.Giao nhận nguyên bao kiện"
        ],
        "dap_an_dung": "A"
    },

    {
        "cau_hoi": "Phương pháp giao nhận nào thường được sử dụng đối với hàng rời có khối lượng lớn như than, quặng, ngũ cốc?",
        "goi_y": [
            "A.Giao nhận nguyên container cặp chì",
            "B.Giao nhận nguyên bao kiện",
            "C.Giao nhận theo mớn nước của tàu",
            "D.Giao nhận theo cây, bó"
        ],
        "dap_an_dung": "C"
    },

    {
        "cau_hoi": "Theo tài liệu, phương pháp giao nhận hàng hóa có thể được thực hiện như thế nào?",
        "goi_y": [
            "A.Chỉ sử dụng một phương pháp duy nhất",
            "B.Kết hợp nhiều phương pháp giao nhận",
            "C.Chỉ áp dụng cho hàng container",
            "D.Chỉ áp dụng cho hàng bao kiện"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Phương pháp giao nhận nào sau đây KHÔNG được liệt kê trong bài?",
        "goi_y": [
            "A.Giao nhận nguyên hầm cặp chì",
            "B.Giao nhận theo mớn nước của tàu",
            "C.Giao nhận theo số lượng, trọng lượng, thể tích",
            "D.Giao nhận theo giá CIF"
        ],
        "dap_an_dung": "D"
    },
    {
        "cau_hoi": "FIO (Free In and Out) có nghĩa là gì?",
        "goi_y": [
            "A.Chủ tàu chịu chi phí xếp và dỡ hàng",
            "B.Người thuê tàu (chủ hàng) chịu chi phí xếp và dỡ hàng",
            "C.Hai bên chia đôi chi phí",
            "D.Cảng chịu toàn bộ chi phí"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Ký hiệu FO + S trong hợp đồng thuê tàu có nghĩa là gì?",
        "goi_y": [
            "A.Người thuê chịu chi phí dỡ hàng và sắp xếp hàng (Stowed)",
            "B.Chủ tàu chịu toàn bộ chi phí",
            "C.Miễn chi phí xếp hàng",
            "D.Chỉ áp dụng cho container"
        ],
        "dap_an_dung": "A"
    },

    {
        "cau_hoi": "Ký hiệu T (Trimmed) trong hợp đồng thuê tàu có nghĩa là gì?",
        "goi_y": [
            "A.Hàng được kiểm đếm",
            "B.San, cào hàng rời",
            "C.Đóng container",
            "D.Niêm phong hàng"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Điều khoản nào quy định cách tính và thanh toán tiền thuê tàu?",
        "goi_y": [
            "A.Quy định về cước phí và thanh toán cước phí",
            "B.Quy định về hàng hóa",
            "C.Quy định về cảng",
            "D.Quy định về trọng tài"
        ],
        "dap_an_dung": "A"
    },

    {
        "cau_hoi": "Despatch là gì?",
        "goi_y": [
            "A.Tiền thưởng khi hoàn thành xếp dỡ sớm hơn thời gian quy định",
            "B.Tiền phạt do chậm xếp dỡ",
            "C.Tiền thuê tàu",
            "D.Tiền bảo hiểm"
        ],
        "dap_an_dung": "A"
    },

    {
        "cau_hoi": "Demurrage là gì?",
        "goi_y": [
            "A.Tiền thưởng khi xếp dỡ nhanh",
            "B.Tiền phạt do vượt thời gian xếp dỡ quy định",
            "C.Tiền thuê tàu",
            "D.Tiền lưu kho"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Weather Working Days (WWD) được hiểu là gì?",
        "goi_y": [
            "A.Ngày dương lịch",
            "B.Ngày làm việc khi thời tiết cho phép",
            "C.Ngày làm việc 24 giờ",
            "D.Ngày nghỉ"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Điều khoản 'Luật pháp và trọng tài' trong hợp đồng thuê tàu nhằm mục đích gì?",
        "goi_y": [
            "A.Quy định phương thức thanh toán",
            "B.Quy định luật áp dụng và cơ quan giải quyết tranh chấp",
            "C.Quy định giá cước",
            "D.Quy định thời gian tàu đến"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Nếu việc xếp dỡ hoàn thành nhanh hơn thời gian quy định thì người thuê tàu có thể được hưởng khoản nào?",
        "goi_y": [
            "A.Demurrage",
            "B.Despatch",
            "C.FIO",
            "D.FO + S"
        ],
        "dap_an_dung": "B"
    },
    {
        "cau_hoi": "Trong quy trình thuê tàu chợ, ai là người lập Booking Request đầu tiên?",
        "goi_y": [
            "A.Hải quan",
            "B.Hãng tàu",
            "C.Chủ hàng hoặc FWD",
            "D.Cảng"
        ],
        "dap_an_dung": "C"
    },
      {
        "cau_hoi": "Cảng biển ký kết hợp đồng ủy thác với chủ hàng để thực hiện công việc nào sau đây?",
        "goi_y": [
            "A.Khai báo hải quan",
            "B.Giao nhận, bốc dỡ, bảo quản và lưu kho hàng hóa",
            "C.Kiểm định chất lượng hàng hóa",
            "D.Mua bảo hiểm hàng hóa"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Sau khi giao nhận hàng hóa, cảng có trách nhiệm gì?",
        "goi_y": [
            "A.Thu thuế xuất nhập khẩu",
            "B.Lập chứng từ kế toán và biên bản giao nhận",
            "C.Phát hành vận đơn",
            "D.Kiểm tra hải quan"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Nếu hàng hóa bị hư hỏng, tổn thất trong khu vực cảng và có biên bản hợp lệ thì ai chịu trách nhiệm?",
        "goi_y": [
            "A.Chủ hàng tự chịu trách nhiệm",
            "B.Hãng tàu chịu trách nhiệm",
            "C.Cảng phải bồi thường nếu lỗi thuộc về cảng",
            "D.Hải quan bồi thường"
        ],
        "dap_an_dung": "C"
    },

    {
        "cau_hoi": "Trong trường hợp nào cảng không chịu trách nhiệm?",
        "goi_y": [
            "A.Hàng còn nguyên bao kiện hoặc nguyên đai, chì nhưng bên trong hư hỏng hoặc không rõ ràng",
            "B.Làm mất hàng trong kho",
            "C.Bốc dỡ sai quy trình",
            "D.Làm hư hỏng hàng do lỗi của cảng"
        ],
        "dap_an_dung": "A"
    },

    {
        "cau_hoi": "Người vận chuyển phải cung cấp gì cho cảng để cảng giao nhận hàng hóa?",
        "goi_y": [
            "A.Hợp đồng mua bán",
            "B.Chứng từ cần thiết",
            "C.Giấy chứng nhận xuất xứ (C/O)",
            "D.Hóa đơn thương mại"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Người vận chuyển có trách nhiệm gì?",
        "goi_y": [
            "A.Đảm bảo tàu đủ điều kiện làm hàng an toàn",
            "B.Thu thuế nhập khẩu",
            "C.Kiểm hóa hàng hóa",
            "D.Cấp C/O"
        ],
        "dap_an_dung": "A"
    },

    {
        "cau_hoi": "Theo hợp đồng đã ký, người vận chuyển phải thực hiện nghĩa vụ nào?",
        "goi_y": [
            "A.Trả chi phí bốc dỡ, đóng gói... cho cảng",
            "B.Trả thuế nhập khẩu",
            "C.Mua bảo hiểm cho chủ hàng",
            "D.Thanh toán phí lưu kho"
        ],
        "dap_an_dung": "A"
    },

    {
        "cau_hoi": "Doanh nghiệp xuất nhập khẩu có thể giao nhận hàng hóa với cảng trong trường hợp nào?",
        "goi_y": [
            "A.Hàng lưu kho tại cảng",
            "B.Hàng nhận trực tiếp từ tàu",
            "C.Cả A và B đều đúng",
            "D.Chỉ khi có đại lý"
        ],
        "dap_an_dung": "C"
    },

    {
        "cau_hoi": "Doanh nghiệp xuất nhập khẩu ký hợp đồng nào với cảng?",
        "goi_y": [
            "A.Hợp đồng thuê tàu",
            "B.Hợp đồng bốc dỡ, vận chuyển, bảo quản và lưu kho",
            "C.Hợp đồng bảo hiểm",
            "D.Hợp đồng giám định"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Doanh nghiệp xuất nhập khẩu theo dõi quá trình giao nhận nhằm mục đích gì?",
        "goi_y": [
            "A.Tính cước vận tải",
            "B.Giải quyết các vấn đề phát sinh",
            "C.Thu thuế",
            "D.Kiểm hóa"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Trong quá trình giao nhận, doanh nghiệp xuất nhập khẩu phải làm gì?",
        "goi_y": [
            "A.Lập các chứng từ cần thiết để có cơ sở pháp lý khiếu nại",
            "B.Phát hành vận đơn",
            "C.Kiểm hóa hàng",
            "D.Thu phí cảng"
        ],
        "dap_an_dung": "A"
    },

    {
        "cau_hoi": "Doanh nghiệp xuất nhập khẩu phải thực hiện nghĩa vụ nào sau đây?",
        "goi_y": [
            "A.Thanh toán các loại phí cho cảng",
            "B.Thu phí lưu kho",
            "C.Thu thuế nhập khẩu",
            "D.Giám định hàng hóa"
        ],
        "dap_an_dung": "A"
    },

    {
        "cau_hoi": "Chức năng quan trọng nhất của Hải quan là gì?",
        "goi_y": [
            "A.Bốc dỡ hàng hóa",
            "B.Kiểm tra, giám sát và kiểm soát hải quan",
            "C.Vận chuyển hàng hóa",
            "D.Lưu kho hàng hóa"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Hải quan đảm bảo thực hiện các quy định của Nhà nước về vấn đề gì?",
        "goi_y": [
            "A.Giá cước vận tải",
            "B.Thuế xuất khẩu và thuế nhập khẩu",
            "C.Bảo hiểm hàng hóa",
            "D.Phí lưu kho"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Hải quan có quyền phát hiện, ngăn chặn và xử lý hành vi nào?",
        "goi_y": [
            "A.Hàng hóa giao chậm",
            "B.Buôn lậu, gian lận thương mại và vận chuyển trái phép hàng hóa qua biên giới",
            "C.Chậm thanh toán cước tàu",
            "D.Thiếu container"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Đối tượng nào không có nhiệm vụ lập chứng từ giao nhận hàng hóa?",
        "goi_y": [
            "A.Cảng biển",
            "B.Doanh nghiệp xuất nhập khẩu",
            "C.Hải quan",
            "D.Người vận chuyển"
        ],
        "dap_an_dung": "C"
    },

    {
        "cau_hoi": "Đơn vị nào chịu trách nhiệm kiểm tra, giám sát và kiểm soát hàng hóa xuất nhập khẩu?",
        "goi_y": [
            "A.Cảng biển",
            "B.Doanh nghiệp xuất nhập khẩu",
            "C.Hải quan",
            "D.Người vận chuyển"
        ],
        "dap_an_dung": "C"
    },

    {
        "cau_hoi": "Đơn vị nào chịu trách nhiệm thanh toán các khoản phí cho cảng?",
        "goi_y": [
            "A.Hải quan",
            "B.Doanh nghiệp xuất nhập khẩu",
            "C.Người vận chuyển",
            "D.Đại lý tàu"
        ],
        "dap_an_dung": "B"
    },
    {
        "cau_hoi": "MBL là viết tắt của cụm từ nào?",
        "goi_y": [
            "A.Master Bill of Lading",
            "B.Marine Booking List",
            "C.Main Booking Letter",
            "D.Manifest Booking List"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Người môi giới thuê tàu được gọi là gì?",
        "goi_y": [
            "A.Carrier",
            "B.Broker",
            "C.Charterer",
            "D.Shipper"
        ],
        "dap_an_dung": "B"
    },
    {
        "cau_hoi": "Sau khi ký hợp đồng thuê tàu chuyến, bước tiếp theo là gì?",
        "goi_y": [
            "A.Đưa hàng ra cảng để xếp lên tàu",
            "B.Làm Shipping Instruction",
            "C.Khai Manifest",
            "D.Đổi vận đơn"
        ],
        "dap_an_dung": "A"
    },

    {
        "cau_hoi": "Thuê chuyến một còn được gọi là gì?",
        "goi_y": [
            "A.Round Trip",
            "B.Consecutive Voyage",
            "C.Single Trip",
            "D.Time Charter"
        ],
        "dap_an_dung": "C"
    },
    {
        "cau_hoi": "Thuê định hạn được gọi bằng tiếng Anh là gì?",
        "goi_y": [
            "A.Bareboat Charter",
            "B.Time Charter",
            "C.Voyage Charter",
            "D.Spot Charter"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "FIO là viết tắt của cụm từ nào?",
        "goi_y": [
            "A.Free In and Out",
            "B.Freight In Order",
            "C.Full In Out",
            "D.Free Inland Operation"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Despatch và Demurrage liên quan đến nội dung nào trong hợp đồng thuê tàu?",
        "goi_y": [
            "A.Thuế xuất nhập khẩu",
            "B.Thời gian làm hàng",
            "C.Đăng kiểm tàu",
            "D.Bảo hiểm hàng hóa"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Nguyên tắc chung về giao nhận hàng hóa là gì?",
        "goi_y": [
            "A.Theo yêu cầu chủ tàu",
            "B.Theo quy định cảng",
            "C.Nhận bằng phương pháp nào thì giao bằng phương pháp ấy",
            "D.Theo yêu cầu hải quan"
        ],
        "dap_an_dung": "C"
    },
    {
        "cau_hoi": "Phương pháp giao nhận nào áp dụng đối với container nguyên?",
        "goi_y": [
            "A.Giao nhận theo mớn nước",
            "B.Giao nhận theo nguyên container cặp chì",
            "C.Giao nhận theo bó",
            "D.Giao nhận theo cây"
        ],
        "dap_an_dung": "B"
    },
    {
        "cau_hoi": "Đơn vị nào KHÔNG có trách nhiệm kiểm tra thuế nhập khẩu?",
        "goi_y": [
            "A.Cảng biển",
            "B.Doanh nghiệp XNK",
            "C.Người vận chuyển",
            "D.Hải quan"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Một trong các trách nhiệm của doanh nghiệp XNK là gì?",
        "goi_y": [
            "A.Thanh toán các loại phí cho cảng",
            "B.Điều khiển tàu",
            "C.Kiểm tra mớn nước tàu",
            "D.Cấp vận đơn"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Người vận chuyển phải chuẩn bị điều gì để làm hàng an toàn?",
        "goi_y": [
            "A.Giấy phép kinh doanh",
            "B.Ánh sáng và trang thiết bị",
            "C.Hợp đồng bảo hiểm",
            "D.Giấy chứng nhận xuất xứ"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Hải quan có nhiệm vụ nào sau đây?",
        "goi_y": [
            "A.Bốc dỡ hàng hóa",
            "B.Kiểm tra, giám sát và kiểm soát hải quan",
            "C.Phát hành vận đơn",
            "D.Lưu kho hàng hóa"
        ],
        "dap_an_dung": "B"
    },
    {
        "cau_hoi": "Khi hàng hóa lưu kho tại cảng bị hư hỏng và có biên bản hợp lệ, cảng phải làm gì?",
        "goi_y": [
            "A.Không chịu trách nhiệm",
            "B.Bồi thường nếu không chứng minh được mình không có lỗi",
            "C.Chuyển trách nhiệm cho hải quan",
            "D.Chuyển trách nhiệm cho hãng tàu"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Trong trường hợp nào cảng không chịu trách nhiệm về hàng hóa bên trong bao kiện?",
        "goi_y": [
            "A.Bao kiện bị rách",
            "B.Dấu chì còn nguyên vẹn và ký mã hiệu sai hoặc không rõ",
            "C.Hàng bị mất",
            "D.Chủ hàng yêu cầu"
        ],
        "dap_an_dung": "B"
    },
    {
        "cau_hoi": "Working days of 24 hours là loại thời gian dùng để xác định nội dung nào?",
        "goi_y": [
            "A.Thời gian bảo hành",
            "B.Thời gian làm hàng",
            "C.Thời gian vận chuyển",
            "D.Thời gian lưu kho"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Thể tích hàng hóa chia cho trọng lượng hàng hóa được gọi là gì?",
        "goi_y": [
            "A.DWC",
            "B.CL",
            "C.SF",
            "D.GRT"
        ],
        "dap_an_dung": "C"
    },
    {
        "cau_hoi": "Loại tàu nào thường được sử dụng để chở hàng bách hóa với số lượng linh hoạt?",
        "goi_y": [
            "A.Thuê tàu chợ",
            "B.Thuê tàu chuyến",
            "C.Thuê tàu trần",
            "D.Time Charter"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Yêu cầu quan trọng nhất khi giao nhận hàng hóa xuất khẩu tại cảng biển là gì?",
        "goi_y": [
            "A.Chỉ cần giao hàng đúng thời gian",
            "B.Nhanh chóng, kết toán chính xác và lập đầy đủ chứng từ",
            "C.Chỉ cần khai hải quan",
            "D.Chỉ cần đóng phí"
        ],
        "dap_an_dung": "B"
    },
    {
        "cau_hoi": "Bước đầu tiên trong quy trình giao nhận hàng xuất khẩu tại cảng biển là gì?",
        "goi_y": [
            "A.Giao hàng cho tàu",
            "B.Lập bộ chứng từ thanh toán",
            "C.Chuẩn bị hàng và nắm tình hình tàu",
            "D.Thông quan"
        ],
        "dap_an_dung": "C"
    },
    {
        "cau_hoi": "Trong quy trình FWD hàng xuất, sau khi booking là bước nào?",
        "goi_y": [
            "A.Phát hành B/L",
            "B.Đóng hàng tại kho hoặc cảng",
            "C.Nộp thuế",
            "D.Nhận D/O"
        ],
        "dap_an_dung": "B"
    },
    {
        "cau_hoi": "Trong quy trình FWD hàng nhập, sau khi nhận Arrival Notice (AN) sẽ thực hiện bước nào?",
        "goi_y": [
            "A.Lấy D/O",
            "B.Nộp thuế và hoàn tất thủ tục hải quan",
            "C.Trả container rỗng",
            "D.Kéo container về kho"
        ],
        "dap_an_dung": "B"
    },
    {
        "cau_hoi": "B/L là viết tắt của cụm từ nào?",
        "goi_y": [
            "A.Bill of Lading",
            "B.Booking List",
            "C.Broker List",
            "D.Board List"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Chức năng nào KHÔNG phải của vận đơn đường biển (B/L)?",
        "goi_y": [
            "A.Biên lai nhận hàng",
            "B.Bằng chứng hợp đồng vận chuyển",
            "C.Chứng từ sở hữu hàng hóa",
            "D.Giấy chứng nhận xuất xứ hàng hóa"
        ],
        "dap_an_dung": "D"
    },
    {
        "cau_hoi": "Ai là người có quyền phát hành vận đơn đường biển?",
        "goi_y": [
            "A.Người mua",
            "B.Hải quan",
            "C.Người có chức năng chuyên chở",
            "D.Ngân hàng"
        ],
        "dap_an_dung": "C"
    },
    {
        "cau_hoi": "Vận đơn 'Shipped on Board' được cấp khi nào?",
        "goi_y": [
            "A.Trước khi đóng hàng",
            "B.Sau khi hàng đã được bốc lên tàu",
            "C.Khi tàu cập cảng",
            "D.Sau khi thanh toán"
        ],
        "dap_an_dung": "B"
    },
    {
        "cau_hoi": "Điều kiện Incoterms nào bắt buộc phải sử dụng Shipped on Board B/L để thanh toán?",
        "goi_y": [
            "A.EXW",
            "B.FCA",
            "C.FOB, CFR, CIF",
            "D.DDP"
        ],
        "dap_an_dung": "C"
    },
    {
        "cau_hoi": "Clean B/L là loại vận đơn như thế nào?",
        "goi_y": [
            "A.Có ghi chú hàng hư hỏng",
            "B.Không có phê chú xấu về hàng hóa hoặc bao bì",
            "C.Chỉ dùng cho container",
            "D.Chỉ dùng cho hàng lỏng"
        ],
        "dap_an_dung": "B"
    },
    {
        "cau_hoi": "Vận đơn có ghi chú bao bì bị rách thuộc loại nào?",
        "goi_y": [
            "A.Clean B/L",
            "B.Straight B/L",
            "C.Unclean B/L",
            "D.Through B/L"
        ],
        "dap_an_dung": "C"
    },
    {
        "cau_hoi": "Vận đơn đích danh (Straight B/L) là vận đơn ghi rõ điều gì?",
        "goi_y": [
            "A.Tên tàu",
            "B.Tên và địa chỉ người nhận hàng",
            "C.Cảng chuyển tải",
            "D.Số container"
        ],
        "dap_an_dung": "B"
    },
    {
        "cau_hoi": "Vận đơn theo lệnh được gọi là gì?",
        "goi_y": [
            "A.Straight B/L",
            "B.To Order B/L",
            "C.Bearer B/L",
            "D.Direct B/L"
        ],
        "dap_an_dung": "B"
    },
    {
        "cau_hoi": "Loại vận đơn nào không ghi tên người nhận hàng?",
        "goi_y": [
            "A.Straight B/L",
            "B.To Order B/L",
            "C.To Bearer B/L",
            "D.Clean B/L"
        ],
        "dap_an_dung": "C"
    },
    {
        "cau_hoi": "Through Bill of Lading được sử dụng khi nào?",
        "goi_y": [
            "A.Hàng đi thẳng không chuyển tải",
            "B.Hàng vận chuyển bằng nhiều con tàu",
            "C.Hàng chỉ đi nội địa",
            "D.Hàng container lạnh"
        ],
        "dap_an_dung": "B"
    },
    {
        "cau_hoi": "Sea Waybill KHÔNG có chức năng nào sau đây?",
        "goi_y": [
            "A.Biên lai nhận hàng",
            "B.Bằng chứng hợp đồng vận chuyển",
            "C.Chứng từ sở hữu hàng hóa",
            "D.Chứng từ vận tải"
        ],
        "dap_an_dung": "C"
    },
    {
        "cau_hoi": "Ưu điểm lớn nhất của Sea Waybill là gì?",
        "goi_y": [
            "A.Có thể ký hậu",
            "B.Nhận hàng nhanh mà không cần vận đơn gốc",
            "C.Dùng thay C/O",
            "D.Có giá trị thanh toán L/C"
        ],
        "dap_an_dung": "B"
    },
    {
        "cau_hoi": "Booking Confirmation là gì?",
        "goi_y": [
            "A.Hợp đồng mua bán",
            "B.Xác nhận đặt chỗ của hãng tàu",
            "C.Giấy chứng nhận bảo hiểm",
            "D.Giấy phép xuất khẩu"
        ],
        "dap_an_dung": "B"
    },
    {
        "cau_hoi": "VGM là viết tắt của cụm từ nào?",
        "goi_y": [
            "A.Verified Gross Mass",
            "B.Valid Goods Manifest",
            "C.Vessel Gross Measurement",
            "D.Volume Gross Method"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Delivery Order (D/O) là chứng từ gì?",
        "goi_y": [
            "A.Lệnh giao hàng",
            "B.Phiếu đóng gói",
            "C.Bản kê khai hàng hóa",
            "D.Hóa đơn thương mại"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Ocean Freight (O/F) được xác định dựa trên yếu tố nào?",
        "goi_y": [
            "A.Màu container",
            "B.Khối lượng, thể tích và tuyến vận chuyển",
            "C.Quốc tịch tàu",
            "D.Tên hãng tàu"
        ],
        "dap_an_dung": "B"
    },
    {
        "cau_hoi": "Theo quy ước đường biển, 1 m³ tương đương bao nhiêu kg?",
        "goi_y": [
            "A.250 kg",
            "B.300 kg",
            "C.333,3 kg",
            "D.500 kg"
        ],
        "dap_an_dung": "C"
    },
    {
        "cau_hoi": "Nếu 1 tấn hàng có thể tích từ 3 CBM trở lên thì được xem là?",
        "goi_y": [
            "A.Hàng nặng",
            "B.Hàng nguy hiểm",
            "C.Hàng nhẹ",
            "D.Hàng quá khổ"
        ],
        "dap_an_dung": "C"
    },
    {
        "cau_hoi": "THC là viết tắt của khoản phí nào?",
        "goi_y": [
            "A.Terminal Handling Charge",
            "B.Transport Handling Cost",
            "C.Total Harbor Charge",
            "D.Truck Handling Charge"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "PSS là phụ phí gì?",
        "goi_y": [
            "A.Phụ phí nhiên liệu",
            "B.Phụ phí cao điểm mùa vụ",
            "C.Phụ phí chiến tranh",
            "D.Phụ phí lưu container"
        ],
        "dap_an_dung": "B"
    },
    {
        "cau_hoi": "GRI là viết tắt của phụ phí nào?",
        "goi_y": [
            "A.General Rate Increase",
            "B.Global Route Insurance",
            "C.General Railway Index",
            "D.Gross Rate Increase"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "DEM (Demurrage) là khoản phí phát sinh do?",
        "goi_y": [
            "A.Trả container rỗng chậm",
            "B.Container lưu tại cảng quá thời gian miễn phí",
            "C.Không khai hải quan",
            "D.Thiếu chứng từ"
        ],
        "dap_an_dung": "B"
    },
    {
        "cau_hoi": "DET (Detention) là khoản phí phát sinh khi nào?",
        "goi_y": [
            "A.Container lưu trên tàu",
            "B.Trả container rỗng quá thời hạn quy định",
            "C.Tàu đến trễ",
            "D.Chưa lấy D/O"
        ],
        "dap_an_dung": "B"
    },
    {
        "cau_hoi": "Loại bảo hiểm nào có phạm vi bảo hiểm rộng nhất?",
        "goi_y": [
            "A.Điều kiện A",
            "B.Điều kiện B",
            "C.Điều kiện C",
            "D.Tất cả như nhau"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Mất mát do hành vi cố ý của người được bảo hiểm có được bồi thường không?",
        "goi_y": [
            "A.Có",
            "B.Chỉ điều kiện A",
            "C.Không",
            "D.Chỉ điều kiện C"
        ],
        "dap_an_dung": "C"
    }
    ]
elif chuong_da_chon == "Câu hỏi hỗn hợp":
    cac_cau_hoi =[  
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
    },
    {
        "cau_hoi": "Dấu hiệu để nhận biết vận đơn chủ (MBL) là:",
        "goi_y": ["A.Vận đơn do người gom hàng (công ty giao nhận) phát hành", 
                "B.Vận đơn do hãng tàu phát hành, mục shipper ghi tên người gom hàng (công ty giao nhận), mục consignee ghi tên đại lý của người gom hàng ở nước nhập khẩu", 
                "C.Tiêu đề vận đơn ghi: Bill of Lading",
                "D. Mục shipper ghi tên người chủ hàng (người bán), mục consignee ghi tên người nhận hàng (người mua)"],
        "dap_an_dung": "B"
    },
    {
        "cau_hoi": "Hợp đồng mua bán hàng hóa có ghi 'Terms of payment: 20% TT in advance, 80% TT must be paid within 3 days after receiving B/L copy...'. Vậy chứng từ nào KHÔNG cần có ký hậu của chuyển tiền 80% giá trị còn lại của hợp đồng?",
        "goi_y": ["A.Sale contract", 
                "B.B/L (copy)", 
                "C.Invoice",
                "D.DO"],
        "dap_an_dung": "D"
    },
    {
        "cau_hoi": "Hợp đồng mua bán hàng hóa có ghi 'Terms of payment: 20% TT in advance, 80% TT must be paid within 3 days after receiving B/L copy...'. Vậy chứng từ nào KHÔNG cần có ký hậu của chuyển tiền 80% giá trị còn lại của hợp đồng?",
        "goi_y": ["A.Sale contract", 
                "B.B/L (copy)", 
                "C.Invoice",
                "D.DO"],
        "dap_an_dung": "D"
    },
    {
        "cau_hoi": "Giả sử lô hàng 01 container 20'DC nhập khẩu theo điều kiện FOB từ Qingdao (Trung Quốc) đến Hải Phòng (Việt Nam). Chi phí gồm: vận chuyển nội địa đầu xuất 120 USD, local charges đầu xuất 300 USD, thủ tục hải quan đầu xuất 45 USD, cước tàu và phụ phí 220 USD, bảo hiểm 180 USD, local charges đầu nhập 240 USD, thủ tục hải quan đầu nhập 65 USD, vận chuyển từ cảng Hải Phòng về kho khách hàng 150 USD. Nếu bạn là nhân viên sales của công ty Logistics, bạn sẽ báo giá cho khách hàng A (bên nhập khẩu) chi phí làm lô hàng nhập này là bao nhiêu?",
        "goi_y": [
            "A. 1.190 USD",
            "B. 1.310 USD",
            "C. 845 USD",
            "D. 625 USD"
        ],
        "dap_an_dung": "C"
    },
    {
        "cau_hoi": "Công ty X tại Việt Nam nhập hàng từ Trung Quốc bằng đường biển. Người bán chịu trách nhiệm và chi phí cho tới khi hàng được giao trên tàu tại cảng đi ở Trung Quốc, người mua chịu mọi chi phí và rủi ro từ đó về KCN Quang Minh Industrial Zone Hanoi (VN). Điều kiện Incoterms 2020 nào phù hợp?",
        "goi_y": [
            "A. FOB, Qingdao, Incoterms 2020",
            "B. CPT, Quang Minh Industrial Zone Hanoi (VN), Incoterms 2020",
            "C. DAP, Quang Minh Industrial Zone Hanoi (VN), Incoterms 2020",
            "D. CIP, Quang Minh Industrial Zone Hanoi (VN), Incoterms 2020"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Hàng rau quả, trái cây xuất khẩu thường được đóng trong loại container nào?",
        "goi_y": [
            "A. 40' RE",
            "B. 40' OT",
            "C. 40' DC",
            "D. 20' RE"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Trên booking có thông tin: Demurrage and Detention for dry free: 10 calendar days. Phí Demurrage: 30 USD/cont 20'/day. Phí Detention: 30 USD/cont 20'/day. Ngày 01/06 lấy vỏ đóng hàng, hạ cont hàng ở bãi ngày 08/06, ngày 20/06 hàng lên tàu. Cont hàng này phải chịu phụ phí như thế nào?",
        "goi_y": [
            "A. Phí DET 150 USD",
            "B. Phí DEM và DET 300 USD",
            "C. Phí DEM 210 USD",
            "D. Phí DEM và DET 600 USD"
        ],
        "dap_an_dung": "D"
    },
    {
        "cau_hoi": "Tính cước theo lô hàng vận chuyển bằng đường hàng không từ cửa đến cửa. Lô hàng gồm 3 kiện, mỗi kiện nặng 60 kg, kích thước 80 cm × 60 cm × 60 cm. Biết biểu cước: dưới 100 kg cước 3 USD/kg; từ 100 kg tới dưới 250 kg cước 2,5 USD/kg; từ 250 kg tới dưới 500 kg cước 2 USD/kg.",
        "goi_y": [
            "A. Không đáp án nào đúng",
            "B. 486 USD",
            "C. 375 USD",
            "D. 405 USD"
        ],
        "dap_an_dung": "D"
    }
    ]
elif chuong_da_chon == "Đề 1":
    cac_cau_hoi =[  
       {
        "cau_hoi": "Thuật ngữ tàu mẹ (Mother Vessel) nhằm chỉ loại tàu nào?",
        "goi_y": [
            "A.Chạy các tuyến đường dài, lấy hàng từ các cảng chuyển tải hàng hóa",
            "B.Chạy tuyến nội địa",
            "C.Chạy gom hàng trong khu vực để chuyển tải tại các cảng chuyển tải hàng hóa quốc tế",
            "D.Chỉ chạy thẳng từ cảng nhận hàng đến cảng dỡ hàng"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Chức năng KHÔNG PHẢI của vận đơn đường biển (B/L) là gì?",
        "goi_y": [
            "A.Là hóa đơn để đòi và trả tiền",
            "B.Là biên lai của người chuyên chở xác nhận họ đã nhận hàng để chở",
            "C.Là bằng chứng về những điều khoản của một hợp đồng vận tải đường biển",
            "D.Là một chứng từ sở hữu hàng hóa sẽ giao cho ai ở cảng đích"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Vận đơn chuyên chở trực tiếp (Direct B/L) áp dụng trong trường hợp nào?",
        "goi_y": [
            "A.Hàng hóa không chuyển tải",
            "B.Hàng hóa có chuyển tải nhưng trách nhiệm thống nhất",
            "C.Hàng hóa có chuyển tải",
            "D.Vận tải đa phương thức"
        ],
        "dap_an_dung": "A"
    },

    {
        "cau_hoi": "Đặc điểm KHÔNG thuộc phương thức tàu chuyến là gì?",
        "goi_y": [
            "A.Tàu chạy theo một lịch trình do chủ tàu định ra",
            "B.Tàu không chạy theo một lịch trình cố định",
            "C.Người thuê tàu có thể mặc cả về giá cước",
            "D.Giá cước chưa bao gồm chi phí xếp dỡ"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Cước phí được trả trước trong tàu chuyến có nghĩa là được trả khi nào?",
        "goi_y": [
            "A.Sau khi giao hàng lên tàu",
            "B.Khi xếp hàng hóa lên tàu và nhận B/L",
            "C.Dỡ hàng ở cảng đích nhận D/O",
            "D.Sau khi tính số lượng hàng vận chuyển"
        ],
        "dap_an_dung": "B"
    },
    {
        "cau_hoi": "Thuật ngữ tàu Feeder nhằm chỉ loại tàu nào?",
        "goi_y": [
            "A.Chạy gom hàng trong khu vực để chuyển tải tại các cảng chuyển tải hàng hóa quốc tế",
            "B.Chạy tuyến nội địa",
            "C.Chạy các tuyến đường dài, lấy hàng từ các cảng chuyển tải hàng hóa",
            "D.Chỉ chạy thẳng từ cảng nhận hàng đến cảng dỡ hàng"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Thuê tàu chợ là việc gì?",
        "goi_y": [
            "A.Chủ hàng liên hệ với chủ tàu hoặc đại lý để booking chỗ trên tàu",
            "B.Chủ hàng thương lượng và ký hợp đồng thuê tàu",
            "C.Thuê nguyên một tàu chở hàng bách hóa",
            "D.Thuê tàu chạy tuyến nội địa"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "NOR (Notice of Readiness) được trao cho ai?",
        "goi_y": [
            "A.Chủ hàng và cảng",
            "B.Chủ hàng và đại lý của họ",
            "C.Cảng",
            "D.Cảng và môi giới"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Đặc điểm thuộc phương thức tàu chợ là gì?",
        "goi_y": [
            "A.Tàu chạy theo một lịch trình công bố trước",
            "B.Tàu không chạy theo lịch trình cố định",
            "C.Người thuê tàu có thể mặc cả giá cước",
            "D.Giá cước chưa bao gồm chi phí xếp dỡ"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Chứng từ vận tải là chứng từ nào?",
        "goi_y": [
            "A.Bill of Lading",
            "B.Certificate of Origin",
            "C.Bill of Exchange",
            "D.Letter of Credit"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Nguyên tắc phạt xếp dỡ chậm trong thuê tàu chuyến là gì?",
        "goi_y": [
            "A.Khi đã bị phạt thì luôn bị phạt",
            "B.Thời gian xếp dỡ hết thì các ngày sau không bị phạt",
            "C.Chỉ phạt trong ngày quy định",
            "D.Khi đã bị phạt thì thường bị phạt"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Vận đơn hoàn hảo (Clean B/L) là vận đơn như thế nào?",
        "goi_y": [
            "A.Không có nhận xét xấu về tình trạng bao bì hoặc hàng hóa",
            "B.Có nhận xét xấu về hàng hóa",
            "C.Không có bản copy",
            "D.Được lập thành 5 bản chính"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Đâu KHÔNG phải là trách nhiệm của người chuyên chở bằng đường biển?",
        "goi_y": [
            "A.Niêm phong, kẹp chì hàng hóa",
            "B.Cung cấp tàu có khả năng đi biển",
            "C.Chất xếp, chăm sóc và dỡ hàng",
            "D.Cấp vận đơn đường biển"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Ai là người cấp Lệnh giao hàng (D/O)?",
        "goi_y": [
            "A.Người chuyên chở",
            "B.Cảng dỡ hàng",
            "C.Người bán",
            "D.Người mua"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Chọn câu SAI về vận đơn đường biển.",
        "goi_y": [
            "A.B/L là hợp đồng vận tải",
            "B.B/L là bằng chứng của hợp đồng vận tải",
            "C.B/L là chứng từ sở hữu hàng hóa",
            "D.B/L là biên lai nhận hàng"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Trong thuê tàu chợ, chứng từ điều chỉnh quan hệ giữa các bên là gì?",
        "goi_y": [
            "A.B/L",
            "B.L/C",
            "C.Hợp đồng chuyên chở hàng hải",
            "D.Hóa đơn cước"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Tàu chợ là tàu như thế nào?",
        "goi_y": [
            "A.Chuyên chở hàng bách hóa trong container",
            "B.Có thưởng phạt xếp dỡ",
            "C.Cước phí do thỏa thuận",
            "D.Chạy tuyến không cố định"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Cước phí trong thuê tàu chuyến bao gồm?",
        "goi_y": [
            "A.Chi phí chở hàng và có thể có chi phí xếp dỡ, sắp đặt hàng",
            "B.Chỉ chi phí chở hàng",
            "C.Chi phí chở hàng và xếp dỡ",
            "D.Chi phí chở hàng và sắp đặt hàng"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Phê chú nào làm mất tính hoàn hảo của vận đơn?",
        "goi_y": [
            "A.Bao bì bị rách",
            "B.Bao bì dùng lại",
            "C.Không biết chất lượng bên trong",
            "D.Bao bì dùng lại và không biết chất lượng bên trong"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Theo Công ước Hamburg, nếu tổn thất rõ rệt thì thông báo tổn thất phải lập khi nào?",
        "goi_y": [
            "A.Không muộn hơn ngày làm việc sau ngày giao hàng",
            "B.Trước hoặc vào lúc giao hàng",
            "C.Sau khi đưa hàng về kho",
            "D.Không muộn hơn hai ngày làm việc"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Vận tải là hoạt động gì?",
        "goi_y": [
            "A.Độc lập",
            "B.Sản xuất vật chất",
            "C.Kinh tế đặc thù",
            "D.Cả ba ý trên"
        ],
        "dap_an_dung": "D"
    },
    {
        "cau_hoi": "Đặc điểm của sản phẩm vận tải là gì?",
        "goi_y": [
            "A.Giống các sản phẩm khác",
            "B.Có thể dự trữ",
            "C.Quá trình tiêu dùng gắn với quá trình sản xuất",
            "D.Không có ý nào đúng"
        ],
        "dap_an_dung": "C"
    },
    {
        "cau_hoi": "Hình thức vận chuyển mà người chuyên chở chịu trách nhiệm trên toàn bộ hành trình là gì?",
        "goi_y": [
            "A.Nhiều chặng",
            "B.Chở suốt",
            "C.Đứt đoạn",
            "D.Không có đáp án đúng"
        ],
        "dap_an_dung": "B"
    },
    {
        "cau_hoi": "Vận tải có tác động đến những lĩnh vực nào?",
        "goi_y": [
            "A.Hoạt động kinh doanh",
            "B.Cán cân thanh toán",
            "C.Cơ cấu hàng hóa và thị trường",
            "D.Cả ba ý trên"
        ],
        "dap_an_dung": "D"
    },
    {
        "cau_hoi": "Điều kiện Incoterms mà người bán có khả năng vận tải và thông quan nhập khẩu là gì?",
        "goi_y": [
            "A.CPT",
            "B.FCA",
            "C.DDU",
            "D.DDP"
        ],
        "dap_an_dung": "D"
    },
    {
        "cau_hoi": "Không nên dành quyền vận tải khi nào?",
        "goi_y": [
            "A.Thị trường cạnh tranh khốc liệt",
            "B.Chênh lệch giá CIF và FOB cao",
            "C.Có khả năng thông quan XNK",
            "D.Muốn chủ động giao nhận"
        ],
        "dap_an_dung": "B"
    },
    {
        "cau_hoi": "Chức năng của cảng biển là gì?",
        "goi_y": [
            "A.Neo đậu tàu",
            "B.Phục vụ hàng hóa và tàu",
            "C.Cả hai không đúng",
            "D.Cả A và B đúng"
        ],
        "dap_an_dung": "D"
    },
    {
        "cau_hoi": "DWCC dùng để chỉ gì?",
        "goi_y": [
            "A.Trọng lượng tịnh hàng hóa",
            "B.Trọng lượng cả bì",
            "C.Trọng lượng tính trên đơn vị thể tích",
            "D.Cả ba đáp án đều sai"
        ],
        "dap_an_dung": "D"
    },
    {
        "cau_hoi": "Dung tích đăng ký tịnh là gì?",
        "goi_y": [
            "A.Toàn bộ các khoảng trống trên tàu",
            "B.Các khoảng trống khép kín trên tàu",
            "C.Các khoảng trống và phòng thủy thủ",
            "D.Các khoảng trống và phòng giải trí"
        ],
        "dap_an_dung": "B"
    },
    {
        "cau_hoi": "Trọng tải tịnh của tàu là gì?",
        "goi_y": [
            "A.Trọng lượng hàng hóa trên tàu",
            "B.Trọng lượng vật phẩm tiêu dùng",
            "C.Hành lý thủy thủ",
            "D.Cả ba đáp án trên"
        ],
        "dap_an_dung": "A"
    }
    ]
elif chuong_da_chon == "Đề 2":
    cac_cau_hoi =[  
        {
        "cau_hoi": "Xuyemax là gì?",
        "goi_y": [
            "A.Tàu của Xuye",
            "B.Tàu được tự do đi qua Xuye",
            "C.Tàu lớn nhất có thể đi qua Xuye",
            "D.Không có đáp án nào đúng"
        ],
        "dap_an_dung": "C"
    },
    {
        "cau_hoi": "Tàu trẻ là tàu có tuổi bao nhiêu?",
        "goi_y": [
            "A.8 - 10 năm",
            "B.10 - 12 năm",
            "C.12 - 14 năm",
            "D.14 - 18 năm"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Đặc điểm của tàu chợ là gì?",
        "goi_y": [
            "A.Chuyên chở container",
            "B.Không thưởng phạt xếp dỡ",
            "C.Cước phí do thỏa thuận",
            "D.Chạy tuyến không cố định"
        ],
        "dap_an_dung": "B"
    },
    {
        "cau_hoi": "Khi thuê tàu chợ, giấy lưu cước tàu chợ thường do ai cấp?",
        "goi_y": [
            "A.Chủ tàu",
            "B.Chủ hàng",
            "C.Môi giới",
            "D.Không có đáp án đúng"
        ],
        "dap_an_dung": "C"
    },
    {
        "cau_hoi": "Vận đơn đường biển KHÔNG phải là gì?",
        "goi_y": [
            "A.Xác nhận quyền sở hữu hàng hóa",
            "B.Xác nhận việc nhận hàng lên tàu",
            "C.Xác nhận một hợp đồng bảo hiểm",
            "D.Xác nhận một hợp đồng chuyên chở"
        ],
        "dap_an_dung": "C"
    },
    {
        "cau_hoi": "Việt Nam đã tham gia công ước nào sau đây?",
        "goi_y": [
            "A.Quy tắc Hague",
            "B.Công ước Hamburg",
            "C.Nghị định thư SDR",
            "D.Không có đáp án đúng"
        ],
        "dap_an_dung": "D"
    },
    {
        "cau_hoi": "Theo luật Anh, thời hạn được coi là tổn thất toàn bộ khi nào?",
        "goi_y": [
            "A.Tàu không về cảng chỉ định sau 3 tháng",
            "B.Tàu không về cảng chỉ định sau 60 ngày",
            "C.Tàu gặp bão về muộn 45 ngày",
            "D.Tàu rời cảng đi 90 ngày chưa đến cảng đích"
        ],
        "dap_an_dung": "B"
    },
    {
        "cau_hoi": "Việc chuyên chở hàng súc vật sống được quy định trong văn bản nào?",
        "goi_y": [
            "A.Quy tắc Hague",
            "B.Công ước Hamburg",
            "C.Luật thương mại quốc tế",
            "D.Hiệp định WTO"
        ],
        "dap_an_dung": "B"
    },
    {
        "cau_hoi": "Giới hạn trách nhiệm là gì?",
        "goi_y": [
            "A.Số tiền tối đa mà chủ tàu phải bồi thường",
            "B.Số tiền người bảo hiểm phải trả",
            "C.Số tiền tối đa được bồi thường",
            "D.Không có đáp án đúng"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Theo Luật Hàng hải Việt Nam, tàu chậm giao được tính trong bao nhiêu ngày?",
        "goi_y": [
            "A.1 ngày",
            "B.3 ngày",
            "C.15 ngày",
            "D.60 ngày"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Để tránh phí xếp hàng lên tàu hai lần, người bán theo điều kiện CIF nên thuê tàu theo điều kiện nào?",
        "goi_y": [
            "A.FO",
            "B.FI",
            "C.FIS",
            "D.FIOT"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Thuê ướt là hình thức thuê nào?",
        "goi_y": [
            "A.Thuê tàu không có thủy thủ",
            "B.Thuê cả tàu và thủy thủ",
            "C.Thuê tàu, thủy thủ và thực phẩm",
            "D.Thuê từng chuyến"
        ],
        "dap_an_dung": "B"
    },
    {
        "cau_hoi": "Đặc trưng nổi bật nhất của container là gì?",
        "goi_y": [
            "A.Thích ứng vận chuyển và xếp dỡ",
            "B.Phù hợp nhiều loại phương tiện",
            "C.Hình dáng thích hợp",
            "D.Thể tích trên 1 m3"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Tàu chạy đến các điểm Hub và hàng được chuyển tiếp là loại tàu nào?",
        "goi_y": [
            "A.Tàu chợ",
            "B.Tàu chuyến",
            "C.Feeder",
            "D.Tàu chạy thẳng"
        ],
        "dap_an_dung": "C"
    },
    {
        "cau_hoi": "Loại hàng nào không thích hợp vận chuyển bằng container?",
        "goi_y": [
            "A.Hàng hải sản đông lạnh",
            "B.Hàng khối lượng lớn",
            "C.Hàng siêu trường siêu trọng",
            "D.Hàng lỏng"
        ],
        "dap_an_dung": "C"
    },
    {
        "cau_hoi": "Bảo hiểm là hình thức gì?",
        "goi_y": [
            "A.Tránh rủi ro",
            "B.Khắc phục rủi ro",
            "C.Phân tán rủi ro vào số đông",
            "D.Hạn chế rủi ro"
        ],
        "dap_an_dung": "C"
    },
    {
        "cau_hoi": "Tác dụng chính của bảo hiểm là gì?",
        "goi_y": [
            "A.Tập trung vốn",
            "B.Tăng thu ngoại tệ",
            "C.Bồi thường",
            "D.Tăng tích lũy ngân sách"
        ],
        "dap_an_dung": "C"
    },
    {
        "cau_hoi": "Rủi ro do thời tiết xấu gây ra được bảo hiểm trong điều kiện bảo hiểm nào?",
        "goi_y": [
            "A.Điều kiện A",
            "B.Cảng dỡ hàng",
            "C.Người bán",
            "D.Người mua"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Chọn câu SAI về vận đơn đường biển (B/L).",
        "goi_y": [
            "A.B/L là hợp đồng vận tải",
            "B.B/L là bằng chứng của hợp đồng vận tải",
            "C.B/L là chứng từ sở hữu hàng hóa",
            "D.B/L là biên lai nhận hàng để chở của người chuyên chở"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Chứng từ điều chỉnh mối quan hệ giữa bên thuê và bên cho thuê trong phương thức thuê tàu chợ là gì?",
        "goi_y": [
            "A.B/L",
            "B.L/C",
            "C.Hợp đồng chuyên chở hàng hải",
            "D.Hóa đơn tính cước vận tải"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Tàu chợ là tàu như thế nào?",
        "goi_y": [
            "A.Chuyên chở hàng bách hóa trong container",
            "B.Có thưởng phạt xếp dỡ",
            "C.Cước phí do thỏa thuận",
            "D.Chạy tuyến không cố định"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Cước phí trong thuê tàu chuyến bao gồm những khoản nào?",
        "goi_y": [
            "A.Chi phí chở hàng và có thể có chi phí xếp dỡ, sắp đặt hàng hóa",
            "B.Chỉ có chi phí chở hàng",
            "C.Chi phí chở hàng và có thể có chi phí xếp dỡ",
            "D.Chi phí chở hàng và có thể có chi phí sắp đặt hàng hóa"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Phê chú (Remarks) nào của thuyền trưởng làm mất tính hoàn hảo của vận đơn?",
        "goi_y": [
            "A.Bao bì bị rách",
            "B.Bao bì dùng lại",
            "C.Không biết chất lượng, số lượng bên trong hàng hóa",
            "D.Bao bì dùng lại và không biết chất lượng bên trong"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Theo Công ước Hamburg, nếu tổn thất của hàng là rõ rệt thì thông báo tổn thất phải được lập khi nào?",
        "goi_y": [
            "A.Không muộn hơn ngày làm việc sau ngày giao hàng",
            "B.Trước hoặc vào lúc giao hàng",
            "C.Sau khi người nhận hàng đưa hàng về kho",
            "D.Không muộn hơn hai ngày làm việc sau ngày giao hàng"
        ],
        "dap_an_dung": "B"
    },
    {
        "cau_hoi": "B/L nhận để xếp (Received for Shipment B/L) có ý nghĩa gì?",
        "goi_y": [
            "A.Người vận chuyển đã nhận hàng",
            "B.Hàng hóa đã được xếp lên tàu",
            "C.Người bán đã hết trách nhiệm",
            "D.Hàng hóa chưa thực sự được xếp lên tàu, trách nhiệm của người bán vẫn còn"
        ],
        "dap_an_dung": "D"
    },
    {
        "cau_hoi": "Có thể chuyển vận đơn theo lệnh thành vận đơn đích danh bằng cách nào?",
        "goi_y": [
            "A.Không thể được",
            "B.Ký hậu theo lệnh",
            "C.Ký hậu để trống",
            "D.Ký hậu theo lệnh trở thành vận đơn đích danh"
        ],
        "dap_an_dung": "D"
    },
    {
        "cau_hoi": "Khi ký hậu vào vận đơn đường biển (B/L), phải ký hậu bằng ngôn ngữ của ai?",
        "goi_y": [
            "A.Ngôn ngữ của vận đơn",
            "B.Ngôn ngữ của người ký hậu",
            "C.Ngôn ngữ của người được ký hậu",
            "D.Ngôn ngữ của quốc gia nơi ký vận đơn"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Theo quy định về thời gian làm hàng, WWDSHEX có nghĩa là gì?",
        "goi_y": [
            "A.Ngày làm việc thời tiết tốt, Chủ nhật và ngày lễ không tính",
            "B.Ngày làm việc thời tiết tốt, Chủ nhật và ngày lễ có tính",
            "C.Ngày làm việc thời tiết tốt, Chủ nhật và ngày lễ không tính trừ khi có làm",
            "D.Ngày làm việc thời tiết tốt, Chủ nhật và ngày lễ không tính dù có làm hay không"
        ],
        "dap_an_dung": "A"
    }
    ]
elif chuong_da_chon == "Đề 3":
    cac_cau_hoi =[  
        {
        "cau_hoi": "Vận đơn đường biển không phải là gì?",
        "goi_y": [
            "A.Xác nhận một hợp đồng bảo hiểm",
            "B.Xác nhận quyền sở hữu hàng hóa",
            "C.Xác nhận một hợp đồng chuyên chở",
            "D.Xác nhận hàng đã được xếp lên tàu"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Đặc điểm của phương thức thuê tàu chợ là gì?",
        "goi_y": [
            "A.Chuyên chở hàng hóa có số lượng tùy ý, cảng xếp dỡ nằm trong lịch trình của tàu",
            "B.Chuyên chở hàng hóa có số lượng cố định, cảng xếp dỡ nằm trong lịch trình của tàu",
            "C.Cảng xếp dỡ không cố định trong lịch trình của tàu",
            "D.Chuyên chở hàng hóa cố định, cảng xếp dỡ tùy chủ hàng quyết định"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Cảng ICD là gì?",
        "goi_y": [
            "A.Là một địa điểm thông quan hàng hóa nằm trong nội địa",
            "B.Là cảng container nằm trong nội địa",
            "C.Là nơi trung chuyển hàng hóa xuất nhập khẩu nằm trong nội địa",
            "D.Là cảng cạn nơi có các dịch vụ Logistics giúp giải phóng hàng nhanh nằm trong nội địa"
        ],
        "dap_an_dung": "D"
    },
    {
        "cau_hoi": "Ưu điểm nổi bật của vận tải biển là gì?",
        "goi_y": [
            "A.Giá thành và chi phí thấp",
            "B.Thời gian vận chuyển nhanh",
            "C.Đảm bảo sự an toàn cho hàng hóa",
            "D.Chở được hàng hóa siêu trường siêu trọng"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Một bộ B/L thường gồm bao nhiêu bản?",
        "goi_y": [
            "A.Phát hành 03 bản gốc và nhiều bản sao",
            "B.Chỉ phát hành một bản gốc và một bản sao",
            "C.Phát hành theo quy định của Công ước Hamburg",
            "D.Phát hành tùy theo yêu cầu của người mua"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Estimated Time Arrival được viết tắt là gì?",
        "goi_y": [
            "A.ETA",
            "B.ETD",
            "C.ETB",
            "D.ETC"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Theo điều kiện FOB (Incoterms 2010), người bán có trách nhiệm gì?",
        "goi_y": [
            "A.Chịu mọi chi phí và rủi ro cho đến khi hàng được giao trên tàu tại cảng xuất khẩu",
            "B.Chịu mọi rủi ro cho đến khi hàng được giao trên tàu tại cảng xuất khẩu",
            "C.Chịu mọi chi phí và rủi ro cho đến khi hàng được giao qua lan can tàu",
            "D.Chịu trách nhiệm thuê tàu"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Theo phương thức thanh toán L/C, yêu cầu xuất trình về vận đơn là gì?",
        "goi_y": [
            "A.Trọn bộ (Full Set) B/L",
            "B.Vận đơn hoàn hảo",
            "C.Vận đơn ký hậu",
            "D.Vận đơn đích danh"
        ],
        "dap_an_dung": "B"
    },
    {
        "cau_hoi": "Booking Confirmation được phát hành bởi ai?",
        "goi_y": [
            "A.Người chuyên chở",
            "B.Công ty giao nhận",
            "C.Người gửi hàng",
            "D.A hoặc B"
        ],
        "dap_an_dung": "D"
    },
    {
        "cau_hoi": "GPS là viết tắt của cụm từ nào?",
        "goi_y": [
            "A.Global Positioning Systems",
            "B.Greenwich Placement Systems",
            "C.German Placement Systems",
            "D.Global Placement Systems"
        ],
        "dap_an_dung": "A"
    },

    {
        "cau_hoi": "Mô tả nào đúng nhất về dịch vụ Feeder Service?",
        "goi_y": [
            "A.Là vận tải đường thủy nội địa",
            "B.Cung cấp hàng hóa cho các tàu mẹ (Mother Vessels)",
            "C.Giúp tàu biển giảm thời gian sử dụng tại cảng",
            "D.Là hành trình giữa cảng biển chính và cảng sông"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Loại chi phí nào không thuộc cơ cấu giá cước vận tải biển?",
        "goi_y": [
            "A.Chi phí đóng gói tại cơ sở người bán",
            "B.Cước vận tải chính và phụ",
            "C.Chi phí xếp dỡ container",
            "D.Chi phí lưu kho bãi và phụ phí"
        ],
        "dap_an_dung": "A"
    },

    {
        "cau_hoi": "Ký hiệu DWT (Deadweight Tonnage) có nghĩa là gì?",
        "goi_y": [
            "A.Trọng tải của tàu biển",
            "B.Trọng lượng thân tàu",
            "C.Dung tích chứa hàng",
            "D.Mớn nước tàu"
        ],
        "dap_an_dung": "A"
    },

    {
        "cau_hoi": "Trên vận đơn theo lệnh, mục Consignee ghi như thế nào?",
        "goi_y": [
            "A.To order of...",
            "B.Tên người nhận hàng",
            "C.Tên Notify Party",
            "D.Tên người gửi hàng"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Nếu thanh toán bằng L/C (ABC Bank), mục Consignee trên B/L sẽ ghi thế nào?",
        "goi_y": [
            "A.To order of ABC Bank",
            "B.Tên người nhập khẩu",
            "C.Tên người mở L/C",
            "D.To order of shipper"
        ],
        "dap_an_dung": "A"
    },
     {
        "cau_hoi": "Nếu trên vận tải đơn, ở mục Consignee ghi là 'TO ORDER' thì để nhận hàng tại cảng đích cần có điều kiện gì?",
        "goi_y": [
            "A.Người nhận hàng cần xuất trình bản original có ký hậu của người gửi hàng (Shipper)",
            "B.Người nhận hàng chỉ cần xuất trình 1 bản copy của vận đơn",
            "C.Người nhận hàng cần xuất trình 1 bản original",
            "D.Ngân hàng của người gửi hàng ký hậu vận đơn"
        ],
        "dap_an_dung": "D"
    },

    {
        "cau_hoi": "Nếu trên hợp đồng ngoại thương có điều kiện Incoterms là FAS hoặc FOB thì trên vận tải đơn, cước tàu sẽ được thể hiện như thế nào?",
        "goi_y": [
            "A.Freight Collect",
            "B.Freight Prepaid",
            "C.Trả trước khi khai hải quan xuất khẩu",
            "D.Trả sau khi phát hành Bill of Lading"
        ],
        "dap_an_dung": "A"
    },

    {
        "cau_hoi": "Nếu trên hợp đồng ngoại thương có điều kiện Incoterms là CFR hoặc CIF thì trên vận tải đơn, cước tàu sẽ được thể hiện như thế nào?",
        "goi_y": [
            "A.Freight Prepaid",
            "B.Freight Collect",
            "C.Trả sau khi khai hải quan nhập khẩu",
            "D.Trả sau khi phát hành Bill of Lading"
        ],
        "dap_an_dung": "A"
    },

    {
        "cau_hoi": "Vận đơn đã xuất trình (Surrendered Bill of Lading) có ý nghĩa gì?",
        "goi_y": [
            "A.Người gửi hàng đã xuất trình cho hãng tàu ở đầu khởi hành thay cho người nhận hàng để nhận hàng tại đích đến",
            "B.Người gửi hàng xuất trình cho hãng tàu tại cảng chuyển tải",
            "C.Người nhận hàng đã xuất trình ở cảng xếp hàng",
            "D.Người nhận hàng đã xuất trình tại cảng dỡ trước khi tàu đến"
        ],
        "dap_an_dung": "A"
    },

    {
        "cau_hoi": "Điện giao hàng (Telex Release) đối với Surrendered Bill of Lading có ý nghĩa gì?",
        "goi_y": [
            "A.Là chỉ thị giao hàng do hãng tàu đầu khởi hành gửi cho đại lý hãng tàu ở cảng đích",
            "B.Là chỉ thị giao hàng do người gửi hàng gửi cho người nhận hàng",
            "C.Là chỉ thị của hãng tàu cảng đích gửi cho hãng tàu đầu khởi hành",
            "D.Là chỉ thị của hãng tàu gửi cho hải quan cảng dỡ"
        ],
        "dap_an_dung": "A"
    },

    {
        "cau_hoi": "Kích thước của container kín 40 feet cao (40HC/40HQ) là bao nhiêu?",
        "goi_y": [
            "A.40' × 8' × 9'6\"",
            "B.40' × 8' × 8'6\"",
            "C.40' × 8' × 8'",
            "D.45' × 8' × 9'6\""
        ],
        "dap_an_dung": "A"
    },

    {
        "cau_hoi": "Phí THC (Terminal Handling Charge) trong vận tải biển bằng container là gì?",
        "goi_y": [
            "A.Phí xếp dỡ hàng do hãng tàu thu người gửi và người nhận hàng",
            "B.Phí nhiên liệu chạy tàu",
            "C.Phí an ninh cảng",
            "D.Phí dịch vụ hàng xuất khẩu"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Phí Demurrage phát sinh khi nào?",
        "goi_y": [
            "A.Chủ hàng để container có hàng tại bãi cảng quá thời gian miễn phí",
            "B.Chủ hàng giữ container tại kho riêng quá thời gian miễn phí",
            "C.Chủ hàng để hàng tại kho CFS quá thời gian",
            "D.Chủ hàng để hàng trong kho ngoại quan quá thời gian"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Phí Detention phát sinh khi nào?",
        "goi_y": [
            "A.Chủ hàng giữ vỏ container của hãng tàu tại kho riêng quá thời hạn cho phép",
            "B.Chủ hàng để container tại bãi cảng quá thời hạn",
            "C.Chủ hàng để hàng tại kho CFS quá thời hạn",
            "D.Chủ hàng để hàng trong kho ngoại quan quá thời hạn"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Trong phương thức FCL, ai chịu trách nhiệm đóng hàng và bấm seal hãng tàu vào container tại đầu cảng xếp?",
        "goi_y": [
            "A.Người gửi hàng",
            "B.Hãng tàu",
            "C.Cơ quan hải quan",
            "D.Người nhận hàng"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Trong phương thức LCL, ai chịu trách nhiệm đóng hàng vào container và bấm seal tại kho CFS?",
        "goi_y": [
            "A.Người gom hàng lẻ (Consolidator)",
            "B.Người gửi hàng",
            "C.Hãng tàu",
            "D.Người nhận hàng"
        ],
        "dap_an_dung": "A"
    },

    {
        "cau_hoi": "Nơi tiến hành giao nhận container rỗng và container có hàng tại cảng là gì?",
        "goi_y": [
            "A.Container Yard (CY)",
            "B.Kho ngoại quan",
            "C.Container Freight Station (CFS)",
            "D.Cầu tàu"
        ],
        "dap_an_dung": "A"
    },

    {
        "cau_hoi": "Trong phương thức gửi hàng LCL, hàng hóa thường được giao nhận tại đâu?",
        "goi_y": [
            "A.Kho CFS (Container Freight Station)",
            "B.Bãi CY (Container Yard)",
            "C.Cầu tàu",
            "D.Kho riêng của chủ hàng"
        ],
        "dap_an_dung": "A"
    },

    {
        "cau_hoi": "Kênh đào Panama giúp rút ngắn hành trình vận tải giữa hai đại dương nào?",
        "goi_y": [
            "A.Thái Bình Dương và Đại Tây Dương",
            "B.Đại Tây Dương và Ấn Độ Dương",
            "C.Thái Bình Dương và Ấn Độ Dương",
            "D.Bắc Băng Dương và Thái Bình Dương"
        ],
        "dap_an_dung": "A"
    }
    ]
elif chuong_da_chon == "Chương 8.1: Thanh toán quốc tế":
    cac_cau_hoi =[  
         {
        "cau_hoi": "Thị trường ngoại hối kỳ hạn là gì?",
        "goi_y": [
            "A.Thị trường phái sinh, trao đổi ngoại tệ trong tương lai",
            "B.Thị trường có hợp đồng chống rủi ro tỷ giá ngoại tệ",
            "C.Thị trường ký hợp đồng tỷ giá xác định ngay nhưng chuyển giao ngoại tệ sau một kỳ hạn",
            "D.Thị trường ký hợp đồng xác định hai tỷ giá cho hai thời điểm hiện tại và kỳ hạn xác định trong hợp đồng"
        ],
        "dap_an_dung": "C"
    },

    {
        "cau_hoi": "Căn cứ chức năng hoạt động, người ta chia các thành viên thị trường ngoại hối thành những nhóm nào?",
        "goi_y": [
            "A.Các ngân hàng và các doanh nghiệp",
            "B.Các nhà kinh doanh, môi giới, ngân hàng thương mại, ngân hàng trung ương",
            "C.Các nhà kinh doanh tiền tệ, môi giới, đầu cơ, các nhà kinh doanh acbit",
            "D.Các nhà kinh doanh, các ngân hàng thương mại, ngân hàng trung ương và môi giới"
        ],
        "dap_an_dung": "C"
    },

    {
        "cau_hoi": "Căn cứ hình thức tổ chức, người ta chia thị trường ngoại hối thành những thị trường nào?",
        "goi_y": [
            "A.Thị trường tiền mặt và thị trường chuyển khoản",
            "B.Thị trường hoán đổi và thị trường quyền chọn",
            "C.Thị trường có tổ chức và thị trường không tổ chức",
            "D.Thị trường giao ngay và thị trường giao sau"
        ],
        "dap_an_dung": "C"
    },

    {
        "cau_hoi": "Căn cứ nghiệp vụ kinh doanh, người ta chia thị trường ngoại hối thành các thị trường nào?",
        "goi_y": [
            "A.Có tổ chức và không tổ chức",
            "B.Tiền mặt, giao ngay, cơ bản, phái sinh",
            "C.Tiền mặt, giao ngay, kỳ hạn, giao sau, hoán đổi, quyền chọn",
            "D.Giao ngay, giao sau, hoán đổi, quyền chọn, cơ bản, phái sinh"
        ],
        "dap_an_dung": "C"
    },

    {
        "cau_hoi": "Ngoại hối là gì?",
        "goi_y": [
            "A.Là ngoại tệ (tiền nước ngoài)",
            "B.Là ngoại tệ và nội tệ có thể thanh toán chuyển đổi với nhau",
            "C.Là ngoại tệ mạnh và vàng",
            "D.Là ngoại tệ, vàng và các công cụ thanh toán bằng ngoại tệ"
        ],
        "dap_an_dung": "D"
    },

    {
        "cau_hoi": "Thị trường nào được coi là trung tâm của thị trường ngoại hối?",
        "goi_y": [
            "A.Thị trường chứng khoán, nơi mua bán chứng khoán bằng ngoại tệ",
            "B.Thị trường tiền tệ London (Anh)",
            "C.Nơi giao dịch giữa các ngân hàng thương mại và các công ty xuất nhập khẩu có ngoại tệ",
            "D.Thị trường ngoại tệ liên ngân hàng"
        ],
        "dap_an_dung": "D"
    },

    {
        "cau_hoi": "Tính chất nào của thị trường ngoại hối thể hiện phạm vi và tầm cỡ của nó?",
        "goi_y": [
            "A.Tính chất không nhất thiết phải tập trung",
            "B.Tính chất hoạt động rộng lớn của các ngân hàng thương mại",
            "C.Tính chất quốc tế và hoạt động liên tục 24/24",
            "D.Tính chất và bản chất chức năng của các đồng tiền"
        ],
        "dap_an_dung": "C"
    },

    {
        "cau_hoi": "Chức năng nào của thị trường ngoại hối đem lại lợi ích trực tiếp cho các doanh nghiệp?",
        "goi_y": [
            "A.Phục vụ luân chuyển các khoản đầu tư quốc tế",
            "B.Đáp ứng việc mua bán ngoại tệ phục vụ thanh toán quốc tế",
            "C.Cung cấp công cụ bảo hiểm rủi ro tỷ giá cho các khoản thu chi ngoại tệ do xuất nhập khẩu",
            "D.Xác định giá trị đồng tiền trong nước"
        ],
        "dap_an_dung": "C"
    },

    {
        "cau_hoi": "Các doanh nghiệp tham gia thị trường kỳ hạn nhằm mục đích gì?",
        "goi_y": [
            "A.Kiếm lợi nhuận từ chênh lệch tỷ giá",
            "B.Thực hiện chính sách tiền tệ quốc gia",
            "C.Bảo hiểm rủi ro tỷ giá và hạn chế ảnh hưởng của biến động tỷ giá",
            "D.Mua bán ngoại tệ phục vụ thanh toán xuất nhập khẩu"
        ],
        "dap_an_dung": "C"
    },
    {
    "cau_hoi": "Qua các mặt biểu hiện nào thì biết được sức mua của tiền tệ biến động?",
    "goi_y": [
        "A.Lãi suất cho vay tăng lên hay giảm xuống",
        "B.Giá vàng",
        "C.Giá ngoại hối",
        "D.Tất cả đáp án trên"
    ],
    "dap_an_dung": "D"
},
{
    "cau_hoi": "Những loại nào được coi là ngoại hối ở nước ta?",
    "goi_y": [
        "A.Séc do ngân hàng Việt Nam phát hành bằng ngoại tệ",
        "B.Hối phiếu ghi bằng USD",
        "C.Công trái quốc gia ghi bằng VND",
        "D.Tất cả các đáp án trên"
    ],
    "dap_an_dung": "D"
},
 {
        "cau_hoi": "Ngoại hối bao gồm những gì?",
        "goi_y": [
            "A.Chỉ ngoại tệ",
            "B.Ngoại tệ và vàng",
            "C.Ngoại tệ, vàng tiêu chuẩn quốc tế, giấy tờ có giá và các công cụ thanh toán bằng ngoại tệ",
            "D.Chỉ vàng tiêu chuẩn quốc tế"
        ],
        "dap_an_dung": "C"
    },

    {
        "cau_hoi": "Theo nghĩa hẹp, thị trường ngoại hối là gì?",
        "goi_y": [
            "A.Thị trường mua bán chứng khoán",
            "B.Thị trường giao dịch vàng",
            "C.Thị trường thực hiện các giao dịch mua bán, trao đổi ngoại tệ",
            "D.Thị trường vốn"
        ],
        "dap_an_dung": "C"
    },

    {
        "cau_hoi": "Sự ra đời và phát triển của thị trường ngoại hối gắn liền với sự phát triển của lĩnh vực nào?",
        "goi_y": [
            "A.Công nghiệp",
            "B.Ngoại thương",
            "C.Nông nghiệp",
            "D.Ngân sách Nhà nước"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Theo hình thức tổ chức, thị trường ngoại hối được chia thành những loại nào?",
        "goi_y": [
            "A.Thị trường giao ngay và kỳ hạn",
            "B.Thị trường có tổ chức và không có tổ chức",
            "C.Thị trường tương lai và quyền chọn",
            "D.Thị trường hoán đổi và giao ngay"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Theo nghiệp vụ kinh doanh, thị trường ngoại hối KHÔNG bao gồm thị trường nào?",
        "goi_y": [
            "A.Spot Market",
            "B.Forward Market",
            "C.Futures Market",
            "D.Money Market"
        ],
        "dap_an_dung": "D"
    },

    {
        "cau_hoi": "Thị trường giao ngay (Spot Market) là gì?",
        "goi_y": [
            "A.Thanh toán sau nhiều tháng",
            "B.Giao dịch mua bán ngoại tệ theo tỷ giá hiện tại và thanh toán trong vòng hai ngày làm việc",
            "C.Thanh toán sau một năm",
            "D.Chỉ dùng để đầu cơ"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Thời gian thanh toán của giao dịch Spot thường là:",
        "goi_y": [
            "A.Ngay lập tức",
            "B.Sau một ngày",
            "C.Trong vòng hai ngày làm việc kể từ ngày giao dịch",
            "D.Sau ba mươi ngày"
        ],
        "dap_an_dung": "C"
    },

    {
        "cau_hoi": "Nhược điểm lớn nhất của thị trường giao ngay là gì?",
        "goi_y": [
            "A.Chi phí cao",
            "B.Không đáp ứng nhu cầu mua bán ngoại tệ trong tương lai",
            "C.Không có tỷ giá",
            "D.Không có ngân hàng tham gia"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Giao dịch kỳ hạn (Forward) là giao dịch như thế nào?",
        "goi_y": [
            "A.Thanh toán ngay",
            "B.Cam kết mua bán ngoại tệ theo tỷ giá xác định trước và thanh toán trong tương lai",
            "C.Chỉ mua vàng",
            "D.Chỉ dành cho ngân hàng"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Mục đích quan trọng nhất của hợp đồng Forward là gì?",
        "goi_y": [
            "A.Đầu cơ giá vàng",
            "B.Phòng ngừa rủi ro hối đoái",
            "C.Đầu tư chứng khoán",
            "D.Huy động vốn"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Thị trường Futures khác thị trường Forward ở điểm nào?",
        "goi_y": [
            "A.Futures được chuẩn hóa và giao dịch trên sở giao dịch",
            "B.Futures thanh toán ngay",
            "C.Futures không có hợp đồng",
            "D.Futures chỉ giao dịch vàng"
        ],
        "dap_an_dung": "A"
    },

    {
        "cau_hoi": "Hợp đồng Futures được thực hiện trên thị trường nào?",
        "goi_y": [
            "A.Thị trường OTC",
            "B.Sở giao dịch quốc tế (IMM)",
            "C.Ngân hàng Nhà nước",
            "D.Thị trường chứng khoán"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Lý do sử dụng hợp đồng Futures là gì?",
        "goi_y": [
            "A.Chỉ để đầu cơ",
            "B.Phòng ngừa rủi ro tỷ giá và tìm kiếm cơ hội kinh doanh",
            "C.Chỉ để thanh toán",
            "D.Chỉ dành cho doanh nghiệp xuất khẩu"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Hoán đổi tiền tệ (Swap) là gì?",
        "goi_y": [
            "A.Mua ngoại tệ giao ngay",
            "B.Bán ngoại tệ kỳ hạn",
            "C.Kết hợp đồng thời một giao dịch mua và một giao dịch bán cùng một lượng ngoại tệ với hai thời điểm thanh toán khác nhau",
            "D.Mua vàng bằng ngoại tệ"
        ],
        "dap_an_dung": "C"
    },

    {
        "cau_hoi": "Lợi ích chính của giao dịch Swap là gì?",
        "goi_y": [
            "A.Tăng lợi nhuận từ lãi suất",
            "B.Phòng ngừa rủi ro hối đoái và giảm chi phí",
            "C.Mua bán cổ phiếu",
            "D.Tăng vốn điều lệ"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Trong các thị trường sau, thị trường nào có thời gian thanh toán sớm nhất?",
        "goi_y": [
            "A.Forward",
            "B.Futures",
            "C.Spot",
            "D.Options"
        ],
        "dap_an_dung": "C"
    },

    {
        "cau_hoi": "Điểm giống nhau giữa Forward và Futures là gì?",
        "goi_y": [
            "A.Đều thanh toán ngay",
            "B.Đều là hợp đồng mua bán ngoại tệ thực hiện trong tương lai",
            "C.Đều giao dịch trên sở giao dịch",
            "D.Đều không có rủi ro"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Điểm khác biệt lớn nhất giữa Forward và Futures là gì?",
        "goi_y": [
            "A.Forward có thanh toán, Futures không",
            "B.Futures được chuẩn hóa và giao dịch trên sở giao dịch, còn Forward là hợp đồng thỏa thuận riêng",
            "C.Forward chỉ dùng cho ngân hàng",
            "D.Futures không có tỷ giá"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Theo bài học, thị trường ngoại hối được phân loại theo bao nhiêu tiêu chí?",
        "goi_y": [
            "A.Hai",
            "B.Ba",
            "C.Bốn",
            "D.Năm"
        ],
        "dap_an_dung": "A"
    },

    {
        "cau_hoi": "Theo nghiệp vụ kinh doanh, thị trường ngoại hối gồm những thị trường nào?",
        "goi_y": [
            "A.Spot, Forward, Swaps, Futures, Options",
            "B.Spot, Chứng khoán, Trái phiếu",
            "C.Forward, Cổ phiếu, Spot",
            "D.Futures, Tiền gửi, Spot"
        ],
        "dap_an_dung": "A"
    },
      {
        "cau_hoi": "Tỷ giá áp dụng trong Spot Market là:",
        "goi_y": [
            "A.Tỷ giá tương lai",
            "B.Tỷ giá giao ngay",
            "C.Tỷ giá dự kiến",
            "D.Không xác định"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Thời gian thanh toán của Spot Market là:",
        "goi_y": [
            "A.Ngay lập tức",
            "B.Trong vòng hai ngày làm việc",
            "C.Sau 30 ngày",
            "D.Sau 90 ngày"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Spot Market thích hợp nhất khi:",
        "goi_y": [
            "A.Doanh nghiệp cần ngoại tệ ngay",
            "B.Doanh nghiệp cần ngoại tệ sau 6 tháng",
            "C.Đầu tư dài hạn",
            "D.Mua trái phiếu"
        ],
        "dap_an_dung": "A"
    },

    {
        "cau_hoi": "Nhược điểm của Spot Market là:",
        "goi_y": [
            "A.Không có tỷ giá",
            "B.Không đáp ứng nhu cầu giao dịch trong tương lai",
            "C.Không có ngân hàng tham gia",
            "D.Không thanh toán được"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Forward Market là:",
        "goi_y": [
            "A.Mua bán ngoại tệ và thanh toán trong tương lai",
            "B.Thanh toán ngay",
            "C.Chỉ mua vàng",
            "D.Chỉ mua chứng khoán"
        ],
        "dap_an_dung": "A"
    },

    {
        "cau_hoi": "Trong hợp đồng Forward, tỷ giá được:",
        "goi_y": [
            "A.Quyết định vào ngày thanh toán",
            "B.Xác định trước khi ký hợp đồng",
            "C.Thay đổi mỗi ngày",
            "D.Không xác định"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Forward giúp doanh nghiệp:",
        "goi_y": [
            "A.Tăng lãi suất",
            "B.Phòng ngừa rủi ro tỷ giá",
            "C.Giảm thuế",
            "D.Tăng doanh thu"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Thanh toán của hợp đồng Forward diễn ra:",
        "goi_y": [
            "A.Ngay lập tức",
            "B.Trong tương lai",
            "C.Sau hai ngày",
            "D.Sau một ngày"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Futures Market là:",
        "goi_y": [
            "A.Hợp đồng mua bán ngoại tệ chuẩn hóa",
            "B.Hợp đồng vay vốn",
            "C.Hợp đồng mua cổ phiếu",
            "D.Hợp đồng bảo hiểm"
        ],
        "dap_an_dung": "A"
    },

    {
        "cau_hoi": "Hợp đồng Futures được giao dịch tại:",
        "goi_y": [
            "A.Ngân hàng",
            "B.Doanh nghiệp",
            "C.Sở giao dịch",
            "D.Hải quan"
        ],
        "dap_an_dung": "C"
    },

    {
        "cau_hoi": "Futures được giao dịch tại:",
        "goi_y": [
            "A.WTO",
            "B.IMF",
            "C.IMM",
            "D.WB"
        ],
        "dap_an_dung": "C"
    },

    {
        "cau_hoi": "Mục đích của Futures là:",
        "goi_y": [
            "A.Chỉ đầu cơ",
            "B.Chỉ thanh toán",
            "C.Phòng ngừa rủi ro và tìm kiếm lợi nhuận",
            "D.Chỉ dành cho ngân hàng"
        ],
        "dap_an_dung": "C"
    },

    {
        "cau_hoi": "Swap là:",
        "goi_y": [
            "A.Kết hợp đồng thời một giao dịch mua và một giao dịch bán cùng một lượng ngoại tệ với hai thời điểm thanh toán khác nhau",
            "B.Hai giao dịch chứng khoán",
            "C.Hai giao dịch vàng",
            "D.Hai giao dịch trái phiếu"
        ],
        "dap_an_dung": "A"
    },

    {
        "cau_hoi": "Đặc điểm của Swap là:",
        "goi_y": [
            "A.Hai giao dịch có thời điểm thanh toán khác nhau",
            "B.Hai giao dịch thanh toán cùng lúc",
            "C.Không có tỷ giá",
            "D.Không có ngoại tệ"
        ],
        "dap_an_dung": "A"
    },

    {
        "cau_hoi": "Mục đích của Swap là:",
        "goi_y": [
            "A.Đầu cơ vàng",
            "B.Giảm chi phí và phòng ngừa rủi ro tỷ giá",
            "C.Tăng lãi suất",
            "D.Phát hành cổ phiếu"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Điểm khác nhau lớn nhất giữa Spot và Forward là:",
        "goi_y": [
            "A.Spot thanh toán trong vòng hai ngày làm việc (T+2), Forward thanh toán trong tương lai",
            "B.Spot không có tỷ giá",
            "C.Forward không có ngoại tệ",
            "D.Spot không có hợp đồng"
        ],
        "dap_an_dung": "A"
    },

    {
        "cau_hoi": "Điểm khác nhau lớn nhất giữa Forward và Futures là:",
        "goi_y": [
            "A.Futures được chuẩn hóa và giao dịch trên sở giao dịch, còn Forward là hợp đồng thỏa thuận riêng",
            "B.Futures không có hợp đồng",
            "C.Forward thanh toán ngay",
            "D.Futures không có tỷ giá"
        ],
        "dap_an_dung": "A"
    },

    {
        "cau_hoi": "Điểm giống nhau giữa Futures và Forward là:",
        "goi_y": [
            "A.Đều thanh toán ngay",
            "B.Đều thực hiện giao dịch trong tương lai",
            "C.Đều giao dịch OTC",
            "D.Đều không có hợp đồng"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Nếu doanh nghiệp biết 3 tháng nữa phải thanh toán 100.000 USD thì nên sử dụng:",
        "goi_y": [
            "A.Spot",
            "B.Forward",
            "C.Tiền gửi tiết kiệm",
            "D.Trái phiếu"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Nếu doanh nghiệp cần thanh toán USD ngay hôm nay thì nên sử dụng:",
        "goi_y": [
            "A.Futures",
            "B.Forward",
            "C.Spot",
            "D.Options"
        ],
        "dap_an_dung": "C"
    },

    {
        "cau_hoi": "Một doanh nghiệp vừa mua USD giao ngay, vừa bán đúng số USD đó theo hợp đồng kỳ hạn nhằm hạn chế rủi ro tỷ giá. Đây là nghiệp vụ:",
        "goi_y": [
            "A.Spot",
            "B.Forward",
            "C.Swap",
            "D.Futures"
        ],
        "dap_an_dung": "C"
    }
    ]
elif chuong_da_chon == "Đề 4":
    cac_cau_hoi =[  
       {
        "cau_hoi": "Kênh đào Suez kết nối giữa những vùng biển nào sau đây?",
        "goi_y": [
            "A.Giữa Địa Trung Hải và Biển Đỏ",
            "B.Giữa Địa Trung Hải và Biển Đen",
            "C.Giữa Biển Baltic và Địa Trung Hải",
            "D.Giữa Biển Caspi và Địa Trung Hải"
        ],
        "dap_an_dung": "A"
    },

    {
        "cau_hoi": "Số hiệu container được các hãng tàu in trên vỏ bên ngoài container có ký hiệu gì?",
        "goi_y": [
            "A.4 chữ cái viết hoa và 7 con số",
            "B.4 chữ cái viết hoa và 6 con số",
            "C.5 chữ cái viết hoa và 6 con số",
            "D.5 chữ cái viết hoa và 7 con số"
        ],
        "dap_an_dung": "A"
    },

    {
        "cau_hoi": "Để nhận hàng tại cảng đích, người nhận hàng có tên trên vận tải đơn cần có chứng từ gì do hãng tàu hoặc người vận chuyển đường biển phát hành?",
        "goi_y": [
            "A.Lệnh giao hàng (D/O)",
            "B.Thông báo hàng đến",
            "C.Hóa đơn cước phí vận chuyển",
            "D.Bản sao vận tải đơn"
        ],
        "dap_an_dung": "A"
    },

    {
        "cau_hoi": "Nếu một chiếc tàu biển của chủ tàu Việt Nam đăng ký và treo cờ Panama thì việc treo cờ đó được xem là gì?",
        "goi_y": [
            "A.Treo cờ thuận tiện (Flag of Convenience)",
            "B.Treo cờ quốc tế",
            "C.Treo cờ bình thường",
            "D.Treo cờ tín hiệu"
        ],
        "dap_an_dung": "A"
    },

    {
        "cau_hoi": "Người nhận hàng cần làm thủ tục cược (mượn) container với hãng tàu trong trường hợp nào?",
        "goi_y": [
            "A.Nhận hàng FCL giao thẳng",
            "B.Nhận hàng FCL rút ruột tại bãi cảng",
            "C.Nhận hàng LCL",
            "D.Nhận hàng FCL rút ruột tại bãi và nhận hàng LCL"
        ],
        "dap_an_dung": "A"
    },

    {
        "cau_hoi": "Đối với hàng hóa cồng kềnh, cước phí vận chuyển thường được tính dựa vào yếu tố nào?",
        "goi_y": [
            "A.Thể tích",
            "B.Trọng lượng",
            "C.Giá trị",
            "D.Thỏa thuận giữa người gửi hàng và người chuyên chở"
        ],
        "dap_an_dung": "A"
    },

    {
        "cau_hoi": "Chọn câu SAI về vận đơn hàng không (AWB).",
        "goi_y": [
            "A.AWB là chứng từ có thể ký hậu được",
            "B.AWB là giấy chứng nhận bảo hiểm",
            "C.AWB là chứng từ khai hải quan",
            "D.AWB là chứng từ không thể ký hậu được"
        ],
        "dap_an_dung": "A"
    },

    {
        "cau_hoi": "Các khu vực thuộc cảng hàng không gồm những khu vực nào?",
        "goi_y": [
            "A.Khu vực phục vụ máy bay, khu vực quản lý hành chính và trạm giao nhận hàng hóa xuất nhập khẩu",
            "B.Khu vực phục vụ máy bay và trạm giao nhận hàng hóa xuất nhập khẩu",
            "C.Trạm giao nhận hàng hóa xuất nhập khẩu và khu vực quản lý hành chính",
            "D.Khu vực quản lý hành chính và khu vực phục vụ máy bay"
        ],
        "dap_an_dung": "A"
    },

    {
        "cau_hoi": "Thiết bị được coi là thiết bị xếp hàng theo đơn vị (ULD) trong vận tải hàng không là gì?",
        "goi_y": [
            "A.Igloo và Pallet",
            "B.Pallet và Igloo",
            "C.Igloo và Container",
            "D.Container và Pallet"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Theo Công ước Warsaw 1929, hàng hóa thuộc trách nhiệm của người chuyên chở hàng không trong giai đoạn nào?",
        "goi_y": [
            "A.Hàng hóa nằm trong máy bay, trường hợp hạ cánh ngoài cảng hàng không hợp lý và trong quá trình vận chuyển đường bộ, đường biển, đường sông để thực hiện hợp đồng vận tải hàng không",
            "B.Chỉ khi hàng hóa nằm trong máy bay hoặc hạ cánh ngoài cảng hàng không hợp lý",
            "C.Chỉ khi vận chuyển bằng đường bộ, đường biển hoặc đường sông để thực hiện hợp đồng vận tải hàng không",
            "D.Chỉ khi hàng hóa nằm trong máy bay"
        ],
        "dap_an_dung": "A"
    },

    {
        "cau_hoi": "Theo Công ước Warsaw 1929, giới hạn trách nhiệm của người chuyên chở đối với hàng hóa bị tổn thất là bao nhiêu?",
        "goi_y": [
            "A.250 Franc vàng/kg",
            "B.300 Franc vàng/kg",
            "C.10000 Franc vàng/kg",
            "D.20000 Franc vàng/kg"
        ],
        "dap_an_dung": "A"
    },

    {
        "cau_hoi": "Trong vận tải hàng không, khi gửi hàng lẻ qua đại lý gom hàng, tại cảng đến người nhận hàng sẽ xuất trình loại vận đơn nào?",
        "goi_y": [
            "A.Vận đơn thứ cấp (HAWB)",
            "B.Vận đơn chủ (MAWB)",
            "C.Vận đơn theo lệnh",
            "D.Cả MAWB và HAWB"
        ],
        "dap_an_dung": "A"
    },

    {
        "cau_hoi": "Vận đơn hàng không (AWB) là gì?",
        "goi_y": [
            "A.Chứng từ sở hữu hàng hóa",
            "B.Bằng chứng của hợp đồng vận tải và xác nhận người chuyên chở đã nhận hàng",
            "C.Chứng từ dùng để nhận hàng ở cảng đến",
            "D.Chứng từ sở hữu hàng hóa và dùng để nhận hàng"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Vận chuyển hàng từ TP.HCM đến Dubai bằng đường biển rồi từ Dubai đến Frankfurt bằng đường hàng không là mô hình vận tải đa phương thức nào?",
        "goi_y": [
            "A.Sea-Air",
            "B.Sea-Road-Air",
            "C.Land Bridge",
            "D.Sea-Air-Road"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Trong vận tải hàng hóa bằng đường hàng không, thời hạn trách nhiệm của người chuyên chở được tính từ khi nào?",
        "goi_y": [
            "A.Hàng hóa được hãng hàng không nhận để chở tại sân bay",
            "B.Hàng hóa được xếp lên máy bay",
            "C.Hàng hóa được nhận để chở tại một địa điểm bất kỳ",
            "D.Hãng hàng không thông báo chấp nhận việc chuyên chở"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Ba bản gốc AWB được phân phối như thế nào?",
        "goi_y": [
            "A.Bản thứ nhất giao cho người gửi hàng, bản thứ hai giao cho người nhận hàng, bản thứ ba giao cho người chuyên chở",
            "B.Bản thứ nhất giao cho người chuyên chở, bản thứ hai và thứ ba giao cho người nhận hàng",
            "C.Bản thứ nhất giao cho người chuyên chở, bản thứ hai giao cho người nhận hàng, bản thứ ba giao cho người gửi hàng",
            "D.Bản thứ nhất giao cho người chuyên chở, bản thứ hai và thứ ba giao cho người gửi hàng"
        ],
        "dap_an_dung": "C"
    },

    {
        "cau_hoi": "Vận đơn hàng không (AWB) có thể được lập bởi ai?",
        "goi_y": [
            "A.Người chuyên chở hàng không, hãng hàng không và người gom hàng",
            "B.Người chuyên chở hàng không và hãng hàng không",
            "C.Hãng hàng không và người gom hàng",
            "D.Người gom hàng và người chuyên chở hàng không"
        ],
        "dap_an_dung": "A"
    },

    {
        "cau_hoi": "Trong vận chuyển hàng không, cước hàng bách hóa thông thường (GCR-N) được áp dụng đối với lô hàng có khối lượng bao nhiêu?",
        "goi_y": [
            "A.Từ 45 kg trở xuống",
            "B.Từ 40 kg trở xuống",
            "C.Từ 50 kg trở xuống",
            "D.Từ 55 kg trở xuống"
        ],
        "dap_an_dung": "A"
    },

    {
        "cau_hoi": "Trọng lượng cả bì (Gross Weight) được dùng để tính cước trong trường hợp hàng hóa là:",
        "goi_y": [
            "A.Hàng nặng",
            "B.Hàng nhẹ",
            "C.Hàng cồng kềnh",
            "D.Hàng nhẹ và hàng cồng kềnh"
        ],
        "dap_an_dung": "A"
    },

    {
        "cau_hoi": "Theo Công ước hàng không, tổn thất do lỗi của người chuyên chở, người phục vụ hoặc đại lý của họ sẽ không được miễn trách theo quy định của văn bản nào?",
        "goi_y": [
            "A.Nghị định thư Montreal 1975",
            "B.Công ước Warsaw 1929",
            "C.Nghị định thư Hague 1955",
            "D.Công ước Guadalajara 1961"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Nếu giá trị hàng hóa được kê khai trên AWB thì người chuyên chở sẽ bồi thường theo nguyên tắc nào?",
        "goi_y": [
            "A.Giá trị đã kê khai",
            "B.Giới hạn trách nhiệm theo công ước điều chỉnh",
            "C.Theo thỏa thuận khi xảy ra tổn thất",
            "D.Giá trị đã kê khai nhưng phải được người chuyên chở chấp nhận"
        ],
        "dap_an_dung": "D"
    },

    {
        "cau_hoi": "Theo thông lệ quốc tế, hàng nhẹ là hàng có mật độ hàng hóa:",
        "goi_y": [
            "A.Nhỏ hơn 6000 cm³/kg",
            "B.Nhỏ hơn 5000 cm³/kg",
            "C.Nhỏ hơn 5500 cm³/kg",
            "D.Nhỏ hơn 6500 cm³/kg"
        ],
        "dap_an_dung": "A"
    }
    ]
elif chuong_da_chon == "Đề 4":
    cac_cau_hoi =[  
      {
        "cau_hoi": "Các điều kiện chủ yếu trong thanh toán quốc tế gồm:",
        "goi_y": [
            "A.Điều kiện về tiền tệ",
            "B.Điều kiện về địa điểm thanh toán",
            "C.Điều kiện về thời gian thanh toán",
            "D.Tất cả các đáp án trên"
        ],
        "dap_an_dung": "D"
    },

    {
        "cau_hoi": "Điều kiện nào quy định đồng tiền được sử dụng để ghi giá hàng hóa?",
        "goi_y": [
            "A.Đồng tiền thanh toán",
            "B.Đồng tiền tính toán",
            "C.Đồng tiền dự trữ",
            "D.Đồng tiền chuyển đổi"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Đồng tiền thanh toán là:",
        "goi_y": [
            "A.Đồng tiền dùng để tính giá hàng hóa",
            "B.Đồng tiền dùng để thanh toán giá trị hợp đồng",
            "C.Đồng tiền của nước xuất khẩu",
            "D.Đồng tiền của nước nhập khẩu"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Đồng tiền tính toán (Accounting Currency) được dùng để:",
        "goi_y": [
            "A.Trả nợ",
            "B.Thanh toán qua ngân hàng",
            "C.Biểu hiện giá cả hàng hóa và tính tổng giá trị hợp đồng",
            "D.Mở L/C"
        ],
        "dap_an_dung": "C"
    },

    {
        "cau_hoi": "Đồng tiền thanh toán (Payment Currency) được dùng để:",
        "goi_y": [
            "A.Ghi giá hàng hóa",
            "B.Thanh toán công nợ và giá trị hợp đồng",
            "C.Xác định thuế",
            "D.Tính lãi vay"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Công cụ nào sau đây dùng để phòng ngừa rủi ro tỷ giá?",
        "goi_y": [
            "A.Hợp đồng kỳ hạn",
            "B.Hợp đồng hoán đổi",
            "C.Hợp đồng tương lai",
            "D.Tất cả các đáp án trên"
        ],
        "dap_an_dung": "D"
    },

    {
        "cau_hoi": "Công cụ nào không được nêu trong slide để bảo đảm rủi ro tỷ giá?",
        "goi_y": [
            "A.Forward",
            "B.Futures",
            "C.Swap",
            "D.Cheque"
        ],
        "dap_an_dung": "D"
    },

    {
        "cau_hoi": "Hợp đồng quyền chọn (Option) được sử dụng chủ yếu nhằm:",
        "goi_y": [
            "A.Phòng ngừa rủi ro tỷ giá",
            "B.Tăng thuế",
            "C.Tăng phí ngân hàng",
            "D.Mở tài khoản"
        ],
        "dap_an_dung": "A"
    },

    {
        "cau_hoi": "Địa điểm thanh toán là:",
        "goi_y": [
            "A.Nơi giao hàng",
            "B.Nơi người bán nhận tiền và người mua trả tiền",
            "C.Nơi mở L/C",
            "D.Nơi làm thủ tục hải quan"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Địa điểm thanh toán phụ thuộc vào:",
        "goi_y": [
            "A.Tương quan lực lượng giữa hai bên",
            "B.Phương thức thanh toán",
            "C.Đồng tiền thanh toán",
            "D.Tất cả các đáp án trên"
        ],
        "dap_an_dung": "D"
    },

    {
        "cau_hoi": "Yếu tố nào sau đây không ảnh hưởng đến địa điểm thanh toán?",
        "goi_y": [
            "A.Phương thức thanh toán",
            "B.Đồng tiền thanh toán",
            "C.Quan hệ giữa hai bên",
            "D.Trọng lượng hàng hóa"
        ],
        "dap_an_dung": "D"
    },

    {
        "cau_hoi": "Điều kiện thời gian thanh toán gồm:",
        "goi_y": [
            "A.Trả trước",
            "B.Trả ngay",
            "C.Trả sau",
            "D.Tất cả các đáp án trên"
        ],
        "dap_an_dung": "D"
    },
     {
        "cau_hoi": "Phương thức thanh toán kết hợp trả trước và trả sau gọi là:",
        "goi_y": [
            "A.Deferred Payment",
            "B.Combined Payment",
            "C.At Sight",
            "D.Spot Payment"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Trong phương thức trả tiền trước:",
        "goi_y": [
            "A.Người bán giao hàng trước",
            "B.Người mua thanh toán trước khi giao hàng",
            "C.Người mua nhận hàng trước",
            "D.Thanh toán sau khi nhận hàng"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Trong trả tiền trước, người hưởng lợi nhiều nhất là:",
        "goi_y": [
            "A.Người mua",
            "B.Người bán",
            "C.Ngân hàng",
            "D.Hãng tàu"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Trong trả tiền trước, rủi ro lớn nhất thuộc về:",
        "goi_y": [
            "A.Người bán",
            "B.Người mua",
            "C.Ngân hàng",
            "D.Hải quan"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Thời điểm thanh toán trong phương thức trả trước là:",
        "goi_y": [
            "A.Sau khi giao hàng",
            "B.Trước khi chuyển giao hàng hóa",
            "C.Sau khi nhận hàng",
            "D.Sau khi kiểm hóa"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Thời điểm giao hàng trong phương thức trả trước là:",
        "goi_y": [
            "A.Trước khi thanh toán",
            "B.Sau khi người mua thanh toán",
            "C.Đồng thời với thanh toán",
            "D.Không xác định"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Trả tiền trước thường áp dụng khi:",
        "goi_y": [
            "A.Người bán chưa tin tưởng người mua",
            "B.Hai bên hợp tác lâu năm",
            "C.Giá trị hợp đồng nhỏ",
            "D.Không có ngân hàng"
        ],
        "dap_an_dung": "A"
    },

    {
        "cau_hoi": "Thanh toán trả ngay là:",
        "goi_y": [
            "A.Thanh toán trước khi ký hợp đồng",
            "B.Thanh toán ngay khi đến thời điểm quy định",
            "C.Thanh toán sau 6 tháng",
            "D.Thanh toán trả góp"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Theo bài học, thanh toán trả ngay có thể diễn ra khi:",
        "goi_y": [
            "A.Người bán đặt hàng hóa dưới quyền định đoạt của người mua",
            "B.Người bán xuất trình bộ chứng từ",
            "C.Người mua nhận hàng",
            "D.Tất cả các đáp án trên"
        ],
        "dap_an_dung": "D"
    },

    {
        "cau_hoi": "Trong trả tiền sau:",
        "goi_y": [
            "A.Người mua thanh toán trước",
            "B.Người bán giao hàng trước, thu tiền sau",
            "C.Thanh toán ngay",
            "D.Không giao hàng"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Trong trả tiền sau, người chịu rủi ro lớn nhất là:",
        "goi_y": [
            "A.Người bán",
            "B.Người mua",
            "C.Ngân hàng",
            "D.Hãng tàu"
        ],
        "dap_an_dung": "A"
    },

    {
        "cau_hoi": "Trong trả tiền sau, người mua:",
        "goi_y": [
            "A.Không có rủi ro đáng kể",
            "B.Chịu toàn bộ rủi ro",
            "C.Phải trả tiền trước",
            "D.Không nhận hàng"
        ],
        "dap_an_dung": "A"
    },
     {
        "cau_hoi": "Thời điểm giao hàng trong phương thức trả tiền sau là:",
        "goi_y": [
            "A.Sau khi thanh toán",
            "B.Trước khi người mua thanh toán",
            "C.Sau khi mở L/C",
            "D.Không xác định"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Trả tiền sau thường áp dụng khi:",
        "goi_y": [
            "A.Người bán chưa biết người mua",
            "B.Người bán tin tưởng người mua",
            "C.Người mua chưa có giấy phép nhập khẩu",
            "D.Hàng hóa bị cấm xuất khẩu"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Phương thức thanh toán quốc tế là:",
        "goi_y": [
            "A.Quá trình người mua trả tiền và người bán nhận tiền thông qua hệ thống ngân hàng",
            "B.Quá trình vận chuyển hàng hóa",
            "C.Quá trình khai báo hải quan",
            "D.Quá trình mua bảo hiểm"
        ],
        "dap_an_dung": "A"
    },

    {
        "cau_hoi": "Ngân hàng trong thanh toán quốc tế có vai trò:",
        "goi_y": [
            "A.Vận chuyển hàng",
            "B.Trung gian thực hiện việc chuyển tiền",
            "C.Kiểm tra chất lượng hàng hóa",
            "D.Đóng gói hàng hóa"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Điểm khác nhau lớn nhất giữa trả tiền trước và trả tiền sau là:",
        "goi_y": [
            "A.Người bán giao hàng trước hay sau khi nhận tiền",
            "B.Đồng tiền thanh toán",
            "C.Địa điểm thanh toán",
            "D.Loại hàng hóa"
        ],
        "dap_an_dung": "A"
    },

    {
        "cau_hoi": "So sánh rủi ro giữa trả tiền trước và trả tiền sau:",
        "goi_y": [
            "A.Trả trước: người bán rủi ro; Trả sau: người mua rủi ro",
            "B.Trả trước: người mua rủi ro; Trả sau: người bán rủi ro",
            "C.Cả hai đều người mua rủi ro",
            "D.Cả hai đều người bán rủi ro"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Doanh nghiệp Việt Nam lần đầu nhập khẩu từ một nhà cung cấp mới. Người bán yêu cầu thanh toán trước 100% giá trị hợp đồng. Mục đích chính của yêu cầu này là:",
        "goi_y": [
            "A.Giảm rủi ro cho người bán",
            "B.Giảm rủi ro cho người mua",
            "C.Giảm thuế nhập khẩu",
            "D.Giảm phí vận tải"
        ],
        "dap_an_dung": "A"
    },

    {
        "cau_hoi": "Doanh nghiệp xuất khẩu giao hàng trước và cho phép khách hàng thanh toán sau 60 ngày. Đây là:",
        "goi_y": [
            "A.Advance Payment",
            "B.At Sight Payment",
            "C.Deferred Payment",
            "D.Combined Payment"
        ],
        "dap_an_dung": "C"
    },

    {
        "cau_hoi": "Một hợp đồng quy định thanh toán 30% trước khi giao hàng và 70% sau khi nhận hàng. Đây là:",
        "goi_y": [
            "A.Trả trước",
            "B.Trả sau",
            "C.Thanh toán hỗn hợp (Combined Payment)",
            "D.Thanh toán giao ngay"
        ],
        "dap_an_dung": "C"
    },

    {
        "cau_hoi": "Nếu doanh nghiệp muốn hạn chế rủi ro do biến động tỷ giá khi thanh toán sau 3 tháng thì nên sử dụng công cụ nào?",
        "goi_y": [
            "A.Hợp đồng kỳ hạn (Forward)",
            "B.Hợp đồng hoán đổi (Swap)",
            "C.Hợp đồng tương lai (Futures)",
            "D.Bất kỳ công cụ phòng ngừa rủi ro tỷ giá nào phù hợp"
        ],
        "dap_an_dung": "A"
    },
    {
    "cau_hoi": "Thời điểm giao hàng trong phương thức trả tiền sau là:",
    "goi_y": [
        "A.Sau khi thanh toán",
        "B.Trước khi người mua thanh toán",
        "C.Sau khi mở L/C",
        "D.Không xác định"
        ],
        "dap_an_dung": "B"
    }
    ]
elif chuong_da_chon == "Chương 8.3: Thanh toán quốc tế":
    cac_cau_hoi =[  
      {
    "cau_hoi": "Các điều kiện chủ yếu trong thanh toán quốc tế gồm:",
    "goi_y": [
        "A.Điều kiện về tiền tệ",
        "B.Điều kiện về địa điểm thanh toán",
        "C.Điều kiện về thời gian thanh toán và phương thức thanh toán",
        "D.Tất cả các đáp án trên"
    ],
    "dap_an_dung": "D"
    },

    {
    "cau_hoi": "Đồng tiền tính toán (Accounting Currency) là đồng tiền dùng để:",
    "goi_y": [
        "A.Thanh toán công nợ",
        "B.Biểu hiện giá cả hàng hóa và tính tổng giá trị hợp đồng ngoại thương",
        "C.Mở L/C",
        "D.Chuyển tiền qua ngân hàng"
    ],
    "dap_an_dung": "B"
    },

    {
    "cau_hoi": "Đồng tiền thanh toán (Payment Currency) là:",
    "goi_y": [
        "A.Đồng tiền dùng để tính giá hàng hóa",
        "B.Đồng tiền dùng để thanh toán giá trị hợp đồng và công nợ",
        "C.Đồng tiền của nước xuất khẩu",
        "D.Đồng tiền của nước nhập khẩu"
    ],
    "dap_an_dung": "B"
    },

    {
    "cau_hoi": "Địa điểm thanh toán phụ thuộc vào yếu tố nào sau đây?",
    "goi_y": [
        "A.Tương quan lực lượng giữa hai bên trong hợp đồng",
        "B.Phương thức thanh toán",
        "C.Đồng tiền thanh toán",
        "D.Tất cả các đáp án trên"
    ],
    "dap_an_dung": "D"
    },

    {
    "cau_hoi": "Trong phương thức trả tiền trước (Advance Payment):",
    "goi_y": [
        "A.Người bán giao hàng trước rồi mới thu tiền",
        "B.Người mua thanh toán trước khi người bán giao hàng",
        "C.Người mua thanh toán sau khi nhận hàng",
        "D.Hai bên thanh toán cùng lúc"
    ],
    "dap_an_dung": "B"
    },

    {
    "cau_hoi": "Trong phương thức trả tiền trước, bên chịu rủi ro lớn hơn là:",
    "goi_y": [
        "A.Người bán",
        "B.Người mua",
        "C.Ngân hàng",
        "D.Hãng tàu"
    ],
    "dap_an_dung": "B"
    },

    {
    "cau_hoi": "Theo bài học, phương thức trả tiền trước thường áp dụng khi:",
    "goi_y": [
        "A.Người bán chưa tin tưởng người mua hoặc hàng hóa có giá trị lớn",
        "B.Hai bên đã hợp tác lâu năm",
        "C.Người mua có uy tín cao",
        "D.Hàng hóa giao nhiều lần"
    ],
    "dap_an_dung": "A"
    },

    {
    "cau_hoi": "Theo phương thức trả tiền ngay (At Sight Payment), việc thanh toán có thể diễn ra:",
    "goi_y": [
        "A.Khi người bán giao hàng dưới quyền định đoạt của người mua",
        "B.Khi người bán xuất trình bộ chứng từ hàng hóa",
        "C.Ngay sau khi người nhập khẩu nhận hàng theo quy định",
        "D.Tất cả các đáp án trên"
    ],
    "dap_an_dung": "D"
    },

    {
    "cau_hoi": "Doanh nghiệp A yêu cầu khách hàng thanh toán toàn bộ tiền hàng trước khi giao hàng nhằm tránh rủi ro không thu được tiền. Doanh nghiệp A đang áp dụng:",
    "goi_y": [
        "A.Deferred Payment",
        "B.At Sight Payment",
        "C.Advance Payment",
        "D.Combined Payment"
    ],
    "dap_an_dung": "C"
    },

    {
    "cau_hoi": "Để phòng ngừa rủi ro do biến động tỷ giá trong thanh toán quốc tế, doanh nghiệp có thể sử dụng:",
    "goi_y": [
        "A.Hợp đồng kỳ hạn (Forward)",
        "B.Hợp đồng hoán đổi (Swap)",
        "C.Hợp đồng tương lai (Futures) hoặc hợp đồng quyền chọn (Options)",
        "D.Tất cả các đáp án trên"
    ],
    "dap_an_dung": "D"
    },

    {
    "cau_hoi": "Điểm khác nhau cơ bản giữa đồng tiền tính toán và đồng tiền thanh toán là:",
    "goi_y": [
        "A.Đồng tiền tính toán dùng để ghi giá hợp đồng; đồng tiền thanh toán dùng để thanh toán thực tế",
        "B.Hai loại đồng tiền luôn giống nhau",
        "C.Đồng tiền thanh toán chỉ là USD",
        "D.Đồng tiền tính toán chỉ dùng trong kế toán"
    ],
    "dap_an_dung": "A"
    },

    {
    "cau_hoi": "Trong phương thức Advance Payment, người bán hầu như không chịu rủi ro vì:",
    "goi_y": [
        "A.Đã nhận được tiền trước khi giao hàng",
        "B.Có bảo hiểm hàng hóa",
        "C.Có ngân hàng bảo lãnh",
        "D.Hàng hóa đã lên tàu"
    ],
    "dap_an_dung": "A"
    },

    {
    "cau_hoi": "Yếu tố nào sau đây không ảnh hưởng đến địa điểm thanh toán?",
    "goi_y": [
        "A.Phương thức thanh toán",
        "B.Đồng tiền thanh toán",
        "C.Quan hệ giữa hai bên",
        "D.Loại phương tiện vận tải sử dụng"
    ],
    "dap_an_dung": "D"
    },
    {
    "cau_hoi": "Chứng từ trong thanh toán quốc tế là:",
    "goi_y": [
        "A.Văn bản chỉ chứa thông tin về hàng hóa",
        "B.Văn bản chứa thông tin về hàng hóa, vận tải, bảo hiểm, thanh toán để nhận hàng, thanh toán hoặc khiếu nại",
        "C.Chỉ là hóa đơn thương mại",
        "D.Chỉ là chứng từ ngân hàng"
    ],
    "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Hệ thống chứng từ trong thanh toán quốc tế được chia thành:",
        "goi_y": [
            "A.Chứng từ xuất khẩu và nhập khẩu",
            "B.Chứng từ thương mại và chứng từ tài chính",
            "C.Chứng từ ngân hàng và hải quan",
            "D.Chứng từ vận tải và bảo hiểm"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Chứng từ nào sau đây thuộc chứng từ tài chính?",
        "goi_y": [
            "A.Hóa đơn thương mại",
            "B.Vận đơn đường biển",
            "C.Hối phiếu",
            "D.Phiếu đóng gói"
        ],
        "dap_an_dung": "C"
    },

    {
        "cau_hoi": "Chứng từ nào sau đây không thuộc chứng từ thương mại?",
        "goi_y": [
            "A.Phiếu đóng gói (Packing List)",
            "B.Giấy chứng nhận xuất xứ (C/O)",
            "C.Hối phiếu (Bill of Exchange)",
            "D.Bảo hiểm đơn (Insurance Policy)"
        ],
        "dap_an_dung": "C"
    },

    {
        "cau_hoi": "Khi nhà xuất khẩu không thường xuyên mua bảo hiểm cho hàng hóa, công ty bảo hiểm sẽ cấp:",
        "goi_y": [
            "A.Giấy chứng nhận bảo hiểm",
            "B.Hợp đồng bảo hiểm bao",
            "C.Bảo hiểm đơn (Insurance Policy)",
            "D.Chứng thư giám định"
        ],
        "dap_an_dung": "C"
    },

    {
        "cau_hoi": "Khi nhà xuất khẩu bán hàng thường xuyên, công ty bảo hiểm sẽ ký:",
        "goi_y": [
            "A.Bảo hiểm đơn",
            "B.Hợp đồng bảo hiểm bao (Open Policy/Open Cover)",
            "C.Hợp đồng vận tải",
            "D.Hối phiếu"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Sau mỗi lần giao hàng theo hợp đồng bảo hiểm bao, công ty bảo hiểm sẽ phát hành:",
        "goi_y": [
            "A.Hóa đơn thương mại",
            "B.Vận đơn",
            "C.Giấy chứng nhận bảo hiểm (Insurance Certificate)",
            "D.Hối phiếu"
        ],
        "dap_an_dung": "C"
    },

    {
        "cau_hoi": "Theo UCP 600, số tiền bảo hiểm tối thiểu thường phải bằng:",
        "goi_y": [
            "A.100% giá FOB",
            "B.105% giá CIF",
            "C.110% giá CIF hoặc CIP (hoặc giá trị hóa đơn theo quy định)",
            "D.120% giá CIF"
        ],
        "dap_an_dung": "C"
    },

    {
        "cau_hoi": "Chứng từ nào xác nhận xuất xứ hàng hóa?",
        "goi_y": [
            "A.Commercial Invoice",
            "B.Packing List",
            "C.Certificate of Origin (C/O)",
            "D.Certificate of Quality"
        ],
        "dap_an_dung": "C"
    },

    {
        "cau_hoi": "Chứng từ nào dùng để thể hiện quy cách đóng gói, số kiện, trọng lượng và cách sắp xếp hàng hóa?",
        "goi_y": [
            "A.Commercial Invoice",
            "B.Packing List",
            "C.Insurance Policy",
            "D.Bill of Lading"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Điểm khác nhau giữa Insurance Policy và Insurance Certificate là:",
        "goi_y": [
            "A.Insurance Policy dùng cho lô hàng đơn lẻ; Insurance Certificate được cấp cho từng lô hàng khi đã có hợp đồng bảo hiểm bao",
            "B.Hai loại hoàn toàn giống nhau",
            "C.Insurance Certificate chỉ dùng cho hàng nhập khẩu",
            "D.Insurance Policy chỉ do ngân hàng phát hành"
        ],
        "dap_an_dung": "A"
    },

    {
        "cau_hoi": "Chứng từ nào sau đây không phải là chứng từ hàng hóa?",
        "goi_y": [
            "A.Commercial Invoice",
            "B.Packing List",
            "C.Certificate of Origin",
            "D.Bill of Exchange"
        ],
        "dap_an_dung": "D"
    },

    {
        "cau_hoi": "Một doanh nghiệp xuất khẩu thực phẩm sang châu Âu cần chứng minh hàng hóa có nguồn gốc từ Việt Nam để được hưởng ưu đãi thuế quan. Chứng từ quan trọng nhất là:",
        "goi_y": [
            "A.Packing List",
            "B.Commercial Invoice",
            "C.Certificate of Origin (C/O)",
            "D.Insurance Certificate"
        ],
        "dap_an_dung": "C"
    },
    {
    "cau_hoi": "Hóa đơn thương mại (Commercial Invoice) là chứng từ do:",
    "goi_y": [
        "A.Ngân hàng lập",
        "B.Người mua lập",
        "C.Người bán lập, thể hiện số tiền người mua phải thanh toán",
        "D.Hãng tàu lập"
    ],
    "dap_an_dung": "C"
    },

    {
        "cau_hoi": "Nội dung nào sau đây không bắt buộc phải có trong Hóa đơn thương mại?",
        "goi_y": [
            "A.Điều kiện giao hàng",
            "B.Điều kiện thanh toán",
            "C.Chi tiết hàng hóa",
            "D.Vận đơn đường biển"
        ],
        "dap_an_dung": "D"
    },

    {
        "cau_hoi": "Chức năng quan trọng nhất của Hóa đơn thương mại là:",
        "goi_y": [
            "A.Là căn cứ tính thuế xuất nhập khẩu và số tiền bảo hiểm",
            "B.Xác nhận xuất xứ hàng hóa",
            "C.Xác nhận hàng đã lên tàu",
            "D.Chứng minh quyền sở hữu hàng hóa"
        ],
        "dap_an_dung": "A"
    },

    {
        "cau_hoi": "Phiếu đóng gói hàng hóa (Packing List) khác Hóa đơn thương mại ở điểm:",
        "goi_y": [
            "A.Không ghi thông tin về hàng hóa",
            "B.Không thể hiện đơn giá, trị giá và điều kiện thanh toán",
            "C.Do ngân hàng phát hành",
            "D.Chỉ dùng trong nhập khẩu"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Thông tin quan trọng nhất của Packing List là:",
        "goi_y": [
            "A.Đơn giá hàng hóa",
            "B.Điều kiện thanh toán",
            "C.Quy cách đóng gói, trọng lượng và kích thước hàng hóa",
            "D.Tỷ giá thanh toán"
        ],
        "dap_an_dung": "C"
    },

    {
        "cau_hoi": "Giấy chứng nhận xuất xứ hàng hóa (C/O) có chức năng:",
        "goi_y": [
            "A.Xác nhận nơi sản xuất hoặc khai thác hàng hóa",
            "B.Xác nhận hàng đã thanh toán",
            "C.Xác nhận hàng đã lên tàu",
            "D.Xác nhận bảo hiểm"
        ],
        "dap_an_dung": "A"
    },

    {
        "cau_hoi": "Một trong những mục đích quan trọng của C/O là:",
        "goi_y": [
            "A.Xác định mức thuế xuất nhập khẩu được hưởng",
            "B.Xác định giá CIF",
            "C.Xác định cước vận tải",
            "D.Xác định tỷ giá ngoại tệ"
        ],
        "dap_an_dung": "A"
    },

    {
        "cau_hoi": "Theo bài học, Form D được sử dụng cho hàng hóa:",
        "goi_y": [
            "A.Xuất khẩu sang Hoa Kỳ",
            "B.Xuất khẩu trong khối ASEAN để hưởng ưu đãi thuế quan",
            "C.Xuất khẩu sang Nhật Bản",
            "D.Xuất khẩu sang EU"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Tại Việt Nam, cơ quan tổ chức thực hiện việc cấp C/O là:",
        "goi_y": [
            "A.Bộ Tài chính",
            "B.Bộ Công Thương",
            "C.Ngân hàng Nhà nước",
            "D.Tổng cục Hải quan"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Bộ Công Thương có thể ủy quyền cấp C/O cho:",
        "goi_y": [
            "A.Phòng Thương mại và Công nghiệp Việt Nam (VCCI)",
            "B.Cục Quản lý Xuất nhập khẩu",
            "C.Ban quản lý một số khu công nghiệp, khu chế xuất",
            "D.Tất cả các đáp án trên"
        ],
        "dap_an_dung": "D"
    }
    ]
elif chuong_da_chon == "Chương 8.4: Thanh toán quốc tế":
    cac_cau_hoi =[  
      {
    "cau_hoi": "Phương tiện thanh toán quốc tế không bao gồm:",
    "goi_y": [
        "A.Hối phiếu",
        "B.Kỳ phiếu",
        "C.Séc",
        "D.Vận đơn"
    ],
    "dap_an_dung": "D"
    },

    {
        "cau_hoi": "Hối phiếu là:",
        "goi_y": [
            "A.Cam kết trả tiền của người mua",
            "B.Mệnh lệnh vô điều kiện do người ký phát lập, yêu cầu người bị ký phát thanh toán một số tiền nhất định",
            "C.Chứng từ sở hữu hàng hóa",
            "D.Giấy xác nhận đã thanh toán"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Trong giao dịch tín dụng thương mại, người ký phát hối phiếu thường là:",
        "goi_y": [
            "A.Ngân hàng",
            "B.Người mua (Importer)",
            "C.Người bán (Exporter)",
            "D.Hãng tàu"
        ],
        "dap_an_dung": "C"
    },

    {
        "cau_hoi": "Đặc điểm nào dưới đây đúng với hối phiếu?",
        "goi_y": [
            "A.Là lời hứa trả tiền của người mua",
            "B.Là mệnh lệnh thanh toán có điều kiện",
            "C.Là mệnh lệnh thanh toán vô điều kiện",
            "D.Không được chuyển nhượng"
        ],
        "dap_an_dung": "C"
    },

    {
        "cau_hoi": "Theo lịch sử phát triển của tín dụng thương mại, trình tự hình thành đúng là:",
        "goi_y": [
            "A.Hối phiếu → Kỳ phiếu → Luật hối phiếu",
            "B.Kỳ phiếu → Hối phiếu → Luật hối phiếu",
            "C.Luật hối phiếu → Kỳ phiếu → Hối phiếu",
            "D.Kỳ phiếu → Luật hối phiếu → Hối phiếu"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Trong các nội dung bắt buộc của hối phiếu, tiêu đề 'Hối phiếu' được ghi nhằm mục đích:",
        "goi_y": [
            "A.Xác định số tiền thanh toán",
            "B.Nhận biết chứng từ có phải là hối phiếu hay không",
            "C.Xác định thời hạn thanh toán",
            "D.Xác định người thụ hưởng"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Lệnh thanh toán ghi trên hối phiếu phải là:",
        "goi_y": [
            "A.Có điều kiện",
            "B.Có điều kiện nếu hai bên thỏa thuận",
            "C.Vô điều kiện",
            "D.Có thể thay đổi sau khi phát hành"
        ],
        "dap_an_dung": "C"
    },

    {
        "cau_hoi": "Đối với hối phiếu At Sight, người bị ký phát phải thanh toán:",
        "goi_y": [
            "A.Sau 30 ngày",
            "B.Sau 60 ngày",
            "C.Ngay khi nhìn thấy hối phiếu",
            "D.Theo ngày ghi trên hóa đơn"
        ],
        "dap_an_dung": "C"
    },

    {
        "cau_hoi": "Đâu không phải là cách quy định thời hạn của hối phiếu kỳ hạn (Usance Bill)?",
        "goi_y": [
            "A.X days after sight",
            "B.X days after signed",
            "C.X days B/L date",
            "D.X days after Letter of Credit opening"
        ],
        "dap_an_dung": "D"
    },

    {
        "cau_hoi": "Theo bài giảng, hối phiếu là loại giấy tờ:",
        "goi_y": [
            "A.Không được chuyển nhượng",
            "B.Chỉ dùng để thanh toán",
            "C.Có giá, có thể chuyển nhượng, sử dụng trong tín dụng ngân hàng và cầm cố/thế chấp",
            "D.Chỉ có giá trị trong nước"
        ],
        "dap_an_dung": "C"
    },
    {
    "cau_hoi": "Nếu trên hối phiếu không quy định địa điểm thanh toán thì địa điểm thanh toán được xác định là:",
    "goi_y": [
        "A.Địa chỉ người ký phát",
        "B.Địa chỉ người bị ký phát",
        "C.Ngân hàng phát hành L/C",
        "D.Địa chỉ người thụ hưởng"
    ],
    "dap_an_dung": "B"
},

{
    "cau_hoi": "Trong thực tế, địa điểm thanh toán hối phiếu thường là:",
    "goi_y": [
        "A.Trụ sở người ký phát",
        "B.Hãng tàu",
        "C.Ngân hàng nơi người bị ký phát mở tài khoản giao dịch",
        "D.Hải quan"
    ],
    "dap_an_dung": "C"
},

{
    "cau_hoi": "Nếu người ký phát không chỉ định người thụ hưởng khác thì người thụ hưởng là:",
    "goi_y": [
        "A.Người bị ký phát",
        "B.Ngân hàng",
        "C.Chính người ký phát",
        "D.Người vận chuyển"
    ],
    "dap_an_dung": "C"
},

{
    "cau_hoi": "Cách ghi 'Pay to the order of Mr. Tran Tien Thua...' là hình thức:",
    "goi_y": [
        "A.Vô danh",
        "B.Đích danh",
        "C.Theo lệnh",
        "D.Chuyển nhượng hạn chế"
    ],
    "dap_an_dung": "C"
    },

    {
        "cau_hoi": "'Pay to the bearer...' có nghĩa là:",
        "goi_y": [
            "A.Thanh toán theo lệnh",
            "B.Thanh toán cho người cầm phiếu",
            "C.Thanh toán cho ngân hàng",
            "D.Thanh toán cho người ký phát"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Trong các nội dung bắt buộc của hối phiếu, yếu tố cuối cùng là:",
        "goi_y": [
            "A.Địa điểm thanh toán",
            "B.Người thụ hưởng",
            "C.Thời hạn thanh toán",
            "D.Tên, địa chỉ và chữ ký của người ký phát"
        ],
        "dap_an_dung": "D"
    },

    {
        "cau_hoi": "Ngoài các nội dung bắt buộc, các thông tin bổ sung trên hối phiếu:",
        "goi_y": [
            "A.Là điều kiện bắt buộc để thanh toán",
            "B.Chỉ mang tính tham khảo, không phải căn cứ từ chối thanh toán",
            "C.Thay thế được các nội dung bắt buộc",
            "D.Có giá trị pháp lý cao hơn"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Kỳ phiếu (Promissory Note) là:",
        "goi_y": [
            "A.Mệnh lệnh thanh toán vô điều kiện",
            "B.Cam kết trả tiền vô điều kiện của người phát hành",
            "C.Giấy chứng nhận sở hữu hàng hóa",
            "D.Lệnh của ngân hàng"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Điểm khác biệt cơ bản giữa kỳ phiếu và hối phiếu là:",
        "goi_y": [
            "A.Kỳ phiếu là lời hứa trả tiền, còn hối phiếu là mệnh lệnh thanh toán",
            "B.Kỳ phiếu do ngân hàng phát hành",
            "C.Hối phiếu không dùng trong thương mại quốc tế",
            "D.Hai chứng từ hoàn toàn giống nhau"
        ],
        "dap_an_dung": "A"
    },

    {
        "cau_hoi": "Theo bài giảng, kỳ phiếu có bao nhiêu nội dung bắt buộc?",
        "goi_y": [
            "A.6",
            "B.7",
            "C.8",
            "D.9"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Nội dung nào sau đây không thuộc các nội dung bắt buộc của kỳ phiếu?",
        "goi_y": [
            "A.Địa điểm trả tiền",
            "B.Người thụ hưởng",
            "C.Người bị ký phát",
            "D.Chữ ký người phát hành"
        ],
        "dap_an_dung": "C"
    },
    {
    "cau_hoi": "Người trả tiền (Drawee) trên séc là:",
    "goi_y": [
        "A.Người mua",
        "B.Người bán",
        "C.Ngân hàng nơi người ký phát mở tài khoản",
        "D.Ngân hàng trung gian"
    ],
    "dap_an_dung": "C"
    },
    {
        "cau_hoi": "Nội dung nào sau đây không bắt buộc trên tờ séc?",
        "goi_y": [
            "A.Tiêu đề 'Séc'",
            "B.Lệnh trả tiền vô điều kiện",
            "C.Điều kiện giao hàng",
            "D.Tên người hưởng"
        ],
        "dap_an_dung": "C"
    },

    {
        "cau_hoi": "Ngày tháng và nơi ký séc nhằm mục đích:",
        "goi_y": [
            "A.Xác định số tiền",
            "B.Xác định người hưởng",
            "C.Xác định thời hạn hiệu lực của séc",
            "D.Xác định tỷ giá"
        ],
        "dap_an_dung": "C"
    },

    {
        "cau_hoi": "Yếu tố nào sau đây là thông tin bắt buộc của người ký phát séc?",
        "goi_y": [
            "A.Mã số thuế",
            "B.Số hiệu tài khoản",
            "C.Số vận đơn",
            "D.Mã SWIFT"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Nếu trên séc ghi điều kiện trả tiền thì theo quy định:",
        "goi_y": [
            "A.Séc vô hiệu",
            "B.Điều kiện đó được coi như không có",
            "C.Phải được ngân hàng chấp nhận",
            "D.Người mua quyết định"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Theo bài giảng, yếu tố nào sau đây bị cấm ghi trên séc?",
        "goi_y": [
            "A.Người hưởng",
            "B.Chữ ký",
            "C.Tiền lãi",
            "D.Địa điểm trả tiền"
        ],
        "dap_an_dung": "C"
    },

    {
        "cau_hoi": "Điều khoản miễn trừ bảo đảm trả tiền trên séc:",
        "goi_y": [
            "A.Có hiệu lực pháp lý",
            "B.Chỉ áp dụng cho ngân hàng",
            "C.Được coi như không có",
            "D.Chỉ áp dụng với séc quốc tế"
        ],
        "dap_an_dung": "C"
    },

    {
        "cau_hoi": "Nếu trên séc có ghi điều khoản chấp nhận thanh toán thì:",
        "goi_y": [
            "A.Có hiệu lực",
            "B.Phải được ngân hàng xác nhận",
            "C.Được coi như không có",
            "D.Làm tăng giá trị pháp lý của séc"
        ],
        "dap_an_dung": "C"
    },

    {
        "cau_hoi": "ATM là viết tắt của:",
        "goi_y": [
            "A.Automatic Transfer Machine",
            "B.Automatic Teller Machine",
            "C.Automatic Trade Machine",
            "D.Automated Teller Method"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Loại thẻ sử dụng tiền có sẵn trong tài khoản là:",
        "goi_y": [
            "A.Credit Card",
            "B.Debit Card",
            "C.Smart Card",
            "D.International Card"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Loại thẻ cho phép chi tiêu trước, trả tiền sau là:",
        "goi_y": [
            "A.Debit Card",
            "B.ATM Card",
            "C.Credit Card",
            "D.Smart Card"
        ],
        "dap_an_dung": "C"
    },

    {
        "cau_hoi": "Theo bài giảng, loại thẻ nào sau đây thuộc nhóm thẻ thanh toán?",
        "goi_y": [
            "A.Thẻ ghi nợ",
            "B.Thẻ tín dụng",
            "C.Thẻ thông minh",
            "D.Tất cả các đáp án trên"
        ],
        "dap_an_dung": "D"
    },

    {
        "cau_hoi": "Người trả tiền (Drawee) của séc là:",
        "goi_y": [
            "A.Người mua",
            "B.Người bán",
            "C.Ngân hàng giữ tài khoản của người ký phát",
            "D.Người ký phát"
        ],
        "dap_an_dung": "C"
    },

    {
        "cau_hoi": "Điểm giống nhau giữa hối phiếu, kỳ phiếu và séc là:",
        "goi_y": [
            "A.Đều là chứng từ vận tải",
            "B.Đều là phương tiện thanh toán quốc tế",
            "C.Đều do ngân hàng phát hành",
            "D.Đều là chứng từ sở hữu hàng hóa"
        ],
        "dap_an_dung": "B"
    },

    {
        "cau_hoi": "Đâu không phải là yếu tố bị cấm trên séc?",
        "goi_y": [
            "A.Điều kiện trả tiền",
            "B.Tiền lãi",
            "C.Người hưởng",
            "D.Điều khoản miễn trừ bảo đảm thanh toán"
        ],
        "dap_an_dung": "C"
    },
    ]
# 3. Phần hiển thị và chấm điểm (Giữ nguyên cho tất cả các chương)
st.header(f"📝 {chuong_da_chon}")
st.write("Hãy hoàn thành các câu hỏi trắc nghiệm dưới đây:")
# Khởi tạo form làm bài 
cau_tra_loi_cua_user = {}
with st.form(key=f"form_{chuong_da_chon}"):  
    for i, ch in enumerate(cac_cau_hoi, 1):
        st.subheader(f"Câu {i}: {ch['cau_hoi']}")
        lua_chon = st.radio("Chọn đáp án:", ch['goi_y'], key=f"cau_{chuong_da_chon}_{i}")
        cau_tra_loi_cua_user[i] = lua_chon[0] if lua_chon else None
        st.write("---")
    submit = st.form_submit_button("Nộp Bài & Xem Kết Quả")

if submit:
    diem = 0
    for i, ch in enumerate(cac_cau_hoi, 1):
        st.write(f"**Câu {i}:**")
        if cau_tra_loi_cua_user[i] == ch['dap_an_dung']:
            st.success(f"🎉 Đúng! Bạn chọn {cau_tra_loi_cua_user[i]}")
            diem += 1
        else:
            st.error(f"❌ Sai rồi! Bạn chọn {cau_tra_loi_cua_user[i]}. Đáp án đúng là {ch['dap_an_dung']}")     
    st.metric(label="Tổng điểm của bạn", value=f"{diem} / {len(cac_cau_hoi)}")