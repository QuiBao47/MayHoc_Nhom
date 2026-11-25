# File: src/preprocessing.py
import os
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


def load_and_preprocess_data(
    filepath="../data/raw/bank-additional-full.csv",
    save_dir="../data/processed",
):
    # 1. Đọc và làm sạch cơ bản
    df = pd.read_csv(filepath, sep=";")
    df_model = df.drop_duplicates().dropna(subset=["y"]).copy()

    # 2. Tách X, y (loại duration để tránh data leakage)
    X = df_model.drop(columns=["y", "duration"])
    y = df_model["y"].map({"no": 0, "yes": 1})

    numeric_features = X.select_dtypes(include="number").columns.tolist()
    categorical_features = X.select_dtypes(exclude="number").columns.tolist()

    # 3. Chia train/test cố định random_state=42
    X_train_raw, X_test_raw, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # 4. Pipeline biến đổi dữ liệu
    numeric_pipeline = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler()),
        ]
    )
    categorical_pipeline = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="most_frequent")),
            (
                "onehot",
                OneHotEncoder(handle_unknown="ignore", sparse_output=False),
            ),
        ]
    )

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_pipeline, numeric_features),
            ("cat", categorical_pipeline, categorical_features),
        ]
    )

    X_train = preprocessor.fit_transform(X_train_raw)
    X_test = preprocessor.transform(X_test_raw)

    # Tự động tạo thư mục data/processed nếu chưa có và lưu file cố định
    os.makedirs(save_dir, exist_ok=True)
    feature_names = preprocessor.get_feature_names_out()

    # Lưu tập đã scale/encode
    pd.DataFrame(X_train, columns=feature_names).to_csv(
        f"{save_dir}/X_train.csv", index=False
    )
    pd.DataFrame(X_test, columns=feature_names).to_csv(
        f"{save_dir}/X_test.csv", index=False
    )
    y_train.to_csv(f"{save_dir}/y_train.csv", index=False)
    y_test.to_csv(f"{save_dir}/y_test.csv", index=False)

    # Lưu thêm tập raw đã chia train/test (để dùng cho SkPipeline + SMOTE tránh data leakage)
    X_train_raw.to_csv(f"{save_dir}/X_train_raw.csv", index=False)
    X_test_raw.to_csv(f"{save_dir}/X_test_raw.csv", index=False)

    return (
        X_train,
        X_test,
        y_train,
        y_test,
        X_train_raw,
        X_test_raw,
        preprocessor,
    )


if __name__ == "__main__":
    load_and_preprocess_data(
        filepath="data/raw/bank-additional-full.csv",
        save_dir="data/processed",
    )
    print("Đã tiền xử lý và lưu dữ liệu sạch vào data/processed/ thành công!")