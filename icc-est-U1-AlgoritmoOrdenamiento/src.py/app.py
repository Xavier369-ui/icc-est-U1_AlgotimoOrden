import random
from typing import List,Dict,Callable,Tuple
from benchmarking import Benchmarking
from short_marking import MetodosOrdenamiento
import matplotlib.pyplot as plt

class App:
    def __init__(self):
        self.tamanios: List[int] = [500, 1000, 3000, 5000,  10000]
        self.tamanios_maximo: int = max(self.tamanios)
        self.arreglo_base: List[int] = self.benchmarking_arreglo(self.tamanios_maximo)
        self.algoritmos: Dict[str,Callable] = {
            "Burbuja": MetodosOrdenamiento.sort_burbuja,
            "Burbuja_mejorado_optimizado": MetodosOrdenamiento.sort_burbuja_mejorado_optimizado,
            "Seleccion": MetodosOrdenamiento.sort_seleccion,
            "Insercion": MetodosOrdenamiento.sort_insercion,
            "Shell": MetodosOrdenamiento.sort_shell,
        }
        self.resultados: List[Tuple[int,str,float]] = []
        
    def benchmarking_arreglo(self,tamanio: int) -> List[int]:
        return random.sample(range(1,tamanio * 10),tamanio)
    
    def grafica_resultado(self) -> None:
        datos_algoritmo = {}
        for tamanio,nombre_algoritmo,tiempo in self.resultados:
            if nombre_algoritmo not in datos_algoritmo:
                datos_algoritmo[nombre_algoritmo] = {"x":[], "y":[]}
            datos_algoritmo[nombre_algoritmo]["x"].append(tamanio)
            datos_algoritmo[nombre_algoritmo]["y"].append(tiempo)
            
        plt.figure(figsize=(10, 6))
        for nombre,datos in datos_algoritmo.items():
            plt.plot(datos["x"],datos["y"],marker="o",label=nombre)
            
        plt.title("Comparacion de algoritmos de ordenamiento")
        plt.xlabel("Cantidad de elementos")
        plt.ylabel("Tiempo de ejecucion(segundo)")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.savefig("grafico_ordenamiento.png")
        plt.show()
    
    def menu(self) -> None:
        for tamanio in self.tamanios:
            arreglo_actual = self.arreglo_base[:tamanio]
            for nombre,metodo in self.algoritmos.items():
                tiempo = Benchmarking.medir_tiempo(metodo,arreglo_actual)
                self.resultados.append((tamanio,nombre,tiempo))
                print(f"Tamaño:{tamanio},Algoritmo:{nombre},Tiempo:{tiempo: .4f},segundos")
        
        self.grafica_resultado()
        
if __name__ == "__main__":
    app = App()
    app.menu()
        
    
                
       
            
            
                 