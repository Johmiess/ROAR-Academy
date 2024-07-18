import PyPDF2 
import os 
# path = os.path.dirname(os.path.abspath(__file__))      
# path += '/' +                                                               
file_handle = open(r'C:\Users\roar\Documents\ROAR-Academy\Part Two\Sense-and-Sensibility-by-Jane-Austen.pdf', 'rb')
pdfReader = PyPDF2.PdfReader(file_handle) 
page_number = len(pdfReader.pages)   # this tells you total pages 
page_object = pdfReader.pages[0]    # We just get page 0 as example 
page_text = page_object.extract_text()   # this is the str type of full page
# print(str(page_text))

freq_dict = {}
for page in range(0,len(pdfReader.pages)):
    page_object = pdfReader.pages[page]    # We just get page 0 as example 
    page_text = str(page_object.extract_text())   # this is the str type of full page
    words_in_page = page_text.split()
    for word in words_in_page:
        if not word.isalpha():
            continue   
        if word == "CHAPTER":
            continue     
        if freq_dict.get(word) == None:
              freq_dict[word] = 1
        else:
              freq_dict[word] += 1
        
print(freq_dict)