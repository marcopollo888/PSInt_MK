class FileManager:
    def __init__(self, file_name):
        self.file_name=file_name
    def update_file(self,text_data):
        uchwyt = open(self.file_name, "a+")
        uchwyt.write(text_data)
        uchwyt.close()
    def read_file(self):
        uchwyt = open(self.file_name, "r")
        print(uchwyt.readlines())
        uchwyt.close()