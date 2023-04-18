import zipfile
import csv

csv_file_path = 'OldFile.csv'
zip_file_path = 'NewFile.csv.tar.gz'

def verify_csv_zip(csv_file_path, zip_file_path):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_file:
        csv_filename = csv_file_path.split("/")[-1]
        if csv_filename not in zip_file.namelist():
            print("Error: CSV file not found in zip file.")
            return False
        with zip_file.open(csv_filename) as csv_file_in_zip:
            with open(csv_file_path, 'r') as original_csv_file:
                csv_reader_zip = csv.reader(csv_file_in_zip)
                csv_reader_original = csv.reader(original_csv_file)
                for row_zip, row_original in zip(csv_reader_zip, csv_reader_original):
                    if row_zip != row_original:
                        print("Error: CSV file contents do not match with zip file contents.")
                        return False
    print("CSV file and zip file match.")
    return True
