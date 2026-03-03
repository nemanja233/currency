import customtkinter as ctk

class Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency converter")


    
        self.label = ctk.CTkLabel(root, 150, 28, text="Pick your currency")
        self.label.grid(row=0, column=0) 

        self.txt_in = ctk.CTkEntry(root, height=20)
        self.txt_in.grid(row=3, column=0) 




        self.option_var_in = ctk.StringVar(value="Euro€")
        self.dropbox = ctk.CTkOptionMenu(master=root,variable=self.option_var_in, values=["Euro€", "US Dollar$"], )   # Deine Währung
        self.dropbox.grid(row=2, column=0)
        


        self.label = ctk.CTkLabel(root, 150, 28, text="In which currency?")             # In Währung
        self.label.grid(row=0, column=2)


        self.textvar_out = ctk.StringVar()
        self.txt_out = ctk.CTkEntry(root, height=20, textvariable=self.textvar_out)         # Ausgabe Text
        self.txt_out.grid(row=3, column=2)   
        

        self.option_var_out = ctk.StringVar(value="Euro€")
        self.dropbox = ctk.CTkOptionMenu(master=root,variable=self.option_var_out, values=["Euro€", "US Dollar$"])  # Ausgabe währung 
        self.dropbox.grid(row=2, column=2)


        self.button = ctk.CTkButton(root, text="Convert", command=self.convert)
        self.button.grid(pady=50, padx=10, row=4, column=1)




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
            


if __name__ == "__main__":
    root = ctk.CTk()
    root.geometry("470x200")
    gui = Window(root)
    root.mainloop()
