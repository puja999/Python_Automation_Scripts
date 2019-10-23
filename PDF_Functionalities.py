#path -  /Users/puja/Desktop/PDF_gen/PDF_merge/URLs_for.pdf'
import PyPDF2
import fpdf
#  /Users/puja/Desktop/PDF_gen/PDF_merge
def merge_pdf(merge_file1,merge_file2):
    merge = PyPDF2.PdfFileMerger()
    file_object1= open(merge_file1, 'rb')
    merge.append(file_object1)
    file_object2 = open(merge_file2, 'rb')
    merge.append(file_object2)
    merge.write('merged_file.pdf')

def split_pdf(file_to_split,page_to_split):
    split_file1 = open('split_file1.pdf', 'wb')
    split_file2 = open('split_file2.pdf', 'wb')
    writer1 = PyPDF2.PdfFileWriter()
    writer2 = PyPDF2.PdfFileWriter()
    file_object1 = open(file_to_split, 'rb')
    reader1 = PyPDF2.PdfFileReader(file_object1)
    for page in range(0,page_to_split):
        each_page=reader1.getPage(page)
        writer1.addPage(each_page)
    writer1.write(split_file1)
    for page in range(page_to_split,reader1.numPages):
        each_page=reader1.getPage(page)
        writer2.addPage(each_page)
    writer2.write(split_file2)

def image_to_pdf(image_path):
    fpdf_object=fpdf.FPDF()
    fpdf_object.add_page('P')
    fpdf_object.image(image_path,w=180,h=250)
    fpdf_object.output('image_to_pdf.pdf','F')


if __name__== "__main__":
    use=int(input("""What is your requirement?
            Enter
               1 for PDF Merge
               2 for PDF Split
               3 for Image to PDF conversion
               """))
    if use == 1:
        merge_file1=input("Enter first file path to be merged\n")
        merge_file2=input("Enter second file path to be merged\n ")
        merge_pdf(merge_file1,merge_file2)
    elif use == 2:
        file_to_split = input("Enter path of file to be split\n")
        page_to_split = int(input("Enter the page number for split\n"))
        split_pdf(file_to_split,page_to_split)
    elif use == 3:
        image_path=input("Enter image path to be converted to PDF\n")
        image_to_pdf(image_path)
