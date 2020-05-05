from .xfoil_module import (
    M_crit,
    alfa_for_file,
    call,
    create_input,
    file_name,
    find_alpha_L_0,
    find_coefficients,
    find_pressure_coefficients,
    output_reader,
    prepare_xfoil,
)

__all__ = [
    "call",
    "create_input",
    "prepare_xfoil",
    "output_reader",
    "alfa_for_file",
    "file_name",
    "find_coefficients",
    "find_pressure_coefficients",
    "find_alpha_L_0",
    "M_crit",
]
