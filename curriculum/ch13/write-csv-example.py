from __future__ import annotations

import csv
from pathlib import Path

import pandas as pd

SOURCE_PATH = Path("data/raw/customers.csv")
OUTPUT_PATH = Path("data/processed/customers_three.csv")


def main() -> None:
    customers = pd.read_csv(SOURCE_PATH, encoding="utf-8")
    sample = customers.head(3)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    sample.to_csv(OUTPUT_PATH, index=False, encoding="utf-8")

    print(OUTPUT_PATH.read_text(encoding="utf-8"))
    print()

    with OUTPUT_PATH.open(encoding="utf-8", newline="") as file:
        rows = list(csv.DictReader(file))

    print("จำนวนแถวที่อ่านกลับมาได้", len(rows))
    print("แถวแรกคือ", repr(rows[0]["customer_id"]), repr(rows[0]["name"]))
    print()

    reloaded = pd.read_csv(OUTPUT_PATH, encoding="utf-8")
    print(reloaded.shape)
    print(reloaded.columns.tolist())
    print()

    print(reloaded.equals(sample))


if __name__ == "__main__":
    main()
