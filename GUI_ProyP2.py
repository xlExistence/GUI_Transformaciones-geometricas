import customtkinter
import tkinter
import tkinter.messagebox

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

class GUI(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Propiedades de pantalla
        self.title("ProyP2. GUI_Transformaciones geométricas")
        self.geometry(f"{1100}x{580}")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # TabView
        self.tabview = customtkinter.CTkTabview(self)
        self.tabview.grid(sticky="nsew", padx=10, pady=(0, 10))
        self.tabview.add("2D")
        self.tabview.add("3D")
        
        Tab_2D = self.tabview.tab("2D")

        self.textbox = customtkinter.CTkTextbox(Tab_2D)
        self.textbox.grid(row=0, column=0, sticky="nsew")
        self.textbox.insert("0.0", "CTkTextbox\n\n" + "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.\n\n" * 20)

        # frame1 = customtkinter.CTkFrame(Tab_2D)
        # frame1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        # label_frame1 = customtkinter.CTkLabel(frame1, text="Frame 1")
        # label_frame1.pack()

        frame2 = customtkinter.CTkFrame(Tab_2D)
        frame2.grid(row=0, column=1, sticky="nsew")
        label_frame2 = customtkinter.CTkLabel(frame2, text="Frame 2")
        label_frame2.pack()

        Tab_2D.grid_columnconfigure(0, weight=1)
        Tab_2D.grid_columnconfigure(1, weight=6)
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

        Tab_3D = self.tabview.tab("3D")
        Tab_3D.grid_columnconfigure(1, weight=1)
        
    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")

if __name__ == "__main__":
    app = GUI()
    app.mainloop()