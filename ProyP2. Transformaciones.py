import numpy as np
import matplotlib.pyplot as plt

def main():
    op = menu(False)
    while op != 3:
        if op == 1:
            angulo_rotacion = float(input("Ingresa el ángulo de rotación (en grados): "))
            centro_rotacion = [float(input("Ingresa los puntos del centro de rotación\n X : ")), float(input(" Y : "))]

            puntos_2d_rotados = [rotacion_2d(punto, angulo_rotacion, centro_rotacion) for punto in puntos_2d]

            plot_2d(puntos_2d, puntos_2d_rotados)

            op = menu(True)
        elif op == 2:
            angulo_rotacion = float(input("Ingresa el ángulo de rotación (en grados): "))
            centro_rotacion = [float(input("Ingresa los puntos del centro de rotación\n X : ")), float(input(" Y : ")), float(input(" Z : "))]
            eje = input("Ingresa el eje base de rotación (x, y o z): ")

            puntos_3d_rotados = [rotacion_3d(punto, angulo_rotacion, centro_rotacion, eje) for punto in puntos_3d]

            plot_3d(puntos_3d, puntos_3d_rotados)

            op = menu(True)
        else:
            op = int(input(" Opción no válida, ingresa nuevamente: "))
            if op == 1 or op == 2:
                print()

def menu(reimprimir):
    if reimprimir:
        print('\n' + '-' * 70 + '\n')
    op = int(input("¿Con cuál tipo de figura deseas trabajar?\n 1) 2D\n 2) 3D\n\n 3) Salir\n\t"))
    print()
    return(op)

def rotacion_2d(punto, angulo, centro):
    # Transformar el ángulo a radianes
    theta = np.radians(angulo)

    # Calcular las coordenadas relativas al centro de rotación
    x_rel = punto[0] - centro[0]
    y_rel = punto[1] - centro[1]

    # Aplicar la matriz de rotación
    x_rot = x_rel * np.cos(theta) - y_rel * np.sin(theta)
    y_rot = x_rel * np.sin(theta) + y_rel * np.cos(theta)

    # Regresar a las coordenadas originales
    x_rot += centro[0]
    y_rot += centro[1]

    return [x_rot, y_rot]

def rotacion_3d(punto, angulo, centro, eje):
    # Transformar el ángulo a radianes
    theta = np.radians(angulo)
    
    # Matriz de rotación según el eje seleccionado
    if eje == 'x':
        matriz_rotacion = np.array([[1, 0, 0],
                                     [0, np.cos(theta), -np.sin(theta)],
                                     [0, np.sin(theta), np.cos(theta)]])
    elif eje == 'y':
        matriz_rotacion = np.array([[np.cos(theta), 0, np.sin(theta)],
                                     [0, 1, 0],
                                     [-np.sin(theta), 0, np.cos(theta)]])
    elif eje == 'z':
        matriz_rotacion = np.array([[np.cos(theta), -np.sin(theta), 0],
                                     [np.sin(theta), np.cos(theta), 0],
                                     [0, 0, 1]])
    else:
        raise ValueError("El eje debe ser 'x', 'y' o 'z'")
        
    # Calcular las coordenadas relativas al centro de rotación
    p_rel = np.array(punto) - np.array(centro)
    
    # Aplicar la matriz de rotación
    p_rotado = np.dot(matriz_rotacion, p_rel)

    # Regresar a las coordenadas originales
    p_rotado += np.array(centro)
    return p_rotado

def plot_2d(puntos_originales, puntos_rotados):
    p = puntos_originales
    c_p = 'ro'
    c_l = 'r-'
    l = 'Original'
    for i in range(2):
        if i == 1:
            p = puntos_rotados
            c_p = 'bo'
            c_l = 'b-'
            l = 'Rotada'

        # Puntos
        plt.plot([punto[0] for punto in p],
                [punto[1] for punto in p],
                c_p, label=l)
        # Lineas
        #  Pared (incompleta)
        for i in range(len(p) - 1):
            plt.plot([p[i][0], p[i+1][0]],
                    [p[i][1], p[i+1][1]], c_l)
        #  Completar pared
        plt.plot([p[0][0], p[4][0]], 
                [p[0][1], p[4][1]], c_l)
        plt.plot([p[2][0], p[4][0]],
                [p[2][1], p[4][1]], c_l)
        
        # Listar los valores de los puntos
        # for i, punto in enumerate(p):
        #     plt.text(punto[0], punto[1], f'({punto[0]:.3f}, {punto[1]:.3f})', fontsize=8, ha='right')

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Rotación 2D')
    plt.legend()
    plt.grid()
    plt.axis('equal')

    plt.show()

def plot_3d(puntos_originales, puntos_rotados):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    p = puntos_originales
    c_p_l = 'r'
    l = 'Original'
    for i in range(2):
        if i == 1:
            p = puntos_rotados
            c_p_l = 'b'
            l = 'Rotada'

        # Puntos
        ax.scatter([punto[0] for punto in p],
                [punto[1] for punto in p],
                [punto[2] for punto in p],
                c=c_p_l, label=l)
        # Lineas
        #  Paredes (incompletas)
        s_p = 0
        for i in range(2):
            if i == 1:
                s_p += 5
            for j in range(int((len(p)) / 2) - 1):
                ax.plot([p[j + s_p][0], p[j+1 + s_p][0]],
                        [p[j + s_p][1], p[j+1 + s_p][1]],
                        [p[j + s_p][2], p[j+1 + s_p][2]], c=c_p_l)
        #  Completar paredes
        s_p = 0
        for i in range(2):
            if i == 1:
                s_p += 5
            ax.plot([p[0 + s_p][0], p[4 + s_p][0]],
                [p[0 + s_p][1], p[4 + s_p][1]],
                [p[0 + s_p][2], p[4 + s_p][2]], c=c_p_l)
            
            ax.plot([p[2 + s_p][0], p[4 + s_p][0]],
                [p[2 + s_p][1], p[4 + s_p][1]],
                [p[2 + s_p][2], p[4 + s_p][2]], c=c_p_l)
        #  Unir paredes
        s_p = 5
        for j in range(int((len(p)) / 2)):
            ax.plot([p[j][0], p[j + s_p][0]],
                    [p[j][1], p[j + s_p][1]],
                    [p[j][2], p[j + s_p][2]], c=c_p_l)
        
        # Listar los valores de los puntos
        # for i, punto in enumerate(p):
        #     ax.text(punto[0], punto[1], punto[2], f'({punto[0]:.3f}, {punto[1]:.3f}, {punto[2]:.3f})', fontsize=8, ha='right')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Rotación 3D')
    ax.legend()

    plt.show()


def pared_3d(y):
    return [[1, y, 1], [5, y, 1], [5, y, 4], [3, y, 6], [1, y, 4]]

puntos_2d = [[1, 1], [5, 1], [5, 4], [3, 6], [1, 4]]
puntos_3d = pared_3d(0) + pared_3d(4)

main()