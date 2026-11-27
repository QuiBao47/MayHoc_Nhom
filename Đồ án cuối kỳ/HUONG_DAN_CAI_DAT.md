# Hướng dẫn cài đặt và chạy chương trình

Dự án phân loại khách hàng đăng ký tiền gửi kỳ hạn từ bộ dữ liệu Bank Marketing. Các bước dưới đây dành cho Windows và dùng PowerShell.

## 1. Yêu cầu

- Python 3.10 trở lên.
- Bộ dữ liệu gốc `DATA/raw/bank-additional-full.csv` (đã có trong thư mục dự án).
- Kết nối Internet để cài các thư viện Python.

## 2. Mở thư mục dự án

Mở PowerShell tại thư mục chứa dự án. Nếu đang ở thư mục gốc của repository, chạy:

```powershell
cd ".\Đồ án cuối kỳ"
```

Nếu đã mở PowerShell tại thư mục `Đồ án cuối kỳ`, có thể bỏ qua lệnh trên. Các lệnh tiếp theo cần được chạy từ thư mục này, nơi có các thư mục `DATA`, `notebooks` và `src`.

## 3. Tạo môi trường và cài thư viện

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install pandas numpy "scikit-learn>=1.2" matplotlib seaborn imbalanced-learn jupyter ipykernel
```

Nếu PowerShell chặn kích hoạt môi trường, chỉ cho phép script trong cửa sổ hiện tại rồi kích hoạt lại:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

## 4. Tiền xử lý dữ liệu

Từ thư mục dự án, chạy:

```powershell
python src\preprocessing.py
```

Chương trình đọc `DATA/raw/bank-additional-full.csv`, chia dữ liệu train/test và lưu dữ liệu đã xử lý vào `DATA/processed/`. Bước này có thể chạy lại nếu muốn tạo mới các tệp dữ liệu đã xử lý.

## 5. Chạy notebook

Khởi động JupyterLab từ thư mục dự án:

```powershell
python -m jupyter lab
```

Trong trình duyệt mở ra:

1. Mở `notebooks/02_EDA/notebooks/01_EDA_and_Preprocessing.ipynb` để xem phân tích dữ liệu và tiền xử lý.
2. Mở `notebooks/03_Baseline/Baseline.ipynb` để chạy và so sánh các mô hình cơ sở.
3. Có thể mở các notebook trong `notebooks/Decision_Tree`, `notebooks/KNN`, `notebooks/Logistic_Regression` hoặc `notebooks/Random_Forest` để xem các thí nghiệm tương ứng.

Trong mỗi notebook, chọn kernel Python thuộc môi trường `.venv`, sau đó chạy các cell theo thứ tự từ trên xuống. Các notebook thí nghiệm có thể cần thời gian chạy lâu hơn notebook baseline.

## 6. Kết quả và dữ liệu

- Dữ liệu gốc: `DATA/raw/`.
- Dữ liệu sau tiền xử lý: `DATA/processed/`.
- Kết quả thí nghiệm, biểu đồ và nhật ký: `notebooks/02_EDA/Experiments/Logs/` và `logs/`.

## 7. Khắc phục lỗi thường gặp

- **Không tìm thấy dữ liệu:** kiểm tra tệp `DATA/raw/bank-additional-full.csv` tồn tại và chạy lệnh từ thư mục `Đồ án cuối kỳ`.
- **Thiếu thư viện (`ModuleNotFoundError`):** kích hoạt `.venv` rồi chạy lại lệnh cài thư viện ở bước 3.
- **Notebook dùng sai kernel:** trong Jupyter chọn kernel Python từ thư mục `.venv` của dự án.
- **Lỗi `sparse_output` của scikit-learn:** kiểm tra phiên bản bằng `python -m pip show scikit-learn`; cần phiên bản 1.2 trở lên.

Khi hoàn tất, thoát môi trường ảo bằng:

```powershell
deactivate
```
