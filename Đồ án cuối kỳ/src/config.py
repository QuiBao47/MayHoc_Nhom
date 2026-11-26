# File: src/config.py
from pathlib import Path

# Tự động lấy đường dẫn thư mục gốc của dự án ("Đồ án cuối kỳ")
ROOT_DIR = Path(__file__).resolve().parent.parent

# Đường dẫn dữ liệu
RAW_DATA_PATH = ROOT_DIR / "DATA" / "raw" / "bank-additional-full.csv"
PROCESSED_DATA_DIR = ROOT_DIR / "DATA" / "processed"
RESULTS_DIR = ROOT_DIR / "notebooks" / "02_EDA" / "Experiments" / "Logs"
EXPERIMENTS_DIR = RESULTS_DIR  # alias để tương thích với evaluation.py

# Tham số chia dữ liệu và huấn luyện cố định cho cả nhóm
RANDOM_STATE = 42
TEST_SIZE = 0.2
N_FOLDS = 3  # Có thể đổi thành 5 khi chạy bản chốt cuối cùng

# Cấu hình cột đặc trưng
TARGET_COL = "y"
DROP_COLS = ["y", "duration"]  # Loại duration để tránh data leakage