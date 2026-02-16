from ft_filter import ft_filter

def test_case(desc, func, data):
    print(f"\n--- {desc} ---")
    real = list(filter(func, data))
    mine = list(ft_filter(func, data))
    print("real :", real)
    print("mine :", mine)
    print("OK   :", real == mine)


def main():
    # mixed tricky data
    data = [0, 1, 2, '', 'hi', None, True, False, [], [1], {}, {'a':1}, -1, 3.5]

    # None function (truthiness filtering)
    test_case("func=None", None, data)

    # keep zeros only (falsy-but-valid case)
    test_case("keep zeros", lambda x: x == 0, data)

    # numbers only
    test_case(
        "numbers only",
        lambda x: isinstance(x, (int, float)),
        data
    )

    # strings length > 1
    test_case(
        "long strings",
        lambda x: isinstance(x, str) and len(x) > 1,
        data
    )

    # truthy bools only
    test_case(
        "True only",
        lambda x: x is True,
        data
    )

    # lists/dicts non-empty
    test_case(
        "non-empty containers",
        lambda x: isinstance(x, (list, dict)) and len(x) > 0,
        data
    )

    # __doc__
    print("\n--- equal documentation ---\n")
    nums = list(range(0, 4))
    print("real : \n")
    print(filter.__doc__, '\n')
    print("mine : \n")
    print(ft_filter.__doc__, '\n')


if __name__ == '__main__':
    main()