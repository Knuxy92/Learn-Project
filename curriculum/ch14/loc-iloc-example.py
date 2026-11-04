from pathlib import Path

import pandas as pd

RAW_DIR = Path(__file__).resolve().parents[2] / "data" / "raw"


def load_orders() -> pd.DataFrame:
    return pd.read_csv(RAW_DIR / "orders.csv", encoding="utf-8")


def main() -> None:
    orders = load_orders()

    print("สามแถวแรกด้วย loc")
    print(orders.loc[0:2, ["order_id", "quantity", "status"]].to_string(index=False))

    print("\nสามแถวแรกด้วย iloc")
    print(orders.iloc[0:3, 0:3].to_string(index=False))

    print("\nค่าเดียวด้วย loc")
    print(orders.loc[0, "order_id"])

    print("\nแถวสุดท้ายสองแถวด้วย iloc ติดลบ")
    print(orders.iloc[-2:, :3].to_string(index=False))

    print("\nคอลัมน์เดียวแบบ Series ด้วย loc")
    print(orders.loc[:4, "status"].tolist())


if __name__ == "__main__":
    main()
