"""Ginerbread."""
from pydantic import BaseModel


class TurboKartRacers(BaseModel):
    """GingerBread games stats.

    Args:
        coins (int): Number of coins gathered in this Game Mode. Defaults to 0.
    """

    coins: int = 0
