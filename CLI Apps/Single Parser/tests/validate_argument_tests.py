
#!/usr/bin/env python3
"""Unit tests for ValidateArgument class.
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
# * validate_argument_test.py: created.
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

import unittest as ut
from validators import ValidateArgument


# =============================================================================
# Utility classes and functions
# =============================================================================


# =============================================================================
# Unit testing classes
# =============================================================================

class TestBoolArgumentNoDefault(ut.TestCase):
    """Test case for boolean type arguments with no default value set.
    """

    def setUp(self):
        """Set test data.
        """

        self._check = ValidateArgument('test_bool', 'boolean', False, False)

    @ut.expectedFailure
    def testErrorMessages(self):
        """Test if proper error messages are displayed to the screen.
        """

        self._check.validate(min_val=10, max_val=50)
        self._check.validate(min_val=10, max_val=50, test_bool=None)
        self._check.validate(min_val=10, max_val=50, test_bool='hello')

    def testForValueError(self):
        """Test for the ValueError exception rise. The excption is thrown when
        argument is not passed or None value is passed and argument has no
        default value set.
        """

        with self.assertRaises(ValueError):
            self._check.validate(min_val=10, max_val=50)
        with self.assertRaises(ValueError):
            self._check.validate(min_val=10, max_val=50, test_bool=None)

    def testForTypeError(self):
        """Test for the type exception rise. The excption is thrown when
        argument is not of the required general type. General types are defined
        as class attribute in the ValidateArgument class, and every type might
        represent more than one python built-in or abstract types of similar
        properties, e.g. 'numerical' type might represent integers, and
        floating point numbers.
        """

        with self.assertRaises(TypeError):
            self._check.validate(min_val=10, max_val=50, test_bool='hello')

    def testForNoError(self):
        """Test for run with no thrown errors.
        """

        self._check.validate(min_val=10, max_val=50, test_bool=False)
        self._check.validate(min_val=10, max_val=50, test_bool=True)


class TestBoolArgumentWithDefault(ut.TestCase):
    """Test case for boolean type arguments with default value set.
    """

    def setUp(self):
        """Set test data.
        """

        self._check = ValidateArgument('test_bool', 'boolean', True, True)

    @ut.expectedFailure
    def testErrorMessages(self):
        """Test if proper error messages are displayed to the screen.
        """

        self._check.validate(min_val=10, max_val=50, test_bool='hello')

    def testForTypeError(self):
        """Test for the type exception rise. The excption is thrown when
        argument is not of the required general type. General types are defined
        as class attribute in the ValidateArgument class, and every type might
        represent more than one python built-in or abstract types of similar
        properties, e.g. 'numerical' type might represent integers, and
        floating point numbers.
        """

        with self.assertRaises(TypeError):
            self._check.validate(min_val=10, max_val=50, test_bool='hello')

    def testForNoError(self):
        """Test for run with no thrown errors.
        """

        self._check.validate(min_val=10, max_val=50, test_bool=False)
        self._check.validate(min_val=10, max_val=50, test_bool=True)


class TestNumericalArgumentNoDefault(ut.TestCase):
    """Test case for boolean type arguments with no default value set.
    """

    def setUp(self):
        """Set test data.
        """

        self._check = ValidateArgument('test_num', 'numerical', False, False)

    @ut.expectedFailure
    def testErrorMessages(self):
        """Test if proper error messages are displayed to the screen.
        """

        self._check.validate(min_val=10, max_val=50)
        self._check.validate(min_val=10, max_val=50, test_num=None)
        self._check.validate(min_val=10, max_val=50, test_num='hello')

    def testForValueError(self):
        """Test for the ValueError exception rise. The excption is thrown when
        argument is not passed or None value is passed and argument has no
        default value set.
        """

        with self.assertRaises(ValueError):
            self._check.validate(min_val=10, max_val=50)
        with self.assertRaises(ValueError):
            self._check.validate(min_val=10, max_val=50, test_num=None)

    def testForTypeError(self):
        """Test for the type exception rise. The excption is thrown when
        argument is not of the required general type. General types are defined
        as class attribute in the ValidateArgument class, and every type might
        represent more than one python built-in or abstract types of similar
        properties, e.g. 'numerical' type might represent integers, and
        floating point numbers.
        """

        with self.assertRaises(TypeError):
            self._check.validate(min_val=10, max_val=50, test_num='hello')

    def testForNoError(self):
        """Test for run with no thrown errors.
        """

        self._check.validate(min_val=10, max_val=50, test_num=354)
        self._check.validate(min_val=10, max_val=50, test_num=3.14)


class TestNumericalArgumentWithDefault(ut.TestCase):
    """Test case for boolean type arguments with default value set.
    """

    def setUp(self):
        """Set test data.
        """

        self._check = ValidateArgument('test_num', 'numerical', True, True)

    @ut.expectedFailure
    def testErrorMessages(self):
        """Test if proper error messages are displayed to the screen.
        """

        self._check.validate(min_val=10, max_val=50, test_num='hello')

    def testForTypeError(self):
        """Test for the type exception rise. The excption is thrown when
        argument is not of the required general type. General types are defined
        as class attribute in the ValidateArgument class, and every type might
        represent more than one python built-in or abstract types of similar
        properties, e.g. 'numerical' type might represent integers, and
        floating point numbers.
        """

        with self.assertRaises(TypeError):
            self._check.validate(min_val=10, max_val=50, test_num='hello')

    def testForNoError(self):
        """Test for run with no thrown errors.
        """

        self._check.validate(min_val=10, max_val=50, test_num=354)
        self._check.validate(min_val=10, max_val=50, test_num=3.14)


class TestIterableArgumentNoDefault(ut.TestCase):
    """Test case for boolean type arguments with no default value set.
    """

    def setUp(self):
        """Set test data.
        """

        self._check = ValidateArgument('test_list', 'iterable', False, False)

    @ut.expectedFailure
    def testErrorMessages(self):
        """Test if proper error messages are displayed to the screen.
        """

        self._check.validate(min_val=10, max_val=50)
        self._check.validate(min_val=10, max_val=50, test_list=None)
        self._check.validate(min_val=10, max_val=50, test_list='hello')

    def testForValueError(self):
        """Test for the ValueError exception rise. The excption is thrown when
        argument is not passed or None value is passed and argument has no
        default value set.
        """

        with self.assertRaises(ValueError):
            self._check.validate(min_val=10, max_val=50)
        with self.assertRaises(ValueError):
            self._check.validate(min_val=10, max_val=50, test_list=None)

    def testForTypeError(self):
        """Test for the type exception rise. The excption is thrown when
        argument is not of the required general type. General types are defined
        as class attribute in the ValidateArgument class, and every type might
        represent more than one python built-in or abstract types of similar
        properties, e.g. 'numerical' type might represent integers, and
        floating point numbers.
        """

        with self.assertRaises(TypeError):
            self._check.validate(min_val=10, max_val=50, test_list='hello')

    def testForNoError(self):
        """Test for run with no thrown errors.
        """

        self._check.validate(
            min_val=10,
            max_val=50,
            test_list=(1, 2, 3)
            )
        self._check.validate(
            min_val=10,
            max_val=50,
            test_list=[1, 2, 3]
            )


class TestIterableArgumentWithDefault(ut.TestCase):
    """Test case for boolean type arguments with default value set.
    """

    def setUp(self):
        """Set test data.
        """

        self._check = ValidateArgument('test_list', 'iterable', True, True)

    @ut.expectedFailure
    def testErrorMessages(self):
        """Test if proper error messages are displayed to the screen.
        """

        self._check.validate(min_val=10, max_val=50, test_list='hello')

    def testForTypeError(self):
        """Test for the type exception rise. The excption is thrown when
        argument is not of the required general type. General types are defined
        as class attribute in the ValidateArgument class, and every type might
        represent more than one python built-in or abstract types of similar
        properties, e.g. 'numerical' type might represent integers, and
        floating point numbers.
        """

        with self.assertRaises(TypeError):
            self._check.validate(min_val=10, max_val=50, test_list='hello')

    def testForNoError(self):
        """Test for run with no thrown errors.
        """

        self._check.validate(
            min_val=10,
            max_val=50,
            test_list=(1, 2, 3)
            )
        self._check.validate(
            min_val=10,
            max_val=50,
            test_list=[1, 2, 3]
            )


# =============================================================================
# Script main body
# =============================================================================

if __name__ == '__main__':
    ut.main()
