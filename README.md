# DSA210-TopMovies
# Top Movies

# Project Idea

## Description
In this project, I will collect and analyze data from IMDB(From Kaggle) and TMDB. I will enrich the research by collecting extra data, such as the time i spend in nature or the time i spend in social media.
## Purpose
I was curious about how properties of the movies, such as the ratings, revenue, etc..
# Description Of Datasets
## Main Dataset (IMDB)
This is our main dataset containing information about the top 5000 movies in IMDB.
- **tconst:** Unique IMDB title ID
- **primaryTitle:** Original movie title
- **startYear:** Release year
- **rank:** Position in IMDB Top 5000 ranking
- **averageRating:** Average IMDB rating
- **numVotes:** Number of IMDb votes
- **runtimeMinutes:** Movie length (in minutes)
- **directors:** Director(s) name(s)
- **writers:** Writer(s) name(s)
- **genres:** Movie genres (e.g. Drama, Action)
## Enrichment Dataset (TMDB)
This dataset contains information about the revenue's and budget's of the movies in TMDB. We will only use it to get the values for the top 5000 movies in IMDB.
- **tmdb_title:** Title of the movie in TMDB
- **budget:** Budget of the movie
- **revenue:** Revenue of the movie

## Tools and Technologies
- **Python:**
- **Jupiter Notebook:**
- **Pandas:**

# Analysis Plan
## Data Collection
-
## Visualization
-
-
## Hypothesis Testing
- **Example Hypothesis:**
  - H₀: Budget of the movie has no effect on the rating.
  - Hₐ: Higher budgets make the movie get higher ratings.
Run regression analysis to identify the strongest predictors of progress.

# Conclusion
By the end of this project, I hope to gain some ideas about the following questions:
-
