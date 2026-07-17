"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    # Starter example profile
    user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}

    recommendations = recommend_songs(user_prefs, songs, k=5)

    # --- Terminal layout ---
    width = 60
    print()
    print("=" * width)
    print("TOP RECOMMENDATIONS".center(width))
    print(
        f"for genre={user_prefs['genre']}, "
        f"mood={user_prefs['mood']}, "
        f"energy={user_prefs['energy']}".center(width)
    )
    print("=" * width)

    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        # Line 1: rank, title + artist (left), score (right-aligned).
        title = f"{song['title']} — {song['artist']}"
        header = f"{rank}. {title}"
        print(f"\n{header:<48}{score:>10.2f}")
        # Line 2: the reasons that produced the score, indented under it.
        print(f"   why: {explanation}")

    print("\n" + "=" * width)


if __name__ == "__main__":
    main()
