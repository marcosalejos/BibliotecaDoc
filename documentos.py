import aspose.words as aw
import PyPDF2

def main():
    file = open("BibliotecaDoc\REENVIO AUTOMATICO.pdf", "rb")
    reader = PyPDF2.PdfReader(file)
    for i in range(len(reader.pages)):
        pagina = reader.pages[i]
        print(pagina.extract_text(0))




if __name__ == '__main__':
    main()