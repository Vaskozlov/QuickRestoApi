import styler.styler as styler

quick_resto_init_variables = {"id", "_id", "class_name", "className"}


class QuickRestoClassGenerator(object):
    def __init__(self, name: str, class_name: str, arguments: dict, enums: set):
        self._lines = []
        self._name = name
        self._enums = enums
        self._class_name = class_name
        self._variables = arguments

        self._create_file_header()
        self._create_class_definition()
        self._create_variables_access()
        self._create_init()

    def get(self) -> str:
        return "\n".join(self._lines)

    def _create_file_header(self) -> None:
        if len(self._enums) != 0:
            self._lines.append("from enum import Enum")

        self._lines.append("from quick_resto_objects.quick_resto_object import QuickRestoObject")

    def _create_class_definition(self) -> None:
        self._lines.append(f"class {self._name}(QuickRestoObject):")

    def _create_variables_access(self) -> None:
        print(self._variables)

        for key, value in self._variables.items():
            if key not in quick_resto_init_variables:
                function_name = styler.to_snake_case(key)

                self._lines.append("    @property")
                self._lines.append(f"    def {function_name}(self) -> {value.__class__.__name__}:")
                self._lines.append(f"        return self._{function_name}")
                self._lines.append("")

    def _create_init(self) -> None:
        arguments = self._create_init_arguments()
        self._lines.append(f"    def __init__(self, {arguments}, **kwargs):")
        self._lines.append(f"        class_name = \"{self._class_name}\"")
        self._lines.append(f"        super().__init__(class_name=class_name, **kwargs)")
        self._lines.append("")

        for key, value in self._variables.items():
            if key not in quick_resto_init_variables:
                variable_name = styler.to_snake_case(key)
                self._lines.append(f"        self._{variable_name}: {value.__class__.__name__} = {key}")

    def _create_init_arguments(self) -> str:
        arguments = []

        for key, value in self._variables.items():
            if key not in quick_resto_init_variables:
                arguments.append(f"{key}: {value.__class__.__name__}")

        return ", ".join(arguments)
