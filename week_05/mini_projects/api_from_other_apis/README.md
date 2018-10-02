# Project: Movie Locations API
*Release: 0.1*


This project provides a simple API to recieve a movie name, retrieve the narrative location and its current Twitter trends.

## Features

#### This release
- [x] Get narrative location for a given movie and its coordinates.
- [x] Get nearest location that Twitter is tracking.
- [x] Get top 10 Twitter trends.
- [x] Write api docs.

#### Next release

- [ ] Option to use filming location.
- [ ] Check partial matches for movie (query does not have to match exact name).


## Usage

Deploy the inventory files below to your server:


| Filename | Description |
| :-- | :-- |
| README.md | This file. |
| environment.py | The executable wisgi server. |
| main.py | The logic for the server. |
| wiki.py | The logic for loading movie data from API source and out to the user. |
| tweet.py | The logic for obtaining Twitter location and its top 10 trends. |
| sql_methods.py | The logic for interacting with MySQL database. |

### Paths

| Location | Path |
| :-- | :-- |
| Root path | `~/`|
| Movie | `~/movie`|
| Load  | `~/movie/load`|

### HTTP request and query methods

| Method | Path | Query | Description | Examples |
| :-- | :-- | :-- | :-- | :-- |
| `GET` | `~/movie` | `?full%20name` | Retrieves the narrative location of a movie, nearest Twitter location and its current top 10 trends. | `~/movie?slumdog%20millionaire` |
| `POST` | `~/movie/load` | na | Loads latest movie data from Wikidata. Specfically, it truncates current mySQL table, queries Wikidata for its latest movie details, and inserts all records into table. | `~~/movie/load` |

### Contribute

- Issue Tracker: https://github.com/lauramayol/laura_python_core/issues
- Source Code: https://github.com/lauramayol/laura_python_core/tree/master/week_05/mini_projects/api_from_other_apis


### Support


If you are having issues, please let me know.
