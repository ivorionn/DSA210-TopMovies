import tmdbsimple as tmdb
import pandas as pd

# Set your TMDB API key here
tmdb.API_KEY = '260f7d68fecb569fc11ce48c80471254'

# List of original IMDb titles from the mismatches
titles = [
    "The Lion King", "Das Boot", "How to Train Your Dragon", "Stand by Me",
    "Yojimbo", "Gangs of Wasseypur", "Ip Man", "Planet of the Apes",
    "8½", "The General", "Nayakan", "A Christmas Story", "Pink Floyd: The Wall",
    "The Act of Killing", "Thuppakki", "X-Men: First Class", "Home Alone",
    "Ex Machina", "The Game", "Airplane!", "Willy Wonka & the Chocolate Factory",
    "A Prophet", "My Left Foot", "3-Iron", "The Return", "Central Station",
    "Rififi", "The Breath", "Major", "Rome, Open City", "Yi Yi", "Sarfarosh",
    "A Christmas Carol", "50/50", "Bonnie and Clyde", "The Day the Earth Stood Still",
    "Mother", "The Girl Who Leapt Through Time", "The Chorus", "Grizzly Man",
    "Blood In, Blood Out", "A Night at the Opera", "The Leopard", "Nostalghia",
    "The Blue Elephant", "Through a Glass Darkly", "Volver", "Confessions",
    "The Edge of Heaven", "Dragon Ball Super: Broly", "My Uncle", "Borat",
    "Begin Again", "National Lampoon's Animal House", "Dead Alive", 
    "March of the Penguins", "Show Me Love", "White Christmas", "Drunken Master II",
    "It's a Mad Mad Mad Mad World", " '83", "Boy A", "The Odd Couple", 
    "Tora! Tora! Tora!", "Mortal World", "Marcel the Shell with Shoes On",
    "A Hero", "1900", "New World", "Between Family", "Seeking True Love",
    "Chup", "Darr", "X-Men", "Bullet Train", "Dumb and Dumber", "Wall Street",
    "The King", "Rust and Bone", "Blow-Up", "Who Am I", "Oliver!", "Magic Carpet Ride",
    "In the House", "To Strike", "The Stranger", "You're Not You", "Super Size Me",
    "Force Majeure", "Suck Me Shakespeer", "Memphis Belle", "Under the Shadow",
    "The Big Boss", "Saturday Night", "Muppet Treasure Island", "Leap!", "Liar Liar",
    "Ace Ventura: Pet Detective", "Non-Stop", "Hocus Pocus", "Nymphomaniac: Vol. I",
    "A Ghost Story", "I See You", "Working Girl", "Florence Foster Jenkins",
    "Ju-on: The Grudge", "The Idiots", "Rare Exports", "In a World...", "Men in Black³",
    "The Mighty Ducks", "Far and Away", "Emma.", "Black Rain", "The Wonder",
    "The Grandmaster", "Batman: The Movie", "Enola Holmes", "Puss in Boots",
    "30 Days of Night", "You're Next", "[Rec]²", "Hoodwinked!", "Last Night",
    "Incident in a Ghostland", "On the Rocks", "Dabangg", "The Bar", "Den of Thieves: Pantera",
    "Resident Evil", "Road Trip", "Sonic the Hedgehog", "Under Siege",
    "The Night Before", "Weekend at Bernie's", "Last Man Standing", "Night Watch",
    "#Alive", "W.", "Rising Sun", "Sleepaway Camp", "Man of the Year",
    "Savi", "Book Club", "Dark Star", "The Woman", "Alien³", "Van Wilder",
    "Delivery Man", "Upside Down", "Dorian Gray", "Diary of a Wimpy Kid"
]

results = []
for title in titles:
    search = tmdb.Search()
    response = search.movie(query=title)
    matched_title = None
    revenue = None

    if search.results:
        # try to find exact match (case-insensitive)
        for r in search.results:
            if r['title'].lower() == title.lower():
                matched = r
                break
        else:
            matched = search.results[0]  # fallback to first result

        movie = tmdb.Movies(matched['id'])
        info = movie.info()
        matched_title = info.get('title')
        budget = info.get("budget")
        revenue = info.get('revenue')

    results.append({
        'imdb_title': title,
        'tmdb_title': matched_title,
        "budget" : budget,
        'revenue': revenue
    })

df = pd.DataFrame(results)
print(df)

# save fixed diff
df.to_csv("topMovies/diff_fix.csv")