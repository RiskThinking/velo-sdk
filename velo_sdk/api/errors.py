from datetime import datetime


class APIError(Exception):
    """
    General exception for API errors.
    Attributes:
        message: The error message.
        code: HTTP status code.
        status: HTTP status text.
        timestamp: When the error occurred.
    """

    def __init__(self, message, code=None, status=None, timestamp=None):
        self.message = message
        self.code = code
        self.status = status or "Error"
        self.timestamp = timestamp or datetime.now()
        super().__init__(f"{self.status}: {self.message}")


class RateLimitError(APIError):
    """
    Exception raised when rate limiting is exceeded.
    """

    def __init__(self, message, status=None, timestamp=None):
        self.message = message
        self.code = 429
        self.status = status or "Error"
        self.timestamp = timestamp or datetime.now()
        super().__init__(message=message, code=429, status=status, timestamp=timestamp)


class InsufficientCreditsError(APIError):
    """
    Exception raised when the user has insufficient API credits.
    This is a non-retryable error that requires the user to add credits.
    """

    def __init__(self, message, status=None, timestamp=None):
        self.message = message
        self.code = 429
        self.status = status or "Error"
        self.timestamp = timestamp or datetime.now()
        super().__init__(message=message, code=429, status=status, timestamp=timestamp)
