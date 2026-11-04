import csv
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"

PRODUCTS = [
    ("P001", "Keyboard", "Accessory", 450),
    ("P002", "Mouse", "Accessory", 300),
    ("P003", "Notebook", "Stationery", 60),
    ("P004", "Monitor", "Display", 4200),
    ("P005", "USB Hub", "Accessory", 890),
    ("P006", "Desk Lamp", "Furniture", 1150),
    ("P007", "Webcam", "Display", 1590),
    ("P008", "Pen", "Stationery", 25),
]

COUNTRIES = ["Thailand", "TH", "thailand ", " Thailand", "Thailand ", "LA", "Laos"]
TIERS = ["gold", "Gold", "GOLD", "silver", "silver ", "bronze", "", "Platinum"]
STATUSES = ["paid", "PAID", "Paid ", "pending", "cancelled", "canceled", "unknown", ""]
NAMES = [
    "Somchai Jaidee",
    "  Nattapong Sri  ",
    "Malee Wongsakul",
    "Kanya P.",
    "Anan Chaiyaporn",
    "Suda Meesuk",
    "Prasit Kaew",
    "Wilai Thongchai",
    "Chatchai Boonmee",
    "Ratana Srisuk",
]


def format_date(rng: random.Random, year: int) -> str:
    month = rng.randint(1, 12)
    day = rng.randint(1, 28)
    style = rng.choice(["iso", "dmy", "slash"])
    if style == "iso":
        return f"{year}-{month:02d}-{day:02d}"
    if style == "dmy":
        return f"{day:02d}/{month:02d}/{year}"
    return f"{year}/{month:02d}/{day:02d}"


def format_price(rng: random.Random, price: int) -> str:
    style = rng.choice(["plain", "comma", "baht", "decimal"])
    if style == "plain":
        return str(price)
    if style == "comma":
        return f"{price:,}"
    if style == "baht":
        return f"฿{price:,}"
    return f"{price:.2f}"


def format_phone(rng: random.Random, index: int) -> str:
    base = f"08{index:02d}{index + 1:03d}{index + 2:03d}"
    style = rng.choice(["local", "dash", "intl", "paren"])
    if style == "local":
        return base
    if style == "dash":
        return f"{base[:3]}-{base[3:6]}-{base[6:]}"
    if style == "intl":
        return f"+66{base[1:]}"
    return f"(66) {base[1:4]}{base[4:]}"


def write_customers(rng: random.Random) -> None:
    rows = []
    for index in range(1, 13):
        name = NAMES[index % len(NAMES)]
        email = f"customer{index}@example.com"
        if index % 4 == 0:
            email = email.upper()
        elif index % 7 == 0:
            email = ""
        rows.append(
            {
                "customer_id": f"C{index:03d}",
                "name": name,
                "email": email,
                "phone": format_phone(rng, index),
                "country": rng.choice(COUNTRIES),
                "signup_date": format_date(rng, 2024),
                "loyalty_tier": rng.choice(TIERS),
            }
        )

    rows.append(dict(rows[2]))
    rows.append(
        {
            "customer_id": "C003",
            "name": "Malee Wongsakul ",
            "email": "malee@example.com",
            "phone": "",
            "country": "Thailand",
            "signup_date": "2024-03-15",
            "loyalty_tier": "Gold",
        }
    )

    with (RAW / "customers.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def messy_product_name(index: int, name: str) -> str:
    if index % 3 == 0:
        return f" {name} "
    if index % 4 == 0:
        return name.upper()

    return name


def write_products() -> None:
    rows = [
        {
            "product_id": product_id,
            "product_name": messy_product_name(index, name),
            "category": category.lower() if index % 2 else category,
            "list_price": price,
        }
        for index, (product_id, name, category, price) in enumerate(PRODUCTS)
    ]

    with (RAW / "products.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def write_orders(rng: random.Random) -> None:
    rows = []
    for index in range(1, 41):
        product_id, _, _, price = PRODUCTS[rng.randrange(len(PRODUCTS))]
        quantity = rng.choice([1, 1, 2, 2, 3, 5, -1, 0, ""])
        unit_price = format_price(rng, price)
        if index % 11 == 0:
            unit_price = ""
        rows.append(
            {
                "order_id": f"O{index:04d}",
                "customer_id": f"C{rng.randint(1, 14):03d}",
                "product_id": product_id,
                "quantity": quantity,
                "unit_price": unit_price,
                "order_date": format_date(rng, 2025),
                "status": rng.choice(STATUSES),
            }
        )

    rows.append(dict(rows[5]))
    rows.append(
        {
            "order_id": "O0006",
            "customer_id": "C006",
            "product_id": "P002",
            "quantity": 1,
            "unit_price": "300",
            "order_date": "2025-02-11",
            "status": "paid",
        }
    )

    with (RAW / "orders.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def write_customers_thai() -> None:
    rows = [
        {
            "customer_id": "C001",
            "name": "สมชาย ใจดี",
            "province": "กรุงเทพมหานคร",
            "email": "somchai@example.com",
        },
        {
            "customer_id": "C002",
            "name": "นัฐพงษ์ ศรี",
            "province": "เชียงใหม่",
            "email": "nattapong@example.com",
        },
        {
            "customer_id": "C003",
            "name": "มาลี วงศ์สกุล",
            "province": "ขอนแก่น",
            "email": "malee@example.com",
        },
    ]

    with (RAW / "customers_th.csv").open("w", newline="", encoding="utf-8-sig") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    RAW.mkdir(parents=True, exist_ok=True)
    rng = random.Random(20250101)

    write_customers(rng)
    write_products()
    write_orders(rng)
    write_customers_thai()

    for path in sorted(RAW.glob("*.csv")):
        lines = path.read_text(encoding="utf-8-sig").count("\n")
        print(f"{path.relative_to(ROOT)}  {lines} บรรทัด")


if __name__ == "__main__":
    main()
