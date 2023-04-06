import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk

class Principal(tk.Frame):
    PAD = 10
    BG_COLOR = '#b0acac'
    FG_COLOR = '#000000'
    FONT_NAME = 'Helvetica'
    FONT_SIZE = 8

    BG_COLOR_ENCRYPT = '#2ab528'
    FG_COLOR_ENCRYPT = '#000000'
    FONT_NAME_ENCRYPT = 'Helvetica'
    FONT_SIZE_ENCRYPT = 8

    BG_COLOR_DECRYPT = '#bd302b'
    FG_COLOR_DECRYPT = '#000000'
    FONT_NAME_DECRYPT = 'Helvetica'
    FONT_SIZE_DECRYPT = 8

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        style = ttk.Style()
        style.theme_use("vista")

        self.algorithm = ('Select', 'PBEWITHHMACSHA512ANDAES_128', 'PBEWITHHMACSHA512ANDAES_256')
        self.generator = ('Select', 'org.jasypt.iv.RandomIvGenerator')

        style.configure("Red.TButton", background="red", foreground="red")
        style.configure("Green.TButton", background="green", foreground="red")
        style.configure("Transparent.TLabel", background=self.BG_COLOR, foreground=self.FG_COLOR)

        self.master.title("CryptoKeeper")
        self.master.geometry("500x400")
        self.master.resizable(False, False)
        self.master.configure(background=self.BG_COLOR)
        self.master.columnconfigure(1, weight=1)

        # Create menu bar
        menubar = tk.Menu(self.master)

        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Close", command=self.master.quit)
        menubar.add_cascade(label="File", menu=filemenu)

        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="About...", command=self.about)
        menubar.add_cascade(label="Help", menu=helpmenu)

        self.master.config(menu=menubar)

        # Create password field
        ttk.Label(self.master, text="Master Password:", font=(self.FONT_NAME, self.FONT_SIZE), style="Transparent.TLabel").grid(row=0, column=0, sticky="w", padx=self.PAD, pady=self.PAD)
        self.password_entry = ttk.Entry(self.master, show="*")
        self.password_entry.grid(row=0, column=1, sticky="we", padx=(self.PAD, self.PAD*2), pady=self.PAD)
        self.password_entry.focus_set()
        
        # Create algorithm dropdown
        ttk.Label(self.master, text="Algorithm:", font=(self.FONT_NAME, self.FONT_SIZE), style="Transparent.TLabel").grid(row=1, column=0, sticky="w", padx=self.PAD, pady=self.PAD)
        self.algorithm_var = tk.StringVar()
        self.algorithm_dropdown = ttk.OptionMenu(self.master, self.algorithm_var, self.algorithm[0], *self.algorithm)
        self.algorithm_dropdown.grid(row=1, column=1, sticky="we", padx=(self.PAD, self.PAD*2), pady=self.PAD)
        
        # Create iv_generator dropdown
        ttk.Label(self.master, text="IV Generator:", font=(self.FONT_NAME, self.FONT_SIZE), style="Transparent.TLabel").grid(row=2, column=0, sticky="w", padx=self.PAD, pady=self.PAD)
        self.iv_generator_var = tk.StringVar()
        self.iv_generator_dropdown = ttk.OptionMenu(self.master, self.iv_generator_var, self.generator[0], *self.generator)
        self.iv_generator_dropdown.grid(row=2, column=1, sticky="we", padx=(self.PAD, self.PAD*2), pady=self.PAD)

        # Create input text field
        ttk.Label(self.master, text="Input Text:", font=(self.FONT_NAME, self.FONT_SIZE), style="Transparent.TLabel").grid(row=3, column=0, sticky="w", padx=self.PAD, pady=self.PAD)
        self.input_text = tk.Text(self.master, height=3, width=50)
        self.input_text.grid(row=3, column=1, columnspan=2, sticky="we", padx=(self.PAD, self.PAD*2), pady=self.PAD)
        
        # Create result field
        ttk.Label(self.master, text="Result:", font=(self.FONT_NAME, self.FONT_SIZE), style="Transparent.TLabel").grid(row=4, column=0, sticky="w", padx=self.PAD, pady=self.PAD)
        self.result_text = tk.Text(self.master, height=8, width=50)
        self.result_text.grid(row=4, column=1, columnspan=2, sticky="we", padx=(self.PAD, self.PAD*2), pady=self.PAD)
        
        # Create encrypt button
        self.encrypt_button = ttk.Button(self.master, text="Encrypt", command=self.encrypt, width=15, style="Green.TButton")
        self.encrypt_button.grid(row=6, column=0, sticky="we", padx=(self.PAD, self.PAD*2), pady=self.PAD)

        # Create decrypt button
        self.decrypt_button = ttk.Button(self.master, text="Decrypt", command=self.decrypt, width=15, style="Red.TButton")
        self.decrypt_button.grid(row=6, column=1, sticky="e", padx=(self.PAD, self.PAD*2), pady=self.PAD)
        
    def encrypt(self):
        password = self.password_entry.get()
        algorithm = self.algorithm_var.get()
        input_text = self.get_input_text()
        iv_generator = self.iv_generator_var.get()
        self.controller.encrypt(password, algorithm, input_text, iv_generator)

    def decrypt(self):
        password = self.password_entry.get()
        algorithm = self.algorithm_var.get()
        input_text = self.get_input_text()
        iv_generator = self.iv_generator_var.get()
        self.controller.decrypt(password, algorithm, input_text, iv_generator)

    def about(self):
        messagebox.showinfo("About", "CryptoKeeper\n\nVersion: 1.0\n\nCopyright (c) 2023, Mauro F.\n\nAll rights reserved.")

    def get_input_text(self):
        return self.input_text.get("1.0", "end-1c")