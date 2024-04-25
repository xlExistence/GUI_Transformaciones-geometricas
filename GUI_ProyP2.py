import customtkinter as ctk, sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

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
        
    # Tab 2D
        Tab_2D = self.tabview.tab("2D")

        # Frame 1
        self.frame1 = ctk.CTkFrame(Tab_2D, fg_color="#201C1C")
        self.frame1.grid(row=0, column=0, sticky="nsew")

        menu_opciones = ctk.CTkOptionMenu(self.frame1, dynamic_resizing=False,
                                          values=["Rotación", "Traslación", "Espejo", "Cambio de escala"],
                                          command=self.mostrar_entradas)
        menu_opciones.place(relx=0.5, rely=0.1, anchor="center")

        # Rotación
        self.rotacion = []
        self.r_angulo_label = ctk.CTkLabel(self.frame1, text="Ángulo de rotación:", anchor="w")
        self.rotacion.append(self.r_angulo_label)
        self.r_angulo_input = ctk.CTkEntry(self.frame1, placeholder_text="Grados (°)")
        self.rotacion.append(self.r_angulo_input)
        self.r_coordenadas_centro_label = ctk.CTkLabel(self.frame1, text="Coordenadas del centro de rotación:", anchor="w")
        self.rotacion.append(self.r_coordenadas_centro_label)
        self.r_centro_x_input = ctk.CTkEntry(self.frame1, placeholder_text="Eje x")
        self.rotacion.append(self.r_centro_x_input)
        self.r_centro_y_input = ctk.CTkEntry(self.frame1, placeholder_text="Eje y")
        self.rotacion.append(self.r_centro_y_input)

        # Traslación
        self.traslacion = []
        self.t_coordenadas_label = ctk.CTkLabel(self.frame1, text="Coordenadas de traslación:", anchor="w")
        self.traslacion.append(self.t_coordenadas_label)
        self.t_x_input = ctk.CTkEntry(self.frame1, placeholder_text="Eje x")
        self.traslacion.append(self.t_x_input)
        self.t_y_input = ctk.CTkEntry(self.frame1, placeholder_text="Eje y")
        self.traslacion.append(self.t_y_input)

        # Espejo
        self.espejo = []
        self.e_eje_label = ctk.CTkLabel(self.frame1, text="Selecciona el eje de reflexión:", anchor="w")
        self.espejo.append(self.e_eje_label)
        self.e_eje = ctk.CTkOptionMenu(self.frame1, dynamic_resizing=False,
                                          values=["Eje x", "Eje y"])
        self.espejo.append(self.e_eje)
        
        # Cambio de escala
        self.cambio_escala = []
        self.ce_coordenadas_centro_label = ctk.CTkLabel(self.frame1, text="Ingresa los nuevos valores de escala:", anchor="w")
        self.cambio_escala.append(self.ce_coordenadas_centro_label)
        self.ce_x_input = ctk.CTkEntry(self.frame1, placeholder_text="Factor x")
        self.cambio_escala.append(self.ce_x_input)
        self.ce_y_input = ctk.CTkEntry(self.frame1, placeholder_text="Factor y")
        self.cambio_escala.append(self.ce_y_input)

        # Botón ejecutar
        btn = ctk.CTkButton(self.frame1, text="Aplicar")
        btn.place(relx=0.5, rely=0.9, anchor="center")

        self.frame1.grid_rowconfigure(0, weight=0)

        # Frame 2
        self.frame2 = ctk.CTkFrame(Tab_2D, fg_color="#818181")
        self.frame2.grid(row=0, column=1, padx=(10, 0), sticky="nsew")

        # fig = plt.figure(figsize=(5, 4))
        # ax = fig.add_subplot(111)
        # ax.plot([1, 2, 3, 4], [10, 20, 25, 30], color='lightblue', linewidth=3)
        # canvas = FigureCanvasTkAgg(fig, master=frame2)
        # canvas.draw()
        # canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

        Tab_2D.grid_columnconfigure(0, weight=1)
        Tab_2D.grid_columnconfigure(1, weight=2)
        Tab_2D.grid_rowconfigure(0, weight=1)

    # Tab 3D
        Tab_3D = self.tabview.tab("3D")
        Tab_3D.grid_columnconfigure(1, weight=1)

        self.mostrar_entradas("Rotación")
        self.actualizar_plot()
    
    # ---------------------------------------

    def actualizar_plot(self):
        fig, _ = plt.subplots()
        canvas = FigureCanvasTkAgg(fig, master=self.frame2)
        canvas.get_tk_widget().pack(side=ctk.TOP, fill=ctk.BOTH, expand=1)

        toolbar = NavigationToolbar2Tk(canvas, self.frame2, pack_toolbar=False)
        toolbar.update()
        toolbar.pack(side=ctk.BOTTOM, fill=ctk.X)

        self.update()

    def mostrar_entradas(self, opcion):
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

    def ocultar_entradas(self, e_restantes):
        for e in e_restantes:
            e.place_forget()

if __name__ == "__main__":
    app = GUI()
    app.mainloop()