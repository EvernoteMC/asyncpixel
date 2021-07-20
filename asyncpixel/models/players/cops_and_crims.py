"""MCGO."""
from pydantic import BaseModel
from pydantic import Field


class Deathmatch(BaseModel):
    """Cops and Crims Deathmatch stats

    Args:
        wins (int): Number of wins. Defaults to 0.
        kills (int): Number of kills. Defaults to 0.
        deaths (int): Number of deaths. Defaults to 0.
        criminal_kills (int): Number of kills as a criminal. Defaults to 0.
        cop_kills (int): Number of kills as a cop. Defaults to 0.
    """

    wins: int = Field(0, alias="game_wins_deathmatch")
    kills: int = 0  # TODO
    deaths: int = 0
    criminal_kills: int = 0
    cop_kills: int = 0


class CopsAndCrims(BaseModel):
    """MCGO games stats.

    Args:
        coins (int): Number of coins. Defaults to 0.
        wins (int): Games won. Defaults to 0.
        kills (int): Number of kills. Defaults to 0.
        deaths (int): Number of deaths. Defaults to 0.
        round_wins (int): Total round wins. Defaults to 0.
        shots_fired (int): Total shots fired. Defaults to 0.
        headshot_kills (int): Headshot kills. Defaults to 0.
        bombs_defused (int): Number of bombs defused. Defaults to 0.
        bombs_planted (int): Number of bombs planted. Defaults to 0.
        criminal_kills (int): Number of kills as a criminal. Defaults to 0.
        cop_kills (int): Number of kills as a cop. Defaults to 0.
        deathmatch (Deathmatch): Total games won of deathmatch. Defaults to 0.
    """

    coins: int = 0
    wins: int = Field(0, alias="game_wins")
    kills: int = 0
    deaths: int = 0
    round_wins: int = 0
    shots_fired: int = 0
    headshot_kills: int = 0
    bombs_defused: int = 0
    bombs_planted: int = 0
    criminal_kills: int = 0
    cop_kills: int = 0
    deathmatch: Deathmatch = Deathmatch()
