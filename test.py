import numpy as np
import matplotlib.pyplot as plt

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

def rotate2D(points, angle):
    """Realiza una rotación 2D en los puntos dados."""
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle), 0],
                                [np.sin(angle), np.cos(angle), 0],
                                [0, 0, 1]])
    # Agregar una fila de unos para poder multiplicar con la matriz de transformación
    points_homo = np.hstack((points, np.ones((len(points), 1))))
    # Aplicar la transformación
    rotated_points = np.dot(rotation_matrix, points_homo.T).T[:, :2]
    return rotated_points

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

def scale2D(points, sx, sy):
    """Realiza un cambio de escala 2D en los puntos dados."""
    scale_matrix = np.array([[sx, 0, 0],
                             [0, sy, 0],
                             [0, 0, 1]])
    # Agregar una fila de unos para poder multiplicar con la matriz de transformación
    points_homo = np.hstack((points, np.ones((len(points), 1))))
    # Aplicar la transformación
    scaled_points = np.dot(scale_matrix, points_homo.T).T[:, :2]
    return scaled_points

def translate3D(points, tx, ty, tz):
    """Realiza una traslación 3D en los puntos dados."""
    translation_matrix = np.array([[1, 0, 0, tx],
                                   [0, 1, 0, ty],
                                   [0, 0, 1, tz],
                                   [0, 0, 0, 1]])
    # Agregar una fila de unos para poder multiplicar con la matriz de transformación
    points_homo = np.hstack((points, np.ones((len(points), 1))))
    # Aplicar la transformación
    translated_points = np.dot(translation_matrix, points_homo.T).T[:, :3]
    return translated_points

def rotate_x3D(points, angle):
    """Realiza una rotación 3D en los puntos dados sobre el eje x."""
    rotation_matrix = np.array([[1, 0, 0, 0],
                                [0, np.cos(angle), -np.sin(angle), 0],
                                [0, np.sin(angle), np.cos(angle), 0],
                                [0, 0, 0, 1]])
    # Agregar una fila de unos para poder multiplicar con la matriz de transformación
    points_homo = np.hstack((points, np.ones((len(points), 1))))
    # Aplicar la transformación
    rotated_points = np.dot(rotation_matrix, points_homo.T).T[:, :3]
    return rotated_points

def rotate_y3D(points, angle):
    """Realiza una rotación 3D en los puntos dados sobre el eje y."""
    rotation_matrix = np.array([[np.cos(angle), 0, np.sin(angle), 0],
                                [0, 1, 0, 0],
                                [-np.sin(angle), 0, np.cos(angle), 0],
                                [0, 0, 0, 1]])
    # Agregar una fila de unos para poder multiplicar con la matriz de transformación
    points_homo = np.hstack((points, np.ones((len(points), 1))))
    # Aplicar la transformación
    rotated_points = np.dot(rotation_matrix, points_homo.T).T[:, :3]
    return rotated_points

def rotate_z3D(points, angle):
    """Realiza una rotación 3D en los puntos dados sobre el eje z."""
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle), 0, 0],
                                [np.sin(angle), np.cos(angle), 0, 0],
                                [0, 0, 1, 0],
                                [0, 0, 0, 1]])
    # Agregar una fila de unos para poder multiplicar con la matriz de transformación
    points_homo = np.hstack((points, np.ones((len(points), 1))))
    # Aplicar la transformación
    rotated_points = np.dot(rotation_matrix, points_homo.T).T[:, :3]
    return rotated_points

def mirror3D(points, plane):
    """Realiza un espejo 3D en los puntos dados con respecto al plano dado."""
    if plane == 'xy':
        mirror_matrix = np.array([[1, 0, 0, 0],
                                  [0, 1, 0, 0],
                                  [0, 0, -1, 0],
                                  [0, 0, 0, 1]])
    elif plane == 'xz':
        mirror_matrix = np.array([[1, 0, 0, 0],
                                  [0, -1, 0, 0],
                                  [0, 0, 1, 0],
                                  [0, 0, 0, 1]])
    elif plane == 'yz':
        mirror_matrix = np.array([[-1, 0, 0, 0],
                                  [0, 1, 0, 0],
                                  [0, 0, 1, 0],
                                  [0, 0, 0, 1]])
    else:
        raise ValueError("Plane must be 'xy', 'xz', or 'yz'")
    # Agregar una fila de unos para poder multiplicar con la matriz de transformación
    points_homo = np.hstack((points, np.ones((len(points), 1))))
    # Aplicar la transformación
    mirrored_points = np.dot(mirror_matrix, points_homo.T).T[:, :3]
    return mirrored_points

def scale3D(points, sx, sy, sz):
    """Realiza un cambio de escala 3D en los puntos dados."""
    scale_matrix = np.array([[sx, 0, 0, 0],
                             [0, sy, 0, 0],
                             [0, 0, sz, 0],
                             [0, 0, 0, 1]])
    # Agregar una fila de unos para poder multiplicar con la matriz de transformación
    points_homo = np.hstack((points, np.ones((len(points), 1))))
    # Aplicar la transformación
    scaled_points = np.dot(scale_matrix, points_homo.T).T[:, :3]
    return scaled_points


def plot_object(points):
    """Visualiza un objeto dado por una lista de puntos en 2D."""
    plt.figure()
    plt.plot(points[:, 0], points[:, 1], 'b-')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Objeto Original')
    plt.grid(True)
    plt.axis('equal')

def plot_transformed_object(points, transformed_points, transform_name):
    """Visualiza un objeto original y su transformación en 2D."""
    plt.figure()
    plt.plot(points[:, 0], points[:, 1], 'b-', label='Original')
    plt.plot(transformed_points[:, 0], transformed_points[:, 1], 'r-', label=transform_name)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Transformación ' + transform_name)
    plt.grid(True)
    plt.axis('equal')
    plt.legend()

# Funciones de visualización
def plot_object2D(points, title):
    """Visualiza un objeto dado por una lista de puntos en 2D."""
    plt.figure()
    plt.plot(points[:, 0], points[:, 1], 'b-')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title(title)
    plt.grid(True)
    plt.axis('equal')

def plot_object3D(points, title):
    """Visualiza un objeto dado por una lista de puntos en 3D."""
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_trisurf(points[:, 0], points[:, 1], points[:, 2], color='b')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(title)

def visualize_transformations2D(original_points, transformed_points_list, transformation_names):
    """Visualiza un objeto original y sus transformaciones en 2D."""
    plt.figure()
    plt.plot(original_points[:, 0], original_points[:, 1], 'b-', label='Original')
    for i, points in enumerate(transformed_points_list):
        plt.plot(points[:, 0], points[:, 1], label=transformation_names[i])
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Transformaciones 2D')
    plt.grid(True)
    plt.axis('equal')
    plt.legend()

def visualize_transformations3D(original_points, transformed_points_list, transformation_names):
    """Visualiza un objeto original y sus transformaciones en 3D."""
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_trisurf(original_points[:, 0], original_points[:, 1], original_points[:, 2], color='b', label='Original')
    for i, points in enumerate(transformed_points_list):
        ax.plot_trisurf(points[:, 0], points[:, 1], points[:, 2], label=transformation_names[i])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Transformaciones 3D')
    ax.legend()

# Ejemplo de uso
# Definir un conjunto de puntos que representan un objeto en 2D
object_points_2D = np.array([[0, 0],
                              [1, 0],
                              [1, 1],
                              [0, 1],
                              [0, 0]])

# Definir un conjunto de puntos que representan un objeto en 3D
object_points_3D = np.array([[0, 0, 0],
                              [1, 0, 0],
                              [1, 1, 0],
                              [0, 1, 0],
                              [0, 0, 1]])

# Realizar las transformaciones en 2D
translated_points_2D = translate2D(object_points_2D, 1, 1)
rotated_points_2D = rotate2D(object_points_2D, np.pi/4)
mirrored_points_2D = mirror2D(object_points_2D, 'x')
scaled_points_2D = scale2D(object_points_2D, 2, 0.5)

# Realizar las transformaciones en 3D
translated_points_3D = translate3D(object_points_3D, 1, 1, 1)
rotated_x_points_3D = rotate_x3D(object_points_3D, np.pi/4)
rotated_y_points_3D = rotate_y3D(object_points_3D, np.pi/4)
rotated_z_points_3D = rotate_z3D(object_points_3D, np.pi/4)
mirrored_points_3D = mirror3D(object_points_3D, 'xy')
scaled_points_3D = scale3D(object_points_3D, 2, 0.5, 3)

# Visualizar las transformaciones en 2D
visualize_transformations2D(object_points_2D, [translated_points_2D, rotated_points_2D, mirrored_points_2D, scaled_points_2D],
                            ['Traslación', 'Rotación', 'Espejo', 'Cambio de Escala'])
plt.show()

# Visualizar las transformaciones en 3D
visualize_transformations3D(object_points_3D, [translated_points_3D, rotated_x_points_3D, rotated_y_points_3D,
                                                rotated_z_points_3D, mirrored_points_3D, scaled_points_3D],
                            ['Traslación', 'Rotación X', 'Rotación Y', 'Rotación Z', 'Espejo', 'Cambio de Escala'])
plt.show()
