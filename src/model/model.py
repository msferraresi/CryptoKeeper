import subprocess
import re

class Model:
    def __init__(self):
        self.result = ""
    
    def encrypt(self, password, algorithm, input_text, iv_generator):
        if self.validate(password, algorithm, input_text, iv_generator):
            command = [
                "java",
                "-cp",
                "src/lib/jasypt-1.9.3.jar",
                "org.jasypt.intf.cli.JasyptPBEStringEncryptionCLI",
                f"ivGeneratorClassName={iv_generator}",
                f"password={password}",
                f"algorithm={algorithm}",
                "input=" + input_text
            ]
            process = subprocess.run(command, capture_output=True, text=True)
            output = process.stdout.strip()
            match = re.search(r"----OUTPUT----------------------\n\n(.+)", output, re.DOTALL)
            if match:
                self.result = match.group(1).strip()
            else:
                self.result = ""
    
    def decrypt(self, password, algorithm, input_text, iv_generator):
        if self.validate(password, algorithm, input_text, iv_generator):
            command = [
                "java",
                "-cp",
                "src/lib/jasypt-1.9.3.jar",
                "org.jasypt.intf.cli.JasyptPBEStringDecryptionCLI",
                f"ivGeneratorClassName={iv_generator}",
                f"password={password}",
                f"algorithm={algorithm}",
                "input=" + input_text
            ]
            process = subprocess.run(command, capture_output=True, text=True)
            output = process.stdout.strip()
            match = re.search(r"----OUTPUT----------------------\n\n(.+)", output, re.DOTALL)
            if match:
                self.result = match.group(1).strip()
            else:
                self.result = ""

    def validate(self, password, algorithm, input_text, iv_generator):
        if password == '':
            self.result = "Master password cannot be empty"
            return False
        if algorithm == 'Select':
            self.result = "Algorithm cannot be empty"
            return False
        if iv_generator == 'Select':
            self.result = "IV generator cannot be empty"
            return False
        if input_text == '':
            self.result = "Input text cannot be empty"
            return False
        return True