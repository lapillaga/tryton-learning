# This file is part of egob-learning.
# Licensed under the GNU General Public License v3 or later (GPLv3+).
# The COPYRIGHT file at the top level of this repository contains the
# full copyright notices and license terms.
# SPDX-License-Identifier: GPL-3.0-or-later
from . import learning

from trytond.pool import Pool

__all__ = ['register']


def register():
    Pool.register(
        learning.Invoice,
        module='learning',
        type_='model',
    )
