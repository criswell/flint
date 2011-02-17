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

from flintlib import *

class HTML(type):
    '''
    Just a convenience data type for our HTML types
    '''
    pass

class PDF(type):
    '''
    Just a convenience data type for our PDF types
    '''
    pass

class DOCX(type):
    '''
    Just a convenience data type for our DOCX types
    '''
    pass

class TemplateBase(object):
    '''
    The base definition of a template
    '''
    def __init__(self, uri, available):
        '''
        @param uri the path to the template
        @param available whether the template is available in the current working environment or not
        '''
        self.uri = uri
        self.available = available

    template_type = None

class TemplateHTML(TemplateBase):
    '''
    Base template for HTML
    '''

    template_type = HTML

class TemplatePDF(TemplateBase):
    '''
    Base template for PDF
    '''
    template_type = PDF

class TemplateDOCX(TemplateBase):
    '''
    Base template for DOCX
    '''
    template_type = DOCX
