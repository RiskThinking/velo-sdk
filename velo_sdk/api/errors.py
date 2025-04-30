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

    def __init__(self, status=None, timestamp=None):
        self.message = "Rate limit exceeded"
        self.code = 429
        self.status = status or "Error"
        self.timestamp = timestamp or datetime.now()
        super().__init__(f"{self.status}: {self.message}")
