"""Arena Brawl"""
from pydantic import BaseModel


class ArenaBrawl(BaseModel):
    """Arena games stats.

    Args:
        coins (int): Number of coins. Defaults to 0.
        keys (int): Number of keys. Defaults to 0.
        wins (int): Games won. Defaults to 0.
        losses (int): Games lost. Defaults to 0.
        kills (int): Number of kills. Defaults to 0.
        deaths (int): Number of deaths. Defaults to 0.
    """

    coins: int = 0
    keys: int = 0
    wins: int = 0
    losses: int = 0
    kills: int = 0
    deaths: int = 0

    @property
    def win_loss_ratio(self) -> float:
        """Games won per game lost.

        Returns:
            float: ratio of wins and losses.
        """
        if self.losses == 0:
            return 0.0
        return self.wins / self.losses

    @property
    def kill_death_ratio(self) -> float:
        """Kills per death.

        Returns:
            float: ratio of kills and deaths.
        """
        if self.deaths == 0:
            return 0.0
        return self.kills / self.deaths
