
#!/usr/bin/env python3
"""Unit tests for ValidateUserChoice class.
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
# 2020-11-21 Ljubomir Kurij <kurijlj@gmail.com>
#
# * validate_user_choice_tsests.py: created.
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
        ValidateUserChoice
        )


# =============================================================================
# Utility classes and functions
# =============================================================================

Case = namedtuple('Case', ['data', 'result'])


# =============================================================================
# Test cases
# =============================================================================

TEST_VALIDATORS = (
    ValidateUserChoice(['hello',], False),
    ValidateUserChoice(['hello',], True),
    ValidateUserChoice(['opt1', 'opt2', 'opt3'], False),
    ValidateUserChoice(['opt1', 'opt2', 'opt3'], True),
    )


# =============================================================================
# Unit testing classes
# =============================================================================

class TestSingleChoice(unittest.TestCase):
    """Test for ValidateUserChoice class with single valid option and None as
    invalid option.
    """

    def setUp(self):
        """Set test data.
        """

        self._vd = TEST_VALIDATORS[0]
        self._tc = (
            Case(UserInput(None), False),
            Case(UserInput((None, None)), False),
            Case(UserInput('ack'), False),
            Case(UserInput(['ack',]), False),
            Case(UserInput('hello'), False),  # This will give Flase when validating
            Case(UserInput(['hello',]), True),
            Case(UserInput(['hello', 'hello']), True),
            Case(UserInput(['hello', 'hello', 'hello']), True),
            )

    def testValidate(self):
        """Test validate method.
        """

        count = 0
        print('\n\nValidator #01:')
        print('Single valid option without None as valid option')
        print('===============================')
        print('')
        print('Running \'Test Validate\' ...')
        for case in self._tc:
            print('Testing case: {0} ...'.format(count))
            self.assertEqual(self._vd.validate(case.data), case.result)
            count += 1
        print('\n')


class TestSingleChoiceWithNone(unittest.TestCase):
    """Test for ValidateUserChoice class with single valid option and None as
    valid option.
    """

    def setUp(self):
        """Set test data.
        """

        self._vd = TEST_VALIDATORS[1]
        self._tc = (
            Case(UserInput(None), True),
            Case(UserInput([None, None]), False),
            Case(UserInput('ack'), False),
            Case(UserInput(['ack',]), False),
            Case(UserInput('hello'), False),  # This will give Flase when validating
            Case(UserInput(['hello',]), True),
            Case(UserInput(['hello', 'hello']), True),
            Case(UserInput(['hello', 'hello', 'hello']), True),
            )

    def testValidate(self):
        """Test validate method.
        """

        count = 0
        print('\n\nValidator #02:')
        print('Single valid option with None as valid option')
        print('===============================')
        print('')
        print('Running \'Test Validate\' ...')
        for case in self._tc:
            print('Testing case: {0} ...'.format(count))
            self.assertEqual(self._vd.validate(case.data), case.result)
            count += 1
        print('\n')


class TestMultiChoice(unittest.TestCase):
    """Test for ValidateUserChoice class with multiple valid options and None
    as invalid option.
    """

    def setUp(self):
        """Set test data.
        """

        self._vd = TEST_VALIDATORS[2]
        self._tc = (
            Case(UserInput(['hello',]), False),
            Case(UserInput(['opt1', 'opt3', 'ack']), False),
            Case(UserInput(['opt1',]), True),
            Case(UserInput(['opt3', 'opt1']), True),
            Case(UserInput(['opt2', 'opt1', 'opt3', 'opt1']), True),
            )

    def testValidate(self):
        """Test validate method.
        """

        count = 0
        print('\n\nValidator #03:')
        print('Multiple valid options without None as valid option')
        print('===============================')
        print('')
        print('Running \'Test Validate\' ...')
        for case in self._tc:
            print('Testing case: {0} ...'.format(count))
            self.assertEqual(self._vd.validate(case.data), case.result)
            count += 1
        print('\n')


class TestMultiChoiceWithNone(unittest.TestCase):
    """Test for ValidateUserChoice class with multiple valid options and None
    as valid option.
    """

    def setUp(self):
        """Set test data.
        """

        self._vd = TEST_VALIDATORS[3]
        self._tc = (
            Case(UserInput(None), True),
            Case(UserInput(['hello',]), False),
            Case(UserInput(['opt1', 'opt3', 'ack']), False),
            Case(UserInput(['opt1',]), True),
            Case(UserInput(['opt3', 'opt1']), True),
            Case(UserInput(['opt2', 'opt1', 'opt3', 'opt1']), True),
            )

    def testValidate(self):
        """Test validate method.
        """

        count = 0
        print('\n\nValidator #04:')
        print('Multiple valid options with None as valid option')
        print('===============================')
        print('')
        print('Running \'Test Validate\' ...')
        for case in self._tc:
            print('Testing case: {0} ...'.format(count))
            self.assertEqual(self._vd.validate(case.data), case.result)
            count += 1
        print('\n')


# =============================================================================
# Script main body
# =============================================================================

if __name__ == '__main__':
    unittest.main()
