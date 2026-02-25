import customtkinter as ctk

class Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency")

    
        self.label = ctk.CTkLabel(root, 150, 28, text="Pick your currency")
        self.label.grid(row=0, column=0) 

        self.txt = ctk.CTkInputDialog(root, text="halo")
        self.txt.grid(row=3, column=0) 

        
        self.dropbox = ctk.CTkOptionMenu(text="aaa")
        self.dropbox.grid(row=2, column=0)
        

        self.label = ctk.CTkLabel(root, 150, 28, text="In which currency?")
        self.label.grid(row=0, column=1)   


    def currency(self):
        pass





if __name__ == "__main__":
    root = ctk.CTk()
    root.geometry("500x500")
    gui = Window(root)
    root.mainloop()
