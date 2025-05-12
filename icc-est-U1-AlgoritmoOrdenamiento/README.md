# 📊 Práctica de Algoritmos de Ordenamiento

## 📌 Información General

- **Título:** Análisis de Algoritmos de Ordenamiento
- **Asignatura:** Estructura de Datos
- **Carrera:** Computación
- **Estudiante:** [Xavier Fajardo y Cristian Arevalo ]
- **Fecha:** [Fecha Actual]
- **Profesor:** Ing. Pablo Torres

---

## 🛠️ Descripción

Este proyecto implementa y compara algoritmos de ordenamiento en **Python**, vemos su desempeño en función del tiempo de ejecución.  
Los algoritmos implementados son:

-  Método Burbuja  
-  Método Burbuja Mejorado  
-  Método Selección  
-  Método Inserción  
-  Método Shell  

Cada algoritmo se aplica a arreglos aleatorios con diferentes tamaños:  
`5,000`, `10,000`, `30,000`, `50,000`, y `100,000` elementos.  
El tiempo de ejecución se mide en segundos utilizando la biblioteca `time`.

---

## 🚀 Instrucciones de Ejecución

1. Instala las dependencias si aún no lo has hecho:
   pip install matplotlib

## 🚀 Grafica 

![Image Altl(https://github.com/Xavier369-ui/icc-est-U1_AlgotimoOrden/blob/4d95927a9e0d86e431111ee7b9581da081366e81/grafico_ordenamiento.png)

## Conclusion

- Los algoritmos de ordenamiento Burbuja , Seleccion e Inserccion presentan una complejidad O(n**2), lo que hace ineficientes para arreglos da datos grandes.
- Shell Sort con una complejidad aproximada de O(n log**2 n),fue el algoritmo mas eficiente en todas las pruebas, validando su ventaja teorica
-Aunque Burnuja mejorado optimiza ligeramente, no ofrece un cambio significativo respecto al normal en arreglos grandes y aleatorios.
-Se garantizo una evaluiacion justa mediante la clonacion del arreglo base,evitando comparaciones sobre arreglos que ya habian sido ordenados.
-Los resultados obtenidos en la practica confirman como la complejidad asintotica predice el comportamiento real,lo cual es esencial al elegir algoritmos en aplicaciones reales. 
