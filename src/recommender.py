from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from a CSV file into a list of dicts, converting numeric columns to int/float."""
    float_columns = {
        "energy", "tempo_bpm", "valence", "danceability", "acousticness",
    }

    songs: List[Dict] = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["id"] = int(row["id"])
            for column in float_columns:
                row[column] = float(row[column])
            songs.append(row)

    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score one song against user prefs (genre +1, mood +1, energy similarity x2), returning (score, reasons)."""
    score = 0.0
    reasons: List[str] = []

    # Genre match: all-or-nothing. Halved from its original +2.0 so genre no
    # longer dominates; it now carries the same weight as a mood match.
    if song["genre"] == user_prefs.get("genre"):
        score += 1.0
        reasons.append("genre match (+1.0)")

    # Mood match: all-or-nothing, equal to a genre match under the new weights.
    if song["mood"] == user_prefs.get("mood"):
        score += 1.0
        reasons.append("mood match (+1.0)")

    # Energy similarity: partial credit for how close the song's energy is to
    # the user's target, doubled so energy is now the strongest single signal.
    # A perfect match is worth 2.0, shrinking toward 0.0 as the song's energy
    # drifts a full 1.0 apart (in either direction).
    target_energy = user_prefs.get("energy")
    if target_energy is not None:
        # Clamp the target into the valid 0.0-1.0 range so out-of-range or
        # non-numeric input can't produce huge negative scores or crash.
        try:
            target_energy = min(1.0, max(0.0, float(target_energy)))
        except (TypeError, ValueError):
            target_energy = None

    if target_energy is not None:
        energy_points = 2.0 * (1.0 - abs(target_energy - song["energy"]))
        score += energy_points
        reasons.append(f"energy similarity (+{energy_points:.2f})")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Score every song with score_song, then return the top k as (song, score, explanation) tuples sorted high-to-low."""
    scored: List[Tuple[Dict, float, str]] = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = ", ".join(reasons) if reasons else "no strong matches"
        scored.append((song, score, explanation))

    # Sort by the numeric score, highest first, and keep the top k.
    # Guard against a negative k, which would otherwise slice from the end
    # and silently return the wrong songs.
    if k < 0:
        k = 0
    scored.sort(key=lambda item: item[1], reverse=True)
    return scored[:k]
