
class ParsedPackage:
    def __init__(self, name = None, description = None, dependencies = [],
                reverse_dep = []):
        self.name = name
        self.description = description
        self.dependencies = dependencies
        self.reverse_dep = reverse_dep

    def add_dependency(self, dependency):
        self.dependencies.append(dependency)

    def add_rev_dep(self, reverse_dep):
        self.reverse_dep.append(reverse_dep)

    def set_attribute(self, attribute, value):
        if attribute == "name":
            self.name = value
        if attribute == "description":
            self.description = value