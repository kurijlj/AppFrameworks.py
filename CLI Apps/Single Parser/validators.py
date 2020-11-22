#!/usr/bin/env python3
"""TODO: Put module docstring HERE.
"""

# =============================================================================
# Copyright (C) 2020 Ljubomir Kurij <kurijlj@gmail.com>
#
# This file is part of Radiochromic Denoiser.
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
# 2020-10-24 Ljubomir Kurij <ljubomir_kurij@protonmail.com.com>
#
# * validators.py: created.
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


# =============================================================================
# Module level constants
# =============================================================================


# =============================================================================
# Validator classes and functions
# =============================================================================

class UserInput():
    """TODO: Put class docstring here.
    """

    def __init__(self, data):
        self._data = data

    @property
    def data(self):
        """TODO: Put method docstring here.
        """

        return self._data

    def isNone(self):
        """TODO: Put method docstring here.
        """

        if self._data is None:
            return True

        return False
