"""National Grid MA."""

from .base import UtilityBase
from .nationalgrid import NationalGrid


class NationalGridMA(NationalGrid, UtilityBase):
    """National Grid MA."""

    @staticmethod
    def name() -> str:
        """Distinct recognizable name of the utility."""
        return "National Grid (MA)"

    @staticmethod
    def subdomain() -> str:
        """Return the opower.com subdomain for this utility."""
        return "ngma"

    @staticmethod
    def supports_realtime_usage() -> bool:
        """Check if Utility supports realtime usage reads."""
        return True
