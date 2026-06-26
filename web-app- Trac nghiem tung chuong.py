import streamlit as st
import os
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
# 2. Tạo thanh menu chọn chương ở bên trái màn hình (Sidebar)
chuong_da_chon = st.sidebar.selectbox(
    "📚 Chọn Chương Ôn Tập:",
    ["Chương 1: Tổng quan về giao nhận hàng hóa", "Chương 2: Giao nhận bằng đường biển", "Câu hỏi hỗn hợp", "Đề 1","Đề 2", "Đề 3", "Đề 4", "Đề 5", "Đề 6"]
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