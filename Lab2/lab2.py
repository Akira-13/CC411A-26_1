from gmpy2 import mpz, ceil, isqrt, sqrt, mpz_random, random_state, powmod, gcd, mod
from random import randint

def oraculo_brute_force(n: mpz, a: mpz) -> list[mpz]:
    """Busca las raices usando fuerza bruta."""
    x = mpz(1)
    possible_roots = []
    while x != n:
        if x in possible_roots:
            x = x + 1
            continue
        if powmod(x, 2, n) == a:
            possible_roots.append(x)
            # si x es raiz, n-x tambien
            possible_roots.append(n-x)
        x = x + 1
    return possible_roots


def fermat(n: mpz) -> tuple[mpz, mpz]:
    """Implementación sencilla del algoritmo de Fermat."""
    x = ceil(sqrt(n))
    y2 = pow(x, 2) - n
    # raiz cuadrada entera
    y = isqrt(y2)
    while pow(y, 2) != y2:
        x = x + 1
        y2 = x**2 - n
        y = isqrt(y2)
    return (x+y, x-y)

def raiz_factorizacion(n: mpz, oraculo) -> mpz:
    y = mpz_random(random_state(randint(0,1000)), n-4) + 2 # Entero entre 2 y n-2
    # a = y**2 % n
    a = powmod(y, 2, n)
    possible_roots = oraculo(n, a)
    x = mpz() 
    if len(possible_roots) == 0:
        return x
    for x in possible_roots:
        if x != mod(y, n) and x != mod(-y, n):
            return gcd(x-y, n) 
    return mpz() 