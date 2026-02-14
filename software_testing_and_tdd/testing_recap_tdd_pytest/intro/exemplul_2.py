def sum_nums(nums, only_evan):
    # Daca un element nu este "int" vom ridica un "TypeError"
    for x in nums:
        if not isinstance(x, int):
            raise TypeError("Elem not int")

    # Daca "only_evan" este True
    # returnam doar suma nr. pare
    if only_evan:
        total = 0
        for x in nums:
            if x % 2 == 0:
                total += x

        return total
    else:
        return sum(nums)
