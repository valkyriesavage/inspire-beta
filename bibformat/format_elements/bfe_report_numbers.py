# -*- coding: utf-8 -*-
##
## $Id$
##
## This file is part of Invenio.
## Copyright (C) 2002, 2003, 2004, 2005, 2006, 2007 CERN.
##
## Invenio is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 2 of the
## License, or (at your option) any later version.
##
## Invenio is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
## General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with Invenio; if not, write to the Free Software Foundation, Inc.,
## 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.
"""BibFormat element - Prints report numbers
"""

__revision__ = ""

def format_element(bfo, separator, limit, extension=" etc."):
    """
    Prints the report numbers of the record (037__a and 088__a)

    @param separator the separator between report numbers.
    @param limit the max number of report numbers to print
    @param extension a prefix printed when limit param is reached
    """

    numbers = bfo.fields("037__a")
    numbers.extend(bfo.fields("088__a"))
    if limit.isdigit() and int(limit) <= len(numbers):
        return separator.join(numbers[:limit]) + extension
    else:
        return separator.join(numbers)
