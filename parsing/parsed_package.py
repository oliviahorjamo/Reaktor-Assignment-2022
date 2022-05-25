
class ParsedPackage:
    def __init__(self, dependencies,
                reverse_dep, extras, reverse_extras, name = None, description = None, optional = True):
        self.name = name
        self.description = description
        self.dependencies = dependencies
        self.reverse_dep = reverse_dep
        self.extras = extras
        self.reverse_extras = reverse_extras
        self.optional = optional

    def add_dependency(self, dependency):
        self.dependencies.add(dependency)

    def add_rev_dep(self, current_package):
        self.reverse_dep.add(current_package)

    def set_description(self, description):
        self.description = description

    def add_optional_dep(self, dependency):
        self.extras.add(dependency)

    def add_optional_rev_dep(self, current_package):
        self.reverse_extras.add(current_package)

    def set_optionality(self, optional):
        self.optional = optional

    def sort_dependencies(self):
        self.dependencies = sorted(self.dependencies, key=lambda package: package.name)
        self.reverse_dep = sorted(self.reverse_dep, key=lambda package: package.name)
        self.extras = sorted(self.extras, key=lambda package: package.name)
        self.reverse_extras = sorted(self.reverse_extras, key=lambda package: package.name)