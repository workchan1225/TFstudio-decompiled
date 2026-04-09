# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: blueprints.pyc (Python 3.11)

from __future__ import annotations
import os
import typing as t
from datetime import timedelta
from globals import current_app
from helpers import send_from_directory
from sansio.blueprints import Blueprint as SansioBlueprint
from sansio.blueprints import BlueprintSetupState
if t.TYPE_CHECKING:
    from wrappers import Response

class Blueprint(SansioBlueprint):
    
    def get_send_file_max_age(self = None, filename = None):
        """Used by :func:`send_file` to determine the ``max_age`` cache
        value for a given file path if it wasn't passed.

        By default, this returns :data:`SEND_FILE_MAX_AGE_DEFAULT` from
        the configuration of :data:`~flask.current_app`. This defaults
        to ``None``, which tells the browser to use conditional requests
        instead of a timed cache, which is usually preferable.

        Note this is a duplicate of the same method in the Flask
        class.

        .. versionchanged:: 2.0
            The default configuration is ``None`` instead of 12 hours.

        .. versionadded:: 0.9
        """
        value = current_app.config['SEND_FILE_MAX_AGE_DEFAULT']
    # WARNING: Decompyle incomplete

    
    def send_static_file(self = None, filename = None):
        '''The view function used to serve files from
        :attr:`static_folder`. A route is automatically registered for
        this view at :attr:`static_url_path` if :attr:`static_folder` is
        set.

        Note this is a duplicate of the same method in the Flask
        class.

        .. versionadded:: 0.5

        '''
        if not self.has_static_folder:
            raise RuntimeError("'static_folder' must be set to serve static_files.")
        max_age = self.get_send_file_max_age(filename)
        return send_from_directory(t.cast(str, self.static_folder), filename, max_age = max_age)

    
    def open_resource(self = None, resource = None, mode = None):
        '''Open a resource file relative to :attr:`root_path` for
        reading.

        For example, if the file ``schema.sql`` is next to the file
        ``app.py`` where the ``Flask`` app is defined, it can be opened
        with:

        .. code-block:: python

            with app.open_resource("schema.sql") as f:
                conn.executescript(f.read())

        :param resource: Path to the resource relative to
            :attr:`root_path`.
        :param mode: Open the file in this mode. Only reading is
            supported, valid values are "r" (or "rt") and "rb".

        Note this is a duplicate of the same method in the Flask
        class.

        '''
        if mode not in frozenset({'r', 'rb', 'rt'}):
            raise ValueError('Resources can only be opened for reading.')
        return open(os.path.join(self.root_path, resource), mode)
