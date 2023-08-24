import PyPDF2

class Pdf_protector():
    
    def __init__(self,file_path,password):
        self.file_path=file_path
        self.password=password 
    def protect(self):
        text_content = []
        pdf_writer=PyPDF2.PdfWriter()
        with open(self.file_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                pdf_writer.add_page(page)
            pdf_file.close()
            
        with open(self.file_path,"wb") as f2:
            pdf_writer.encrypt(self.password)
            pdf_writer.write(f2)
            print("pdf protected")
if __name__ =="__main__":
    filepath=input("File path: ")
    password=input("Password: ")
    Pdf_protector(filepath,password).protect()