"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from tabulate import tabulate

from src.recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    # Starter example profile
    user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}

    recommendations = recommend_songs(user_prefs, songs, k=5)

    # --- Terminal layout ---
    print()
    print("TOP RECOMMENDATIONS")
    print(
        f"for genre={user_prefs['genre']}, "
        f"mood={user_prefs['mood']}, "
        f"energy={user_prefs['energy']}"
    )

    # Build one table row per recommendation. The final "Why" column carries the
    # reasons string that recommend_songs produced for each score.
    rows = [
        [rank, song["title"], song["artist"], f"{score:.2f}", explanation]
        for rank, (song, score, explanation) in enumerate(recommendations, start=1)
    ]
    print(tabulate(
        rows,
        headers=["#", "Title", "Artist", "Score", "Why (reasons)"],
        tablefmt="grid",
        disable_numparse=True,  # keep 2.00 / 1.90 instead of 2 / 1.9
    ))


if __name__ == "__main__":
    main()
