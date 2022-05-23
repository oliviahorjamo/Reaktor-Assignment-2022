
class ParsedPackage:
    def __init__(self, dependencies,
                reverse_dep, extras, reverse_extras, name = None, description = None):
        self.name = name
        self.description = description
        self.dependencies = dependencies
        self.reverse_dep = reverse_dep
        self.extras = extras
        self.reverse_extras = reverse_extras

    def add_dependency(self, dependency):
        self.dependencies.append(dependency)
        print("self name:", self.name)
        print("self dependencies", self.dependencies)
        for dep in self.dependencies:
            print(dep.name)

    def add_rev_dep(self, current_package):
        self.reverse_dep.append(current_package)
        print("self name:", self.name)
        print("self rev dep", self.reverse_dep)
        for dep in self.reverse_dep:
            print(dep.name)

    def set_attribute(self, attribute, value):
        if attribute == "name":
            self.name = value
        if attribute == "description":
            self.description = value

    def add_optional_dep(self, dependency):
        self.extras.append(dependency)
        print("self name:", self.name)
        print("self extras", self.extras)

    def add_optional_rev_dep(self, current_package):
        self.reverse_extras.append(current_package)
        print("self name:", self.name)
        print("self reverse extras", self.reverse_extras)