"""Bedwars."""
from pydantic import BaseModel
from pydantic import Field
from pydantic import PrivateAttr


class BedwarsMode(BaseModel):
    """Bedwars Mode stats.

    Args:
        winstreak (int): Winstreak. Defaults to 0.
        games_played (int): Total number of games played. Defaults to 0.
        wins (int): Games won. Defaults to 0.
        losses (int): Games lost. Defaults to 0.
        final_kills (int): Number of final kills. Defaults to 0.
        final_deaths (int): Number of final deaths. Defaults to 0.
        beds_broken (int): Number of beds broken. Defaults to 0.
        beds_lost (int): Number of beds lost. Defaults to 0.
        kills (int): Number of kills. Defaults to 0.
        deaths (int): Number of deaths. Defaults to 0.
    """
    _mode: str = PrivateAttr()

    def __init__(self, mode: str, **kwargs):
        super().__init__(**kwargs)
        self._mode = mode

    winstreak: int = Field(0, alias=f"{_mode}_winstreak")
    games_played: int = Field(0, alias=f"{_mode}_games_played_bedwars")
    wins: int = Field(0, alias=f"{_mode}_wins_bedwars")
    losses: int = Field(0, alias=f"{_mode}_losses_bedwars")
    final_kills: int = Field(0, alias=f"{_mode}_final_kills_bedwars")
    final_deaths: int = Field(0, alias=f"{_mode}_final_deaths_bedwars")
    beds_broken: int = Field(0, alias=f"{_mode}_beds_broken_bedwars")
    beds_lost: int = Field(0, alias=f"{_mode}_beds_lost_bedwars")
    kills: int = Field(0, alias=f"{_mode}_kills_bedwars")
    deaths: int = Field(0, alias=f"{_mode}_deaths_bedwars")

    @property
    def kill_death_ratio(self) -> float:
        """Kills per death.

        Returns:
            float: ratio of kills and deaths.
        """
        if self.deaths == 0:
            return 0.0
        return self.kills / self.deaths

    @property
    def final_kill_death_ratio(self) -> float:
        """Final kills per final death.

        Returns:
            float: ratio of final kills and final deaths.
        """
        if self.final_deaths == 0:
            return 0.0
        return self.final_kills / self.final_deaths

    @property
    def beds_broken_lost_ratio(self) -> float:
        """Beds broken per bed lost.

        Returns:
            float: ratio of beds broken and beds lost.
        """
        if self.beds_lost == 0:
            return 0.0
        return self.beds_broken / self.beds_lost

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
    def win_percentage(self) -> float:
        """Percentage of games won.

        Returns:
            float: ratio of wins and games played.
        """
        if self.losses == 0:
            return 0.0
        return (self.wins / self.games_played) * 100


class Bedwars(BaseModel):
    """Bedwars Stats.

    Args:
        coins (int)
        experience (int)
        winstreak (int)
        games_played (int)
        wins (int)
        losses (int)
        final_kills (int)
        final_deaths (int)
        beds_broken (int)
        beds_lost (int)
        kills (int)
        deaths (int)
        solo (BedwarsMode)
        doubles (BedwarsMode)
        threes (BedwarsMode)
        fours (BedwarsMode)
        four_v_four (BedwarsMode)
    """
    coins: int = 0
    experience: int = Field(0, alias="Experience")
    winstreak: int = 0
    games_played: int = Field(0, alias="games_played_bedwars")
    wins: int = Field(0, alias="wins_bedwars")
    losses: int = Field(0, alias="losses_bedwars")
    final_kills: int = Field(0, alias="final_kills_bedwars")
    final_deaths: int = Field(0, alias="final_deaths_bedwars")
    beds_broken: int = Field(0, alias="beds_broken_bedwars")
    beds_lost: int = Field(0, alias="beds_lost_bedwars")
    kills: int = Field(0, alias="kills_bedwars")
    deaths: int = Field(0, alias="deaths_bedwars")

    solo = BedwarsMode(mode="eight_one")
    doubles = BedwarsMode(mode="eight_two")
    threes = BedwarsMode(mode="four_three")
    fours = BedwarsMode(mode="four_four")
    four_v_four = BedwarsMode(mode="two_four")

    @property
    def level(self) -> int:
        """Bedwars Level

        Returns:
            int: bedwars level
        """
        return 0

    @property
    def kill_death_ratio(self) -> float:
        """Kills per death.

        Returns:
            float: ratio of kills and deaths.
        """
        if self.deaths == 0:
            return 0.0
        return self.kills / self.deaths

    @property
    def final_kill_death_ratio(self) -> float:
        """Final kills per final death.

        Returns:
            float: ratio of final kills and final deaths.
        """
        if self.final_deaths == 0:
            return 0.0
        return self.final_kills / self.final_deaths

    @property
    def beds_broken_lost_ratio(self) -> float:
        """Beds broken per bed lost.

        Returns:
            float: ratio of beds broken and beds lost.
        """
        if self.beds_lost == 0:
            return 0.0
        return self.beds_broken / self.beds_lost

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
    def win_percentage(self) -> float:
        """Percentage of games won.

        Returns:
            float: ratio of wins and games played.
        """
        if self.losses == 0:
            return 0.0
        return (self.wins / self.games_played) * 100
