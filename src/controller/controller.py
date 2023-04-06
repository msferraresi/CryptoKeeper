class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
    
    def encrypt(self, password, algorithm, input_text, iv_generator):
        self.model.encrypt(password, algorithm, input_text, iv_generator)
        self.view.result_text.delete("1.0", "end")
        self.view.result_text.insert("1.0", self.model.result)
    
    def decrypt(self, password, algorithm, input_text, iv_generator):
        self.model.decrypt(password, algorithm, input_text, iv_generator)
        self.view.result_text.delete("1.0", "end")
        self.view.result_text.insert("1.0", self.model.result)