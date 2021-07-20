"""Build Battle."""
from pydantic import BaseModel
from pydantic import Field


class BuildBattle(BaseModel):
    """Build Battle games stats.

    Args:
        coins (int): Number of coins. Defaults to 0.
        score (int): Total score. Defaults to 0.
        games_played (int): Total games played. Defaults to 0.
        votes (int): Number of votes. Defaults to 0.
        wins (int): Games won. Defaults to 0.
        losses (int): Games lost. Defaults to 0.
        solo_wins (int): Solo games won. Defaults to 0.
        team_wins (int): Team games won. Defaults to 0.
        pro_wins (int): Pro games won. Defaults to 0.
        guess_the_build_wins (int): Guess the Build games won. Defaults to 0.
    """

    coins: int = 0
    score: int = 0
    games_played: int = 0
    votes: int = 0
    wins: int = 0
    losses: int = games_played - wins
    solo_wins: int = Field(0, alias="wins_solo_normal")
    team_wins: int = Field(0, alias="wins_team_normal")
    pro_wins: int = Field(0, alias="wins_solo_pro")
    guess_the_build_wins: int = Field(0, alias="wins_guess_the_build")

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
