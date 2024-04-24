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
        self.geometry(f"{1100}x{580}")

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
        frame1 = ctk.CTkFrame(Tab_2D, fg_color="#201C1C")
        frame1.grid(row=0, column=0, sticky="nsew")

        label_frame1 = ctk.CTkLabel(frame1, text=f"{frame1.cget("fg_color")}")
        label_frame1.grid(row=0, column=0)

        # btn = ctk.CTkButton(frame1, command=self.update_window)
        # btn.grid(row=1, column=0)

        # Frame 2
        self.frame2 = ctk.CTkFrame(Tab_2D, fg_color="#818181")
        self.frame2.grid(row=0, column=1, padx=(10, 0), sticky="nsew")

        # fig = plt.figure(figsize=(5, 4))
        # ax = fig.add_subplot(111)
        # ax.plot([1, 2, 3, 4], [10, 20, 25, 30], color='lightblue', linewidth=3)
        # canvas = FigureCanvasTkAgg(fig, master=frame2)
        # canvas.draw()
        # canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

        frame1.grid_rowconfigure(0, weight=1)
        frame1.grid_rowconfigure(1, weight=5)

        Tab_2D.grid_columnconfigure(0, weight=1)
        Tab_2D.grid_columnconfigure(1, weight=2)
        Tab_2D.grid_rowconfigure(0, weight=1)

        # create radiobutton frame
        # self.radiobutton_frame = customtkinter.CTkFrame(Tab_2D)
        # self.radiobutton_frame.grid(row=0, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
        # self.radio_var = tkinter.IntVar(value=0)
        # self.label_radio_group = customtkinter.CTkLabel(master=Tab_2D, text="CTkRadioButton Group:")
        # self.label_radio_group.grid(row=0, column=1, columnspan=10, padx=10, pady=10, sticky="")
        # self.radio_button_1 = customtkinter.CTkRadioButton(master=Tab_2D, variable=self.radio_var, value=0)
        # self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")
        # self.radio_button_2 = customtkinter.CTkRadioButton(master=Tab_2D, variable=self.radio_var, value=1)
        # self.radio_button_2.grid(row=2, column=2, pady=10, padx=20, sticky="n")
        # self.radio_button_3 = customtkinter.CTkRadioButton(master=Tab_2D, variable=self.radio_var, value=2)
        # self.radio_button_3.grid(row=3, column=2, pady=10, padx=20, sticky="n")

    # Tab 3D
        Tab_3D = self.tabview.tab("3D")
        Tab_3D.grid_columnconfigure(1, weight=1)

        self.update_window()
    
    def update_window(self):
        fig, _ = plt.subplots()
        canvas = FigureCanvasTkAgg(fig, master=self.frame2)
        canvas.get_tk_widget().pack(side=ctk.TOP, fill=ctk.BOTH, expand=1)

        toolbar = NavigationToolbar2Tk(canvas, self.frame2, pack_toolbar=False)
        toolbar.update()
        toolbar.pack(side=ctk.BOTTOM, fill=ctk.X)

        self.update()
        
    def open_input_dialog_event(self):
        dialog = ctk.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        ctk.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")

if __name__ == "__main__":
    app = GUI()
    app.mainloop()