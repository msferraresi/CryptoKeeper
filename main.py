
import tkinter as tk
from src.controller.controller import Controller
from src.model.model import Model
from src.view.viewPrincipal import Principal

def main():
    # Create model, view and controller
    model = Model()
    root = tk.Tk()
    viewPricipal = Principal(master=root)
    controller = Controller(model=model, view=viewPricipal)
    
    # Bind buttons to controller methods
    viewPricipal.encrypt_button.config(command=lambda: controller.encrypt(viewPricipal.password_entry.get(), viewPricipal.algorithm_var.get(), viewPricipal.get_input_text(), viewPricipal.iv_generator_var.get()))
    viewPricipal.decrypt_button.config(command=lambda: controller.decrypt(viewPricipal.password_entry.get(), viewPricipal.algorithm_var.get(), viewPricipal.get_input_text(), viewPricipal.iv_generator_var.get()))
    # Run application
    viewPricipal.mainloop()

if __name__ == "__main__":
    main()
