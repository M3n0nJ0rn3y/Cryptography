m = 120
r = 0


while m % 2 == 0:
    m = m / 2
    r += 1

print(f'{m} * 2^{r}')