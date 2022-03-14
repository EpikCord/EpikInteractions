class EpikCordException(Exception):
    """
    A class that all exceptions will inherit from for easy broad error handling
    """
    ...

class InvalidArgumentType(TypeError, EpikCordException):
    """
    An exception that is thrown when an argument is passed in the wrong type
    """
    ...

class TooManyComponents(EpikCordException):
    """
    An exception that is thrown when too many components are passed in to an action row
    """
    ...

class CustomIdIsTooBig(EpikCordException):
    """
    An exception that is thrown when the custom id is too big
    """
    ...

class TooManySelectMenuOptions(EpikCordException):
    """
    An exception that is thrown when too many options are passed in to a select menu
    """
    ...

class InvalidComponentStyle(EpikCordException):
    """
    An exception that is thrown when a component style is invalid
    """
    ...

class LabelIsTooBig(EpikCordException):
    """
    An exception that is thrown when a label is too big
    """
    ...

class ThreadArchived(EpikCordException):
    """
    An exception that is thrown when a thread is archived
    """
    ...

class NotFound404(EpikCordException):
    """
    An exception that is thrown when a resource is not found
    """
    ...