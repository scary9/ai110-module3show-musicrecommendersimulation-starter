# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Real-world recommenders like Spotify and YouTube predict what you'll like next by
turning both users and songs into numbers and scoring how well they match. They mostly
rely on collaborative filtering — "people with taste like yours also loved this" — which
needs huge amounts of user data. My version instead uses content-based filtering, which
fits a tiny catalog with no user history, and it prioritizes recommendations that are
simple and explainable over ones that are surprising.

My recommender uses content-based filtering to score how well each song matches a
user's taste. Each `Song` uses four features — genre, mood, energy, and acousticness —
and the `UserProfile` stores a favorite genre, a favorite mood, a target energy level,
and whether the user likes acoustic music. The `Recommender` computes each song's score
as a weighted total of genre match, mood match, energy closeness, and acousticness,
with genre weighted highest because it's the strongest taste signal. To choose what to
recommend, it scores every song, sorts them from highest to lowest, and returns the
top `k`.

**Algorithm Recipe:**

For each song, start the score at 0 and add up three signals:

1. **Genre match — +2.0 points.** If the song's genre exactly matches the user's favorite genre, add 2.0; otherwise add nothing. Genre is weighted highest because it's the strongest single signal of taste.
2. **Mood match — +1.0 point.** If the song's mood exactly matches the user's favorite mood, add 1.0; otherwise add nothing. Mood is a real preference but a softer one, so it's worth half of a genre match.
3. **Energy similarity — +0.0 to +1.0 points.** Compute `1 - abs(target_energy - song_energy)`. A perfect energy match adds a full 1.0, and the points shrink toward 0 as the song's energy drifts away from the user's target (in either direction). Unlike genre and mood, this is a partial "closeness" score, not all-or-nothing.

Add the three parts together for the song's total score, so a perfect song scores **4.0** (2.0 + 1.0 + 1.0). After scoring every song, sort from highest to lowest and return the top `k`.

**Potential bias:** Because genre is weighted twice as heavily as mood, this system might over-prioritize genre and overlook great songs that match the user's mood but sit in a different genre. It also only rewards *exact* genre and mood matches, so closely related tags (like "pop" vs. "indie pop") score nothing even when a listener would find them similar.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Below is real output from running `python -m src.main` with the profile
`genre=pop, mood=happy, energy=0.8`:

```
Loaded songs: 18

============================================================
                    TOP RECOMMENDATIONS
           for genre=pop, mood=happy, energy=0.8
============================================================

1. Sunrise City — Neon Echo                           3.98
   why: genre match (+2.0), mood match (+1.0), energy similarity (+0.98)

2. Gym Hero — Max Pulse                               2.87
   why: genre match (+2.0), energy similarity (+0.87)

3. Rooftop Lights — Indigo Parade                     1.96
   why: mood match (+1.0), energy similarity (+0.96)

4. Concrete Kingdom — Vell Kato                       1.00
   why: energy similarity (+1.00)

5. Night Drive Loop — Neon Echo                       0.95
   why: energy similarity (+0.95)

============================================================
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

### Multiple User Profiles

Real terminal output from running the recommender (`k=5`) against three distinct
taste profiles. Each block is the unedited output for that profile.

**High-Energy Pop** — `{genre: pop, mood: happy, energy: 0.85}`

```
Loaded songs: 18

============================================================
                    TOP RECOMMENDATIONS
           for genre=pop, mood=happy, energy=0.85
============================================================

1. Sunrise City — Neon Echo                           3.97
   why: genre match (+2.0), mood match (+1.0), energy similarity (+0.97)

2. Gym Hero — Max Pulse                               2.92
   why: genre match (+2.0), energy similarity (+0.92)

3. Rooftop Lights — Indigo Parade                     1.91
   why: mood match (+1.0), energy similarity (+0.91)

4. Concrete Kingdom — Vell Kato                       0.95
   why: energy similarity (+0.95)

5. Storm Runner — Voltline                            0.94
   why: energy similarity (+0.94)

============================================================
```

**Chill Lofi** — `{genre: lofi, mood: chill, energy: 0.40}`

```
Loaded songs: 18

============================================================
                    TOP RECOMMENDATIONS
           for genre=lofi, mood=chill, energy=0.4
============================================================

1. Midnight Coding — LoRoom                           3.98
   why: genre match (+2.0), mood match (+1.0), energy similarity (+0.98)

2. Library Rain — Paper Lanterns                      3.95
   why: genre match (+2.0), mood match (+1.0), energy similarity (+0.95)

3. Focus Flow — LoRoom                                3.00
   why: genre match (+2.0), energy similarity (+1.00)

4. Spacewalk Thoughts — Orbit Bloom                   1.88
   why: mood match (+1.0), energy similarity (+0.88)

5. Paper Boats — Wren & Willow                        0.98
   why: energy similarity (+0.98)

============================================================
```

**Deep Intense Rock** — `{genre: rock, mood: intense, energy: 0.90}`

```
Loaded songs: 18

============================================================
                    TOP RECOMMENDATIONS
          for genre=rock, mood=intense, energy=0.9
============================================================

1. Storm Runner — Voltline                            3.99
   why: genre match (+2.0), mood match (+1.0), energy similarity (+0.99)

2. Gym Hero — Max Pulse                               1.97
   why: mood match (+1.0), energy similarity (+0.97)

3. Neon Overdrive — Pulsewave                         0.95
   why: energy similarity (+0.95)

4. Iron Verdict — Ashfall                             0.92
   why: energy similarity (+0.92)

5. Sunrise City — Neon Echo                           0.92
   why: energy similarity (+0.92)

============================================================
```

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



