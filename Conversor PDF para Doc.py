from pdf2docx import Converter
import os


pdf_file = input('Insira o caminho do arquivo PDF. (Exemplo: C:\Trabalhos\Arquivo.pdf): ')
docx_file = os.path.splitext(pdf_file)[0] + '.docx'

# Converta PDF para DOCX
cv = Converter(pdf_file)
cv.convert(docx_file, start=0, end=None)
cv.close()

print(f'Arquivo convertido com sucesso!! {docx_file}')