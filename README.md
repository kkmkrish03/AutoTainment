# README #

This README would normally document whatever steps are necessary to get your application up and running.

### What is this repository for? ###

* Quick summary
* Version
* [Learn Markdown](https://bitbucket.org/tutorials/markdowndemo)

### How do I get set up? ###

* Summary of set up
* Configuration
* Dependencies
* Database configuration
* How to run tests
* Deployment instructions

### Contribution guidelines ###

* Writing tests
* Code review
* Other guidelines

### Who do I talk to? ###

* Repo owner or admin
* Other community or team contact


#### Skils
- Python
    * list
    * random module
    * input()

#### Advance Skills
- Pandas
- APIs


## Git CMD
git init
git add .
git commit -m "initial commit"
git remote add origin https://github.com/{username}/AutoTainment.git
git push -u origin master


## Git credential manager
https://github.com/git-ecosystem/git-credential-manager/tree/main
https://github.com/git-ecosystem/git-credential-manager/blob/release/docs/install.md

sudo dpkg -i https://github.com/git-ecosystem/git-credential-manager/releases/download/v2.2.2/gcm-linux_amd64.2.2.2.deb
git-credential-manager configure

git config --global credential.credentialStore secretservice
or 
git config --global credential.credentialStore plaintext

git remote add origin https://github.com/kkmkrish03/AutoTainment.git



Movie Rating Comparison Tool: Build a program that allows users to enter the title of a movie, and the application fetches its ratings from IMDb, Rotten Tomatoes, and MyAnimeList. It then presents the ratings side by side, allowing users to compare how a movie is perceived across different platforms.

Movie Recommendation Engine: Develop a movie recommendation system that suggests movies to users based on their preferences. The program could take input from the user on their favorite movies and genres and use movie metadata from IMDb, Rotten Tomatoes, and MyAnimeList to recommend similar titles that match their tastes.

Movie Insights and Analytics: Create a tool that fetches movie metadata and provides analytical insights. For example, you could analyze the top-rated movies of a specific genre, the most popular movies of a particular year, or compare the average ratings of movies from different sources.

Movie Watchlist Organizer: Build an application that allows users to maintain a watchlist of movies they want to see. The program could fetch movie details from the three sources and let users add, remove, and prioritize movies in their watchlist.

Movie Release Tracker: Develop a tool that tracks upcoming movie releases and fetches relevant details from IMDb, Rotten Tomatoes, and MyAnimeList. Users can get notifications or check a calendar of upcoming releases for movies they're interested in.

Movie Metadata Visualizer: Create a graphical interface that displays movie metadata in a visually appealing manner. Use libraries like Matplotlib or Plotly to create charts and graphs that show statistics about movie ratings, genres, release dates, and more.

Movie Social Media Sharing: Build a program that fetches metadata for a selected movie and generates an attractive social media post with the movie's poster, synopsis, and ratings. Users can then share these posts directly to their social media accounts.

Movie Genre Analyzer: Develop a tool that analyzes the distribution of movie genres across the three platforms. It could show which genres are more prevalent on each platform and identify any differences in preferences.

Movie Franchise Explorer: Create an application that fetches metadata for movies belonging to a specific franchise or series. Users can explore details of all movies in the franchise, including ratings, release dates, and chronological order.

Movie Rating Aggregator: Build a program that fetches ratings for a movie from IMDb, Rotten Tomatoes, and MyAnimeList and calculates an aggregated rating based on a custom formula. This formula could take into account the popularity of the platforms and user preferences.
