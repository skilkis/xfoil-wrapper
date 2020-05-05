import os

from xfoil.xfoil_module import call


def test_xfoil_in_path():
    """Tests if XFOIL executables are currently in the system path."""
    assert any(os.path.join("xfoil", "bin") for d in os.environ["PATH"])
    os.system("xfoil")


def test_imports():
    """Testing if all functions from xfoil_module are importable."""
    from xfoil import (  # noqa F401
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


def test_call(in_tmpdir):
    """Tests if XFOIL can execute in a temporary directory."""
    call("naca0012", alfas=0)
