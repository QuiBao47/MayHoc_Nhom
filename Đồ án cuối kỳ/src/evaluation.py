# File: src/evaluation.py
import os
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import (
    ConfusionMatrixDisplay,
    accuracy_score,
    average_precision_score,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
)


def evaluate_model(
    model_name,
    y_true,
    y_pred,
    y_prob=None,
    save_dir="../results",
    show_plot=True,
):
    """
    Tính toán đầy đủ chỉ số phân lớp, lưu kết quả vào file CSV tổng hợp
    và xuất hình ảnh Confusion Matrix.
    """
    os.makedirs(save_dir, exist_ok=True)

    metrics = {
        "Model": model_name,
        "Accuracy": round(accuracy_score(y_true, y_pred), 4),
        "Precision": round(precision_score(y_true, y_pred, zero_division=0), 4),
        "Recall": round(recall_score(y_true, y_pred, zero_division=0), 4),
        "F1_Score": round(f1_score(y_true, y_pred, zero_division=0), 4),
        "ROC_AUC": round(roc_auc_score(y_true, y_prob), 4) if y_prob is not None else None,
        "PR_AUC": round(average_precision_score(y_true, y_prob), 4) if y_prob is not None else None,
    }

    # In bảng chỉ số ra màn hình
    print(f"=== KẾT QUẢ ĐÁNH GIÁ: {model_name} ===")
    for k, v in metrics.items():
        if k != "Model" and v is not None:
            print(f"  - {k}: {v:.4f}")

    # Lưu hoặc cập nhật dòng kết quả của mô hình vào file results/model_comparison.csv
    summary_path = os.path.join(save_dir, "model_comparison.csv")
    new_row = pd.DataFrame([metrics])

    if os.path.exists(summary_path):
        df_summary = pd.read_csv(summary_path)
        # Ghi đè nếu tên mô hình đã tồn tại, ngược lại thêm dòng mới
        df_summary = df_summary[df_summary["Model"] != model_name]
        df_summary = pd.concat([df_summary, new_row], ignore_index=True)
    else:
        df_summary = new_row

    df_summary.to_csv(summary_path, index=False)

    # Vẽ và lưu Confusion Matrix
    cm = confusion_matrix(y_true, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["No (0)", "Yes (1)"])
    fig, ax = plt.subplots(figsize=(5, 4))
    disp.plot(cmap="Blues", ax=ax, values_format="d")
    ax.set_title(f"Confusion Matrix - {model_name}")
    plt.tight_layout()

    safe_name = model_name.lower().replace(" ", "_").replace("(", "").replace(")", "")
    fig_path = os.path.join(save_dir, f"cm_{safe_name}.png")
    plt.savefig(fig_path, dpi=300)

    if show_plot:
        plt.show()
    else:
        plt.close(fig)

    return metrics