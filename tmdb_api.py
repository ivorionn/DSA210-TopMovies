import pandas as pd
import numpy as np
import tmdbsimple as tmdb

# API KEY for to pull data from TMDB
tmdb.API_KEY = "260f7d68fecb569fc11ce48c80471254"

# To store which titles are mismatching from Kaggle dataset and tmbd api
diff = pd.DataFrame({"imdb_title" : [], "tmdb_title" : []})

# Read our Kaggle dataset as a dataframe
imdb_data = pd.read_csv("topMovies/results_with_crew.csv")

# Store our movies' titles as a list for API calls
movie_titles = imdb_data["primaryTitle"]
movie_titles = list(movie_titles)

# Instantiate a search object for movie titles that we are gonna search in API
search = tmdb.Search()

# Empty lists for newer columns
imdb_titles = []
tmdb_titles = []
budgets = []
revenues = []
# Some titles may fail to gather data from the API
error_titles = []

# for each title we have in imdb_data
for title in movie_titles:
    # response stores a dictionary for results of search
    response = search.movie(query=title)
    # tries to print the first result's id 
    try:
        print(response["results"][0]["id"])
    # if an error happens, such as no results may not have been found
    except:
        print(f"Some problem happenned with {title}")
        # Appends the title to error list to checkout later
        error_titles.append(title)
        # To prevent any slip in the dataframe, columns assigned to data of 
        # tmdb are None
        imdb_titles.append(title)
        tmdb_titles.append(None)
        budgets.append(None)
        revenues.append(None)
        continue
    
    # Request for first result's id
    movie = tmdb.Movies(response["results"][0]["id"])
    # Store info as a dictionary in the response
    response = movie.info()

    # Appends each value accordingly to its column name 
    imdb_titles.append(title)
    tmdb_titles.append(movie.title)
    budgets.append(movie.budget)
    revenues.append(movie.revenue)

    # if imdb_data and tmdb's titles are equal no problem, prints True
    if movie.title == title:
        print(movie.title == title)
    # if they are not then prints both titles and store this values in diff(df)
    else:
        print(f"{title}, {movie.title}")
        diff.loc[len(diff)] = [title, movie.title]

    # Prints budget, revenue and then one empty line
    print(movie.budget)
    print(movie.revenue)
    print()

# Prints df which holds mismatching values for titles
print(diff)
# Prints, in which titles, error happened during pulling the data
print(f"\nError Titles: \n{error_titles}\n")
# A df to store imdb and tmdb titles, and each movie's budget and revenue
budget_revenue = pd.DataFrame(
    {"imdb_title" : imdb_titles,
     "tmdb_titles" : tmdb_titles,
     "budget" : budgets,
     "revenue" : revenues}
)
# Prints budget_revenue and saves budget_revenue and diff to harddrive
print(budget_revenue)
budget_revenue.to_csv("topMovies/budget_revenue.csv")
diff.to_csv("topMovies/diff.csv")

