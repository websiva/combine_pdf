import fitz
import os,sys

exe_file_location = os.getcwd()

def combine_pdfs():
    input_folder = exe_file_location
    directory_folder=input_folder.replace("/","\\")
    print(directory_folder)
    output_path = f"{exe_file_location}\\combined_file.pdf"
    
    pdf_merger = fitz.open()
    pdf_files = [file for file in os.listdir(input_folder) if file.endswith(".pdf")]

    pdf_files.sort()

    for pdf_file in pdf_files:
        pdf_file_path = os.path.join(input_folder, pdf_file)
        pdf_document = fitz.open(pdf_file_path)
        pdf_merger.insert_pdf(pdf_document)

    pdf_merger.save(output_path)
    pdf_merger.close()


if __name__ == "__main__":
    combine_pdfs()
