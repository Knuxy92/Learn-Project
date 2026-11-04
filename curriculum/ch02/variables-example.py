def demo_create_variables() -> None:
    name = "Nattapong Sri"
    age = 34
    spend = 1250.5
    is_member = True

    print(name)
    print(age)
    print(spend)
    print(is_member)


def demo_reassign() -> None:
    spend = 1250.5
    print(spend)

    spend = spend + 250
    print(spend)


def demo_multiple_assignment() -> None:
    name, age = "Malee Wongsakul", 28
    print(name, age)


def main() -> None:
    demo_create_variables()
    demo_reassign()
    demo_multiple_assignment()


if __name__ == "__main__":
    main()
