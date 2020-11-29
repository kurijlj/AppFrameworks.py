
#!/usr/bin/env python3
"""Unit tests for ValidateNumericalInput class.
"""

# =============================================================================
# Copyright (C) 2020 Ljubomir Kurij <kurijlj@gmail.com>
#
# This file is part of AppFrameworks.py.
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option)
# any later version.
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
# more details.
# You should have received a copy of the GNU General Public License along with
# this program.  If not, see <http://www.gnu.org/licenses/>.
#
# =============================================================================


# =============================================================================
#
# 2020-11-27 Ljubomir Kurij <kurijlj@gmail.com>
#
# * validate_numerical_input_tests.py: created.
#
# =============================================================================


# ============================================================================
#
# TODO:
#
#
# ============================================================================


# ============================================================================
#
# References (this section should be deleted in the release version)
#
#
# ============================================================================

# =============================================================================
# Modules import section
# =============================================================================

import unittest
from collections import namedtuple
from validators import (
        UserInput,
        ValidateNumericalInput
        )


# =============================================================================
# Utility classes and functions
# =============================================================================

Case = namedtuple('Case', ['input', 'expected'])


# =============================================================================
# Unit testing classes
# =============================================================================

class TestValidateNumericalInput(unittest.TestCase):
    """Test for ValidateNumericalInput with None as not valid option.
    """

    def setUp(self):
        """Set test data.
        """

        self._validators = (
            ValidateNumericalInput(
                min_val=-10,
                max_val=10,
                incl_min=False,
                incl_max=True
                ),
            )

        self._cases = (
            Case(UserInput(None), False),
            Case(UserInput(20), False),
            Case(UserInput(-11), False),
            Case(UserInput([0, 1, -20]), False),
            Case(UserInput(9.99), True),
            Case(UserInput(0), True),
            Case(UserInput([0, 1, -2]), True),
            Case(UserInput(5), True),
            Case(UserInput((-3,)), True),
            )

    def testValidate(self):
        """Test validate method.
        """

        for validator in self._validators:
            for case in self._cases:
                self.assertEqual(
                    validator.validate(case.input),
                    case.expected
                    )

# =============================================================================
# Script main body
# =============================================================================

if __name__ == '__main__':
    unittest.main()
