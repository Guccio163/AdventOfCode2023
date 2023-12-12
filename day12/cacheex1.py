from functools import cache

def f(line):
    P, N = line.split()
    P = '?'.join([P] * 5)
    N = [int(n) for n in N.split(',')] * 5

    @cache
    def dp(p, n, r=0):
        if p >= len(P): return n == len(N)

        if P[p] in '.?': r += dp(p+1, n)

        if n == len(N): return r

        if P[p] in '#?' and \
            (p + N[n] <= len(P) and '.' not in P[p:p+N[n]]) and \
            (p + N[n] == len(P) or  '#' not in [P[p+N[n]]]):
                r += dp(p+N[n]+1, n+1)

        return r

    return dp(0, 0)

print(sum(map(f, open('data12.txt'))))