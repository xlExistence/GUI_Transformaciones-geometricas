import numpy as np
import matplotlib.pyplot as plt

def main():
    transformaciones_2D = {1: "Rotación 2D", 2: "Traslación 2D", 3: "Espejo 2D", 4: "Cambio de escala 2D"}
    transformaciones_3D = {1: "Rotación 3D", 2: "Traslación 3D", 3: "Espejo 3D", 4: "Cambio de escala 3D"}
    figs = {1: "2D", 2: "3D", 3: ''}

    fig, transf = menu(False, False, figs)
    while fig != 3 and transf != 6:
        transformaciones = transformaciones_2D if fig == 1 else transformaciones_3D
        
        if transf in transformaciones:
            if transf == 1:


            fig, transf = menu(True, fig, figs)
        elif transf == 5:
            fig, transf = menu(True, False, figs)
        else:
            transf = int(input(" Opción no válida, ingresa nuevamente: "))
            if transf in transformaciones or transf == 5:
                print()

def menu(reprint, fig_select, figs):
    if reprint:
        print('\n' + '-' * 70 + '\n')

    if not fig_select:
        fig = int(input("¿Con cuál tipo de figura deseas trabajar?\n 1) 2D\n 2) 3D\n\n 3) Salir\n\t"))
        while fig not in figs:
            fig = int(input(" Opción no válida, ingresa nuevamente: "))
        print()
        if fig == 3:
            return fig, False

        transf = int(input(f"[ Figura {figs[fig]} ]\nSelecciona una transformación a realizar:\n 1) Rotación\n 2) Traslación\n 3) Espejo\n 4) Cambio de escala\n\n 5) Seleccionar otro tipo de figura\n\n 6) Salir\n\t"))
    else:
        fig = fig_select
        transf = int(input(f"[ Figura {figs[fig]} ]\nSelecciona una transformación a realizar:\n 1) Rotación\n 2) Traslación\n 3) Espejo\n 4) Cambio de escala\n\n 5) Seleccionar otro tipo de figura\n\n 6) Salir\n\t"))

    print()
    return fig, transf

# TRANSFORMACIONES 2D

def rotacion_2D(points, angle):
    """Realiza una rotación 2D en los puntos dados."""
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle), 0],
                                [np.sin(angle), np.cos(angle), 0],
                                [0, 0, 1]])
    # Agregar una fila de unos para poder multiplicar con la matriz de transformación
    points_homo = np.hstack((points, np.ones((len(points), 1))))
    # Aplicar la transformación
    rotated_points = np.dot(rotation_matrix, points_homo.T).T[:, :2]
    return rotated_points

def translate2D(points, tx, ty):
    """Realiza una traslación 2D en los puntos dados."""
    translation_matrix = np.array([[1, 0, tx],
                                   [0, 1, ty],
                                   [0, 0, 1]])
    # Agregar una fila de unos para poder multiplicar con la matriz de transformación
    points_homo = np.hstack((points, np.ones((len(points), 1))))
    # Aplicar la transformación
    translated_points = np.dot(translation_matrix, points_homo.T).T[:, :2]
    return translated_points

def mirror2D(points, axis):
    """Realiza un espejo 2D en los puntos dados con respecto al eje dado."""
    if axis == 'x':
        mirror_matrix = np.array([[1, 0, 0],
                                  [0, -1, 0],
                                  [0, 0, 1]])
    elif axis == 'y':
        mirror_matrix = np.array([[-1, 0, 0],
                                  [0, 1, 0],
                                  [0, 0, 1]])
    else:
        raise ValueError("Axis must be 'x' or 'y'")
    # Agregar una fila de unos para poder multiplicar con la matriz de transformación
    points_homo = np.hstack((points, np.ones((len(points), 1))))
    # Aplicar la transformación
    mirrored_points = np.dot(mirror_matrix, points_homo.T).T[:, :2]
    return mirrored_points

# TRANSFORMACIONES 3D



# PLOT DE FIGURAS

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

# DEFINIR FIGURAS Y LLAMAR A LA FUNCION PRINCIPAL

def pared_3d(y):
    return [[1, y, 1], [5, y, 1], [5, y, 4], [3, y, 6], [1, y, 4]]

casa_2d = [[1, 1], [5, 1], [5, 4], [3, 6], [1, 4]]
casa_3d = pared_3d(0) + pared_3d(4)

main()