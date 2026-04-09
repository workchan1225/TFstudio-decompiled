# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: emulation.pyc (Python 3.11)

from __future__ import annotations
from enum import Enum
from typing import TYPE_CHECKING, Any, TypeVar
from selenium.webdriver.common.bidi.common import command_builder
if TYPE_CHECKING:
    from selenium.webdriver.remote.websocket_connection import WebSocketConnection

class ScreenOrientationNatural(Enum):
    '''Natural screen orientation.'''
    PORTRAIT = 'portrait'
    LANDSCAPE = 'landscape'


class ScreenOrientationType(Enum):
    '''Screen orientation type.'''
    PORTRAIT_PRIMARY = 'portrait-primary'
    PORTRAIT_SECONDARY = 'portrait-secondary'
    LANDSCAPE_PRIMARY = 'landscape-primary'
    LANDSCAPE_SECONDARY = 'landscape-secondary'

E = TypeVar('E', ScreenOrientationNatural, ScreenOrientationType)

def _convert_to_enum(value = None, enum_class = None):
    if isinstance(value, enum_class):
        return value
# WARNING: Decompyle incomplete


class ScreenOrientation:
    '''Represents screen orientation configuration.'''
    
    def __init__(self = None, natural = None, type = None):
        '''Initialize ScreenOrientation.

        Args:
            natural: Natural screen orientation ("portrait" or "landscape").
            type: Screen orientation type ("portrait-primary", "portrait-secondary",
                "landscape-primary", or "landscape-secondary").

        Raises:
            ValueError: If natural or type values are invalid.
        '''
        self.natural = _convert_to_enum(natural, ScreenOrientationNatural)
        self.type = _convert_to_enum(type, ScreenOrientationType)

    
    def to_dict(self = None):
        return {
            'natural': self.natural.value,
            'type': self.type.value }



class GeolocationCoordinates:
    '''Represents geolocation coordinates.'''
    
    def __init__(self, latitude, longitude, accuracy = None, altitude = None, altitude_accuracy = None, heading = (1, None, None, None, None), speed = ('latitude', 'float', 'longitude', 'float', 'accuracy', 'float', 'altitude', 'float | None', 'altitude_accuracy', 'float | None', 'heading', 'float | None', 'speed', 'float | None')):
        '''Initialize GeolocationCoordinates.

        Args:
            latitude: Latitude coordinate (-90.0 to 90.0).
            longitude: Longitude coordinate (-180.0 to 180.0).
            accuracy: Accuracy in meters (>= 0.0), defaults to 1.0.
            altitude: Altitude in meters or None, defaults to None.
            altitude_accuracy: Altitude accuracy in meters (>= 0.0) or None, defaults to None.
            heading: Heading in degrees (0.0 to 360.0) or None, defaults to None.
            speed: Speed in meters per second (>= 0.0) or None, defaults to None.

        Raises:
            ValueError: If coordinates are out of valid range or if altitude_accuracy is provided without altitude.
        '''
        self.latitude = latitude
        self.longitude = longitude
        self.accuracy = accuracy
        self.altitude = altitude
        self.altitude_accuracy = altitude_accuracy
        self.heading = heading
        self.speed = speed

    latitude = (lambda self = None: self._latitude)()
    latitude = (lambda self = None, value = None: if not  <= -90, value or -90, value <= 90:
passraise ValueError('latitude must be between -90.0 and 90.0'))()
    longitude = (lambda self = None: self._longitude)()
    longitude = (lambda self = None, value = None: if not  <= -180, value or -180, value <= 180:
passraise ValueError('longitude must be between -180.0 and 180.0'))()
    accuracy = (lambda self = None: self._accuracy)()
    accuracy = (lambda self = None, value = None: if value < 0:
raise ValueError('accuracy must be >= 0.0')self._accuracy = value)()
    altitude = (lambda self = None: self._altitude)()
    altitude = (lambda self = None, value = None: self._altitude = value)()
    altitude_accuracy = (lambda self = None: self._altitude_accuracy)()
    altitude_accuracy = (lambda self = None, value = None: pass# WARNING: Decompyle incomplete
)()
    heading = (lambda self = None: self._heading)()
    heading = (lambda self = None, value = None: pass# WARNING: Decompyle incomplete
)()
    speed = (lambda self = None: self._speed)()
    speed = (lambda self = None, value = None: pass# WARNING: Decompyle incomplete
)()
    
    def to_dict(self = None):
        result = {
            'latitude': self.latitude,
            'longitude': self.longitude,
            'accuracy': self.accuracy }
    # WARNING: Decompyle incomplete



class GeolocationPositionError:
    '''Represents a geolocation position error.'''
    TYPE_POSITION_UNAVAILABLE = 'positionUnavailable'
    
    def __init__(self = None, type = None):
        if type != self.TYPE_POSITION_UNAVAILABLE:
            raise ValueError(f'''type must be "{self.TYPE_POSITION_UNAVAILABLE}"''')
        self.type = type

    
    def to_dict(self = None):
        return {
            'type': self.type }



class Emulation:
    '''BiDi implementation of the emulation module.'''
    
    def __init__(self = None, conn = None):
        self.conn = conn

    
    def set_geolocation_override(self = None, coordinates = None, error = None, contexts = (None, None, None, None), user_contexts = ('coordinates', 'GeolocationCoordinates | None', 'error', 'GeolocationPositionError | None', 'contexts', 'list[str] | None', 'user_contexts', 'list[str] | None', 'return', 'None')):
        '''Set geolocation override for the given contexts or user contexts.

        Args:
            coordinates: Geolocation coordinates to emulate, or None.
            error: Geolocation error to emulate, or None.
            contexts: List of browsing context IDs to apply the override to.
            user_contexts: List of user context IDs to apply the override to.

        Raises:
            ValueError: If both coordinates and error are provided, or if both contexts
                and user_contexts are provided, or if neither contexts nor
                user_contexts are provided.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def set_timezone_override(self = None, timezone = None, contexts = None, user_contexts = (None, None, None)):
        """Set timezone override for the given contexts or user contexts.

        Args:
            timezone: Timezone identifier (IANA timezone name or offset string like '+01:00'),
                or None to clear the override.
            contexts: List of browsing context IDs to apply the override to.
            user_contexts: List of user context IDs to apply the override to.

        Raises:
            ValueError: If both contexts and user_contexts are provided, or if neither
                contexts nor user_contexts are provided.
        """
        pass
    # WARNING: Decompyle incomplete

    
    def set_locale_override(self = None, locale = None, contexts = None, user_contexts = (None, None, None)):
        '''Set locale override for the given contexts or user contexts.

        Args:
            locale: Locale string as per BCP 47, or None to clear override.
            contexts: List of browsing context IDs to apply the override to.
            user_contexts: List of user context IDs to apply the override to.

        Raises:
            ValueError: If both contexts and user_contexts are provided, or if neither
                contexts nor user_contexts are provided, or if locale is invalid.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def set_scripting_enabled(self = None, enabled = None, contexts = None, user_contexts = (False, None, None)):
        '''Set scripting enabled override for the given contexts or user contexts.

        Args:
            enabled: False to disable scripting, None to clear the override.
                Note: Only emulation of disabled JavaScript is supported.
            contexts: List of browsing context IDs to apply the override to.
            user_contexts: List of user context IDs to apply the override to.

        Raises:
            ValueError: If both contexts and user_contexts are provided, or if neither
                contexts nor user_contexts are provided, or if enabled is True.
        '''
        if enabled:
            raise ValueError('Only emulation of disabled JavaScript is supported (enabled must be False or None)')
    # WARNING: Decompyle incomplete

    
    def set_screen_orientation_override(self = None, screen_orientation = None, contexts = None, user_contexts = (None, None, None)):
        '''Set screen orientation override for the given contexts or user contexts.

        Args:
            screen_orientation: ScreenOrientation object to emulate, or None to clear the override.
            contexts: List of browsing context IDs to apply the override to.
            user_contexts: List of user context IDs to apply the override to.

        Raises:
            ValueError: If both contexts and user_contexts are provided, or if neither
                contexts nor user_contexts are provided.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def set_user_agent_override(self = None, user_agent = None, contexts = None, user_contexts = (None, None, None)):
        '''Set user agent override for the given contexts or user contexts.

        Args:
            user_agent: User agent string to emulate, or None to clear the override.
            contexts: List of browsing context IDs to apply the override to.
            user_contexts: List of user context IDs to apply the override to.

        Raises:
            ValueError: If both contexts and user_contexts are provided, or if neither
                contexts nor user_contexts are provided.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def set_network_conditions(self = None, offline = None, contexts = None, user_contexts = (False, None, None)):
        '''Set network conditions for the given contexts or user contexts.

        Args:
            offline: True to emulate offline network conditions, False to clear the override.
            contexts: List of browsing context IDs to apply the conditions to.
            user_contexts: List of user context IDs to apply the conditions to.

        Raises:
            ValueError: If both contexts and user_contexts are provided, or if neither
                contexts nor user_contexts are provided.
        '''
        pass
    # WARNING: Decompyle incomplete
