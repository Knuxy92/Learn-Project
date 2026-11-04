def demo_check_types() -> None:
    samples = [42, 3.5, "C001", True, None]

    for value in samples:
        print(f"{value!r} -> {type(value).__name__}")


def demo_text_concat() -> None:
    print("C" + "001")


def demo_convert() -> None:
    print(int("42") + 8)
    print(float("1250.50"))
    print(int(float("1250.50")))
    print(str(2024))
    print(int(3.9))
    print(float(7))
    print(bool(0), bool(""), bool("paid"))


def demo_bool_is_int() -> None:
    print(True + 1)
    print(True + True + False)
    print(isinstance(True, int))


def demo_none() -> None:
    email = None

    print(email)
    print(type(email).__name__)
    print(email is None)


def demo_format_spend() -> None:
    spend = 1250.5

    print(f"ยอดใช้จ่าย {spend} บาท")
    print(f"ยอดใช้จ่าย {spend:.2f} บาท")
    print(f"ยอดใช้จ่าย {spend:,.2f} บาท")


def main() -> None:
    demo_check_types()
    demo_convert()
    demo_bool_is_int()
    demo_none()
    demo_text_concat()
    demo_format_spend()


if __name__ == "__main__":
    main()
