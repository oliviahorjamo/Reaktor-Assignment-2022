#from parsing.parsed_package import ParsedPackage
import re
from parsed_package import ParsedPackage
file = "/home/hdolivia/Documents/Työt/Työhakemuksia/Reaktor - Software Developer Trainee/Preassignment/Reaktor-Assignment-2022/poetry.lock"


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
        package = ParsedPackage(dependencies = [], reverse_dep = [],
            extras = [], reverse_extras = [], name = name)
        self.add_package(package)
        return package

    def find_package_with_name(self, name):
        for package in self.parsed_packages:
            if package.name == name:
                return package

    def parse_name(self, line):
        return re.search(r'(?<= = ")[^"]*',line).group(0)

    def parse_description(self, line):
        return re.search(r'(?<== ")[."]*',line).group(0)

    def parse_package_line(self, line):
        attribute = re.findall(r"[^ =]*", line)[0]
        if attribute == "name":
            name = self.parse_name(line)
            package = self.find_package_with_name(name=name)
            self.set_current_package(package=package, name=name)
        elif attribute == "description":
            description = self.parse_description(line)
            self.current_package.set_attribute(attribute, description)
        print("self.current_package", self.current_package.name)

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
        if self.check_if_dep_optional(line):
            self.add_optional_dependency(dependency=dependency)
            self.add_optional_reverse_dependency(dependency=dependency)
        else:
            self.add_dependency(dependency=dependency)
            self.add_reverse_dependency(dependency=dependency)

    def check_if_dep_optional(self, line):
        if "optional" in line:
            optional = re.search(r'(?<=optional = )[^,]*',line).group(0)
            if optional == "true":
                return True
            elif optional == "false":
                return False
        return False
        
    def add_dependency(self, dependency):
        self.current_package.add_dependency(dependency=dependency)

    def add_reverse_dependency(self, dependency):
        dependency.add_rev_dep(current_package = self.current_package)

    def add_optional_dependency(self, dependency):
        self.current_package.add_optional_dep(dependency=dependency)

    def add_optional_reverse_dependency(self, dependency):
        dependency.add_optional_rev_dep(current_package = self.current_package)

parser = Parser()
parser.set_file(file)