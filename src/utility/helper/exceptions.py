
from typing import Optional, Mapping, Any, Union

class AutoTainmentException(Exception):
    """Base exception class for Program."""


class APIException(AutoTainmentException):
    """Exception due to an error response from API."""
    
