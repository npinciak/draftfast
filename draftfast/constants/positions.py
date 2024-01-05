from enum import Enum
from draftfast.constants.leagues import Leagues
from draftfast.constants.sites import Sites
from draftfast.rules_utils import get_nfl_positions, get_nfl_showdown_positions

class ShowdownPositions(Enum):
    Cpt = "CPT"
    Flex = "FLEX"

class MvpPositions(Enum):
    Mvp = "MVP"
    Star = "STAR"
    Pro = "PRO"
    Util = "UTIL"

class FootballPositions(Enum):
    QB = "QB"
    RB = "RB"
    WR = "WR"
    TE = "TE"
    DST = "DST"

class BasketballPositions(Enum):
    PG = "PG"
    SG = "SG"
    SF = "SF"
    PF = "PF"
    C = "C"
    G = "G"
    F = "F"

class Soccer(Enum):
    F = "F"
    M = "M"
    D = "D"
    GK = "GK"
    G = "G"

class El(Enum):
    G = "G"
    F = "F"

class Racing(Enum):
    D = "D"
    Cnstr = "CNSTR"

class Golf(Enum):
    G = "G"

class Tennis(Enum):
    P = "P"

class BaseballPositions(Enum):
    P = "P"
    SP = "P"
    RP = "P"
    C = "C"
    First = "1B"
    Second = "2B"
    Third = "3B"
    SS = "SS"
    OF = "OF"

class Hockey(Enum):
    C = "C"
    W = "W"
    D = "D"
    G = "G"



POSITIONS_BY_SITE_BY_LEAGUE = {
   [Sites.Draftkings.value]: {
       [Leagues.Nba.value]: [
           [BasketballPositions.PG.value, 1, 3],
           [BasketballPositions.SG.value, 1, 3],
           [BasketballPositions.SF.value, 1, 3],
           [BasketballPositions.PF.value, 1, 3],
           [BasketballPositions.C.value, 1, 2],
        ],
        [Leagues.NbaShowdown.value]: [
            [ShowdownPositions.Cpt.value, 1, 1],
            [ShowdownPositions.Flex.value, 5, 5],
        ],
        [Leagues.Wnba.value]: [
            [BasketballPositions.PG.value, 1, 3],
            [BasketballPositions.SG.value, 1, 3],
            [BasketballPositions.SF.value, 1, 4],
            [BasketballPositions.PF.value, 1, 4],
        ],
        [Leagues.Nfl.value]: get_nfl_positions(),
        [Leagues.NflShowdown.value]: get_nfl_showdown_positions(dk=True),
        [Leagues.Mlb.value]: [
            [BaseballPositions.SP.value, 0, 2],
            [BaseballPositions.RP.value, 0, 2],
            [BaseballPositions.C.value, 1, 1],
            [BaseballPositions.First.value, 1, 1],
            [BaseballPositions.Second.value, 1, 1],
            [BaseballPositions.Third.value, 1, 1],
            [BaseballPositions.SS.value, 1, 1],
            [BaseballPositions.OF.value, 3, 3],
        ],
        [Leagues.Soccer.value]: [
            [Soccer.F.value, 2, 3],
            [Soccer.M.value, 2, 3],
            [Soccer.D.value, 2, 3],
            [Soccer.GK.value, 1, 2],
        ],
        [Leagues.EuroLeague.value]: [
            [Soccer.G.value, 2, 3],
            [Soccer.F.value, 3, 4],
        ],
        [Leagues.Nhl.value]: [
            [Hockey.C.value, 2, 3],
            [Hockey.W.value, 3, 4],
            [Hockey.D.value, 2, 3],
            [Hockey.G.value, 1, 1],
        ],
        [Leagues.NhlShowdown.value]: [
            [ShowdownPositions.Flex.value, 6, 6],
        ],
        [Leagues.MlbShowdown.value]: [
            [ShowdownPositions.Cpt.value, 1, 1],
            [ShowdownPositions.Flex.value, 5, 5],
        ],
        [Leagues.Xfl.value]: [[FootballPositions.QB.value, 1, 1], [FootballPositions.RB.value, 1, 3], [FootballPositions.WR.value, 2, 4], [FootballPositions.DST.value, 1, 1]],
        [Leagues.Tennis.value]: [
            [Tennis.P.value, 6, 6],
        ],
        [Leagues.Pga.value]: [
            [Golf.G.value, 6, 6],
        ],
        [Leagues.PgaCaptain.value]: [
            [ShowdownPositions.Cpt.value, 1, 1],
            [Golf.G.value, 5, 5],
        ],
        [Leagues.CsgoShowdown.value]: [
            [ShowdownPositions.Cpt.value, 1, 1],
            [ShowdownPositions.Flex.value, 5, 5],
        ],
        [Leagues.F1Showdown.value]: [
            [ShowdownPositions.Cpt.value, 1, 1],
            [Racing.D.value, 4, 4],
            [Racing.Cnstr.value, 1, 1],
        ],
        [Leagues.Nascar.value]: [
            [Racing.D.value, 6, 6],
        ],
    },
    [Sites.Fanduel.value]: {
        [Leagues.Nba.value]: [
            [BasketballPositions.PG.value, 2, 2],
            [BasketballPositions.SG.value, 2, 2],
            [BasketballPositions.SF.value, 2, 2],
            [BasketballPositions.PF.value, 2, 2],
            [BasketballPositions.C.value, 1, 1],
        ],
        [Leagues.Mlb.value]: [
            [BaseballPositions.Pitcher.value, 1, 1],
            [BaseballPositions.First.value, 1, 2],  # TODO - allow C or 1B
            [BaseballPositions.Second.value, 1, 2],
            [BaseballPositions.Third.value, 1, 2],
            [BaseballPositions.SS.value, 1, 2],
            [BaseballPositions.OF.value, 3, 4],
        ],
        [Leagues.MlbMvp.value]: [
            [MvpPositions.Mvp.value, 1, 1],
            [MvpPositions.Star.value, 1, 1],
            [MvpPositions.Util.value, 3, 3],
        ],
        [Leagues.NbaMvp.value]: [
            [MvpPositions.Mvp.value, 1, 1],
            [MvpPositions.Star.value, 1, 1],
            [MvpPositions.Pro.value, 1, 1],
            [MvpPositions.Util.value, 2, 2],
        ],
        [Leagues.Wnba.value]: [
            [BasketballPositions.G.value, 3, 3],
            [BasketballPositions.F.value, 4, 4],
        ],
        [Leagues.Nfl.value]: get_nfl_positions(d_abbrev="D"),
        [Leagues.NflMvp.value]: get_nfl_showdown_positions(fd=True),
        [Leagues.Nascar.value]: [
            [Racing.D.value, 5, 5],
        ],
        [Leagues.Pga.value]: [
            [Golf.G.value, 6, 6],
        ],
    }
}

NBA_GENERAL_POSITIONS = [
    [BasketballPositions.G.value, 3, 4],
    [BasketballPositions.F.value, 3, 4],
    [BasketballPositions.C.value, 1, 2],
]

MLB_GENERAL_POSITIONS = [
    [BaseballPositions.P.value, 2, 2],
]

WNBA_GENERAL_POSITIONS = [
    [BasketballPositions.G.value, 2, 3],
    [BasketballPositions.F.value, 3, 4],
]

