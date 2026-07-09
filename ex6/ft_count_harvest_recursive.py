def ft_count_harvest_recursive() -> None:
    days = int(input("Days until harvest: "))
    i = 1

    def helper(start: int, finish: int) -> None:
        if start == finish + 1:
            return
        print(f"Day {start}")
        helper(start + 1, finish)
    helper(i, days)
    print("Harvest time!")
