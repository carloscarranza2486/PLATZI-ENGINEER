"""Typing con Python"""

variable = 42  # int
print(f"Variable {variable}, del tipo {type(variable)}")

variable = "Texto de prueba"
print(f"Variable {variable}, del tipo {type(variable)}")

otra_variable: int = 44
print(f"Variable {otra_variable}, del tipo {type(otra_variable)}")

otra_variable = ""


user_id: int | None = None
