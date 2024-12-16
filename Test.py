import tkinter as tk
from PIL import Image, ImageTk
import os

class HomePage:
    def __init__(self, master):
        self.master = master
        master.title("Tech Utilidades")

        # Carrega a imagem
        self.logo_image = Image.open("nome_da_imagem.png")
        self.logo_image = ImageTk.PhotoImage(self.logo_image)
        
        # Cria um widget Label para exibir a imagem
        self.logo_label = tk.Label(master, image=self.logo_image)
        self.logo_label.pack()  # Coloque o label onde você deseja na interface
        
        
        # Criação dos botões
        self.button_shutdown = tk.Button(master, text="Cronometro Shutdown", command=self.go_to_shutdown_page)
        self.button_shutdown.pack(side="left", padx=10, pady=10)
        
        self.button_form = tk.Button(master, text="Screen shot", command=self.go_to_form_page)
        self.button_form.pack(side="right", padx=10, pady=10)
        
    def go_to_shutdown_page(self):
        self.master.destroy()  # fecha a página inicial
        root = tk.Tk()  # cria uma nova janela
        shutdown_page = ShutdownPage(root)  # cria a página de shutdown
        root.mainloop()
        
    def go_to_form_page(self):
        self.master.destroy()  # fecha a página inicial
        root = tk.Tk()  # cria uma nova janela
        form_page = FormPage(root)  # cria a página de formulário
        root.mainloop()

class ShutdownPage:
    def __init__(self, master):
        self.master = master
        master.title("Shutdown Page")
        
        # Criação dos widgets da página
        
        self.hours = 0
        self.minutes = 0
        
        # Criação do label para horas
        self.label_hours = tk.Label(master, text="Horas:")
        self.label_hours.grid(row=0, column=0)
        
        # Criação do botão + horas
        self.button_plus_hours = tk.Button(master, text="+", command=self.add_hour)
        self.button_plus_hours.grid(row=0, column=1)
        
        # Criação do botão - horas
        self.button_minus_hours = tk.Button(master, text="-", command=self.subtract_hour)
        self.button_minus_hours.grid(row=0, column=2)
        
        # Criação do label para minutos
        self.label_minutes = tk.Label(master, text="Minutos:")
        self.label_minutes.grid(row=1, column=0)
        
        # Criação do botão + minutos
        self.button_plus_minutes = tk.Button(master, text="+", command=self.add_minute)
        self.button_plus_minutes.grid(row=1, column=1)
        
        # Criação do botão - minutos
        self.button_minus_minutes = tk.Button(master, text="-", command=self.subtract_minute)
        self.button_minus_minutes.grid(row=1, column=2)
        
        # Criação do rótulo para exibir o tempo selecionado
        self.label_selected_time = tk.Label(master, text="00:00")
        self.label_selected_time.grid(row=2, columnspan=3)
        
        # Criação do botão para definir o tempo de desligamento
        self.button_set_time = tk.Button(master, text="Definir Tempo", command=self.set_time)
        self.button_set_time.grid(row=3, columnspan=3)
        
        # Criação do botão para iniciar o shutdown
        self.button_shutdown = tk.Button(master, text="Shutdown", command=self.shutdown)
        self.button_shutdown.grid(row=4, columnspan=3)
        
        # Criação do botão para cancelar o desligamento
        self.button_cancel_shutdown = tk.Button(master, text="Cancelar Desligamento", command=self.cancel_shutdown, state="normal")
        self.button_cancel_shutdown.grid(row=5, columnspan=6)
        
        self.shutdown_scheduled = False
        
        # Botão para voltar para a página inicial
        self.button_home = tk.Button(master, text="Home", command=self.go_to_home_page)
        self.button_home.grid(row=6, columnspan=3, padx=10, pady=10)
    def add_hour(self):
        self.hours += 1
        self.update_display()
        
    def subtract_hour(self):
        if self.hours > 0:
            self.hours -= 1
            self.update_display()
        
    def add_minute(self):
        if self.minutes < 59:
            self.minutes += 1
            self.update_display()
        
    def subtract_minute(self):
        if self.minutes > 0:
            self.minutes -= 1
            self.update_display()
        
    def update_display(self):
        time_string = "{:02d}:{:02d}".format(self.hours, self.minutes)
        self.label_selected_time.config(text=time_string)
    def set_time(self):
        total_minutes = self.hours * 60 + self.minutes
        time_string = "-s -t {:d}".format(total_minutes * 60)  # Convertendo para segundos
        os.system("shutdown " + time_string)
        self.shutdown_scheduled = True
        self.button_cancel_shutdown.config(state="normal")

    def cancel_shutdown(self):
            os.system("shutdown /a")
            self.shutdown_scheduled = False
            self.button_cancel_shutdown.config(state="disabled")
    

        
    def shutdown(self):
        os.system("shutdown -s")

        
        
    def go_to_home_page(self):
        self.master.destroy()  # fecha a página de shutdown
        root = tk.Tk()  # cria uma nova janela
        home_page = HomePage(root)  # cria a página inicial
        root.mainloop()

class FormPage:
    def __init__(self, master):
        self.master = master
        master.title("")
        
        # Criação dos widgets do formulário
        # ...
        
        # Botão para voltar para a página inicial
        self.button_home = tk.Button(master, text="Home", command=self.go_to_home_page)
        self.button_home.grid(row=6, columnspan=3, padx=10, pady=10)
        
    def go_to_home_page(self):
        self.master.destroy()  # fecha a página do formulário
        root = tk.Tk()  # cria uma nova janela
        home_page = HomePage(root)  # cria a página inicial
        root.mainloop()

root = tk.Tk()
home_page = HomePage(root)
root.mainloop()
