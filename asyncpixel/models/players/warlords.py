"""Battleground."""
from pydantic import BaseModel
from pydantic import Field


class Warlords(BaseModel):
    """Battleground games stats.

    Args:
        coins (int): Number of coins gathered in this Game Mode. Defaults to 0.
        wins (int): Games won. Defaults to 0.
        losses (int): Games lost. Defaults to 0.
        kills (int): Number of kills. Defaults to 0.
        assists (int): Number of assists. Defaults to 0.
        deaths (int): Number of deaths. Defaults to 0.
        damage_dealt (int): Amount of damage dealt. Defaults to 0.
        damage_taken (int): Amount of damage taken. Defaults to 0.
        damage_prevented (int): Amount of damage prevented. Defaults to 0.
        healed (int): Amount healed. Defaults to 0.
    """

    coins: int = 0
    wins: int = 0
    losses: int = 0
    kills: int = 0
    assists: int = 0
    deaths: int = 0
    damage_dealt: int = Field(0, alias="damage")
    damage_taken: int = 0
    damage_prevented: int = 0
    healed: int = Field(0, alias="heal")

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
