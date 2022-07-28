import pyttsx3, PyPDF2, os

def reader(file_path):
    book = open(file_path, 'rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    print(f'Total number of pages in the file are {pages}.')
    return [pages, pdfReader]

def speaKer(page_num, pdfReader):
    speaker = pyttsx3.init()
    page = pdfReader.getPage(page_num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()

def main():
    print("\t Welcome to Text Reader")
    file_path = input("Enter the full path of the .pdf file which you want to listen : ")

    if os.path.exists(file_path):
        reader_info = reader(file_path)
    
        start_page = int(input("Enter the page number from which reading will start : "))
        end_page = int(input("Enter the page number at which reading will stop : "))

        if ((start_page <= reader_info[0]) & (end_page <= reader_info[0]) & (start_page<= end_page)):
            for i in range(start_page-1, end_page+1):
                speaKer(i, reader_info[1])
            print("Reading is Completed Successfully.")
        else:
            print("Enter valid page numbers")
    else:
        print("This path is not valid or .pdf does not exist here")
main()