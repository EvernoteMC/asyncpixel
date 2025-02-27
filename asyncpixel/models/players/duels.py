"""Duels."""
from pydantic import BaseModel
from pydantic import Field


class Duels(BaseModel):
    """Duels games stats.

    Args:
        coins (int): Number of coins gathered in this Game Mode. Defaults to 0.
        current_winstreak (int): Current winstreak. Defaults to 0.
        best_winstreak (int): Best winstreak. Defaults to 0.
        games_played (int): Total number of games played. Defaults to 0.
        wins (int): Games won. Defaults to 0.
        losses (int): Games lost. Defaults to 0.
        kills (int): Number of kills. Defaults to 0.
        deaths (int): Number of deaths. Defaults to 0.
        melee_swings (int): Number of melee swings. Defaults to 0.
        melee_hits (int): Number of melee hits. Defaults to 0.
        bow_shots (int): Number of bow shots. Defaults to 0.
        bow_hits (int): Number of bow hits. Defaults to 0.
        blocks_placed (int): Number of blocks placed. Defaults to 0.
        damage_dealt (int): Amount of damage dealt. Defaults to 0.
    """

    coins: int = 0
    current_winstreak: int = 0
    best_winstreak: int = Field(0, alias="best_overall_winstreak")
    games_played: int = Field(0, alias="games_played_duels")
    wins: int = 0
    losses: int = 0
    kills: int = 0
    deaths: int = 0
    melee_swings: int = 0
    melee_hits: int = 0
    bow_shots: int = 0
    bow_hits: int = 0
    blocks_placed: int = 0
    damage_dealt: int = 0

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
