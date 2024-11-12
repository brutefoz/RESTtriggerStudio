import csv

class CSVUtil:
    @staticmethod
    def read_csv(file_name):
        with open(file_name, mode='r') as file:
            csv_reader = csv.DictReader(file)
            data = [row for row in csv_reader]
        return data