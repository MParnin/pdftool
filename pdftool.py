#! python3
# pdftool.py - Tool to split, merge, and rotate PDFs

# Function to split PDF into multiple PDF pages
## Code
import os
def split_pdf(pdf_path):
    with open(pdf_path,"rb") as f:
        reader = PdfReader(f)
        # Get all pages
        for page_num in range(0, len(reader.pages)): # Loop through pages
            selected_page = reader.pages[page_num]
            # Writer
            writer = PdfWriter()
            writer.add_page(selected_page) # Embedding of the page
            filename = os.path.splitext(pdf_path)[0]
            output_filename = f"{filename}_{page_num + 1}.pdf"
            # save and compile to pdf
            with open(output_filename, "wb") as out:
                writer.write(out)
            
            print("Created:{}".format(output_filename))

## Input
split_pdf("test.pdf")

# Function to extract specific pages from PDF
## Code
import os
def split_specific(pdf_path,start_page:int=0,end_page:int=0):
    with open(pdf_path,"rb") as f:
        reader = PdfReader(f)
        writer = PdfWriter()
        for page_num in range(start_page -1, end_page): 
            selected_page = reader.pages[page_num]
            writer.add_page(selected_page)
            filename = os.path.splitext(pdf_path)[0]
            output_filename = f"{filename}_{start_page}_to_{end_page}.pdf"
        with open(output_filename, "wb") as out:
            writer.write(out)
            
            print("Created:{}".format(output_filename))

## Input
split_specific("test.pdf",2,4)

# Function to locate all PDFs in a directory
## Code
def fetch_all_pdfs(parent_folder: str):
    target_files = []
    for path, subdirs, files in os.walk(parent_folder):
        for name in files:
            if name.endswith(".pdf"):
                target_files.append(os.path.join(path, name))
    return target_files

## Input
fetch_all_pdfs("./test")

# Function to merge all PDFs in a directory
## Code
from PyPDF2 import PdfMerger
def merge_pdf(list_of_pdfs,output_filename="Merged_file.pdf"):
    merger = PdfMerger()
    with open(output_filename, "wb") as f:
        for file in list_of_pdfs:
            merger.append(file)
        merger.write(f)
        
        print("Created:{}".format(output_filename))

## Input
pdf_list=fetch_all_pdfs("./test")
merge_pdf(pdf_list)

# Function to rotate a page clockwise 90 degrees by default
## Code
def rotate_pdf(pdf_path,page_num:int,rotation: int = 90):
    with open(pdf_path, "rb") as f:
        reader = PdfReader(f)
        writer = PdfWriter()
        writer.add_page(reader.pages[page_num])
        writer.pages[page_num].rotate(rotation)
        filename = os.path.splitext(pdf_path)[0]
        output_filename = f"{filename}_{rotation}_rotated_page.pdf"
        with open(output_filename, "wb") as out:
            writer.write(out)
                
        print("Created:{}".format(output_filename))

## Input
rotate_pdf("test.pdf",0)
