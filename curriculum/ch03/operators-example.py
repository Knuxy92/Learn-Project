def demo_arithmetic() -> None:
    print(450 * 3)
    print(7 / 2)
    print(7 // 2)
    print(7 % 2)
    print(2**10)


def demo_precedence() -> None:
    print(450 + 3 * 100)
    print((450 + 3) * 100)


def demo_augmented() -> None:
    total = 1000.0

    total -= 100
    print(total)


def demo_float_precision() -> None:
    print(0.1 + 0.2)
    print(round(0.1 + 0.2, 2))


def demo_string_operators() -> None:
    print("C" + "001")
    print("-" * 10)


def main() -> None:
    demo_arithmetic()
    demo_precedence()
    demo_augmented()
    demo_float_precision()
    demo_string_operators()


if __name__ == "__main__":
    main()
