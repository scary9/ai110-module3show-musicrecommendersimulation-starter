# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**TheVibe 1.0**

It checks the "vibe" of each song and matches it to what you're in the mood for.

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

**Goal / Task.** TheVibe tries to guess which songs a listener will like. You tell it your favorite genre, your favorite mood, and how much energy you want. It then picks the songs that fit you best and puts them in order, best match first.

**Who it's for.** This is a classroom project, not a real app. It runs on a tiny made-up song list. It is meant for learning how recommenders work.

**What it assumes.** It assumes you can name one favorite genre and one favorite mood. It also assumes your taste fits into three things: genre, mood, and energy. Real people are more complicated than that.

**Intended for:** exploring and explaining how a simple recommender scores songs.

**Not intended for:** real music apps, real playlists, or any choice that actually matters. It has too few songs and ignores a lot of what makes a song feel a certain way.

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

**Algorithm summary.** TheVibe gives every song a score, then sorts the songs from highest score to lowest. The top few are your recommendations.

Each song earns points three ways:

- **Genre:** if the song's genre matches yours, it gets 1 point.
- **Mood:** if the song's mood matches yours, it gets 1 point.
- **Energy:** the closer the song's energy is to what you asked for, the more points it gets. A perfect match is worth 2 points, and it drops toward 0 as the energy gets further away.

Add those up and you get the song's score. A perfect song scores 4.

**What I changed from the starter.** At first, genre was the biggest deal (worth 2 points) and energy was smaller (worth up to 1). I flipped that. Now genre is worth 1 and energy is worth up to 2. This made energy the strongest signal. It changed the results, but it did not always make them better — it just moved the balance around.

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data  

Describe the dataset the model uses.  

**Data used.** The song list has 18 songs. It came with the starter project. I did not add or remove any songs.

**Features.** Each song has a title, artist, genre, mood, energy, tempo, valence (how happy or sad it sounds), danceability, and acousticness. The scoring only uses three of these: genre, mood, and energy. The rest sit unused.

**Genres and moods.** There are 15 genres, but 13 of them have only one song. Only lofi (3 songs) and pop (2 songs) have more than one. Moods are spread thin too — most moods appear just once.

**What's missing.** The list is very small, so most tastes have few real matches. It also has no way to describe things like "calm but happy," because those song details are not part of the score. So parts of real musical taste are simply left out.

---

## 5. Strengths  

Where does your system seem to work well  

**Strengths.** TheVibe works best for listeners whose genre has more than one song, like lofi and pop fans. The lofi fan gets a whole list of calm, low-energy songs that fit, and that matched what I expected.

The top pick is usually right. When a song matches on genre, mood, and energy all at once, it wins — which is exactly what should happen.

It also does a good job of telling different listeners apart. A calm listener and a loud listener get completely different lists, so the energy setting clearly works. And every recommendation comes with a short "why" line, so you can see the reason behind each pick.

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

The biggest weakness I found is that some genres are badly underrepresented, which makes the system favor certain users. Out of 15 genres, 13 have only one song each, while lofi has three and pop has two. Because of this, a lofi fan gets several real matches, but a metal or country fan gets one good match and then filler songs that only share a similar energy level. The scoring also ignores features it could use, like acousticness and valence, so a "calm but happy" listener can't really be matched. In short, how good your recommendations are depends more on whether your genre is well represented than on the scoring logic itself.

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

**Profiles I tested.** I ran three made-up listeners through the recommender and looked at their top 5 songs:

- **High-Energy Pop** — likes pop, a happy mood, and high energy (0.85)
- **Chill Lofi** — likes lofi, a chill mood, and low energy (0.40)
- **Deep Intense Rock** — likes rock, an intense mood, and high energy (0.90)

**The thing that surprised me: why "Gym Hero" keeps showing up for people who just want Happy Pop.** Gym Hero is a pop song, but its mood is "intense," not "happy" — it's basically a workout track. Yet it lands at #2 for the Happy Pop listener. The reason is that the system gives a song points for three separate things (matching genre, matching mood, and having a similar energy level), and a song only needs to do well on *some* of them to rank high. Gym Hero is a real pop song (so it earns the genre points) and it's very high energy (so it earns almost all the energy points), and those two wins together are enough to beat songs that actually are happy. The one thing it gets wrong — the mood — isn't punished hard enough to keep it down. So the listener asked for "happy pop" and got a "pop song that is loud," because two out of three matches was enough.

**Comparing the profiles (each pair):**

- **High-Energy Pop vs. Chill Lofi:** These are near opposites, and the outputs prove the energy setting is doing real work. Happy Pop's list is full of loud songs (Sunrise City, Gym Hero, all around 0.8–0.9 energy), while Chill Lofi's list is full of quiet ones (Midnight Coding, Library Rain, around 0.3–0.4 energy). This makes sense: when one listener wants high energy and the other wants low, the "energy gap" score pulls them toward completely different ends of the catalog.

- **High-Energy Pop vs. Deep Intense Rock:** Both want high energy, and you can see them overlap — Gym Hero and Storm Runner show up on *both* lists. The difference is which one comes first: the pop fan gets Sunrise City on top, the rock fan gets Storm Runner on top, because the genre and mood matches act as the tie-breaker between two people who both like loud music. This makes sense and shows genre/mood still matter even when energy is similar.

- **Chill Lofi vs. Deep Intense Rock:** These two share almost nothing — one wants calm and quiet, the other wants loud and aggressive — and their lists have zero songs in common. That is the clearest sign the system is really separating listeners by taste, not just handing everyone the same popular songs.

**What this tells me:** the recommender is behaving as designed and the top pick is usually right, but the results also reveal its main flaw — a song can rank high by matching genre and energy while completely missing the mood the person asked for, which is exactly the Gym Hero problem above.

No need for numeric metrics unless you created some.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

**Ideas for improvement.**

1. **Add more songs.** The biggest problem is the tiny list. More songs per genre would give everyone real matches, not just lofi and pop fans.

2. **Use the features I'm ignoring.** Things like acousticness and valence are already in the data. Using them would let me match tastes like "calm but happy" or "acoustic music," which the system can't do now.

3. **Make mood count for more.** Right now a song can rank high while missing the mood you asked for (the Gym Hero problem). Giving mood more weight, or requiring it to match, would fix that.

---

## 9. Personal Reflection  

A few sentences about your experience.  

My biggest learning moment was that the data mattered more than the scoring. Most of the unfairness came from the song list being small and uneven, not the rule. AI tools helped me run tests fast and spot patterns, but I still had to check their claims, since once a change was called "more accurate" when it really wasn't. I was surprised that just adding up points and sorting still felt like a real recommendation, even though it doesn't understand music at all. If I kept going, I'd add more songs, use more song details like acousticness, and make mood count for more.
