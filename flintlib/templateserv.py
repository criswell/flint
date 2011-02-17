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
from flintlib.template import *

class TemplateServices(object):
    '''
    Flint's general purpose template services
    '''
    def __init__(self, config, cwd, force=False):
        '''
        Constructor for the template services
        @param config the current config instance
        @param cwd the current working directory
        @param force Whether operations should be forced or not
        '''
        self._cwd = cwd
        self._force = force
        self._config = config
        self._key_systemwide = 'systemwide'
        self._templates = {}
        self._queue_systemwide_templates()

    def _queue_systemwide_templates(self):
        '''
        Find the system-wide templates
        '''
        if not self._templates.has_key(self._key_systemwide):
            self._templates.
