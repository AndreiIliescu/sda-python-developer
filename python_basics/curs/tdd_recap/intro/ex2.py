def sum_nums(nums, only_even):
    # Daca un element nu este int
    # Vom ridica un type error
    for x in nums:
        if not isinstance(x, int):
            raise TypeError('Elem not int')

    # Daca only_even este true
    # Returnam doar suma nr pare
    if only_even:
        total = 0
        for x in nums:
            if x % 2 == 0:
                total += x

        return total
    else:
        return sum(nums)
