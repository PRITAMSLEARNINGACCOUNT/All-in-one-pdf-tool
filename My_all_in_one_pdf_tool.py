from pypdf import *


def reduce_size(pdf_name, name):
    pdf_reader = PdfReader(pdf_name)
    pdf_writer = PdfWriter()
    # print(pdf_reader.pages)

    for i in pdf_reader.pages:
        pdf_writer.add_page(i)
    pdf_writer.add_metadata(pdf_reader.metadata)
    # for ia in pdf_writer.pages:
    #     ia.compress_content_streams()
    with open(name, "wb") as write:
        pdf_writer.write(write)
    print("Successfully reduced size of the pdf you gave and saved it into your current directory or current path.")
    pdf_writer.close()


def encrypt_pdf(path, name, execute_name):
    pdf_reader = PdfReader(f"{path}\{name}")
    pdf_writer = PdfWriter()
    for fuck in pdf_reader.pages:
        pdf_writer.add_page(fuck)
    password = input("Enter you password??\n")
    pdf_writer.encrypt(password)
    with open(execute_name, "wb") as helloworld:
        pdf_writer.write(helloworld)
    print("So the pdf is now successfully encrypted and saved it into your current directory or current path.")
    pdf_writer.close()


def decrypt_pdf(directory, pdf_name, output_pdf, pass_key):
    pdf_reader = PdfReader(f"{directory}\{pdf_name}")
    pdf_reader.decrypt(pass_key)
    pdf_writer = PdfWriter()
    for fuck in pdf_reader.pages:
        pdf_writer.add_page(fuck)
    with open(execute_name, "wb") as helloworld:
        pdf_writer.write(helloworld)
    print("So the pdf is now successfully decrypted and saved it into your current directory or current path.")
    pdf_writer.close()


def merge_pdf():
    pages = int(input("Enter how many pdf's do you want to merge in one pdf?\n"))
    varriable = PdfWriter()
    for i in range(pages):
        string = input(
            "Enter the name of the pdf you want to merge one by one??\n")
        string_2 = input("Enter where do you keep your pdf??\n")
        if string.endswith(".pdf") == True:
            string = string
        else:
            string = string+".pdf"
        with open(f"{string_2}\{string}", "rb") as input_1:
            varriable.append(input_1)

    execute_name = input("Enter the name of the executed pdf file???\n")
    if execute_name.endswith(".pdf") == True:
        execute_name = execute_name
    else:
        execute_name = execute_name+".pdf"
    with open(execute_name, "wb") as hello:
        varriable.write(hello)
    varriable.close()
    print("Pdf's are merged successfully and saved it into your current directory or current path.")


# Except merge pdf
want = input(
    "What do you want to do(Reduce PDF,Merge PDF,Encrypt PDF or Decrypt PDF)???\n")
if want == "reduce" or want == "Reduce" or want == "REDUCE":

    path = input("Enter the path where you kept your pdf file??\n")
    pdf_name = input("Enter The name of your pdf??\n")
    if pdf_name.endswith(".pdf") == True:
        actual_anme = f"{path}\{pdf_name}"
    else:
        actual_anme = f"{path}\{pdf_name}.pdf"

    execute_name = input("Enter the name of the executed pdf file???\n")
    if execute_name.endswith(".pdf") == True:
        execute_name = execute_name
    else:
        execute_name = execute_name+".pdf"
    reduce_size(actual_anme, execute_name)
elif want == "Merge" or want == "MERGE" or want == "merge":
    merge_pdf()
elif want == "Encrypt" or want == "ENCRYPT" or want == "encrypt":
    path = input("Enter the path where you kept your pdf file??\n")
    pdf_name = input("Enter The name of your pdf??\n")
    if pdf_name.endswith(".pdf") == True:
        pdf_name = pdf_name
    else:
        pdf_name = pdf_name+".pdf"
    execute_name = input("Enter the name of the executed pdf file???\n")
    if execute_name.endswith(".pdf") == True:
        execute_name = execute_name
    else:
        execute_name = execute_name+".pdf"
    encrypt_pdf(path, pdf_name, execute_name)
elif want == "decrypt" or want == "DECRYPT" or want == "Decrypt":
    password = input("Enter the password of the pdf?\n")
    path = input("Enter the path where you kept your pdf file??\n")
    pdf_name = input("Enter The name of your pdf??\n")
    if pdf_name.endswith(".pdf") == True:
        pdf_name = pdf_name
    else:
        pdf_name = pdf_name+".pdf"
    execute_name = input("Enter the name of the executed pdf file???\n")
    if execute_name.endswith(".pdf") == True:
        execute_name = execute_name
    else:
        execute_name = execute_name+".pdf"
    decrypt_pdf(path, pdf_name, execute_name, password)
else:
    print("Invalid Input.")
