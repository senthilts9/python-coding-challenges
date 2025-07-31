import sys

def solve():
    mod = 1000000007
    inv3 = pow(3, mod - 2, mod)  # modular inverse of 3 mod mod
    data = sys.stdin.read().strip().split()
    if not data:
        return
    T = int(data[0])
    res = []
    for i in range(1, T + 1):
        n = int(data[i])
        m = (n - 1) // 2
        m_mod = m % mod
        m2 = (m_mod * m_mod) % mod
        m3 = (m2 * m_mod) % mod
        term = (16 * m3 + 30 * m2 + 26 * m_mod) % mod
        s = (1 + (term * inv3) % mod) % mod
        res.append(str(s))
    sys.stdout.write("\n".join(res))

if __name__ == '__main__':
    solve()
