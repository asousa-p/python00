def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    capitalize = seed_type.capitalize()
    if unit == "packets":
        print(f"{capitalize} seeds: {quantity} packets available")
    elif unit == "grams":
        print(f"{capitalize} seeds: {quantity} grams total")
    elif unit == "area":
        print(f"{capitalize} seeds: covers {quantity} square meters")
    else:
        print("Unknown unit type")
