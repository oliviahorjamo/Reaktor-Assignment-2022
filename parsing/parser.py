from parsing.parsed_package import ParsedPackage
import re


class Parser:
    def __init__(self, file = None):
        self.file = file
        self.current_package = None
        self.parsed_packages = []

    def set_file(self, file):
        self.file = file

    def parse_file(self):
        f = open(self.file, "r")
        new_package = False
        new_dependencies = False
        new_extras = False
        for line in f:
            if line == "\n":
                new_package = False
                new_dependencies = False
                new_extras = False
            if new_package:
                self.parse_package_line(line)
            if new_dependencies:
                self.parse_dependency_line(line)
            if new_extras:
                self.parse_extras_line(line)
            if "[[package]]" in line:
                new_package = True
            if "[package.dependencies]" in line:
                new_dependencies = True
            if "[package.extras]" in line:
                new_extras = True
        self.sort_packages()
        #self.checking_printing()

    def sort_packages(self):
        self.parsed_packages.sort(key=lambda package: package.name.lower())

    def create_new_package(self, name):
        package = ParsedPackage(dependencies = set(), reverse_dep = set(),
            extras = set(), reverse_extras = set(), name = name)
        self.add_package(package)
        return package

    def find_package_with_name(self, name):
        for package in self.parsed_packages:
            if package.name == name:
                return package

    def parse_name(self, line):
        return re.search(r'(?<= = ")[^"]*',line).group(0)

    def parse_description(self, line):
        return re.search(r'(?<== ")[^"]*',line).group(0)

    def parse_package_line(self, line):
        attribute = re.findall(r"[^ =]*", line)[0]
        if attribute == "name":
            name = self.parse_name(line)
            self.handle_parsed_package_name(name)
        elif attribute == "description":
            description = self.parse_description(line)
            self.handle_parsed_description(description)
        
    def handle_parsed_package_name(self, name):
        package = self.find_package_with_name(name=name)
        if package is None:
            package = self.create_new_package(name=name)
            self.set_current_package(package=package)
        else:
            self.set_current_package(package=package)
        package.set_optionality(optional=False)

    def handle_parsed_description(self, description):
        self.current_package.set_description(description)

    def set_current_package(self, package):
        self.current_package = package

    def add_package(self, package):
        self.parsed_packages.append(package)

    def parse_dependency_line(self, line):
        package_name = re.findall(r"[^ =]*", line)[0]
        optional = self.check_if_dep_optional(line)
        self.handle_parsed_dep(package_name=package_name, optional=optional)

    def check_if_dep_optional(self, line):
        if "optional" in line:
            optional = re.search(r'(?<=optional = )[^,]*',line).group(0)
            if optional == "true":
                return True
            elif optional == "false":
                return False
        return False

    def parse_extras_line(self, line):
        packages = re.findall('"([^"]*)"', line)
        for package_name in packages:
            package_name = package_name.strip().split()[0]
            self.handle_parsed_dep(package_name, optional = True)

    def handle_parsed_dep(self, package_name, optional):
        package = self.find_package_with_name(package_name)
        if package is None:
            dependency = self.create_new_package(name=package_name)
        else:
            dependency = package
        if optional:
            self.add_optional_dependency(dependency=dependency)
            self.add_optional_reverse_dependency(dependency=dependency)
        else:
            self.add_dependency(dependency=dependency)
            self.add_reverse_dependency(dependency=dependency)
            
        
    def add_dependency(self, dependency):
        self.current_package.add_dependency(dependency=dependency)

    def add_reverse_dependency(self, dependency):
        dependency.add_rev_dep(current_package = self.current_package)

    def add_optional_dependency(self, dependency):
        self.current_package.add_optional_dep(dependency=dependency)

    def add_optional_reverse_dependency(self, dependency):
        dependency.add_optional_rev_dep(current_package = self.current_package)

    def checking_printing(self):
        print("all packages")
        for package in self.parsed_packages:
            print("package name:", package.name)
            print("package description", package.description)
            print("package optionality", package.optional)
            for dep in package.dependencies:
                print("dependency name:", dep.name)
                print("optionality:", dep.optional)
            for op_dep in package.extras:
                print("optional dependency:", op_dep.name)
            for rev_rep in package.reverse_dep:
                print("reverse dependency", rev_rep.name)
            for op_rev_dep in package.reverse_extras:
                print("optional reverse dependency:", op_rev_dep.name)

parser = Parser()