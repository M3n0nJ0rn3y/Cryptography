def gcd(a, m):
    # a = m * q + r
    m_1 = (a//m)
    q = m
    r = a%m

    # a = m_1 * q + r