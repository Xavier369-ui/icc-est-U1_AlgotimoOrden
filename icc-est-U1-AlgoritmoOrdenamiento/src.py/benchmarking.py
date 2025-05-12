import time
from typing import Callable,List

class Benchmarking:
    def medir_tiempo(funcion: Callable,arreglo: list[int]) -> float:
        inicio = time.time()
        funcion(arreglo)
        fin = time.time()
        return fin - inicio