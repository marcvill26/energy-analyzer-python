import pymupdf #le estamos pidiendo a python la libreria pymupdf

def read_pdf(file_path): # una funcion que significa define 
    document = pymupdf.open(file_path) #file path es la ruta del archivo
    
    text = ''
    
    for page in document:
        text += page.get_text('text')
        
    document.close()
    return text