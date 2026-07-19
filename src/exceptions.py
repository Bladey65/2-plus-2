class MathematicalParadoxError(Exception):
    """Raised when the universe breaks and basic addition fails."""
    def __init__(self, message="Reality error: Sum does not equal four."):
        super().__init__(message)

class TemporalLatencyWarning(Warning):
    """Raised when the addition takes longer than 0.000001 seconds."""
    pass