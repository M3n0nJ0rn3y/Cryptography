def square_n_multiply(base, exponent, modulus=None) -> int:
    bin_exp = bin(exponent)[2:]
    result = 1

    if modulus is not None:
        base = base % modulus  # Check that base is within mod.

    for bit in bin_exp:
        result = result * result  # Square on each step
        if modulus is not None:
            result = result % modulus

        if bit == '1':
            result = result * base  # Multiply if bit is equal to one.
            if modulus is not None:
                result = result % modulus

    return result



if __name__ == '__main__':
    sol = square_n_multiply(3, 5)
    print(sol)

    sol_2 = square_n_multiply(3, 5, 5)
    print(sol_2)

