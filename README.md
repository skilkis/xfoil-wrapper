# XFOIL Wrapper

[![Python 3.8][python_badge]](https://www.python.org/downloads/release/python-382/)
[![License: MIT][mit_badge]](https://opensource.org/licenses/MIT)
[![Code Style: Black][black_badge]](https://github.com/ambv/black)
[![CICD: GitHub Actions][build_status]](https://github.com/skilkis/xfoil_wrapper/actions)

This repository serves as an easy installer for AeroPy's [XFOIL Module]. All
rights to [xfoil_module] remain with the original author [Pedro Leal].

The command to install xfoil_wrapper is as follows:

``` cmd
pip install xfoil@https://github.com/skilkis/xfoil_wrapper.zip
```

*Note that currently binaries are only included for the Windows operating
system.*

In the future, code quality updates to make the wrapper more extendible are
planned and a compiled-source implementation similar to that of [xfoil-python]
will be investigated.

If you would like to contribute to this project by adding support for
additional operating systems, please submit a pull request!

<!-- Un-wrapped Links below -->
[python_badge]: https://img.shields.io/badge/python-3.7%20|%203.8-blue.svg
[mit_badge]: https://img.shields.io/badge/license-MIT%202.0-brightgreen.svg
[black_badge]: https://img.shields.io/badge/code%20style-black-000000.svg
[build_status]: https://github.com/skilkis/xfoil_wrapper/workflows/build/badge.svg
[Git]: https://git-scm.com/
[XFOIL Module]: https://github.com/leal26/AeroPy/blob/master/aeropy/xfoil_module.py
[Pedro Leal]: https://github.com/leal26
[xfoil_module]: src/xfoil/xfoil_module.py
[xfoil-python]: https://github.com/DARcorporation/xfoil-python
