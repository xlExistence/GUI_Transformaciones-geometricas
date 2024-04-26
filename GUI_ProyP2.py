import customtkinter as ctk, sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import numpy as np

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")

class GUI(ctk.CTk):
    def __init__(self):
        super().__init__()

    # Propiedades de pantalla
        self.title("ProyP2. GUI_Transformaciones geométricas")
        self.geometry(f"{1100}x{600}")
        self.resizable(False, False)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.protocol("WM_DELETE_WINDOW", lambda: sys.exit())
        self.update()

    # TabView
        self.tabview = ctk.CTkTabview(self)
        self.tabview.grid(sticky="nsew", padx=10, pady=(0, 10))
        self.tabview.add("2D")
        self.tabview.add("3D")

     # ---------------------------------------

    # Tab 2D
        self.Tab_2D = self.tabview.tab("2D")

        # Frame 1 -----------------------------------------------------------------------------------
        self.frame1_1 = ctk.CTkFrame(self.Tab_2D, fg_color="#201C1C")
        self.frame1_1.grid(row=0, column=0, sticky="nsew")

        self.menu_opciones = ctk.CTkOptionMenu(self.frame1_1, dynamic_resizing=False,
                                          values=["Rotación", "Traslación", "Espejo", "Cambio de escala"],
                                          command=self.mostrar_entradas_2D)
        self.menu_opciones.place(relx=0.5, rely=0.1, anchor="center")

        #  Rotación
        self.rotacion = []
        self.r_angulo_label = ctk.CTkLabel(self.frame1_1, text="Ángulo de rotación:", anchor="w")
        self.rotacion.append(self.r_angulo_label)
        self.r_angulo_input = ctk.CTkEntry(self.frame1_1, placeholder_text="Grados (°)")
        self.rotacion.append(self.r_angulo_input)
        self.r_coordenadas_centro_label = ctk.CTkLabel(self.frame1_1, text="Coordenadas del centro de rotación:", anchor="w")
        self.rotacion.append(self.r_coordenadas_centro_label)
        self.r_centro_x_input = ctk.CTkEntry(self.frame1_1, placeholder_text="Eje x")
        self.rotacion.append(self.r_centro_x_input)
        self.r_centro_y_input = ctk.CTkEntry(self.frame1_1, placeholder_text="Eje y")
        self.rotacion.append(self.r_centro_y_input)

        #  Traslación
        self.traslacion = []
        self.t_coordenadas_label = ctk.CTkLabel(self.frame1_1, text="Valores del vector de traslación:", anchor="w")
        self.traslacion.append(self.t_coordenadas_label)
        self.t_x_input = ctk.CTkEntry(self.frame1_1, placeholder_text="Eje x")
        self.traslacion.append(self.t_x_input)
        self.t_y_input = ctk.CTkEntry(self.frame1_1, placeholder_text="Eje y")
        self.traslacion.append(self.t_y_input)

        #  Espejo
        self.espejo = []
        self.e_eje_label = ctk.CTkLabel(self.frame1_1, text="Selecciona el eje de reflexión:", anchor="w")
        self.espejo.append(self.e_eje_label)
        self.e_eje = ctk.CTkOptionMenu(self.frame1_1, dynamic_resizing=False,
                                          values=["Eje x", "Eje y"])
        self.espejo.append(self.e_eje)
        
        #  Cambio de escala
        self.cambio_escala = []
        self.ce_coordenadas_centro_label = ctk.CTkLabel(self.frame1_1, text="Ingresa los nuevos valores de escala:", anchor="w")
        self.cambio_escala.append(self.ce_coordenadas_centro_label)
        self.ce_x_input = ctk.CTkEntry(self.frame1_1, placeholder_text="Factor x")
        self.cambio_escala.append(self.ce_x_input)
        self.ce_y_input = ctk.CTkEntry(self.frame1_1, placeholder_text="Factor y")
        self.cambio_escala.append(self.ce_y_input)

        #  Botón ejecutar
        self.btn = ctk.CTkButton(self.frame1_1, text="Aplicar", command=self.aplicar_transformacion_2D)
        self.btn.place(relx=0.5, rely=0.9, anchor="center")

        # Frame 2 -----------------------------------------------------------------------------------
        self.frame1_2 = ctk.CTkFrame(self.Tab_2D, fg_color="#818181")
        self.frame1_2.grid(row=0, column=1, padx=(10, 0), sticky="nsew")


        self.Tab_2D.grid_columnconfigure(0, weight=1)
        self.Tab_2D.grid_columnconfigure(1, weight=2)
        self.Tab_2D.grid_rowconfigure(0, weight=1)

     # ---------------------------------------

    # Tab 3D
        self.Tab_3D = self.tabview.tab("3D")

        # Frame 1 -----------------------------------------------------------------------------------
        self.frame2_1 = ctk.CTkFrame(self.Tab_3D, fg_color="#201C1C")
        self.frame2_1.grid(row=0, column=0, sticky="nsew")

        self.menu_opciones_3D = ctk.CTkOptionMenu(self.frame2_1, dynamic_resizing=False,
                                          values=["Rotación", "Traslación", "Espejo", "Cambio de escala"],
                                          command=self.mostrar_entradas_3D)
        self.menu_opciones_3D.place(relx=0.5, rely=0.1, anchor="center")

        #  Rotación
        self.rotacion_3D = []
        self.r_angulo_label_3D = ctk.CTkLabel(self.frame2_1, text="Ángulo de rotación:", anchor="w")
        self.rotacion_3D.append(self.r_angulo_label_3D)
        self.r_angulo_input_3D = ctk.CTkEntry(self.frame2_1, placeholder_text="Grados (°)")
        self.rotacion_3D.append(self.r_angulo_input_3D)
        self.r_coordenadas_centro_label_3D = ctk.CTkLabel(self.frame2_1, text="Coordenadas del centro de rotación:", anchor="w")
        self.rotacion_3D.append(self.r_coordenadas_centro_label_3D)
        self.r_centro_x_input_3D = ctk.CTkEntry(self.frame2_1, placeholder_text="Eje x")
        self.rotacion_3D.append(self.r_centro_x_input_3D)
        self.r_centro_y_input_3D = ctk.CTkEntry(self.frame2_1, placeholder_text="Eje y")
        self.rotacion_3D.append(self.r_centro_y_input_3D)
        self.r_centro_z_input_3D = ctk.CTkEntry(self.frame2_1, placeholder_text="Eje z")
        self.rotacion_3D.append(self.r_centro_z_input_3D)
        self.r_eje_base_label_3D = ctk.CTkLabel(self.frame2_1, text="Eje base de rotación:", anchor="w")
        self.rotacion_3D.append(self.r_eje_base_label_3D)
        self.r_eje_base_3D = ctk.CTkOptionMenu(self.frame2_1, dynamic_resizing=False,
                                          values=["Eje x", "Eje y", "Eje z"])
        self.rotacion_3D.append(self.r_eje_base_3D)

        #  Traslación
        self.traslacion_3D = []
        self.t_coordenadas_label_3D = ctk.CTkLabel(self.frame2_1, text="Valores del vector de traslación:", anchor="w")
        self.traslacion_3D.append(self.t_coordenadas_label_3D)
        self.t_x_input_3D = ctk.CTkEntry(self.frame2_1, placeholder_text="Eje x")
        self.traslacion_3D.append(self.t_x_input_3D)
        self.t_y_input_3D = ctk.CTkEntry(self.frame2_1, placeholder_text="Eje y")
        self.traslacion_3D.append(self.t_y_input_3D)
        self.t_z_input_3D = ctk.CTkEntry(self.frame2_1, placeholder_text="Eje z")
        self.traslacion_3D.append(self.t_z_input_3D)

        #  Espejo
        self.espejo_3D = []
        self.e_eje_label_3D = ctk.CTkLabel(self.frame2_1, text="Selecciona el eje de reflexión:", anchor="w")
        self.espejo_3D.append(self.e_eje_label_3D)
        self.e_eje_3D = ctk.CTkOptionMenu(self.frame2_1, dynamic_resizing=False,
                                          values=["Eje x", "Eje y", "Eje z"])
        self.espejo_3D.append(self.e_eje_3D)
        
        #  Cambio de escala
        self.cambio_escala_3D = []
        self.ce_coordenadas_centro_label_3D = ctk.CTkLabel(self.frame2_1, text="Ingresa los nuevos valores de escala:", anchor="w")
        self.cambio_escala_3D.append(self.ce_coordenadas_centro_label_3D)
        self.ce_x_input_3D = ctk.CTkEntry(self.frame2_1, placeholder_text="Factor x")
        self.cambio_escala_3D.append(self.ce_x_input_3D)
        self.ce_y_input_3D = ctk.CTkEntry(self.frame2_1, placeholder_text="Factor y")
        self.cambio_escala_3D.append(self.ce_y_input_3D)
        self.ce_z_input_3D = ctk.CTkEntry(self.frame2_1, placeholder_text="Factor z")
        self.cambio_escala_3D.append(self.ce_z_input_3D)

        #  Botón ejecutar
        self.btn_3D = ctk.CTkButton(self.frame2_1, text="Aplicar", command=self.aplicar_transformacion_3D)
        self.btn_3D.place(relx=0.5, rely=0.9, anchor="center")

        # Frame 2 -----------------------------------------------------------------------------------
        self.frame2_2 = ctk.CTkFrame(self.Tab_3D, fg_color="#818181")
        self.frame2_2.grid(row=0, column=1, padx=(10, 0), sticky="nsew")


        self.Tab_3D.grid_columnconfigure(0, weight=1)
        self.Tab_3D.grid_columnconfigure(1, weight=2)
        self.Tab_3D.grid_rowconfigure(0, weight=1)
    
    # ---------------------------------------

        # Creación de figura para graficacion 2D
        self.fig_2D, self.ax_2D = plt.subplots()
        self.canvas_2D = FigureCanvasTkAgg(self.fig_2D, master=self.frame1_2)
        self.canvas_2D.get_tk_widget().pack(fill=ctk.BOTH, expand=1)

        toolbar = NavigationToolbar2Tk(self.canvas_2D, self.frame1_2, pack_toolbar=False)
        toolbar.update()
        toolbar.pack(side=ctk.BOTTOM, fill=ctk.X)
    
        # Elementos iniciales (mostrar botones y figuras)
        self.mostrar_entradas_2D("Rotación")
        self.mostrar_entradas_3D("Rotación")
        self.actualizar_plot_2D(Transformaciones.figura_2d())
        self.actualizar_plot_3D(Transformaciones.figura_3d())

    def actualizar_plot_2D(self, p, titulo='', new_p=None):
        self.ax_2D.clear()

        c_p = 'ro'
        c_l = 'r-'
        l = 'Original'
        for i in range(2):
            # Puntos
            self.ax_2D.plot([punto[0] for punto in p],
                            [punto[1] for punto in p],
                            c_p, label=l)
            # Lineas
            for i in range(len(p)):
                if i == len(p) - 1:
                    self.ax_2D.plot([p[0][0], p[len(p) - 1][0]], 
                                    [p[0][1], p[len(p) - 1][1]], c_l)
                    break
                self.ax_2D.plot([p[i][0], p[i+1][0]],
                                [p[i][1], p[i+1][1]], c_l)
            
            if new_p:
                p = new_p
                c_p = 'bo'
                c_l = 'b-'
                l = "Transformado"
            else:
                break

        self.ax_2D.set_xlabel('X')
        self.ax_2D.set_ylabel('Y')
        self.ax_2D.set_title(f'{titulo}')
        self.ax_2D.legend()
        self.ax_2D.grid(True)
        self.ax_2D.set_aspect('equal')

        # plt.xlabel('X')
        # plt.ylabel('Y')
        # plt.title(f"{titulo}")
        # plt.grid()
        # plt.axis('equal')

        self.canvas_2D.draw()

        self.update()
        self.bind_validacion()
    
    def actualizar_plot_3D(self, p, new_p=None):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        
        x = [1, 2, 3, 4, 5]
        y = [1, 2, 3, 4, 5]
        z = [1, 2, 3, 4, 5]
        
        ax.plot(x, y, z)
        
        canvas = FigureCanvasTkAgg(fig, master=self.frame2_2)
        canvas.get_tk_widget().pack(side=ctk.TOP, fill=ctk.BOTH, expand=1)
        
        toolbar = NavigationToolbar2Tk(canvas, self.frame2_2, pack_toolbar=False)
        toolbar.update()
        toolbar.pack(side=ctk.BOTTOM, fill=ctk.X)
        
        self.update()

    def mostrar_entradas_2D(self, opcion):
        seleccion = ["Rotación", "Traslación", "Espejo", "Cambio de escala"].index(opcion) + 1
        if seleccion == 1: # Rotación
            self.r_angulo_label.place(relx=0.1, rely=0.2)
            self.r_angulo_input.place(relx=0.15, rely=0.26, relwidth=0.7)            
            self.r_coordenadas_centro_label.place(relx=0.1, rely=0.35)
            self.r_centro_x_input.place(relx=0.15, rely=0.43, relwidth=0.7)
            self.r_centro_y_input.place(relx=0.15, rely=0.51, relwidth=0.7)

            self.ocultar_entradas((self.traslacion + self.espejo + self.cambio_escala))

        elif seleccion == 2: # Traslación
            self.t_coordenadas_label.place(relx=0.1, rely=0.2)
            self.t_x_input.place(relx=0.15, rely=0.28, relwidth=0.7)
            self.t_y_input.place(relx=0.15, rely=0.36, relwidth=0.7)

            self.ocultar_entradas((self.rotacion + self.espejo + self.cambio_escala))

        elif seleccion == 3: # Espejo (Reflexión)
            self.e_eje_label.place(relx=0.1, rely=0.2)
            self.e_eje.place(relx=0.5, rely=0.3, anchor="center")

            self.ocultar_entradas((self.rotacion + self.traslacion + self.cambio_escala))
        
        else: # Cambio de escala
            self.ce_coordenadas_centro_label.place(relx=0.1, rely=0.2)
            self.ce_x_input.place(relx=0.15, rely=0.28, relwidth=0.7)
            self.ce_y_input.place(relx=0.15, rely=0.36, relwidth=0.7)
            
            self.ocultar_entradas((self.rotacion + self.traslacion + self.espejo))

    def mostrar_entradas_3D(self, opcion):
        seleccion = ["Rotación", "Traslación", "Espejo", "Cambio de escala"].index(opcion) + 1
        if seleccion == 1: # Rotación
            self.r_angulo_label_3D.place(relx=0.1, rely=0.2)
            self.r_angulo_input_3D.place(relx=0.15, rely=0.26, relwidth=0.7)            
            self.r_coordenadas_centro_label_3D.place(relx=0.1, rely=0.35)
            self.r_centro_x_input_3D.place(relx=0.15, rely=0.43, relwidth=0.7)
            self.r_centro_y_input_3D.place(relx=0.15, rely=0.51, relwidth=0.7)
            self.r_centro_z_input_3D.place(relx=0.15, rely=0.59, relwidth=0.7)
            self.r_eje_base_label_3D.place(relx=0.1, rely=0.67)
            self.r_eje_base_3D.place(relx=0.5, rely=0.76, anchor="center")

            self.ocultar_entradas((self.traslacion_3D + self.espejo_3D + self.cambio_escala_3D))

        elif seleccion == 2: # Traslación
            self.t_coordenadas_label_3D.place(relx=0.1, rely=0.2)
            self.t_x_input_3D.place(relx=0.15, rely=0.28, relwidth=0.7)
            self.t_y_input_3D.place(relx=0.15, rely=0.36, relwidth=0.7)
            self.t_z_input_3D.place(relx=0.15, rely=0.44, relwidth=0.7)

            self.ocultar_entradas((self.rotacion_3D + self.espejo_3D + self.cambio_escala_3D))

        elif seleccion == 3: # Espejo (Reflexión)
            self.e_eje_label_3D.place(relx=0.1, rely=0.2)
            self.e_eje_3D.place(relx=0.5, rely=0.3, anchor="center")

            self.ocultar_entradas((self.rotacion_3D + self.traslacion_3D + self.cambio_escala_3D))
        
        else: # Cambio de escala
            self.ce_coordenadas_centro_label_3D.place(relx=0.1, rely=0.2)
            self.ce_x_input_3D.place(relx=0.15, rely=0.28, relwidth=0.7)
            self.ce_y_input_3D.place(relx=0.15, rely=0.36, relwidth=0.7)
            self.ce_z_input_3D.place(relx=0.15, rely=0.44, relwidth=0.7)
            
            self.ocultar_entradas((self.rotacion_3D + self.traslacion_3D + self.espejo_3D))

    def ocultar_entradas(self, e_restantes):
        for e in e_restantes:
            e.place_forget()

    def aplicar_transformacion_2D(self):
        transformacion = self.menu_opciones.get()
        puntos_originales = Transformaciones.figura_2d()

        if transformacion == "Rotación":
            angulo_r = float(self.r_angulo_input.get())
            centro_r_x = float(self.r_centro_x_input.get())
            centro_r_y = float(self.r_centro_y_input.get())

            puntos_rotados = [Transformaciones.rotacion_2d(punto, angulo_r, [centro_r_x, centro_r_y]) for punto in puntos_originales]

            self.actualizar_plot_2D(puntos_originales, "Transformación: Rotación", puntos_rotados)
        elif transformacion == "Traslación":
            vector_traslacion = [float(self.t_x_input.get()), float(self.t_y_input.get())]

            puntos_trasladados = Transformaciones.traslacion_2d(puntos_originales, vector_traslacion)

            self.actualizar_plot_2D(puntos_originales, "Transformación: Traslación", puntos_trasladados)
        elif transformacion == "Espejo":
            eje = self.e_eje.get()

            puntos_reflejados = Transformaciones.espejo_2d(puntos_originales, eje)

            self.actualizar_plot_2D(puntos_originales, "Transformación: Espejo", puntos_reflejados)
        elif transformacion == "Cambio de escala":
            factor_x = float(self.ce_x_input.get())
            factor_y = float(self.ce_y_input.get())

            puntos_escalados = Transformaciones.cambio_escala_2d(puntos_originales, [factor_x, factor_y])

            self.actualizar_plot_2D(puntos_originales, "Transformación: Cambio de escala", puntos_escalados)


    def aplicar_transformacion_3D(self):
        transformacion = self.menu_opciones_3D.get()

    def validar_entrada(self, entrada, can_neg):
        valor = entrada.get()

        if can_neg:
            if valor == '' or (valor == '-' and '.' not in valor):
                return True
            elif valor.replace('.', '', 1).lstrip('-').isdigit():
                return True
        elif valor.replace('.', '', 1).isdigit() and float(valor) >= 0:
            return True

        self.bell()
        entrada.delete(len(valor)-1, ctk.END)
        return False
    def bind_validacion(self):
        # Rotación
        self.r_angulo_input.bind("<KeyRelease>", lambda event: self.validar_entrada(self.r_angulo_input, True))
        self.r_centro_x_input.bind("<KeyRelease>", lambda event: self.validar_entrada(self.r_centro_x_input, False))
        self.r_centro_y_input.bind("<KeyRelease>", lambda event: self.validar_entrada(self.r_centro_y_input, False))

        # Traslación
        self.t_x_input.bind("<KeyRelease>", lambda event: self.validar_entrada(self.t_x_input, True))
        self.t_y_input.bind("<KeyRelease>", lambda event: self.validar_entrada(self.t_y_input, True))

        # Espejo
        # -

class Transformaciones():

# 2D

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
    
    def traslacion_2d(puntos, vector_t):
        # Suma de coordenadas con el vector de traslación
        return [[punto[0] + vector_t[0], punto[1] + vector_t[1]] for punto in puntos]
    
    def espejo_2d(puntos, eje):
        # Inversión de valores en base al eje
        if eje == "Eje x":
            return [[punto[0], -punto[1]] for punto in puntos]
        elif eje == "Eje y":
            return [[-punto[0], punto[1]] for punto in puntos]
        
    def cambio_escala_2d(puntos, factores):
        # Calcular el centroide
        centroid_x = sum(punto[0] for punto in puntos) / len(puntos)
        centroid_y = sum(punto[1] for punto in puntos) / len(puntos)

        # Ajustar cada punto al centroide
        puntos_ajustados = [[punto[0] - centroid_x, punto[1] - centroid_y] for punto in puntos]

        # Escalar los puntos ajustados
        puntos_escala = [[punto[0] * factores[0], punto[1] * factores[1]] for punto in puntos_ajustados]

        # Reajustar los puntos escalados al punto original
        puntos_reajustados = [[punto[0] + centroid_x, punto[1] + centroid_y] for punto in puntos_escala]

        return puntos_reajustados

# 3D

    

# FIGURAS

    def figura_2d():
        return [[1, 1], [5, 1], [5, 5], [1, 5]] # Cuadrado
    
    def figura_3d():
        return [[1, 0, 1], [5, 0, 1], [5, 0, 5], [1, 0, 5], [1, 4, 1], [5, 4, 1], [5, 4, 5], [1, 4, 5]] # Cubo

if __name__ == "__main__":
    app = GUI()
    app.mainloop()