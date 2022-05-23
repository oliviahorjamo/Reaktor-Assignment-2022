from parsing.parsed_package import ParsedPackage
import re

class Parser:
    def __init__(self, file = None):
        self.file = file
        self.current_package = None
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
            print("current line:", line)
            if line == "\n":
                new_package = False
                new_dependencies = False
                new_extras = False
            if new_package:
                self.parse_package_line(line)
            if new_dependencies:
                self.parse_dependency_line(line)
            if "[[package]]" in line:
                new_package = True
            if "[package.dependencies]" in line:
                new_dependencies = True
            if "[package.extras]" in line:
                new_extras = True

    def create_new_package(self, name):
        package = ParsedPackage(name = name)
        self.add_package(package)
        return package

    def find_package_with_name(self, name):
        for package in self.parsed_packages:
            if package.name == name:
                return package

    def parse_package_line(self, line):
        attribute = re.findall(r"[^ =]*", line)[0]
        value = re.search(r'(?<==).*',line)
        if value is not None:
            value = value.group(0)
        if attribute == "name":
            package = self.find_package_with_name(name=value)
            self.set_current_package(package = package, name = value)
        else:
            self.current_package.set_attribute(attribute, value)

    def set_current_package(self, package, name):
        if package is None:
            self.current_package = self.create_new_package(name=name)
        else:
            self.current_package = package

    def add_package(self, package):
        self.parsed_packages.append(package)
        print("äsken lisätty package", self.parsed_packages[-1].name)

    def parse_dependency_line(self, line):
        package_name = re.findall(r"[^ =]*", line)[0]
        package = self.find_package_with_name(package_name)
        if package is None:
            dependency = self.create_new_package(name=package_name)
        else:
            dependency = package
        

    def add_reverse_dep(self):
        pass

parser = Parser()