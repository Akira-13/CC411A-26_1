import time
import matplotlib.pyplot as plt
from gmpy2 import mpz, next_prime
import random

# Import your functions from lab2.py
from lab2 import fermat, raiz_factorizacion, oraculo_brute_force

def generate_semiprime(bits):
    """Genera N = p*q"""
    p_bits = bits // 2
    q_bits = bits - p_bits
    
    p = next_prime(mpz(random.getrandbits(p_bits)) + 2)
    q = next_prime(mpz(random.getrandbits(q_bits)) + 2)
    
    return p * q

def profile_and_show(start_bits, max_bits):
    start_bits = start_bits
    max_bits = max_bits
    bit_sizes = list(range(start_bits, max_bits + 1))
    
    fermat_times = []
    raiz_times = []

    print(f"{'Bits':<5} | {'N':<8} | {'Fermat':<15} | {'Raiz Result':<10}")
    print("-" * 55)

    for bits in bit_sizes:
        n = generate_semiprime(bits)
        
        # Perfilar Fermat
        t0 = time.perf_counter()
        res_fermat = fermat(n)
        t_fermat = time.perf_counter() - t0
        fermat_times.append(t_fermat)

        # Perfilar Raiz Factorizacion
        t1 = time.perf_counter()
        res_raiz = raiz_factorizacion(n, oraculo_brute_force)
        t_raiz = time.perf_counter() - t1
        raiz_times.append(t_raiz)

        # Mostrar Resultados
        print(f"{bits:<5} | {int(n):<8} | {str(res_fermat):<15} | {int(res_raiz):<10}")

    return bit_sizes, fermat_times, raiz_times

def generate_graph(bits, t_fermat, t_raiz):
    plt.figure(figsize=(10, 6))
    plt.plot(bits, t_fermat, marker='o', label='Fermat', color='blue')
    plt.plot(bits, t_raiz, marker='s', label='Raiz Factorizacion (Brute Force)', color='red')
    
    plt.title('Tiempo vs. Número de bits')
    plt.xlabel('Bits en N')
    plt.ylabel('Tiempo (segundos)')
    plt.yscale('log') # Escala logarítmica
    plt.legend()
    plt.grid(True, which="both", ls="--", alpha=0.5)
    
    plt.savefig('perfilado.png')
    plt.show()

if __name__ == "__main__":
    bits, t_f, t_r = profile_and_show(5, 20)
    generate_graph(bits, t_f, t_r)