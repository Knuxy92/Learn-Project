def parse_quantity(text: str) -> int:
    return int(text)


def parse_quantity_safe(text: str) -> int | None:
    try:
        return int(text)
    except ValueError:
        return None


def parse_quantity_any(value) -> int | None:
    try:
        return int(value)
    except (ValueError, TypeError):
        return None


def lookup_tier(tiers: dict[str, str], customer_id: str) -> str:
    try:
        return tiers[customer_id]
    except KeyError:
        return "Unknown"


def require_positive_quantity(text: str) -> int:
    quantity = int(text)
    if quantity <= 0:
        raise ValueError(f"จำนวนต้องมากกว่าศูนย์ แต่ได้ {quantity}")
    return quantity


if __name__ == "__main__":
    print(f"parse_quantity_safe('3') ได้ {parse_quantity_safe('3')}")
    print(f"parse_quantity_safe('') ได้ {parse_quantity_safe('')}")
    print(f"parse_quantity_safe('สอง') ได้ {parse_quantity_safe('สอง')}")
    print(f"parse_quantity_any(None) ได้ {parse_quantity_any(None)}")
    print(f"parse_quantity_any('7') ได้ {parse_quantity_any('7')}")

    tiers = {"C001": "Gold", "C002": "Silver"}
    print(f"lookup_tier('C001') ได้ {lookup_tier(tiers, 'C001')}")
    print(f"lookup_tier('C999') ได้ {lookup_tier(tiers, 'C999')}")

    print(f"require_positive_quantity('2') ได้ {require_positive_quantity('2')}")
    try:
        require_positive_quantity("0")
    except ValueError as error:
        print(f"จับได้ {error}")

    try:
        parse_quantity("")
    except ValueError as error:
        print(f"ValueError บอกว่า {error}")

    try:
        parse_quantity(None)
    except TypeError as error:
        print(f"TypeError บอกว่า {error}")
