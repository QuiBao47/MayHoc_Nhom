# Train / Validation / Test Split

## Dataset: Bank Marketing (bank-additional-full.csv)
- **Tổng mẫu**: 41,188
- **Train**: 32,950 mẫu (80%) → X_train.csv / y_train.csv
- **Test**: 8,238 mẫu (20%) → X_test.csv / y_test.csv
- **Validation**: Dùng Cross-Validation (K=3) trên tập Train

## Lưu ý
- Dữ liệu đã được xử lý nằm tại DATA/processed/
- andom_state=42, stratify=y để đảm bảo tỷ lệ lớp đồng đều
- Chưa tách Validation set riêng vì dùng CV nội bộ

## Files tham chiếu (tại DATA/processed/)
- X_train.csv, y_train.csv
- X_test.csv, y_test.csv
- X_train_raw.csv, X_test_raw.csv (dữ liệu chưa scale, dùng cho SMOTE)
