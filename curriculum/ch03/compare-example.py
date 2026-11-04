def demo_comparisons() -> None:
    print(450 > 300)
    print(450 == 450.0)
    print("paid" == "PAID")
    print("paid" == "paid ")
    print("paid".strip() == "paid")


def demo_chained_comparison() -> None:
    print(500 <= 500 < 1000)


def demo_boolean_operators() -> None:
    print(True and False)
    print(True or False)
    print(not True)


def demo_truthiness() -> None:
    print(bool(0), bool(-1), bool(""), bool("0"))


def demo_none_check() -> None:
    tier = None

    print(tier is None)


def main() -> None:
    demo_comparisons()
    demo_chained_comparison()
    demo_boolean_operators()
    demo_truthiness()
    demo_none_check()


if __name__ == "__main__":
    main()
