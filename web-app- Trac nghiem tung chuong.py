import streamlit as st
import streamlit_analytics
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
    ["Chương 1: Tổng quan về giao nhận hàng hóa", "Chương 2: Giao nhận bằng đường biển", "Câu hỏi hỗn hợp"]
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
        "cau_hoi": "Theo phương thức vận tải, giao nhận KHÔNG bao gồm?",
        "goi_y": [
            "A.Đường biển",
            "B.Đường sắt",
            "C.Đường hàng không",
            "D.Đường vũ trụ"
        ],
        "dap_an_dung": "D"
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
        "cau_hoi": "Landbridge là gì?",
        "goi_y": [
            "A.Cầu hàng không",
            "B.Cầu đất liền",
            "C.Cầu vượt biển",
            "D.Cầu container"
        ],
        "dap_an_dung": "B"
    },
    {
        "cau_hoi": "Cargo Space (CS) là gì?",
        "goi_y": [
            "A.Trọng tải tàu",
            "B.Dung tích chứa hàng của tàu",
            "C.Mớn nước tàu",
            "D.Dung tích đăng ký"
        ],
        "dap_an_dung": "B"
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
        "cau_hoi": "Shipping Instruction được viết tắt là gì?",
        "goi_y": [
            "A.SI",
            "B.CI",
            "C.PI",
            "D.BI"
        ],
        "dap_an_dung": "A"
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
        "cau_hoi": "HBL là viết tắt của cụm từ nào?",
        "goi_y": [
            "A.House Bill of Lading",
            "B.Harbor Bill",
            "C.Heavy Bill",
            "D.Holder Bill"
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