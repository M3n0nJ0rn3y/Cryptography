def square_n_multiply(base, exponent, modulus=None) -> int:
    bin_exp = bin(exponent)[2:]
    result = 1

    if modulus is not None:
        base = base % modulus  # Ensure base is within modulus

    for bit in bin_exp:
        result = result * result  # Square step
        if modulus is not None:
            result = result % modulus  # Apply modulus

        if bit == '1':
            result = result * base  # Multiply step
            if modulus is not None:
                result = result % modulus  # Apply modulus

    return result if modulus is None else result % modulus



if __name__ == '__main__':
    sol = square_n_multiply(3, 5)
    print(sol)

    sol_2 = square_n_multiply(3, 5, 5)
    print(sol_2)

