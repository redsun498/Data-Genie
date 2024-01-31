import pandas as pd 

def get_access_token(client_id, client_secret):
    '''
    This is a function that's used to get an access token from Spotify's API.
    An access token is a string representing the authorization granted to the client (in this case, the application)
    Hand is used in HTTP transactions to prove the authenticity of the sender and the receiver. 
    '''
    auth_url = 'https://accounts.spotify.com/api/token'
    auth_header = {
        'Authorization': f'Basic {base64.b64encode((client_id + ":" + client_secret).encode()).decode()}'
    }
    auth_data = {
        'grant_type': 'client_credentials',
    }
    auth_response = requests.post(auth_url, data=auth_data, headers=auth_header)
    auth_response_data = auth_response.json()
    access_token = auth_response_data['access_token']
    return access_token

def get_genres(access_token, limit = 50, offset = 0):

    genres_url = 'https://api.spotify.com/v1/browse/categories'
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    params = {
        'limit': limit,
        'offset': offset
    }
#genres_url is the Spotify API endpoint for browsing available categories (genres).
#headers is a dictionary containing an 'Authorization" key.
#The value of this key is created by appending the access token received from the get_access_token() function to the string 'Bearer ##This is a method of authentication required by Spotify's API.
#params is a dictionary of parameters to be sent with the request.
#In this case, 'Limit' and 'offset' are used to control pagination. "Limit' restricts the number of items returned in the response ##(default is set to 50), and 'offset' is the index of the first item to return.
#The requests.get() function sends a GET request to the genres URL with the headers and parameters defined earlier.

#The server's response to this request is stored in response.
    response = requests.get (genres_url, headers = headers, params=params)
    genres_data = response.json()
    genres = [(category ['id'], category['name']) for category in genres_data['categories']['items']]
#A List comprehension is used to iterate over each category (genre) in genres _datal 'categories ']l'items'].
##For each category, a tuple containing the category ID and name is created and added to the genres List. 
    return genres

def get_artist_genre(artist_id):
    artist = sp.artist(artist_id)
    return artist['genres'][0].

#Original and correct
def create_dataframe(query_list, limit=50):
    data = {
        'Track ID': [],
        'Track name': [],
        'Artist name': [],
        'Popularity score': [],
        'Release year': [],
        'Genre': []
    }

    for query in query_list:
        search_results = sp.search(q=query, limit=limit, type='track', market='US')
        tracks = search_results['tracks']['items']
     
        for track in tracks: 
            data['Track ID'].append(track['id'])
            data['Track name'].append(track['name'])
            data['Artist name'].append(track['artists'][0]['name'])
            data['Popularity score'].append(track['popularity'])
            data['Release year'].append(track['album']['release_date'][:4])
            data['Genre'].append(query)
            
        time.sleep(2)

    df = pd.DataFrame(data)
    return df

#Genres that i got from the get_genres function 
genres = [
    'genre:"New Releases"','genre:"Hip-Hop"','genre:"Pop"','genre:"Country"','genre:"Latin"','genre:"Charts"','genre:"Student"',
    'genre:"Rock"','genre:"Dance/Electronic"','genre:"In the car"','genre:"Discover"','genre:"Mood"','genre:"Indie"','genre:"Disney"',
    'genre:"R&B"','genre:"Christian & Gospel"','genre:"Workout"','genre:"Música Mexicana"','genre:"La Tierra del Corrido"','genre:"K-pop"',
    'genre:"Chill"','genre:"Netflix"','genre:"Sleep"','genre:"Party"','genre:"At Home"','genre:"Decades"','genre:"Love"','genre:"Metal"',
    'genre:"Jazz"','genre:"Trending"','genre:"Frequency"','genre:"Classical"','genre:"Folk & Acoustic"','genre:"Focus"',
    'genre:"Soul"','genre:"Kids & Family"','genre:"Gaming"','genre:"Anime"','genre: "Punk"','genre: "Ambient"', 'genre:"Blues"', 'genre: "Cooking & Dining"', 'genre: "Alternative"','genre:"Travel"', 'genre:"Caribbean"',
    'genre: "Afro"', 'genre: "Songwriters"', 'genre: "Nature & Noise"'
        ]

df = create_dataframe(genres, limit=50)