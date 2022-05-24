
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
        self.dependencies.add(dependency)

    def add_rev_dep(self, current_package):
        self.reverse_dep.add(current_package)

    def set_attribute(self, attribute, value):
        if attribute == "name":
            self.name = value
        if attribute == "description":
            self.description = value

    def add_optional_dep(self, dependency):
        self.extras.add(dependency)

    def add_optional_rev_dep(self, current_package):
        self.reverse_extras.add(current_package)