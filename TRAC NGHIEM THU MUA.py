import streamlit as st
import os
st.set_page_config(
    page_title="Trắc Nghiệm Thu Mua - Ôn Thi Logistics",
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
st.title("Ôn Luyện Trắc Nghiệm TThu mua")
st.write("""
Chào mừng bạn đến với hệ thống **ôn thi trắc nghiệm logistics** trực tuyến. 
Tại đây tổng hợp các câu hỏi bài tập về **giao nhận hàng hóa quốc tế**, **vận tải đường biển**, 
quy trình xuất nhập khẩu và các nghiệp vụ cảng biển mới nhất giúp bạn ôn tập hiệu quả.
""")
# 2. Tạo thanh menu chọn chương ở bên trái màn hình (Sidebar)
chuong_da_chon = st.sidebar.selectbox(
    "📚 Chọn Chương Ôn Tập:",
    ["Đề 1", "Đề 2", "Đề 3", "Đề 4"]
)
# Hiển thị số lượt truy cập nhỏ ở góc dưới sidebar để bạn theo dõi
st.sidebar.write(f"📊 **Lượt truy cập:** {tong_luot}")
# 3. Thiết lập kho câu hỏi cho từng chương
if chuong_da_chon == "Đề 1":
    cac_cau_hoi = [
    {
        "cau_hoi": "Lợi ích chính của mua hàng theo nhu cầu là?",
        "goi_y": [
        "A. Dễ dàng nhận được hàng hóa chất lượng cao hơn",
        "B. Tiết kiệm chi phí nhờ mua số lượng lớn",
        "C. Được chiết khấu khi mua số lượng lớn",
        "D. Giảm thiểu chi phí lưu kho và tồn kho"
        ],
        "dap_an_dung": "D"
    },
    {
        "cau_hoi": "Mua hàng theo nhu cầu thường gây ra hạn chế nào?",
        "goi_y": [
        "A. Khó điều chỉnh dự báo nhu cầu thị trường",
        "B. Tăng chi phí vận chuyển vì phải đặt hàng nhiều lần",
        "C. Gây áp lực về không gian lưu trữ hàng tồn kho",
        "D. Không tận dụng được mức giá ưu đãi khi mua số lượng lớn"
        ],
        "dap_an_dung": "B"
    },
    {
        "cau_hoi": "Trong sản xuất dược phẩm, loại hàng nào được xếp vào nhóm nguyên liệu tá dược?",
        "goi_y": [
        "A. Tá dược",
        "B. Thành phần hoạt chất",
        "C. Bao bì thuốc",
        "D. Chất ổn định"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Hoạt động thu mua nằm ở phần nào trong chuỗi cung ứng?",
        "goi_y": [
        "A. Cuối chuỗi cung ứng",
        "B. Đầu chuỗi cung ứng",
        "C. Giữa chuỗi cung ứng",
        "D. Sau hoạt động phân phối"
        ],
        "dap_an_dung": "B"
    },
    {
        "cau_hoi": "Lợi ích chính của mua hàng phi tập trung là gì?",
        "goi_y": [
        "A. Tăng cường khả năng đàm phán giá với nhà cung cấp",
        "B. Tăng khả năng đáp ứng nhu cầu cụ thể của từng phòng ban",
        "C. Giảm chi phí nhờ mua hàng với số lượng lớn",
        "D. Giảm rủi ro lưu trữ hàng hóa"
        ],
        "dap_an_dung": "B"
    },
    {
        "cau_hoi": "Những yếu tố nào thường được xem xét khi quyết định mua hàng số lượng lớn?",
        "goi_y": [
        "A. Tất cả các yếu tố trên",
        "B. Khả năng lưu trữ và chi phí lưu kho",
        "C. Mức độ biến động của giá nguyên vật liệu",
        "D. Khả năng dự đoán nhu cầu chính xác"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Một trong những ưu điểm của mua hàng theo lô lớn là?",
        "goi_y": [
        "A. Dễ dàng thích ứng với biến động của thị trường",
        "B. Giảm chi phí vận chuyển nhờ mua hàng thường xuyên",
        "C. Tối ưu hóa không gian lưu kho",
        "D. Giảm chi phí đơn vị khi mua số lượng lớn"
        ],
        "dap_an_dung": "D"
    },
    {
        "cau_hoi": "Lợi ích lớn nhất của mua hàng tập trung là gì?",
        "goi_y": [
        "A. Tăng cường quyền tự chủ của các bộ phận",
        "B. Tận dụng quy mô để đàm phán giá tốt hơn với nhà cung cấp",
        "C. Dễ dàng thích ứng với nhu cầu thay đổi",
        "D. Tăng tính linh hoạt trong mua sắm hàng hóa"
        ],
        "dap_an_dung": "B"
    },
    {
        "cau_hoi": "Mua hàng theo lô lớn thường gây ra tình trạng nào sau đây trong doanh nghiệp?",
        "goi_y": [
        "A. Tăng khả năng linh hoạt khi nhu cầu thay đổi",
        "B. Giảm chi phí vận chuyển nhờ các lô hàng nhỏ",
        "C. Dễ thiếu hụt nguồn cung",
        "D. Giảm khả năng linh hoạt khi nhu cầu thay đổi"
        ],
        "dap_an_dung": "D"
    },
    {
        "cau_hoi": "Mua hàng theo lô lớn thường phù hợp khi?",
        "goi_y": [
        "A. Không gian lưu kho hạn chế",
        "B. Nhu cầu của doanh nghiệp không ổn định",
        "C. Doanh nghiệp muốn giảm chi phí đơn hàng và tận dụng khuyến mãi",
        "D. Doanh nghiệp cần linh hoạt trong việc đặt hàng"
        ],
        "dap_an_dung": "C"
    },
    {
        "cau_hoi": "Vị trí của bộ phận mua hàng trong doanh nghiệp ảnh hưởng trực tiếp đến:",
        "goi_y": [
        "A. Khả năng tiêu thụ sản phẩm trên thị trường",
        "B. Chiến lược marketing và quảng bá sản phẩm",
        "C. Mức độ hài lòng của khách hàng với sản phẩm",
        "D. Chi phí sản xuất và khả năng cạnh tranh giá thành của sản phẩm"
        ],
        "dap_an_dung": "D"
    },
    {
        "cau_hoi": "Hạn chế chính của mua hàng theo lô lớn là?",
        "goi_y": [
        "A. Tăng chi phí tồn kho và lưu trữ",
        "B. Không tận dụng được khuyến mãi từ nhà cung cấp",
        "C. Dễ dẫn đến tình trạng thiếu hụt nguyên vật liệu",
        "D. Tăng chi phí vận chuyển do mua thường xuyên"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Mua hàng theo nhu cầu thường được áp dụng khi?",
        "goi_y": [
        "A. Doanh nghiệp muốn mua nguyên vật liệu với số lượng lớn",
        "B. Doanh nghiệp có nhu cầu không thường xuyên và khó dự đoán",
        "C. Doanh nghiệp muốn tận dụng các chương trình khuyến mãi",
        "D. Doanh nghiệp có nhu cầu ổn định và dự đoán trước được"
        ],
        "dap_an_dung": "B"
    },
    {
        "cau_hoi": "Khó khăn mà doanh nghiệp áp dụng mua hàng tập trung thường gặp là?",
        "goi_y": [
        "A. Tăng chi phí vận chuyển",
        "B. Đàm phán giá với nhà cung cấp",
        "C. Tăng khả năng dự trữ hàng tồn kho",
        "D. Điều phối nguồn hàng giữa các bộ phận"
        ],
        "dap_an_dung": "D"
    },
    {
        "cau_hoi": "Khi thu mua nguyên vật liệu sản xuất, doanh nghiệp cần ưu tiên yếu tố nào?",
        "goi_y": [
        "A. Thời gian giao hàng nhanh nhất",
        "B. Chất lượng tốt nhất",
        "C. Giá cả thấp nhất",
        "D. Sự kết hợp giữa chất lượng, giá cả và thời gian giao hàng"
        ],
        "dap_an_dung": "D"
    },
    {
        "cau_hoi": "Chức năng nào sau đây không thuộc trách nhiệm của bộ phận thu mua trong doanh nghiệp?",
        "goi_y": [
        "A. Kiểm tra và giám sát chất lượng hàng hóa",
        "B. Đánh giá và lựa chọn nhà cung cấp chiến lược",
        "C. Tìm kiếm nhà cung cấp và đàm phán giá",
        "D. Phân phối sản phẩm đến tay khách hàng"
        ],
        "dap_an_dung": "D"
    },
    {
        "cau_hoi": "Bộ phận mua hàng thường làm việc chặt chẽ với bộ phận nào trong doanh nghiệp?",
        "goi_y": [
        "A. Bộ phận bán hàng",
        "B. Bộ phận kế toán",
        "C. Bộ phận marketing",
        "D. Bộ phận sản xuất và kho vận"
        ],
        "dap_an_dung": "D"
    },
    {
        "cau_hoi": "Doanh nghiệp nào dưới đây thường áp dụng mua hàng theo nhu cầu?",
        "goi_y": [
        "A. Tập đoàn sản xuất xe hơi",
        "B. Nhà máy sản xuất lớn với nhu cầu nguyên liệu đều đặn",
        "C. Doanh nghiệp nhỏ với nhu cầu thay đổi liên tục",
        "D. Công ty dệt may có kế hoạch sản xuất dài hạn"
        ],
        "dap_an_dung": "C"
    },
    {
        "cau_hoi": "Mua hàng theo lô lớn thường phù hợp với?",
        "goi_y": [
        "A. Doanh nghiệp lớn có kế hoạch sản xuất dài hạn",
        "B. Các cửa hàng bán lẻ nhỏ",
        "C. Doanh nghiệp nhỏ với nhu cầu không ổn định",
        "D. Các doanh nghiệp sản xuất theo đơn đặt hàng ngắn hạn"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Những yếu tố nào thường được xem xét khi doanh nghiệp lựa chọn mua hàng phi tập trung?",
        "goi_y": [
        "A. Khả năng dự trữ và quản lý hàng tồn kho",
        "B. Tất cả các yếu tố trên",
        "C. Tính linh hoạt trong việc mua sắm",
        "D. Khả năng đàm phán với nhà cung cấp"
        ],
        "dap_an_dung": "C"
    }
    ]
     
elif chuong_da_chon == "Đề 2":
    cac_cau_hoi =[  
    {
        "cau_hoi": "Bước đầu tiên trong quy trình xác định yêu cầu mua hàng là gì?",
        "goi_y": [
        "A. Lập kế hoạch ngân sách",
        "B. Đàm phán với nhà cung cấp",
        "C. Phân tích thị trường",
        "D. Xác định nhu cầu sử dụng hàng hóa hoặc dịch vụ"
        ],
        "dap_an_dung": "D"
    },
    {
        "cau_hoi": "Mục đích của việc kiểm tra và phê duyệt đơn đặt hàng là gì?",
        "goi_y": [
        "A. Để đảm bảo đơn hàng tuân thủ chính sách công ty",
        "B. Để kiểm tra tình trạng tồn kho",
        "C. Để lập hóa đơn cho khách hàng",
        "D. Để chọn nhà cung cấp phù hợp"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Nếu hàng hóa không đạt tiêu chuẩn chất lượng, bộ phận tiếp nhận nên làm gì?",
        "goi_y": [
        "A. Lưu trữ hàng hóa vào kho",
        "B. Thanh toán cho nhà cung cấp",
        "C. Thông báo cho bộ phận mua hàng và nhà cung cấp",
        "D. Vận chuyển hàng hóa đến khách hàng"
        ],
        "dap_an_dung": "C"
    },
    {
        "cau_hoi": "Khi tiếp nhận hàng hóa, việc kiểm tra số lượng và chất lượng thường được tiến hành vào lúc nào?",
        "goi_y": [
        "A. Khi hàng hóa đã lưu trữ trong kho",
        "B. Trước khi đơn hàng được phát",
        "C. Ngay khi hàng hóa đến từ nhà cung cấp",
        "D. Sau khi sản phẩm được bán ra thị trường"
        ],
        "dap_an_dung": "C"
    },
    {
        "cau_hoi": "Tại sao việc kiểm tra chất lượng hàng hóa ngay khi tiếp nhận lại quan trọng?",
        "goi_y": [
        "A. Để đảm bảo hàng hóa đáp ứng yêu cầu trước khi lưu trữ hoặc sử dụng",
        "B. Để tiết kiệm chi phí nhân công",
        "C. Để giảm chi phí vận chuyển",
        "D. Để tránh mất mát hàng hóa khi lưu kho"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Hóa đơn mua bán hàng hóa là gì?",
        "goi_y": [
        "A. Tài liệu xác nhận việc giao hàng",
        "B. Tài liệu ghi nhận khoản nợ của khách hàng",
        "C. Tài liệu ghi nhận giao dịch mua bán hàng hóa giữa người bán và người mua",
        "D. Tài liệu báo cáo tài chính"
        ],
        "dap_an_dung": "C"
    },
    {
        "cau_hoi": "Ai thường chịu trách nhiệm kiểm tra hàng hóa khi tiếp nhận?",
        "goi_y": [
        "A. Bộ phận bảo trì",
        "B. Bộ phận kế toán",
        "C. Bộ phận kho hoặc kiểm soát chất lượng (KCS)",
        "D. Bộ phận marketing"
        ],
        "dap_an_dung": "C"
    },
    {
        "cau_hoi": "Trong quy trình đặt hàng, bước nào đảm bảo rằng hàng hóa hoặc dịch vụ được đặt mua là cần thiết và hợp lệ?",
        "goi_y": [
        "A. Kiểm tra chất lượng hàng hóa",
        "B. Lập hóa đơn",
        "C. Phê duyệt đơn đặt hàng",
        "D. Nhận hàng"
        ],
        "dap_an_dung": "C"
    },
    {
        "cau_hoi": "Yếu tố nào dưới đây không phải là yếu tố cần xem xét khi lựa chọn nhà cung cấp?",
        "goi_y": [
        "A. Số lượng nhân viên của nhà cung cấp",
        "B. Giá cả",
        "C. Khả năng giao hàng đúng hạn",
        "D. Chất lượng sản phẩm"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Điều nào sau đây giúp đo lường hiệu quả của mối quan hệ với nhà cung cấp?",
        "goi_y": [
        "A. Số lượng nhà cung cấp chiến lược và hợp đồng lâu dài",
        "B. Tỷ lệ hàng tồn kho cao",
        "C. Thời gian giao hàng trung bình",
        "D. Tỷ lệ đơn hàng bị trả lại"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Thông tin nào không cần thiết phải cập nhật thường xuyên trong quy trình xác định yêu cầu mua hàng?",
        "goi_y": [
        "A. Danh sách nhân viên trong bộ phận mua hàng",
        "B. Danh sách các nhà cung cấp",
        "C. Giá cả hàng hóa trên thị trường",
        "D. Tình trạng tồn kho"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Tại sao việc xác định yêu cầu mua hàng chính xác lại quan trọng?",
        "goi_y": [
        "A. Để đảm bảo hoạt động sản xuất diễn ra suôn sẻ",
        "B. Để tránh tồn kho quá mức",
        "C. Để giảm thiểu chi phí",
        "D. Tất cả các phương án trên"
        ],
        "dap_an_dung": "D"
    },
    {
        "cau_hoi": "Hóa đơn VAT (Value Added Tax) là gì?",
        "goi_y": [
        "A. Hóa đơn chỉ sử dụng cho hàng hóa xuất khẩu",
        "B. Hóa đơn ghi nhận giá trị hàng hóa đã bao gồm thuế",
        "C. Hóa đơn ghi nhận giá trị hàng hóa không bao gồm thuế",
        "D. Hóa đơn được cấp cho khách hàng nước ngoài"
        ],
        "dap_an_dung": "B"
    },
    {
        "cau_hoi": "Bước đầu tiên trong quy trình tiếp nhận hàng hóa là gì?",
        "goi_y": [
        "A. Tiếp nhận đơn đặt hàng từ nhà cung cấp",
        "B. Xử lý khiếu nại về hàng hóa",
        "C. Kiểm tra chất lượng hàng hóa",
        "D. Lưu trữ hàng hóa vào kho"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Đo lường hiệu suất mua hàng liên quan đến việc tuân thủ quy định và pháp luật bao gồm chỉ số nào?",
        "goi_y": [
        "A. Số lượng sai phạm pháp lý liên quan đến hoạt động mua hàng",
        "B. Thời gian xử lý đơn hàng",
        "C. Chi phí vận chuyển trung bình",
        "D. Số lượng nhà cung cấp chiến lược"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Thông thường, yêu cầu mua hàng có thể được phát sinh từ đâu?",
        "goi_y": [
        "A. Chỉ từ bộ phận mua hàng",
        "B. Chỉ từ bộ phận marketing",
        "C. Bộ phận sản xuất và bộ phận kho",
        "D. Bộ phận kế toán và bộ phận nhân sự"
        ],
        "dap_an_dung": "C"
    },
    {
        "cau_hoi": "Tỷ lệ đơn hàng bị trả lại do chất lượng kém phản ánh yếu tố nào của hiệu suất mua hàng?",
        "goi_y": [
        "A. Quản lý tồn kho",
        "B. Chất lượng sản phẩm và dịch vụ",
        "C. Tốc độ xử lý đơn hàng",
        "D. Khả năng tuân thủ ngân sách"
        ],
        "dap_an_dung": "B"
    },
    {
        "cau_hoi": "Ai thường chịu trách nhiệm lập đơn đặt hàng trong tổ chức?",
        "goi_y": [
        "A. Bộ phận sản xuất",
        "B. Bộ phận mua hàng",
        "C. Bộ phận nhân sự",
        "D. Bộ phận kế toán"
        ],
        "dap_an_dung": "B"
    },
    {
        "cau_hoi": "Khi xác định yêu cầu mua hàng, thông tin nào sau đây là cần thiết?",
        "goi_y": [
        "A. Tất cả các phương án trên",
        "B. Thời gian cần thiết để nhận hàng",
        "C. Số lượng hàng hóa cần mua",
        "D. Mô tả chi tiết về hàng hóa hoặc dịch vụ cần mua"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Tài liệu nào thường được sử dụng để xác nhận việc giao hàng từ nhà cung cấp?",
        "goi_y": [
        "A. Hóa đơn thanh toán",
        "B. Báo giá",
        "C. Phiếu giao hàng",
        "D. Đơn đặt hàng"
        ],
        "dap_an_dung": "C"
    }
    ]
elif chuong_da_chon == "Đề 3":
    cac_cau_hoi =[  
    {
        "cau_hoi": "Doanh nghiệp bạn đang chi nhiều ngân sách cho các tấm thép dùng để sản xuất, và có nhiều nhà cung cấp cạnh tranh. Đâu là chiến lược phù hợp nhất?",
        "goi_y": [
        "A. Lập kế hoạch dự phòng thay thế",
        "B. Tự động hóa hệ thống mua hàng",
        "C. Tập trung vào kiểm tra chất lượng",
        "D. Đàm phán giảm giá và đa dạng nguồn"
        ],
        "dap_an_dung": "D"
    },
    {
        "cau_hoi": "Chiến lược phù hợp với nhóm Bottleneck là gì?",
        "goi_y": [
        "A. Đơn giản hóa hợp đồng",
        "B. Chuyển thành sản phẩm Routine",
        "C. Dự trữ hàng tồn kho cao và duy trì quan hệ nhà cung cấp",
        "D. Tập trung vào đàm phán giá"
        ],
        "dap_an_dung": "C"
    },
    {
        "cau_hoi": "Một mặt hàng nguyên liệu A vừa có giá trị cao vừa khó thay thế. Lựa chọn hành động đúng là:",
        "goi_y": [
        "A. Đặt hàng theo nhu cầu",
        "B. Phát triển thêm nhà cung cấp thay thế",
        "C. Đàm phán giá",
        "D. Tăng tồn kho"
        ],
        "dap_an_dung": "B"
    },
    {
        "cau_hoi": "Một công ty dự định sử dụng chatbot tự động để xử lý mua văn phòng phẩm. Đây là ứng dụng hiệu quả cho nhóm:",
        "goi_y": [
        "A. Strategic",
        "B. Routine",
        "C. Bottleneck",
        "D. Leverage"
        ],
        "dap_an_dung": "B"
    },
    {
        "cau_hoi": "Mục tiêu chính của mô hình định vị nhà cung cấp là gì?",
        "goi_y": [
        "A. Lập kế hoạch mua nguyên vật liệu",
        "B. Tối ưu chi phí và giảm rủi ro cung ứng",
        "C. Giám sát chất lượng sản phẩm đầu ra",
        "D. Phân tích dòng tiền"
        ],
        "dap_an_dung": "B"
    },
    {
        "cau_hoi": "Theo mô hình, nhóm nào thường chiếm 20% mặt hàng nhưng 80% chi tiêu?",
        "goi_y": [
        "A. Bottleneck",
        "B. Routine",
        "C. Strategic",
        "D. Leverage"
        ],
        "dap_an_dung": "D"
    },
    {
        "cau_hoi": "Một nhà bán lẻ muốn tối ưu việc mua giấy vệ sinh, khăn lau và nước rửa tay. Hành động đúng là:",
        "goi_y": [
        "A. Giao hàng theo nhu cầu thực tế",
        "B. Kiểm tra chất lượng từng lô hàng",
        "C. Dùng phần mềm tự động đặt hàng",
        "D. Lập hợp đồng khung dài hạn"
        ],
        "dap_an_dung": "C"
    },
    {
        "cau_hoi": "Một công ty sản xuất xe máy phát hiện ra bộ lọc dầu chỉ có một nhà cung cấp. Bộ lọc không đắt nhưng nếu thiếu thì cả dây chuyền sản xuất phải dừng. Nhóm phù hợp nhất là:",
        "goi_y": [
        "A. Strategic",
        "B. Bottleneck",
        "C. Leverage",
        "D. Routine"
        ],
        "dap_an_dung": "B"
    },
    {
        "cau_hoi": "Nếu sản phẩm Leverage bị lạm dụng độc quyền, điều đó thể hiện gì?",
        "goi_y": [
        "A. Thiếu năng lực thương lượng",
        "B. Quản trị kém, phân loại sai nhóm",
        "C. Nhà cung cấp không uy tín",
        "D. Doanh nghiệp mua sai sản phẩm"
        ],
        "dap_an_dung": "B"
    },
    {
        "cau_hoi": "Nếu không quản lý tốt nhóm Leverage, hậu quả có thể là:",
        "goi_y": [
        "A. Dư thừa hàng tồn",
        "B. Tăng chi phí kiểm kê",
        "C. Lợi nhuận giảm",
        "D. Tăng chi phí mua hàng và mất cơ hội đàm phán"
        ],
        "dap_an_dung": "D"
    },
    {
        "cau_hoi": "Bạn đang bị ép giá bởi một nhà cung cấp duy nhất cung cấp thiết bị độc quyền. Mô hình nào phản ánh đúng nhất tình huống này?",
        "goi_y": [
        "A. Strategic",
        "B. Leverage",
        "C. Routine",
        "D. Bottleneck"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Một nhà máy điện gió có 3 nhà cung cấp trụ turbine, mỗi bên chiếm thị phần tương đương, giá trị cao và rủi ro cao. Hướng quản lý là:",
        "goi_y": [
        "A. Chuyển toàn bộ sang nhập khẩu",
        "B. Đa dạng hóa và giám sát chặt",
        "C. Tập trung mua một nhà cung cấp",
        "D. Lựa chọn sản phẩm thay thế rẻ hơn"
        ],
        "dap_an_dung": "B"
    },
    {
        "cau_hoi": "Trong nhóm Bottleneck, yếu tố nào có thể làm tăng chi phí sản phẩm có giá trị thấp?",
        "goi_y": [
        "A. Số lượng mua nhiều",
        "B. Phí lưu kho cao",
        "C. Độc quyền cung ứng",
        "D. Đòn bẩy thị trường"
        ],
        "dap_an_dung": "C"
    },
    {
        "cau_hoi": "Một sản phẩm đang từ nhóm Strategic được chuyển sang Leverage là biểu hiện của:",
        "goi_y": [
        "A. Thành công trong kiểm soát nguồn và giá trị",
        "B. Sự thất bại trong cung ứng",
        "C. Chiến lược hợp đồng sai lầm",
        "D. Rủi ro tăng cao"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Nhóm sản phẩm nào có thể tận dụng sức mạnh mua sắm để đàm phán giá?",
        "goi_y": [
        "A. Bottleneck",
        "B. Leverage",
        "C. Strategic",
        "D. Routine"
        ],
        "dap_an_dung": "B"
    },
    {
        "cau_hoi": "Đâu là một đặc điểm của nhóm Routine?",
        "goi_y": [
        "A. Không nên mất nhiều thời gian quản lý",
        "B. Dễ bị gián đoạn nguồn cung",
        "C. Tác động lớn đến lợi nhuận",
        "D. Đòi hỏi đàm phán giá chi tiết"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Bạn phát hiện nhà cung cấp sản phẩm chiến lược không giao hàng đúng tiến độ nhiều lần. Biện pháp ưu tiên là:",
        "goi_y": [
        "A. Đàm phán tăng giá",
        "B. Cắt hợp đồng ngay",
        "C. Thiết lập nhà cung cấp thay thế",
        "D. Chuyển toàn bộ mua trong nước"
        ],
        "dap_an_dung": "C"
    },
    {
        "cau_hoi": "Bạn đang quản lý danh mục gồm 500 mặt hàng. 400 trong số đó là văn phòng phẩm, giá trị thấp. Chiến lược hiệu quả là:",
        "goi_y": [
        "A. Thiết lập nhà cung cấp chiến lược",
        "B. Kiểm tra chất lượng nghiêm ngặt",
        "C. Mua số lượng lớn để giảm giá",
        "D. Tự động hóa mua sắm"
        ],
        "dap_an_dung": "D"
    },
    {
        "cau_hoi": "Khi đánh giá một nhóm sản phẩm có giá trị cao, dễ thay thế nhà cung cấp, bạn nên:",
        "goi_y": [
        "A. Tăng lượng tồn kho",
        "B. Tránh thay đổi nhà cung cấp",
        "C. Đàm phán giá mạnh",
        "D. Giảm tần suất đặt hàng"
        ],
        "dap_an_dung": "C"
    },
    {
        "cau_hoi": "Trong doanh nghiệp, nhóm sản phẩm nào nên được giám sát chất lượng và hiệu suất nhà cung cấp thường xuyên nhất?",
        "goi_y": [
        "A. Routine",
        "B. Strategic",
        "C. Leverage",
        "D. Bottleneck"
        ],
        "dap_an_dung": "B"
    },
    {
        "cau_hoi": "Trong nhóm Strategic, yếu tố nào cần đặc biệt quan tâm?",
        "goi_y": [
        "A. Tập trung đàm phán giá",
        "B. Lập kế hoạch thay thế và đối tác chiến lược",
        "C. Đơn giản hóa hợp đồng",
        "D. Tăng số lượng mua vào"
        ],
        "dap_an_dung": "B"
    },
    {
        "cau_hoi": "Một công ty công nghệ cao cần chip điện tử đặc biệt mà chỉ có một nhà sản xuất toàn cầu. Đây là sản phẩm:",
        "goi_y": [
        "A. Bottleneck",
        "B. Strategic",
        "C. Routine",
        "D. Leverage"
        ],
        "dap_an_dung": "B"
    },
    {
        "cau_hoi": "Mặt hàng nào sau đây KHÔNG nên đưa vào nhóm Bottleneck?",
        "goi_y": [
        "A. Linh kiện sản xuất đặc chủng",
        "B. Bu lông inox đại trà",
        "C. Bộ vi xử lý của hãng duy nhất",
        "D. Phần mềm độc quyền"
        ],
        "dap_an_dung": "B"
    },
    {
        "cau_hoi": "Trong mô hình định vị nguồn cung, trục ngang đại diện cho yếu tố nào?",
        "goi_y": [
        "A. Tổng chi phí hoặc giá trị chi tiêu",
        "B. Rủi ro cung ứng",
        "C. Giá trị chiến lược",
        "D. Khả năng thay thế nhà cung cấp"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Bạn phụ trách thu mua vật tư bảo hộ (mũ, áo phản quang). Để tiết kiệm chi phí, bạn nên:",
        "goi_y": [
        "A. Đàm phán hợp đồng dài hạn",
        "B. Xây dựng quan hệ chiến lược",
        "C. Phân tích kỹ nhu cầu sử dụng",
        "D. Tự động hóa đặt hàng định kỳ"
        ],
        "dap_an_dung": "D"
    },
    {
        "cau_hoi": "Đặc điểm của nhóm Bottleneck là:",
        "goi_y": [
        "A. Khó thay thế, rủi ro cao",
        "B. Giá trị thấp, rủi ro thấp",
        "C. Tác động lợi nhuận cao, rủi ro thấp",
        "D. Dễ thay thế, giá trị cao"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Nguy cơ chính khi chỉ có một nhà cung cấp trong nhóm Strategic là:",
        "goi_y": [
        "A. Mất tính ổn định cung ứng",
        "B. Khó kiểm soát chất lượng",
        "C. Khó xác định nhu cầu",
        "D. Tăng chi phí lưu kho"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Một công ty logistic cần giấy in cho bộ phận hành chính. Biện pháp hiệu quả nhất là:",
        "goi_y": [
        "A. Giữ tồn kho cao",
        "B. Tìm nhà cung cấp chiến lược",
        "C. Kiểm tra chất lượng giấy kỹ",
        "D. Thiết lập hệ thống đặt hàng định kỳ"
        ],
        "dap_an_dung": "D"
    },
    {
        "cau_hoi": "Trong tình huống giá vật tư chính yếu tăng mạnh, bạn đang áp dụng mô hình định vị. Việc đầu tiên cần làm là:",
        "goi_y": [
        "A. Chuyển nhà cung cấp ngay",
        "B. Phân loại lại theo giá trị và rủi ro",
        "C. Dừng mua hàng",
        "D. Tăng tồn kho khẩn cấp"
        ],
        "dap_an_dung": "B"
    },
    {
        "cau_hoi": "Nhóm sản phẩm nào có chi phí thấp và rủi ro cung ứng thấp?",
        "goi_y": [
        "A. Bottleneck",
        "B. Strategic",
        "C. Routine",
        "D. Leverage"
        ],
        "dap_an_dung": "C"
    }
    ]
elif chuong_da_chon == "Đề 3":
    cac_cau_hoi =[  
    {
        "cau_hoi": "Check Sheet ghi nhận lỗi bao bì tăng liên tục. Hành động đúng là:",
        "goi_y": [
        "A. Tăng tần suất kiểm tra kho",
        "B. Giảm số lượng đặt hàng",
        "C. Ngưng nhập hàng trong 1 tháng",
        "D. Yêu cầu nhà cung cấp cải tiến đóng gói"
        ],
        "dap_an_dung": "D"
    },
    {
        "cau_hoi": "Công ty bạn muốn chuyển yêu cầu từ khách hàng thành kỹ thuật đặt hàng đầu vào. Nên dùng công cụ nào?",
        "goi_y": [
        "A. QFD",
        "B. Check Sheet",
        "C. Scatter",
        "D. Flowchart"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Trong biểu đồ Pareto có 5 lỗi, lỗi C chiếm 45%, lỗi B 25%, bạn nên:",
        "goi_y": [
        "A. Không làm gì cả",
        "B. Xử lý lỗi A trước vì có thứ tự đầu bảng",
        "C. Xử lý lỗi E vì dễ làm",
        "D. Tập trung xử lý lỗi C và B"
        ],
        "dap_an_dung": "D"
    },
    {
        "cau_hoi": "Nếu bạn đang xây dựng biểu đồ Pareto, bước đầu tiên nên làm gì?",
        "goi_y": [
        "A. Tạo bảng phân loại lỗi",
        "B. Thu thập dữ liệu lỗi",
        "C. Loại nhà cung cấp yếu",
        "D. Ký hợp đồng mới"
        ],
        "dap_an_dung": "B"
    },
    {
        "cau_hoi": "Sau khi phân tích, bạn thấy nhà cung cấp A có xu hướng giao trễ và tỷ lệ lỗi cao. Biện pháp phù hợp nhất là:",
        "goi_y": [
        "A. Giữ nguyên vì có lịch sử hợp tác lâu dài",
        "B. Bỏ qua vì chưa ảnh hưởng đến sản xuất",
        "C. Tăng giá mua từ nhà cung cấp A",
        "D. Giảm đơn hàng từ nhà cung cấp A"
        ],
        "dap_an_dung": "D"
    },
    {
        "cau_hoi": "Trong giai đoạn Define của DMAIC, công cụ QFD được sử dụng nhằm:",
        "goi_y": [
        "A. Kiểm soát tiến độ giao hàng",
        "B. Xây dựng biểu đồ Pareto",
        "C. Phân tích nguyên nhân gốc rễ",
        "D. Chuyển đổi nhu cầu khách hàng thành yêu cầu kỹ thuật"
        ],
        "dap_an_dung": "D"
    },
    {
        "cau_hoi": "Bạn cần thuyết phục lãnh đạo đầu tư hệ thống ERP cho thu mua. Bạn nên dẫn chứng từ bước nào trong DMAIC?",
        "goi_y": [
        "A. Measure và Analyze",
        "B. Improve và Measure",
        "C. Control và Define",
        "D. Define và Control"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Nếu Flowchart cho thấy thời gian xét duyệt PR lâu nhất, hành động ưu tiên là:",
        "goi_y": [
        "A. Cải tiến quy trình duyệt PR",
        "B. Đào tạo lại kế toán",
        "C. Tăng số lượng đơn hàng",
        "D. Cắt giảm nhà cung cấp"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Công cụ Flowchart trong thu mua giúp:",
        "goi_y": [
        "A. Mua hàng hóa giá rẻ hơn",
        "B. Tăng lợi nhuận trực tiếp",
        "C. Giảm chi phí vận tải",
        "D. Chuẩn hóa và tối ưu quy trình"
        ],
        "dap_an_dung": "D"
    },
    {
        "cau_hoi": "Bạn muốn kiểm tra độ ổn định của chất lượng hàng hóa theo thời gian. Biểu đồ phù hợp là:",
        "goi_y": [
        "A. Biểu đồ kiểm soát (Control Chart)",
        "B. Histogram",
        "C. Check Sheet",
        "D. Flowchart"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Một biểu đồ Scatter có dạng nghiêng hướng lên từ trái sang phải thể hiện gì?",
        "goi_y": [
        "A. Tương quan dương",
        "B. Tương quan âm",
        "C. Tương quan không rõ rệt",
        "D. Không có liên hệ"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Trong kiểm tra đầu vào, Check Sheet không dùng để:",
        "goi_y": [
        "A. Phân loại lỗi",
        "B. Ghi nhận dữ liệu lỗi",
        "C. Theo dõi xu hướng lỗi",
        "D. Kiểm tra tương quan giữa 2 yếu tố"
        ],
        "dap_an_dung": "D"
    },
    {
        "cau_hoi": "Khi cần đánh giá hiệu suất nhiều nhà cung cấp về đúng hạn và chất lượng, bạn nên dùng:",
        "goi_y": [
        "A. Check Sheet",
        "B. Scatter Diagram",
        "C. QFD",
        "D. Supplier Scorecard"
        ],
        "dap_an_dung": "D"
    },
    {
        "cau_hoi": "Phân tích Pareto tuân theo nguyên tắc nào?",
        "goi_y": [
        "A. 80/20",
        "B. 70/30",
        "C. 90/10",
        "D. 60/40"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Trong quá trình triển khai cải tiến DMAIC, bạn muốn tự động hóa bước duyệt đơn hàng. Đây là thuộc giai đoạn nào?",
        "goi_y": [
        "A. Define",
        "B. Measure",
        "C. Analyze",
        "D. Improve"
        ],
        "dap_an_dung": "D"
    },
    {
        "cau_hoi": "Dữ liệu lỗi theo biểu đồ Pareto cho thấy lỗi C chiếm 60%, lỗi B 20%. Hành động phù hợp là:",
        "goi_y": [
        "A. Ưu tiên xử lý lỗi C và B",
        "B. Không hành động",
        "C. Xử lý lỗi A trước",
        "D. Tập trung vào lỗi D"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Công cụ nào thường được dùng để phân tích mối tương quan giữa 2 biến trong thu mua?",
        "goi_y": [
        "A. Pareto",
        "B. Check Sheet",
        "C. Histogram",
        "D. Scatter Diagram"
        ],
        "dap_an_dung": "D"
    },
    {
        "cau_hoi": "Giai đoạn nào trong DMAIC đề xuất các giải pháp cải tiến?",
        "goi_y": [
        "A. Improve",
        "B. Measure",
        "C. Analyze",
        "D. Control"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Trong buổi họp đánh giá nhà cung cấp, dữ liệu Check Sheet có thể giúp:",
        "goi_y": [
        "A. So sánh giá thị trường",
        "B. Tăng đơn hàng ngay lập tức",
        "C. Phát hiện lỗi định kỳ để cải tiến",
        "D. Phân tích xu hướng tiêu dùng"
        ],
        "dap_an_dung": "C"
    },
    {
        "cau_hoi": "Mục tiêu của biểu đồ Histogram là:",
        "goi_y": [
        "A. Đánh giá mức độ hợp tác của nhà cung cấp",
        "B. Tính toán chi phí vận chuyển",
        "C. So sánh giá từ nhiều nhà cung cấp",
        "D. Hiển thị tần suất và xu hướng dữ liệu"
        ],
        "dap_an_dung": "D"
    },
    {
        "cau_hoi": "Giai đoạn nào trong chu trình DMAIC tập trung vào đo lường hiệu suất?",
        "goi_y": [
        "A. Measure",
        "B. Analyze",
        "C. Define",
        "D. Control"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Nếu Check Sheet ghi nhận lỗi loại C xuất hiện liên tục trong 4 ngày liên tiếp, bạn nên:",
        "goi_y": [
        "A. Bỏ qua vì là lỗi nhẹ",
        "B. Ưu tiên xử lý lỗi C trước",
        "C. Thay đổi người mua hàng",
        "D. Gỡ bỏ nhà cung cấp"
        ],
        "dap_an_dung": "B"
    },
    {
        "cau_hoi": "Khi đánh giá sai lệch kích thước hàng hóa qua nhiều lô, biểu đồ nào sẽ giúp xác định phân bố?",
        "goi_y": [
        "A. Pareto",
        "B. Scatter",
        "C. Check Sheet",
        "D. Histogram"
        ],
        "dap_an_dung": "D"
    },
    {
        "cau_hoi": "Bạn nhận thấy Flowchart thu mua có 9 bước nhưng một bước chiếm tới 40% thời gian. Biện pháp cải tiến là:",
        "goi_y": [
        "A. Tự động hóa bước đó nếu có thể",
        "B. Giao cho phòng ban khác",
        "C. Chia nhỏ thành các bước con",
        "D. Bỏ qua bước đó"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Biểu đồ Histogram cho thấy phần lớn dữ liệu tập trung vào nhóm C, một số nhỏ ở nhóm A và E.",
        "goi_y": [
        "A. Nhà cung cấp có sai số cực lớn",
        "B. Lỗi xảy ra ngẫu nhiên",
        "C. Không thể đánh giá",
        "D. Dữ liệu có phân phối chuẩn hoặc gần chuẩn"
        ],
        "dap_an_dung": "D"
    },
    {
        "cau_hoi": "Trong phân tích Six Sigma, 'gốc rễ của vấn đề' được xác định ở giai đoạn nào?",
        "goi_y": [
        "A. Improve (Cải thiện)",
        "B. Measure (Đo lường)",
        "C. Control (Kiểm soát)",
        "D. Analyze (Phân tích)"
        ],
        "dap_an_dung": "D"
    },
    {
        "cau_hoi": "Sau khi thu thập dữ liệu lỗi đầu vào, công ty muốn xác định lỗi nào xuất hiện nhiều nhất để ưu tiên cải tiến. Nên dùng công cụ nào?",
        "goi_y": [
        "A. Check Sheet",
        "B. Pareto",
        "C. Scatter",
        "D. QFD"
        ],
        "dap_an_dung": "B"
    },
    {
        "cau_hoi": "Mục tiêu chính của phương pháp Six Sigma trong quản lý thu mua là gì?",
        "goi_y": [
        "A. Giảm biến động và sai sót trong quy trình",
        "B. Mở rộng thị trường đầu vào",
        "C. Tăng số lượng nhà cung cấp",
        "D. Tăng doanh số bán hàng"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Một doanh nghiệp phát hiện rằng thời gian giao hàng tăng dần đến số lỗi tăng. Biểu đồ thể hiện tốt nhất mối liên hệ này là:",
        "goi_y": [
        "A. Scatter Diagram (Biểu đồ phân tán)",
        "B. Check Sheet (Phiếu kiểm tra)",
        "C. Pareto",
        "D. Flowchart (Lưu đồ)"
        ],
        "dap_an_dung": "A"
    },
    {
        "cau_hoi": "Một công ty ghi nhận rằng cứ khi đơn hàng giao trễ trên 5 ngày, tỷ lệ lỗi sản phẩm tăng. Biểu đồ nào phù hợp để kiểm tra mối liên hệ này?",
        "goi_y": [
        "A. Scatter Diagram",
        "B. Histogram",
        "C. Flowchart",
        "D. Pareto"
        ],
        "dap_an_dung": "A"
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