from typing import List

class MetodosOrdenamiento:
    def sort_burbuja(arreglo: List[int ]) -> List[int]:
        arr = arreglo.copy()
        for i in range(len(arr)):
            for j in range (0,len(arr)-i-1):
                if arr[j] > arr[j+1]:
                    arr[j],arr[j+1] = arr[j+1],arr[j]
        return arr
    
    def sort_burbuja_mejorado_optimizado(arreglo: List[int]) -> List[int]:
        arr = arreglo.copy()
        n = len(arr)
        for i in range(n):
            for j in range(0,n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j],arr[j+1] = arr[j+1],arr[j]
        return arr
    
    def sort_seleccion(arreglo: List[int]) -> List[int]:
        arr = arreglo.copy()
        for i in range(len(arr)):
            Mi = i
            for j in range(i+1,len(arr)):
                if arr[j] < arr[Mi]:
                    Mi = j
            arr[i],arr[Mi] = arr[Mi],arr[i]
        return arr
    
    def sort_insercion(arreglo: List[int]) -> List[int]:
        arr = arreglo.copy()
        for i in range(1,len(arr)):
            key = arr[i]
            j = i -1
            while j >= 0 and arr[j] > key:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = key
        return arr
    
    
    def sort_shell(arreglo: List[int]) -> List[int]:
        arr = arreglo.copy()
        n = len(arr)
        gap = n // 2
        while gap > 0:
            for i in range(gap,n):
                aux = arr[i]
                j = i
                while j >= gap and arr[j - gap] > aux:
                    arr[j] = arr[j - gap]
                    j -= gap
                arr[j] = aux
            gap //= 2
        return arr