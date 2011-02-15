# flint - Sam's general purpose resume generation tool
# Copyright (C) 2010 Sam Hart (hartsn@gmail.com)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# directory definitions
TEMPLATE_DIRECTORY = "templates"
HTML_DIRECTORY = "html"
DOCX_DIRECTORY = "docx"
PDF_DIRECTORY = "pdf"

TEMPLATE_HTML = "%s/%s" % (TEMPLATE_DIRECTORY, HTML_DIRECTORY)
TEMPLATE_DOCX = "%s/%s" % (TEMPLATE_DIRECTORY, DOCX_DIRECTORY)
TEMPLATE_PDF = "%s/%s" % (TEMPLATE_DIRECTORY, PDF_DIRECTORY)

# Config directories
CONFIG_DIRECTORY = ".flint"
CONFIG_FILE = "flintrc"
