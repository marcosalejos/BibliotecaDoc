import PyPDF2

def main():
    file = open("REENVIO AUTOMATICO.pdf", "rb")
    reader = PyPDF2.PdfReader(file)
    texto = "vacaciones"

    for i in range(len(reader.pages)):
        pagina = reader.pages[i].extract_text()
        print(pagina)





if __name__ == '__main__':
    main()