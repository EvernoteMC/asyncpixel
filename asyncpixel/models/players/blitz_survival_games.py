"""Hunger Games."""
from pydantic import BaseModel
from pydantic import Field


class BlitzSurvivalGames(BaseModel):
    """Hunger Games games stats.

    Args:
        coins (int): Number of coins. Defaults to 0.
        games_played (int): Total number of games played. Defaults to 0.
        blitz_uses (int): Number of blitz star uses. Defaults to 0.
        wins (int): Number of wins. Defaults to 0.
        kills (int): Number of kills. Defaults to 0.
        deaths (int): Number of deaths. Defaults to 0.
        solo_normal_wins (int): Number of solo normal wins. Defaults to 0.
        solo_normal_kills (int): Number of solo normal kills. Defaults to 0.
        solo_chaos_wins (int): Number of solo chaos wins. Defaults to 0.
        solo_chaos_kills (int): Number of solo chaos kills. Defaults to 0.
        solo_wins (int): Number of solo wins. Defaults to 0.
        solo_kills (int): Number of solo kills. Defaults to 0.
        team_wins (int): Number of team wins. Defaults to 0.
        team_kills (int): Number of team kills. Defaults to 0.
        taunt_kills (int): Number of taunt kills. Defaults to 0.
        mobs_spawned (int): Number of mobs spawned. Defaults to 0.
        chests_opened (int): Number of chests opened. Defaults to 0.
        damage_dealt (int): Amount of damage dealt. Defaults to 0.
        damage_taken (int): Amount of damage taken. Defaults to 0.
        arrows_fired (int): Number of arrows fired. Defaults to 0.
        arrows_hit (int): Number of arrows hit. Defaults to 0.
        potions_drunk (int): Number of potions drunk. Defaults to 0.
        potions_thrown (int): Number of potions thrown. Defaults to 0.
        time_played (int): Time played in seconds. Defaults to 0.
    """

    coins: int = 0
    games_played: int = 0
    blitz_uses: int = 0
    kills: int = 0
    deaths: int = 0
    solo_normal_wins: int = Field(0, alias="wins_solo_normal")
    solo_normal_kills: int = Field(0, alias="kills_solo_normal")
    solo_chaos_wins: int = Field(0, alias="wins_solo_chaos")
    solo_chaos_kills: int = Field(0, alias="kills_solo_chaos")
    # solo_wins: int = solo_normal_wins + solo_chaos_wins
    # solo_kills: int = solo_normal_kills + solo_chaos_kills
    team_wins: int = 0
    team_kills: int = Field(0, alias="kills_teams_normal")
    # wins: int = solo_wins + team_wins
    taunt_kills: int = 0
    mobs_spawned: int = 0
    chests_opened: int = 0
    damage_dealt: int = 0
    damage_taken: int = 0
    arrows_fired: int = 0
    arrows_hit: int = 0
    potions_drunk: int = 0
    potions_thrown: int = 0
    time_played: int = 0

    @property
    def kill_death_ratio(self) -> float:
        """Kills per death.

        Returns:
            float: ratio of kills and deaths.
        """
        if self.deaths == 0:
            return 0.0
        return self.kills / self.deaths
