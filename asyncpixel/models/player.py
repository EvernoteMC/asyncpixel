"""Player objects."""
import datetime
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Union

from asyncpixel import utils
from asyncpixel.constants import get_game_types
from pydantic import BaseModel
from pydantic import Field
from pydantic import validator
from pydantic.class_validators import root_validator
from pydantic.types import UUID4

from .game_type import GameType
from .players import Arcade
from .players import ArenaBrawl
from .players import Bedwars
from .players import BlitzSurvivalGames
from .players import BuildBattle
from .players import CopsAndCrims
from .players import Duels
from .players import MegaWalls
from .players import MurderMystery
from .players import Paintball
from .players import Pit
from .players import Quakecraft
from .players import SkyWars
from .players import SmashHeroes
from .players import SpeedUHC
from .players import TNTGames
from .players import TurboKartRacers
from .players import UHC
from .players import VampireZ
from .players import Walls
from .players import Warlords
from .utils import to_camel


class Stats(BaseModel):
    """Game Stats.

    Args:
        arcade (Optional[Arcade]): Arcade stats.
        arena_brawl (Optional[ArenaBrawl]): Arena Brawl stats.
        bedwars (Optional[Bedwars]): Bedwars stats.
        blitz_survival_games (Optional[BlitzSurvivalGames]): Blitz Survival Games stats.
        build_battle (Optional[BuildBattle]): Build Battle stats.
        cops_and_crims (Optional[CopsAndCrims]): Cops and Crims stats.
        duels (Optional[Duels]): Duels stats.
        mega_walls (Optional[MegaWalls]): Mega Walls stats.
        murder_mystery (Optional[MurderMystery]): Murder Mystery stats.
        paintball (Optional[Paintball]): Paintball stats.
        pit (Optional[Pit]): Pit stats.
        quakecraft (Optional[Quake]): Quakecraft stats.
        skywars (Optional[SkyWars]): SkyWars stats.
        smash_heroes (Optional[SmashHeroes]): Smash Heroes stats.
        speed_uhc (Optional[SpeedUHC]): Speed UHC stats.
        tnt_games (Optional[TNTGames]): TNT Games stats.
        turbo_kart_racers (Optional[TurboKartRacers]): Turbo Kart Racers stats.
        uhc (Optional[UHC]): UHC stats.
        vampirez (Optional[VampireZ]): VampireZ stats.
        walls (Optional[Walls]): Walls stats.
        warlords (Optional[Warlords]): Warlords stats.
    """

    arcade: Optional[Arcade] = Field(alias="Arcade")
    arena_brawl: Optional[ArenaBrawl] = Field(alias="Arena")
    bedwars: Optional[Bedwars] = Field(alias="Bedwars")
    blitz_survival_games: Optional[BlitzSurvivalGames] = Field(alias="HungerGames")
    build_battle: Optional[BuildBattle] = Field(alias="BuildBattle")
    cops_and_crims: Optional[CopsAndCrims] = Field(alias="MCGO")
    duels: Optional[Duels] = Field(alias="Duels")
    mega_walls: Optional[MegaWalls] = Field(alias="Walls3")
    murder_mystery: Optional[MurderMystery] = Field(alias="MurderMystery")
    paintball: Optional[Paintball] = Field(alias="Paintball")
    pit: Optional[Pit] = Field(alias="Pit")
    quakecraft: Optional[Quakecraft] = Field(alias="Quakecraft")
    skywars: Optional[SkyWars] = Field(alias="SkyWars")
    smash_heroes: Optional[SmashHeroes] = Field(alias="SuperSmash")
    speed_uhc: Optional[SpeedUHC] = Field(alias="SpeedUHC")
    tnt_games: Optional[TNTGames] = Field(alias="TNTGames")
    turbo_kart_racers: Optional[TurboKartRacers] = Field(alias="GingerBread")
    uhc: Optional[UHC] = Field(alias="UHC")
    vampirez: Optional[VampireZ] = Field(alias="VampireZ")
    walls: Optional[Walls] = Field(alias="Walls")
    warlords: Optional[Warlords] = Field(alias="Battleground")


class Social(BaseModel):
    """Social accounts.

    Args:
        twitter (Optional[str]): Twitter.
        youtube (Optional[str]): YouTube.
        instagram (Optional[str]): Instagram.
        twitch (Optional[str]): Twitch.
        discord (Optional[str]): Discord.
        hypixel_forums (Optional[str]): Hypixel Forums.
    """

    twitter: Optional[str]
    youtube: Optional[str]
    instagram: Optional[str]
    twitch: Optional[str]
    discord: Optional[str]
    hypixel_forums: Optional[str]

    @root_validator(pre=True)
    def get_social_media(  # noqa: D102
        cls, values: Dict[str, Any]  # noqa: B902, N805, D102
    ) -> Dict[str, Any]:
        out = values.copy()
        for k, v in out["links"].items():
            out[k.lower()] = v
        return out


class Player(BaseModel):
    """Player.

    Args:
        uuid (UUID4): uuid of user.
        displayname (Optional[str]): Display name of user.
        rank (Optional[str]): Rank of user
        first_login (datetime.datetime): First login date.
        last_login (Optional[datetime.datetime]): Most recent login date.
        last_logout (Optional[datetime.datetime]): Last logout.
        stats (Stats): Stats for various game types.
        social_media (Optional[Social]): Social media accounts.
        id (Optional[str]): id of user.
        playername (Optional[str]): Playername.
        known_aliases (Optional[List[str]]): known aliases.
        known_aliases_lower (Optional[List[str]]): known aliases in lowercase.
        achievements_one_time (Optional[List[str]]): Achievements.
        mc_version_rp (Optional[str]): Minecraft version.
        network_exp (Optional[float]): Network experience.
        karma (Optional[int]): Player karma.
        last_adsense_generate_time (Optional[datetime.datetime]): Last generate
            time for adsense.
        last_claimed_reward (Optional[int]): Last claimed reward.
        total_rewards (Optional[int]): Total rewards.
        total_daily_rewards (Optional[int]): Total daily awards.
        reward_streak (Optional[int]): Current reward streak.
        reward_score (Optional[int]): Reward score.
        reward_high_score (Optional[int]): High score for rewards.
        friend_requests_uuid (Optional[List[UUID4]]): UUID of friend requests.
        achievement_tracking (Optional[List[str]]): Achievement tracking.
        achievement_points (Optional[int]): achievement points.
        current_gadget (Optional[str]): Current equipped gadget.
        channel (Optional[str]): Channel.
        most_recent_game_type (Optional[GameType]): Most recent Game Type that
            has been played.
        level (Optional[float]): Level of user.
        raw (Dict[str, Any]): raw data
    """

    uuid: UUID4
    displayname: Optional[str]
    rank: Optional[str]

    @root_validator(pre=True)
    def create_rank(  # noqa: D102
        cls, values: Dict[str, Any]  # noqa: B902, N805, D102
    ) -> Dict[str, Any]:
        out = values.copy()
        rank = utils.get_rank(
            values.get("rank"),
            values.get("prefix"),
            values.get("monthlyPackageRank"),
            values.get("newPackageRank"),
            values.get("packageRank"),
        )
        out["rank"] = rank
        return out

    first_login: datetime.datetime
    last_login: Optional[datetime.datetime]
    last_logout: Optional[datetime.datetime]
    stats: Stats
    social_media: Optional[Social]

    id: Optional[str] = Field(alias="_id")
    playername: Optional[str]
    known_aliases: Optional[List[str]]
    known_aliases_lower: Optional[List[str]]
    achievements_one_time: Optional[List[str]]
    mc_version_rp: Optional[str]
    network_exp: Optional[float]
    karma: Optional[int]
    last_adsense_generate_time: Optional[datetime.datetime]
    last_claimed_reward: Optional[int]
    total_rewards: Optional[int]
    total_daily_rewards: Optional[int]
    reward_streak: Optional[int]
    reward_score: Optional[int]
    reward_high_score: Optional[int]
    friend_requests_uuid: Optional[List[UUID4]]
    achievement_tracking: Optional[List[str]]
    achievement_points: Optional[int]
    current_gadget: Optional[str]
    channel: Optional[str]
    most_recent_game_type: Optional[GameType]

    @validator("most_recent_game_type", pre=True)
    def validate_game_type(  # noqa: D102
        cls, v: Union[str, int]  # noqa: B902, N805
    ) -> GameType:
        try:
            game_type = [game for game in get_game_types() if game.id == v][0]
        except Exception:
            game_type = [game for game in get_game_types() if game.type_name == v][0]
        return game_type

    level: float

    @root_validator(pre=True)
    def create_level(  # noqa: D102
        cls, values: Dict[str, Any]  # noqa: B902, N805, D102
    ) -> Dict[str, Any]:
        out = values.copy()
        exp = float(out.get("networkExp"))  # type: ignore
        out["level"] = utils.calc_player_level(exp)
        return out

    raw: Dict[str, Any]

    @root_validator(pre=True)
    def create_raw(  # noqa: D102
        cls, values: Dict[str, Any]  # noqa: B902, N805, D102
    ) -> Dict[str, Any]:
        out = values.copy()
        out["raw"] = out
        return out

    class Config:
        """Config."""

        alias_generator = to_camel
