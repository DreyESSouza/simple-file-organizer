import customtkinter as ctk
import logic

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class Root(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Organizer")
        self.geometry("230x140")
        self.resizable(False, False)

        self.label = ctk.CTkLabel(self, text="Choose a folder to organize!", font=("Arial",15))
        self.label.grid(row=0, column=0, padx=23, pady=10)

        self.button = ctk.CTkButton(self, text= "Click here", command=self.organize)
        self.button.grid(row=1, column=0, padx=23, pady=8)

        self.result = ctk.CTkLabel(self, text= "")
        self.result.grid(row=2, column=0, pady=6)

    def show_result(self, chosen_folder):
        if chosen_folder:
            self.result.configure(text=f"Files organized in:\n{chosen_folder}")
        else:
            self.result.configure(text="")

    def organize(self):
        chosen_folder = logic.choose_folder()
        logic.select_and_organize(chosen_folder)
        self.show_result(chosen_folder)

if __name__ == "__main__":
    root = Root()
    root.mainloop()