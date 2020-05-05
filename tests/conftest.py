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

"""Contains Pytest configuration options."""

import os

import pytest


@pytest.fixture(scope="function")
def in_tmpdir(tmpdir):
    """Runs the current test in a temporary directory.

    Returns:
        Value of Pytest fixture `tmpdir`.
    """
    test_dir = tmpdir.chdir()  # Changing directory to tmpdir
    assert os.getcwd() != test_dir  # Ensuring cwd has been changed

    yield tmpdir  # Test will run at this point and yield the value of tmpdir

    # After the test runs, the working directory will be restored
    test_dir.chdir()
    assert os.getcwd() == test_dir
