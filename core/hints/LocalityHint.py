# coding: utf-8
"""
    core.hints.LocatityHint
    ~~~~~~~~~~~~~

    A LocalityHint is subclass of the LocationHint object.

    Requirements: geoclue

    :copyright: 2016 Ray Gomez (codenomad@gmail.com), see AUTHORS for more details
    :license: MIT, see LICENSE for more details
"""

from core.hints.abstractions import LocationHint


class LocalityHint(LocationHint):
    """ This is a subclass of the LocationHint object that focuses specifically on determining a location based on
    physical locality of the user (ie GPS).
    """

    def __init__(self, requirements):
        super(LocalityHint, self).__init__()
        self.requirements = requirements

    def is_location(self):
        """ Abstract method that should be implemented in all subclasses, erroring out if not available """
        pass
