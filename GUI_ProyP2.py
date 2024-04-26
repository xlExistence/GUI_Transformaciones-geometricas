import customtkinter as ctk, sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import numpy as np
import ast
import copy

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

        self.ventana_aux = None

        self.figura2D = []
        self.uniones2D = []
        self.figura3D = []
        self.uniones3D = []

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

        #  Botón agregar punto
        self.btn_add = ctk.CTkButton(self.frame1_1, text="+", command=self.ventana_añadir_2D)
        self.btn_add.place(relx=0.87, rely=0.02, relwidth=0.09)
        #  Botón unir punto
        self.btn_bind = ctk.CTkButton(self.frame1_1, text="---", command=self.ventana_unir_2D)
        self.btn_bind.place(relx=0.87, rely=0.085, relwidth=0.09)

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
        self.e_eje_label = ctk.CTkLabel(self.frame1_1, text="Selecciona el plano de reflexión:", anchor="w")
        self.espejo.append(self.e_eje_label)
        self.e_eje = ctk.CTkOptionMenu(self.frame1_1, dynamic_resizing=False,
                                          values=["Plano x", "Plano y"])
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

        #  Botón agregar punto
        self.btn_add_3D = ctk.CTkButton(self.frame2_1, text="+", command=self.ventana_añadir_3D)
        self.btn_add_3D.place(relx=0.87, rely=0.02, relwidth=0.09)
        #  Botón unir punto
        self.btn_bind_3D = ctk.CTkButton(self.frame2_1, text="---", command=self.ventana_unir_3D)
        self.btn_bind_3D.place(relx=0.87, rely=0.085, relwidth=0.09)

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
        self.e_eje_label_3D = ctk.CTkLabel(self.frame2_1, text="Selecciona el plano de reflexión:", anchor="w")
        self.espejo_3D.append(self.e_eje_label_3D)
        self.e_eje_3D = ctk.CTkOptionMenu(self.frame2_1, dynamic_resizing=False,
                                          values=["Plano xy", "Plano xz", "Plano yz"])
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

        # Creación de figura para graficacion 3D
        self.fig_3D = plt.figure()
        self.ax_3D = self.fig_3D.add_subplot(111, projection='3d')
        self.canvas_3D = FigureCanvasTkAgg(self.fig_3D, master=self.frame2_2)
        self.canvas_3D.get_tk_widget().pack(fill=ctk.BOTH, expand=1)

        toolbar_3D = NavigationToolbar2Tk(self.canvas_3D, self.frame2_2, pack_toolbar=False)
        toolbar_3D.update()
        toolbar_3D.pack(side=ctk.BOTTOM, fill=ctk.X)
    
        # Elementos iniciales (mostrar botones y figuras)
        self.mostrar_entradas_2D("Rotación")
        self.mostrar_entradas_3D("Rotación")
        self.actualizar_plot_2D(self.figura2D)
        self.actualizar_plot_3D(self.figura3D)

    
    def ventana_añadir_2D(self):
        if not self.ventana_aux:
            self.ventana_aux = ctk.CTkToplevel(self)
            self.ventana_aux.title("Añadir punto")
            self.ventana_aux.geometry(f"{300}x{200}")
            self.ventana_aux.resizable(False, False)
            self.ventana_aux.protocol("WM_DELETE_WINDOW", self.close_ventana)

            self.p_label = ctk.CTkLabel(self.ventana_aux, text="Ingresa las coordenadas del punto:")
            self.p_label.place(relx=0.5, rely=0.1, anchor="center")

            self.p_eje_x = ctk.CTkEntry(self.ventana_aux, placeholder_text="x")
            self.p_eje_x.place(relx=0.5, rely=0.3, anchor="center")
            self.p_eje_y = ctk.CTkEntry(self.ventana_aux, placeholder_text="y")
            self.p_eje_y.place(relx=0.5, rely=0.5, anchor="center")

            self.p_añadir_btn = ctk.CTkButton(self.ventana_aux, text="Añadir", command=self.añadir_punto_2D)
            self.p_añadir_btn.place(relx=0.5, rely=0.7, anchor="center")

    def ventana_unir_2D(self):
        if not self.ventana_aux:
            self.ventana_aux = ctk.CTkToplevel(self)
            self.ventana_aux.title("Unir puntos")
            self.ventana_aux.geometry(f"{300}x{200}")
            self.ventana_aux.resizable(False, False)
            self.ventana_aux.protocol("WM_DELETE_WINDOW", self.close_ventana)

            if len(self.figura2D) >= 2:
                self.ups_label = ctk.CTkLabel(self.ventana_aux, text="Selecciona los puntos a unir:")
                self.ups_label.place(relx=0.5, rely=0.1, anchor="center")

                self.u_p1_2D = ctk.CTkOptionMenu(self.ventana_aux, dynamic_resizing=False,
                                                values=list(map(str, self.figura2D)),
                                                command=self.punto_seleccionado_2D)
                self.u_p1_2D.place(relx=0.3, rely=0.3, anchor="center", relwidth=0.3)
            else:
                self.ups_label = ctk.CTkLabel(self.ventana_aux, text="No es posible unir puntos")
                self.ups_label.place(relx=0.5, rely=0.3, anchor="center")

                self.p_cerrar_btn = ctk.CTkButton(self.ventana_aux, text="Cerrar", command=self.close_ventana)
                self.p_cerrar_btn.place(relx=0.5, rely=0.7, anchor="center")
    def punto_seleccionado_2D(self, p1):
        puntos_restantes = copy.deepcopy(self.figura2D)
        puntos_restantes.remove(ast.literal_eval(p1))
        self.u_p2_2D = ctk.CTkOptionMenu(self.ventana_aux, dynamic_resizing=False,
                                        values=list(map(str, puntos_restantes)))
        self.u_p2_2D.place(relx=0.7, rely=0.3, anchor="center", relwidth=0.3)

        self.p_unir_btn = ctk.CTkButton(self.ventana_aux, text="Unir", command=self.unir_puntos_2D)
        self.p_unir_btn.place(relx=0.5, rely=0.7, anchor="center")
        
    def añadir_punto_2D(self):
        x = float(self.p_eje_x.get()) if '.' in self.p_eje_x.get() else int(self.p_eje_x.get())
        y = float(self.p_eje_y.get()) if '.' in self.p_eje_y.get() else int(self.p_eje_y.get())

        if [x, y] not in self.figura2D:
            self.figura2D.append([x, y])
            
        self.actualizar_plot_2D(self.figura2D)

        self.ventana_aux.destroy()
        self.ventana_aux = None
    def unir_puntos_2D(self):
        i_p1 = self.figura2D.index(ast.literal_eval(self.u_p1_2D.get()))
        i_p2 = self.figura2D.index(ast.literal_eval(self.u_p2_2D.get()))

        if [i_p1, i_p2] not in self.uniones2D and [i_p2, i_p1] not in self.uniones2D:
            self.uniones2D.append([i_p1, i_p2])

        self.actualizar_plot_2D(self.figura2D)

        self.ventana_aux.destroy()
        self.ventana_aux = None
    

    def ventana_añadir_3D(self):
        if not self.ventana_aux:
            self.ventana_aux = ctk.CTkToplevel(self)
            self.ventana_aux.title("Añadir punto")
            self.ventana_aux.geometry(f"{300}x{230}")
            self.ventana_aux.resizable(False, False)
            self.ventana_aux.protocol("WM_DELETE_WINDOW", self.close_ventana)

            self.p_label_3D = ctk.CTkLabel(self.ventana_aux, text="Ingresa las coordenadas del punto:")
            self.p_label_3D.place(relx=0.5, rely=0.1, anchor="center")

            self.p_eje_x_3D = ctk.CTkEntry(self.ventana_aux, placeholder_text="x")
            self.p_eje_x_3D.place(relx=0.5, rely=0.27, anchor="center")
            self.p_eje_y_3D = ctk.CTkEntry(self.ventana_aux, placeholder_text="y")
            self.p_eje_y_3D.place(relx=0.5, rely=0.44, anchor="center")
            self.p_eje_z_3D = ctk.CTkEntry(self.ventana_aux, placeholder_text="z")
            self.p_eje_z_3D.place(relx=0.5, rely=0.61, anchor="center")

            self.p_añadir_btn_3D = ctk.CTkButton(self.ventana_aux, text="Añadir", command=self.añadir_punto_3D)
            self.p_añadir_btn_3D.place(relx=0.5, rely=0.78, anchor="center")

    def ventana_unir_3D(self):
        if not self.ventana_aux:
            self.ventana_aux = ctk.CTkToplevel(self)
            self.ventana_aux.title("Unir puntos")
            self.ventana_aux.geometry(f"{330}x{200}")
            self.ventana_aux.resizable(False, False)
            self.ventana_aux.protocol("WM_DELETE_WINDOW", self.close_ventana)

            if len(self.figura3D) >= 2:
                self.ups_label_3D = ctk.CTkLabel(self.ventana_aux, text="Selecciona los puntos a unir:")
                self.ups_label_3D.place(relx=0.5, rely=0.1, anchor="center")

                self.u_p1_3D = ctk.CTkOptionMenu(self.ventana_aux, dynamic_resizing=False,
                                                values=list(map(str, self.figura3D)),
                                                command=self.punto_seleccionado_3D)
                self.u_p1_3D.place(relx=0.3, rely=0.3, anchor="center", relwidth=0.3)
            else:
                self.ups_label_3D = ctk.CTkLabel(self.ventana_aux, text="No es posible unir puntos")
                self.ups_label_3D.place(relx=0.5, rely=0.3, anchor="center")

                self.p_cerrar_btn_3D = ctk.CTkButton(self.ventana_aux, text="Cerrar", command=self.close_ventana)
                self.p_cerrar_btn_3D.place(relx=0.5, rely=0.7, anchor="center")
    def punto_seleccionado_3D(self, p1):
        puntos_restantes = copy.deepcopy(self.figura3D)
        puntos_restantes.remove(ast.literal_eval(p1))
        self.u_p2_3D = ctk.CTkOptionMenu(self.ventana_aux, dynamic_resizing=False,
                                        values=list(map(str, puntos_restantes)))
        self.u_p2_3D.place(relx=0.7, rely=0.3, anchor="center", relwidth=0.3)

        self.p_unir_btn_3D = ctk.CTkButton(self.ventana_aux, text="Unir", command=self.unir_puntos_3D)
        self.p_unir_btn_3D.place(relx=0.5, rely=0.7, anchor="center")

    def añadir_punto_3D(self):
        x = float(self.p_eje_x_3D.get()) if '.' in self.p_eje_x_3D.get() else int(self.p_eje_x_3D.get())
        y = float(self.p_eje_y_3D.get()) if '.' in self.p_eje_y_3D.get() else int(self.p_eje_y_3D.get())
        z = float(self.p_eje_z_3D.get()) if '.' in self.p_eje_z_3D.get() else int(self.p_eje_z_3D.get())

        if [x, y, z] not in self.figura3D:
            self.figura3D.append([x, y, z])
            
        self.actualizar_plot_3D(self.figura3D)

        self.ventana_aux.destroy()
        self.ventana_aux = None
    def unir_puntos_3D(self):
        i_p1 = self.figura3D.index(ast.literal_eval(self.u_p1_3D.get()))
        i_p2 = self.figura3D.index(ast.literal_eval(self.u_p2_3D.get()))

        if [i_p1, i_p2] not in self.uniones3D and [i_p2, i_p1] not in self.uniones3D:
            self.uniones3D.append([i_p1, i_p2])

        self.actualizar_plot_3D(self.figura3D)

        self.ventana_aux.destroy()
        self.ventana_aux = None


    def close_ventana(self):
        self.ventana_aux.destroy()
        self.ventana_aux = None


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
            for i in range(len(self.uniones2D)):
                self.ax_2D.plot([p[self.uniones2D[i][0]][0], p[self.uniones2D[i][1]][0]],
                                [p[self.uniones2D[i][0]][1], p[self.uniones2D[i][1]][1]], c_l)
            
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

        self.canvas_2D.draw()

        self.update()
        self.bind_validacion()
    
    def actualizar_plot_3D(self, p, titulo='', new_p=None):
        self.ax_3D.clear()
        
        c_p_l = 'r'
        l = 'Original'
        for i in range(2):
            # Puntos
            self.ax_3D.scatter([punto[0] for punto in p],
                               [punto[1] for punto in p],
                               [punto[2] for punto in p],
                               c=c_p_l, label=l)
            # Lineas
            for i in range(len(self.uniones3D)):
                self.ax_3D.plot([p[self.uniones3D[i][0]][0], p[self.uniones3D[i][1]][0]],
                                [p[self.uniones3D[i][0]][1], p[self.uniones3D[i][1]][1]], 
                                [p[self.uniones3D[i][0]][2], p[self.uniones3D[i][1]][2]], c=c_p_l)
            
            if new_p:
                p = new_p
                c_p_l = 'b'
                l = "Transformado"
            else:
                break

        self.ax_3D.set_xlabel('X')
        self.ax_3D.set_ylabel('Y')
        self.ax_3D.set_zlabel('Z')
        self.ax_3D.set_title(f'{titulo}')
        self.ax_3D.legend()
        self.ax_3D.grid(True)
        self.ax_3D.set_aspect('equal')
        
        self.canvas_3D.draw()
        
        self.update()
        self.bind_validacion_3D()

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
        puntos_originales = self.figura2D

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
        puntos_originales = self.figura3D

        if transformacion == "Rotación":
            angulo_r = float(self.r_angulo_input_3D.get())
            centro_r_x = float(self.r_centro_x_input_3D.get())
            centro_r_y = float(self.r_centro_y_input_3D.get())
            centro_r_z = float(self.r_centro_z_input_3D.get())
            eje_r = self.r_eje_base_3D.get()

            puntos_rotados = [Transformaciones.rotacion_3d(punto, angulo_r, [centro_r_x, centro_r_y, centro_r_z], eje_r) for punto in puntos_originales]

            self.actualizar_plot_3D(puntos_originales, "Transformación: Rotación 3D", puntos_rotados)
        elif transformacion == "Traslación":
            vector_traslacion = [float(self.t_x_input_3D.get()), float(self.t_y_input_3D.get()), float(self.t_z_input_3D.get())]

            puntos_trasladados = Transformaciones.traslacion_3d(puntos_originales, vector_traslacion)

            self.actualizar_plot_3D(puntos_originales, "Transformación: Traslación 3D", puntos_trasladados)
        elif transformacion == "Espejo":
            eje = self.e_eje_3D.get()

            puntos_reflejados = Transformaciones.espejo_3d(puntos_originales, eje)

            self.actualizar_plot_3D(puntos_originales, "Transformación: Espejo 3D", puntos_reflejados)
        elif transformacion == "Cambio de escala":
            factor_x = float(self.ce_x_input_3D.get())
            factor_y = float(self.ce_y_input_3D.get())
            factor_z = float(self.ce_z_input_3D.get())

            puntos_escalados = Transformaciones.cambio_escala_3d(puntos_originales, [factor_x, factor_y, factor_z])

            self.actualizar_plot_3D(puntos_originales, "Transformación: Cambio de escala 3D", puntos_escalados)


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
        self.r_centro_x_input.bind("<KeyRelease>", lambda event: self.validar_entrada(self.r_centro_x_input, True))
        self.r_centro_y_input.bind("<KeyRelease>", lambda event: self.validar_entrada(self.r_centro_y_input, True))

        # Traslación
        self.t_x_input.bind("<KeyRelease>", lambda event: self.validar_entrada(self.t_x_input, True))
        self.t_y_input.bind("<KeyRelease>", lambda event: self.validar_entrada(self.t_y_input, True))

        # Espejo
        # -

        # Cambio de escala
        self.ce_x_input.bind("<KeyRelease>", lambda event: self.validar_entrada(self.ce_x_input, False))
        self.ce_y_input.bind("<KeyRelease>", lambda event: self.validar_entrada(self.ce_y_input, False))
    def bind_validacion_3D(self):
        # Rotación
        self.r_angulo_input_3D.bind("<KeyRelease>", lambda event: self.validar_entrada(self.r_angulo_input_3D, True))
        self.r_centro_x_input_3D.bind("<KeyRelease>", lambda event: self.validar_entrada(self.r_centro_x_input_3D, True))
        self.r_centro_y_input_3D.bind("<KeyRelease>", lambda event: self.validar_entrada(self.r_centro_y_input_3D, True))
        self.r_centro_z_input_3D.bind("<KeyRelease>", lambda event: self.validar_entrada(self.r_centro_z_input_3D, True))

        # Traslación
        self.t_x_input_3D.bind("<KeyRelease>", lambda event: self.validar_entrada(self.t_x_input_3D, True))
        self.t_y_input_3D.bind("<KeyRelease>", lambda event: self.validar_entrada(self.t_y_input_3D, True))
        self.t_z_input_3D.bind("<KeyRelease>", lambda event: self.validar_entrada(self.t_z_input_3D, True))

        # Espejo
        # -

        # Cambio de escala
        self.ce_x_input_3D.bind("<KeyRelease>", lambda event: self.validar_entrada(self.ce_x_input_3D, False))
        self.ce_y_input_3D.bind("<KeyRelease>", lambda event: self.validar_entrada(self.ce_y_input_3D, False))
        self.ce_z_input_3D.bind("<KeyRelease>", lambda event: self.validar_entrada(self.ce_z_input_3D, False))

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
        if eje == "Plano x":
            return [[punto[0], -punto[1]] for punto in puntos]
        elif eje == "Plano y":
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

    def rotacion_3d(punto, angulo, centro, eje):
        # Transformar el ángulo a radianes
        theta = np.radians(angulo)
        
        # Matriz de rotación según el eje seleccionado
        if eje == 'Eje x':
            matriz_rotacion = np.array([[1, 0, 0],
                                        [0, np.cos(theta), -np.sin(theta)],
                                        [0, np.sin(theta), np.cos(theta)]])
        elif eje == 'Eje y':
            matriz_rotacion = np.array([[np.cos(theta), 0, np.sin(theta)],
                                        [0, 1, 0],
                                        [-np.sin(theta), 0, np.cos(theta)]])
        elif eje == 'Eje z':
            matriz_rotacion = np.array([[np.cos(theta), -np.sin(theta), 0],
                                        [np.sin(theta), np.cos(theta), 0],
                                        [0, 0, 1]])
            
        # Calcular las coordenadas relativas al centro de rotación
        p_rel = np.array(punto) - np.array(centro)
        
        # Aplicar la matriz de rotación
        p_rotado = np.dot(matriz_rotacion, p_rel)

        # Regresar a las coordenadas originales
        p_rotado += np.array(centro)
        return p_rotado
    
    def traslacion_3d(puntos, vector_t):
        # Suma de coordenadas con el vector de traslación
        return [[punto[0] + vector_t[0], punto[1] + vector_t[1], punto[2] + vector_t[2]] for punto in puntos]

    def espejo_3d(puntos, plano):
        # Inversión de valores en base al plano
        if plano == "Plano xy":
            return [[punto[0], punto[1], -punto[2]] for punto in puntos]
        elif plano == "Plano xz":
            return [[punto[0], -punto[1], punto[2]] for punto in puntos]
        elif plano == "Plano yz":
            return [[-punto[0], punto[1], punto[2]] for punto in puntos]
    
    def cambio_escala_3d(puntos, factores):
        # Calcular el centroide
        centroid_x = sum(punto[0] for punto in puntos) / len(puntos)
        centroid_y = sum(punto[1] for punto in puntos) / len(puntos)
        centroid_z = sum(punto[2] for punto in puntos) / len(puntos)

        # Ajustar cada punto al centroide
        puntos_ajustados = [[punto[0] - centroid_x, punto[1] - centroid_y, punto[2] - centroid_z] for punto in puntos]

        # Escalar los puntos ajustados
        puntos_escala = [[punto[0] * factores[0], punto[1] * factores[1], punto[2] * factores[2]] for punto in puntos_ajustados]

        # Reajustar los puntos escalados al punto original
        puntos_reajustados = [[punto[0] + centroid_x, punto[1] + centroid_y, punto[2] + centroid_z] for punto in puntos_escala]

        return puntos_reajustados

if __name__ == "__main__":
    app = GUI()
    app.mainloop()