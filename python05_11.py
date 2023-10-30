#!/usr/bin/env python3

#11. Escrevendo um roteiro para encontrar a interseção, diferença, união e diferença simétrica entre esses dois conjuntos.
#Conjuntos A e B: 
A = {3, 14, 15, 9, 26, 5, 35, 9}
B = {60, 22, 14, 0, 9}

#Intersecção entre A e B
interseção = A & B
print("A interseção  entre A e B é: ", interseção)

#Diferença entre A e B
diferença = A - B
print("A diferença entre A e B é: ", diferença)

#União entre A e B
união = A | B
print("A união entre A e B é: ", união)

#Diferença simétrica entre A e B
dif_simétrica = A ^ B
print("A diferença simétrica entre A e B é: ", dif_simétrica)