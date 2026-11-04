def format_amount(value: float, currency: str = "บาท", decimals: int = 2) -> str:
    return f"{value:,.{decimals}f} {currency}"


def safe_int(value: str | int | None, default: int = 0) -> int:
    if isinstance(value, int):
        return value
    if isinstance(value, str) and value.strip().lstrip("+-").isdecimal():
        return int(value)
    return default


def append_note_bad(notes: list[str] = []) -> list[str]:  # noqa: B006
    notes.append("ตรวจแล้ว")
    return notes


def append_note(notes: list[str] | None = None) -> list[str]:
    result = [] if notes is None else notes
    result.append("ตรวจแล้ว")
    return result


def main() -> None:
    print("== ค่าเริ่มต้น ==")
    print(format_amount(1150))
    print(format_amount(1150, currency="USD"))
    print(format_amount(1150, decimals=0))

    print("== ค่าเริ่มต้นที่แก้ได้ ==")
    print(append_note_bad())
    print(append_note_bad())

    print("== แก้ด้วย None ==")
    print(append_note())
    print(append_note())

    print("== safe_int ==")
    print(safe_int("12"))
    print(safe_int("x", -1))
    print(safe_int(None))


if __name__ == "__main__":
    main()
