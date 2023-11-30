import mysql.connector
import cv2
import pytesseract
import my_library as lib
import os
import tkinter as tk
from tkinter import filedialog

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


class UploadDocumentsGUI:
    def __init__(self, master):
        self.master = master
        master.title("Upload Documents")

        # Create widgets
        self.document_type_label = tk.Label(master, text="Document Type:")
        self.document_type_entry = tk.Entry(master)
        self.file_paths_label = tk.Label(master, text="File Paths (comma separated):")
        self.file_paths_entry = tk.Entry(master)
        self.upload_button = tk.Button(master, text="Upload", command=self.upload_file)
        self.quit_button = tk.Button(master, text="Quit", command=master.quit)

        # Lay out widgets
        self.document_type_label.grid(row=0, column=0)
        self.document_type_entry.grid(row=0, column=1)
        self.file_paths_label.grid(row=1, column=0)
        self.file_paths_entry.grid(row=1, column=1)
        self.upload_button.grid(row=2, column=0)
        self.quit_button.grid(row=2, column=1)

    def upload_file(self):
        document_type = self.document_type_entry.get()
        file_paths = self.file_paths_entry.get().split(",")

        if all([os.path.isfile(file_path) for file_path in file_paths]):
            # Connecting to my Sql Server
            with mysql.connector.connect(
                host="localhost",
                user="root",
                password="Johin2004!",
                database="documents"
            ) as cnx:
                for file_path in file_paths:
                    try:
                        with open(file_path, 'rb') as img:
                            img_data = img.read()
                            cursor = cnx.cursor()
                            stmt = "INSERT INTO documents (Name, image, document_type) VALUES (%s, %s,%s)"
                            cursor.execute(stmt, (file_path, img_data, document_type))
                            cnx.commit()
                            cursor.close()
                        print(f"{file_path} uploaded successfully")
                    except FileNotFoundError:
                        print(f"{file_path} not found. Skipping Upload")
                        continue
        else:
            print("One or more files not found. Please try again.")


def main():
    root = tk.Tk()
    gui = UploadDocumentsGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()

