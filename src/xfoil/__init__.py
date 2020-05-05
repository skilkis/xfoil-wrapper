import os
import sys

import pkg_resources

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

# Updating path temporarily to make XFOIL binaries callable.
# Currently only Windows is supported!
PLATFORM = sys.platform
if PLATFORM == "win32":
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "bin", PLATFORM)
    os.environ["PATH"] += pkg_resources.resource_filename("xfoil", "bin")
else:
    raise NotImplementedError(
        "Currently XFOIL can only be called from Windows"
    )
