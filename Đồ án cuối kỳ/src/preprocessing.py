# File: src/preprocessing.py
import os
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


def load_and_preprocess_data(
    filepath="../DATA/raw/bank-additional-full.csv",
    save_dir="../DATA/processed",
):
    # 1. Äá»c vÃ  lÃ m sáº¡ch cÆ¡ báº£n
    df = pd.read_csv(filepath, sep=";")
    df_model = df.drop_duplicates().dropna(subset=["y"]).copy()

    # 2. TÃ¡ch X, y (loáº¡i duration Ä‘á»ƒ trÃ¡nh data leakage)
    X = df_model.drop(columns=["y", "duration"])
    y = df_model["y"].map({"no": 0, "yes": 1})

    numeric_features = X.select_dtypes(include="number").columns.tolist()
    categorical_features = X.select_dtypes(exclude="number").columns.tolist()

    # 3. Chia train/test cá»‘ Ä‘á»‹nh random_state=42
    X_train_raw, X_test_raw, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # 4. Pipeline biáº¿n Ä‘á»•i dá»¯ liá»‡u
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

    # Tá»± Ä‘á»™ng táº¡o thÆ° má»¥c data/processed náº¿u chÆ°a cÃ³ vÃ  lÆ°u file cá»‘ Ä‘á»‹nh
    os.makedirs(save_dir, exist_ok=True)
    feature_names = preprocessor.get_feature_names_out()

    # LÆ°u táº­p Ä‘Ã£ scale/encode
    pd.DataFrame(X_train, columns=feature_names).to_csv(
        f"{save_dir}/X_train.csv", index=False
    )
    pd.DataFrame(X_test, columns=feature_names).to_csv(
        f"{save_dir}/X_test.csv", index=False
    )
    y_train.to_csv(f"{save_dir}/y_train.csv", index=False)
    y_test.to_csv(f"{save_dir}/y_test.csv", index=False)

    # LÆ°u thÃªm táº­p raw Ä‘Ã£ chia train/test (Ä‘á»ƒ dÃ¹ng cho SkPipeline + SMOTE trÃ¡nh data leakage)
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
        filepath="DATA/raw/bank-additional-full.csv",
        save_dir="DATA/processed",
    )
    print("ÄÃ£ tiá»n xá»­ lÃ½ vÃ  lÆ°u dá»¯ liá»‡u sáº¡ch vÃ o data/processed/ thÃ nh cÃ´ng!")
