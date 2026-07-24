class LLMError(Exception):
    """Base exception for all LLM related errors."""
    pass
class LLMAPIError(LLMError):
    """Raised when Gemini API Call fails."""
    pass

class LLMResponseError(LLMError):
    """Raised when Gemini returns invalid response."""
    pass