import customtkinter as ctk

TRANSLATIONS = {
    "de": {
        "title":       "Währungsrechner",
        "label_in":    "Wähle deine Währung",
        "label_out":   "In welche Währung?",
        "convert_btn": "Umrechnen",
        "toggle_btn":  "🌐 English",
        "currencies":  ["Euro€", "US Dollar$"],
    },
    "en": {
        "title":       "Currency Converter",
        "label_in":    "Pick your currency",
        "label_out":   "In which currency?",
        "convert_btn": "Convert",
        "toggle_btn":  "🌐 Deutsch",
        "currencies":  ["Euro€", "US Dollar$"],
    },
}

class Window:
    def __init__(self, root):
        self.root = root
        self.lang = "de"
        
    
        self.label_in = ctk.CTkLabel(root, 150, 28, text="")
        self.label_in.grid(row=0, column=0) 

        self.txt_in = ctk.CTkEntry(root, height=20)
        self.txt_in.grid(row=3, column=0) 




        self.option_var_in = ctk.StringVar(value="Euro€")
        self.dropbox = ctk.CTkOptionMenu(master=root,variable=self.option_var_in, values=["Euro€", "US Dollar$"], )   # Deine Währung
        self.dropbox.grid(row=2, column=0)
        


        self.label_out = ctk.CTkLabel(root, 150, 28, text="")             # In Währung
        self.label_out.grid(row=0, column=2)


        self.textvar_out = ctk.StringVar()
        self.txt_out = ctk.CTkEntry(root, height=20, textvariable=self.textvar_out)         # Ausgabe Text
        self.txt_out.grid(row=3, column=2)   
        

        self.option_var_out = ctk.StringVar(value="Euro€")
        self.dropbox = ctk.CTkOptionMenu(master=root,variable=self.option_var_out, values=["Euro€", "US Dollar$"])  # Ausgabe währung 
        self.dropbox.grid(row=2, column=2)


        self.button = ctk.CTkButton(root, text="", command=self.convert)
        self.button.grid(pady=10, padx=10, row=4, column=1)

        self.btn_lang = ctk.CTkButton(root, text="", command=self.toggle_lang)
        self.btn_lang.grid(pady=10, padx=10, row=5, column=1)

        self.translator()


    def translator(self):
        t = TRANSLATIONS[self.lang]
        self.root.title(t["title"])
        self.label_in.configure(text=t["label_in"])
        self.label_out.configure(text=t["label_out"])
        self.button.configure(text=t["convert_btn"])
        self.btn_lang.configure(text=t["toggle_btn"])



    def toggle_lang(self):
        self.lang = "en" if self.lang == "de" else "de"
        self.translator()



    def convert(self):
        if self.option_var_in.get()== "Euro€" and self.option_var_out.get()=="US Dollar$":
            user_input = self.txt_in.get()
            rechnung = float(user_input) * 1.16
            str(rechnung)
            self.textvar_out.set(f"{rechnung:.2f}$")


        elif self.option_var_in.get()== "US Dollar$" and self.option_var_out.get()=="Euro€":
            user_input = self.txt_in.get()
            rechnung = float(user_input) * 0.86
            str(rechnung)
            self.textvar_out.set(f"{rechnung:.2f}€")

        else:
            user_input = self.txt_in.get()
            self.textvar_out.set(f"{user_input}€")


if __name__ == "__main__":
    root = ctk.CTk()
    root.geometry("470x200")
    gui = Window(root)
    root.mainloop()
