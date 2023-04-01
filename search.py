import os
import csv

def search_word_in_csv(file_path, search_word):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row_number, row in enumerate(reader, start=1):
            for col_number, cell in enumerate(row, start=1):
                if search_word.lower() in cell.lower():
                    print("-------------------------")
                    print(cell)
                    print(f'Found "{search_word}" in {file_path} at row {row_number}, column {col_number}')

def main():
    search_word = input("Enter the word you want to search for: ")
    root_folder = "messages"

    for dirpath, dirnames, filenames in os.walk(root_folder):
        for filename in filenames:
            if filename == "messages.csv":
                file_path = os.path.join(dirpath, filename)
                search_word_in_csv(file_path, search_word)

if __name__ == "__main__":
    main()
