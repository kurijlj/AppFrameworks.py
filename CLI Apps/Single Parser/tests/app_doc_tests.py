
#!/usr/bin/env python3
"""Unit tests for AppDoc class.
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
# * app_doc_tsests.py: created.
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
from app import AppDoc


# =============================================================================
# Test cases
# =============================================================================

TEST_CASES = (
    AppDoc(),
    )


# =============================================================================
# Unit testing classes
# =============================================================================

class TestImproperAttributeAssignment(unittest.TestCase):
    """Test AppDoc class methods for passing values of unsupported type.
    """

    def setUp(self):
        """Set test data to first (and only) test case.
        """

        self._dataset = TEST_CASES[0]

    def testImproperAttributeAssignment(self):
        """Test newAppDescription TypeError trigger.
        """

        with self.assertRaises(TypeError):
            self._dataset.newAppDescription(None)

        with self.assertRaises(TypeError):
            self._dataset.newAppName(34)

        with self.assertRaises(TypeError):
            self._dataset.newAuthorName(3.12)

        with self.assertRaises(TypeError):
            self._dataset.newBugMail(None)

        with self.assertRaises(TypeError):
            self._dataset.newEpilog(None)

        with self.assertRaises(TypeError):
            self._dataset.newLicense(None)

        with self.assertRaises(TypeError):
            self._dataset.newReleaseYear(None)

        with self.assertRaises(TypeError):
            self._dataset.newVersionString(None)

    @unittest.expectedFailure
    def testProperAttributeAssignment(self):
        """Test newAppDescription TypeError trigger.
        """

        with self.assertRaises(TypeError):
            self._dataset.newAppDescription('Description')

        with self.assertRaises(TypeError):
            self._dataset.newAppName('Application')

        with self.assertRaises(TypeError):
            self._dataset.newAuthorName('Great Otter')

        with self.assertRaises(TypeError):
            self._dataset.newBugMail('greatotter@otterville.com')

        with self.assertRaises(TypeError):
            self._dataset.newEpilog('Good bye!')

        with self.assertRaises(TypeError):
            self._dataset.newLicense('BSD License')

        with self.assertRaises(TypeError):
            self._dataset.newReleaseYear('2020')

        with self.assertRaises(TypeError):
            self._dataset.newVersionString('0.2.2345')


# =============================================================================
# Script main body
# =============================================================================

if __name__ == '__main__':
    unittest.main()
