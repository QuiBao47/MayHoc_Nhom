# 🏦 Bank Marketing — Dự Báo Đăng Ký Tiền Gửi Kỳ Hạn

## Mô tả
Dự đoán khách hàng có đăng ký tiền gửi kỳ hạn sau chiến dịch marketing qua điện thoại hay không.

- **Dataset**: UCI Bank Marketing (41,188 mẫu, 20 features)
- **Bài toán**: Phân loại nhị phân (Binary Classification)
- **Model tốt nhất**: Random Forest Tuned — F1=0.522, ROC-AUC=0.812

## Cấu Trúc Dự Án
`
Đồ án cuối kỳ/
├── DATA/
│   ├── features/keep.txt       # Danh sách features
│   ├── figures/                # Biểu đồ EDA
│   ├── processed/              # Dữ liệu đã xử lý
│   └── raw/                    # Dữ liệu gốc
├── logs/                       # Nhật ký toàn dự án
├── notebooks/
│   ├── 02_EDA/                 # EDA + Experiments/Logs/
│   ├── 03_Baseline/            # Notebook tổng hợp + experiment_log.md
│   ├── Decision_Tree/
│   ├── KNN/
│   ├── Logistic_Regression/
│   ├── Random_Forest/
│   └── Train_Validation_Test/  # Thông tin về data split
└── src/
    ├── config.py               # Cấu hình đường dẫn
    ├── preprocessing.py        # Pipeline tiền xử lý
    └── evaluation.py           # Module đánh giá
`

## Cách Chạy

### Tiền xử lý dữ liệu
`ash
cd "Đồ án cuối kỳ"
python src/preprocessing.py
`

### Chạy notebook
Mở 
otebooks/03_Baseline/Baseline.ipynb trong Jupyter.

## Thành Viên Nhóm
| Thành viên | Phụ trách |
|---|---|
| Nguyễn Hoàng Anh | Logistic Regression (EXP-01) |
| Tía Quang Minh | KNN (EXP-02, EXP-06) |
| Phát | Decision Tree (EXP-03) |
| Huỳnh Quí Bảo | Random Forest (EXP-04, EXP-08, EXP-12, EXP-16) |

## Kết Quả
Xem chi tiết tại [
otebooks/03_Baseline/experiment_log.md](notebooks/03_Baseline/experiment_log.md)
