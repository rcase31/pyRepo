"""
Class created to easily work with CSV files.

"""


class MyCSVManager:
    working_directory = "C:/Users/rafae/Desktop/"
    delimiter = ','
    all_lines = []

    def __init__(self, working_directory):
        self.working_directory = working_directory

    def __init__(self):
        pass

    def open(self, file_name) -> list:
        with open(self.working_directory + file_name + '.csv',
                  errors='ignore') as csv_file:
            self.all_lines = csv_file.readlines()
            # Just in case the file is semicolon separated
            if ';' in self.all_lines[0]:
                for i in range(len(self.all_lines)):
                    self.all_lines[i] = self.all_lines[i].split(';')
            return self.all_lines

    def save_lines(self, file_name):
        with open(self.working_directory + file_name + '.csv', mode='w') as \
                out_file:
            for line in self.all_lines:
                out_file.write(self.delimiter.join(line))
