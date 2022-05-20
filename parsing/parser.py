from parsing.parsed_package import ParsedPackage
import re

class Parser:
    def __init__(self, file = None):
        self.file = file
        self.parsed_packages = []

    def set_file(self, file):
        self.file = file
        self.parse_file()

    def parse_file(self):
        f = open(self.file, "r")
        new_package = False
        new_dependencies = False
        new_extras = False
        for line in f:
            print(line)
            if "[[package]]" in line:
                new_package = True
                package_in_parsing = ParsedPackage()
            if "[package.dependencies]" in line:
                new_dependencies = False
            if "[package.extras]" in line:
                new_extras = False
            if line == "\n":
                new_package = False
                new_dependencies = False
                new_extras = False
            if new_package:
                self.set_package_attributes(line, package_in_parsing)

    def set_package_attributes(self, line, package_in_parsing):
        attribute = re.findall(r"/[^ =]*/", line)[0]
        print("attribute", attribute)

    def create_parsed_package(self):
        pass

    def add_dependency(self):
        pass

    def add_reverse_dep(self):
        pass

parser = Parser()