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
except ImportError:
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
        self.config_file = "%s/.flintrc" % self._cwd
        self._force = force
        self._config = configparser.ConfigParser()
        self.config_set = False

    def create(self, resume_name):
        '''
        Creates a default configuration file for the previously set working
        directory.
        @param resume_name The resume name to associate with this resume
        '''
        self._config.add_section("main")
        self._config.set("main", "resume_name", resume_name)

        # Some silly defaults we will want the user to overwrite
        # FIXME - It would be lovely if these could also be stored system-wide
        # and then loaded (optionally) from there
        self._config.add_section("contact")
        self._config.set("contact", "author", "YOUR NAME HERE")
        self._config.set("contact", "address_line1", "ADDRESS 01")
        self._config.set("contact", "address_line2", "ADDRESS 02")
        self._config.set("contact", "address_line3", "ADDRESS 03")
        # FIXME this is pretty US centric, if anyone else cares about it, we
        # will want to fix it
        self._config.set("contact", "city", "CITY")
        self._config.set("contact", "state", "STATE")
        self._config.set("contact", "zip", "ZIP")
        self._config.set("contact", "phone", "PHONE")
        self._config.set("contact", "email", "EMAIL ADDRESS")
        self._config.set("contact", "url1", "URL 01 (like a homepage)")
        self._config.set("contact", "url2", "URL 02 (like an ohloh profile)")

        self._save()

        self.config_set = True

    def _save(self):
        '''
        Saves the config
        '''
        fp = open(self.config_file, mode="w")
        self._config.write(fp)
        fp.close()
