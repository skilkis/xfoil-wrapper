# MIT License
#
# Copyright (c) 2020 San Kilkis
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.

"""Entry point for setuptools, configuration is in setup.cfg."""

import os
import shutil
import sys

from setuptools import setup
from setuptools.command.install import install

XFOIL_BINARY_DIRS = {"win32": "bin/win32"}

INSTALLER_DIR = os.path.dirname(__file__)


class XFOILInstaller(install):
    """Executed initially before all other setup occurs."""

    def run(self):
        """Copies the correct binaries into :py:attr:`build_lib`."""
        platform = sys.platform
        try:
            binary_dir = XFOIL_BINARY_DIRS[platform]
            dst_dir = os.path.join(self.build_lib, "xfoil", "bin")
            shutil.rmtree(dst_dir, ignore_errors=True)
            shutil.copytree(
                src=os.path.join(INSTALLER_DIR, binary_dir), dst=dst_dir
            )

        except KeyError:
            raise OSError(
                f"The current operating system '{platform}' is not supported"
            )
        super().run()  # Running setuptools installer


if __name__ == "__main__":
    setup(use_scm_version=True, cmdclass={"install": XFOILInstaller})
