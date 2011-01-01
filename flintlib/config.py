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

try:
    import configparser
except ImportError
    import ConfigParser as configparser

class Config:
    '''
    The flint configuration class
    '''

    def __init__(self, cwd, force=False):
        '''
        General constructor for flint config class
        @param cwd The current working directory
        @param force Whether operations should be forced or not
        '''
        self._cwd = cwd
        self._force = force
        self._config = configparser.ConfigParser()
