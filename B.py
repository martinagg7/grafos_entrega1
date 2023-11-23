from collections import deque

def encontrar_vecinos(x, y):
    return [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)]

desplazamiento_filas = [1, -1, 0, 0]  
desplazamiento_columnas = [0, 0, -1, 1]  

def buscar_ruta_inicial(cuadricula):
    for i in range(n):
        for j in range(m):
            if cuadricula[i][j] == 'A':
                return i, j

def bfs(cuadricula, inicio, fin):
    queue = deque([(inicio, 0, "")])
    visitado = set()

    while queue:
        (fila, columna), distancia, ruta = queue.popleft()

        for i in range(4):
            fila_vecino = fila + desplazamiento_filas[i]
            columna_vecino = columna + desplazamiento_columnas[i]

            if 0 <= fila_vecino < n and 0 <= columna_vecino < m and cuadricula[fila_vecino][columna_vecino] != '#' and (fila_vecino, columna_vecino) not in visitado:
                if cuadricula[fila_vecino][columna_vecino] == 'B':
                    return True, distancia + 1, ruta + obtener_direccion(i)

                visitado.add((fila_vecino, columna_vecino))
                queue.append(((fila_vecino, columna_vecino), distancia + 1, ruta + obtener_direccion(i)))

    return False, 0, ""

def obtener_direccion(i):
    if i == 0:
        return "L"
    elif i == 1:
        return "R"
    elif i == 2:
        return "U"
    elif i == 3:
        return "D"


n, m = map(int, input().split())
cuadricula = []

for _ in range(n):
    cuadricula.append(input())

# encontrar l(A)
inicio = buscar_ruta_inicial(cuadricula)

#ruta más corta utilizando 
encontrada, longitud, descripcion = bfs(cuadricula, inicio, 'B')

if encontrada:
    print("SÍ")
    print(longitud)
    print(descripcion)
else:
    print("NO")
