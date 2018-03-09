"""# Problem Set 3: Scraping and Cleaning Twitter Data

Now that you know how to scrape data from Twitter, let's extend the exercise a little so you can show us what you know. You will set up the scraper, clean the resulting data, and visualize it. Make sure you get your own Twitter key (AND make sure that you don't accidentally push it to GitHub); careful with your `.gitignore`.

## Graphic Presentation

Make sure to label all your axes and add legends and units (where appropriate)! Think of these graphs as though they were appearing in a published report for an audience unfamiliar with the data.

## Don't Work on Incomplete Data!

One of the dangers of cleaning data is that you inadvertently delete data that is pertinent to your analysis. If you find yourself getting strange results, you can always run previous portions of your script again to rewind your data. See the section called 'reloading your Tweets in the workshop.

## Deliverables

### Push to GitHub

1. A Python script that contains your scraper code in the provided submission folder. You can copy much of the provided scraper, but you'll have to customize it. This should include the code to generate two scatterplots, and the code you use to clean your datasets.
2. Extra Credit: A Python script that contains the code you used to scrape Wikipedia with the BeautifulSoup library.

### Submit to Stellar

1. Your final CSV files---one with no search term, one with your chosen search term---appropriately cleaned.
2. Extra Credit: A CSV file produced by your BeautifulSoup scraper."""

## Instructions

### Step 1

#Using the Twitter REST API, collect at least 2,000 tweets. Do not specify a search term. Use a lat/lng of `42.359416,-71.093993` and a radius of `5mi`. This will take 1-2 minutes to run.

import jsonpickle
import tweepy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
import os
os.listdir()
os.chdir('week-04')
from twitter_keys import api_key, api_secret

def auth(key, secret):
  auth = tweepy.AppAuthHandler(key, secret)
  api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)
  # Print error and exit if there is an authentication error
  if (not api):
      print ("Can't Authenticate")
      sys.exit(-1)
  else:
      return api

api = auth(api_key, api_secret)

def parse_tweet(tweet):
    p = pd.Series()
    if tweet.coordinates != None:
        p['lat'] = tweet.coordinates['coordinates'][0]
        p['lon'] = tweet.coordinates['coordinates'][1]
    else:
        p['lat'] = None
        p['lon'] = None
        p['location'] = tweet.user.location
        p['id'] = tweet.id_str
        p['content'] = tweet.text
        p['user'] = tweet.user.screen_name
        p['user_id'] = tweet.user.id_str
        p['time'] = str(tweet.created_at)
    return p


def get_tweets(
    geo,
    out_file,
    search_term = '',
    tweet_per_query = 100,
    tweet_max = 150,
    since_id = None,
    max_id = -1,
    write = False
  ):
  tweet_count = 0
  all_tweets = pd.DataFrame()
  while tweet_count < tweet_max:
    try:
      if (max_id <= 0):
        if (not since_id):
          new_tweets = api.search(
            q = search_term,
            rpp = tweet_per_query,
            geocode = geo
          )
        else:
          new_tweets = api.search(
            q = search_term,
            rpp = tweet_per_query,
            geocode = geo,
            since_id = since_id
          )
      else:
        if (not since_id):
          new_tweets = api.search(
            q = search_term,
            rpp = tweet_per_query,
            geocode = geo,
            max_id = str(max_id - 1)
          )
        else:
          new_tweets = api.search(
            q = search_term,
            rpp = tweet_per_query,
            geocode = geo,
            max_id = str(max_id - 1),
            since_id = since_id
          )
      if (not new_tweets):
        print("No more tweets found")
        break
      for tweet in new_tweets:
        all_tweets = all_tweets.append(parse_tweet(tweet), ignore_index = True)
      max_id = new_tweets[-1].id
      tweet_count += len(new_tweets)
    except tweepy.TweepError as e:
      # Just exit if any error
      print("Error : " + str(e))
      break
  print (f"Downloaded {tweet_count} tweets.")
  if write == True:
       all_tweets.to_json(out_file)
  return all_tweets

latlng = '42.359416,-71.093993' # Eric's office (ish)
# Set a search distance
radius = '5mi'
# See tweepy API reference for format specifications
geocode_query = latlng + ',' + radius
# set output file location
file_name = 'data/tweets.json'
# set threshold number of Tweets. Note that it's possible
# to get more than one
t_max = 2000

full_tweets = get_tweets(
  geo = geocode_query,
  tweet_max = t_max,
  write = True,
  out_file = file_name
)

full_tweets.to_json('data/tweets.json')

full_tweets.shape
full_tweets.head()

```

### Step 2

#Clean up the data so that variations of the same user-provided location name are replaced with a single variation. Once you've cleaned up the locations, create a pie chart of user-provided locations. Your pie chart should strive for legibility! Let the [`matplotlib` documentation](https://matplotlib.org/api/_as_gen/matplotlib.axes.Axes.pie.html) be your guide!

tweets = pd.read_json('data/tweets.json')
tweets.head()
tweets.dtypes
tweets['location'].unique()


loc_tweets = tweets[tweets['location'] != '']
count_tweets = loc_tweets.groupby('location')['id'].count()
count_location = loc_tweets['location'].value_counts().reset_index()

count_location[:30]

boston_list = tweets[tweets['location'].str.contains("Boston", case=False, na=False)]['location']
tweets['location'].replace(boston_list, 'Boston, MA', inplace = True)

java_list = tweets[tweets['location'].str.contains("kerjen", case=False, na=False)]['location']
tweets['location'].replace(java_list, 'Kerjen, Srengat, East Java', inplace = True)

seattle_list = tweets[tweets['location'].str.contains("seattle", case=False, na=False)]['location']
tweets['location'].replace(seattle_list, 'Seattle, WA', inplace = True)
nyc_list = tweets[tweets['location'].str.contains("NYC", case=False, na=False)]['location']
tweets['location'].replace(nyc_list, 'New York, NY', inplace = True)
chicago_list = tweets[tweets['location'].str.contains("chicago", case=False, na=False)]['location']
tweets['location'].replace(chicago_list, 'Chicago, IL', inplace = True)

tweets['location'].replace("",'Missing Location Data',inplace=True)
tweets['location'].replace("intersectional feminist",'Other Location',inplace=True)
tweets['location'].replace("Pakoda stall",'Other Location',inplace=True)
tweets['location'].replace("poTayto",'Other Location',inplace=True)
tweets['location'].replace("Lost in a dream",'Other Location',inplace=True)
tweets['location'].replace("In The Groove",'Other Location',inplace=True)
tweets['location'].replace("Cali",'California, USA',inplace=True)
tweets['location'].replace("NJ",'Other Location',inplace=True)
tweets['location'].replace("On a bookshelf",'Other Location',inplace=True)




location_count_frame= tweets['location'].value_counts().to_frame()


location_pie = location_count_frame[location_count_frame['location']>2]
location_pie

colors = ["#697dc6","#5faf4c","#7969de","#b5b246","#cc54bc","#4bad89","#d84577","#4eacd7","#cf4e33","#894ea8","#cf8c42","#d58cc9","#737632","#9f4b75","#c36960"]

plt.pie(location_pie['location'], labels=location_pie['location'].get_values(),  shadow=False, colors=colors)
plt.title("Self-Reported Tweet Locations within 5 mile Radius of Eric's Office (At least 2 Pings)")
plt.axis('equal')
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5), labels=location_pie['location'].keys())
plt.tight_layout()
plt.show()


#All other tweets that had a count of less than two were left alone, because it would be too tough to clean generally.
#If I had more time, I would classify all of those under "Other Location", but I didn't want to be late on this!

### Step 3

#Create a scatterplot showing all of the tweets are that are geolocated (i.e., include a latitude and longitude).

tweets_geo = tweets[tweets['lon'].notnull() & tweets['lat'].notnull()]
len(tweets_geo)

#Only two tweets are geolocated! Wild!
len(tweets)

# Use a scatter plot to make a quick visualization of the data points
# N.B., WHEN I DID THIS, I ONLY HAD SIX OUT OF ABOUT 100 TWEETS!
plt.scatter(tweets_geo['lon'], tweets_geo['lat'], s = 25)
plt.show

### Step 4

#Pick a search term (e.g., "housing", "climate", "flood") and collect tweets containing it. Use the same lat/lon and search radius for Boston as you used above. Use a maximum of 2,000 tweets; depending on the search term, you may find that there are fewer than 2,000 tweets available.

latlng = '42.359416,-71.093993' # Eric's office (ish)
# Set a search distance
radius = '5mi'
# See tweepy API reference for format specifications
geocode_query = latlng + ',' + radius
# RESET set output file location
file_name = 'data/food_tweets.json'
# set threshold number of Tweets. Note that it's possible
# to get more than one
t_max = 2000


food_tweets = get_tweets(
  search_term = 'food',
  geo = geocode_query,
  tweet_max = t_max,
  write = True,
  out_file = file_name
)



### Step 5

#Clean the search term data as with the previous data.
food_tweets = pd.read_json('data/food_tweets.json')
food_tweets.head()
#tweets.dtypes
food_tweets['location'].unique()

loc_food_tweets = food_tweets[food_tweets['location'] != '']
count_food_tweets = loc_food_tweets.groupby('location')['id'].count()
count_food_location = loc_food_tweets['location'].value_counts().reset_index()

count_food_location[:30]

boston_list = food_tweets[food_tweets['location'].str.contains("Boston", case=False, na=False)]['location']
food_tweets['location'].replace(boston_list, 'Boston, MA', inplace = True)

usa_list = food_tweets[food_tweets['location'].str.contains("United States", case=False, na=False)]['location']
food_tweets['location'].replace(usa_list, 'USA', inplace = True)

food_tweets['location'].replace("",'Missing Location Data',inplace=True)

chicago_list = food_tweets[food_tweets['location'].str.contains("Chicago", case=False, na=False)]['location']
food_tweets['location'].replace(chicago_list, 'Chicago, IL', inplace = True)

cambridge_list = food_tweets[food_tweets['location'].str.contains("Cambridge, Massachusetts", case=False, na=False)]['location']
food_tweets['location'].replace(cambridge_list, 'Cambridge, MA', inplace = True)
food_tweets['location'].replace('ABQ | DC | Global', 'Other Location', inplace = True)
food_tweets['location'].replace('Global', 'Other Location', inplace = True)
food_tweets['location'].replace('Earth', 'Other Location', inplace = True)
food_tweets['location'].replace('ABQ | DC | Global', 'Other Location', inplace = True)
food_tweets['location'].replace('US of A', 'USA', inplace = True)
food_tweets['location'].replace('new delhi', 'New Delhi', inplace = True)


### Step 6

#Create a scatterplot showing all of the tweets that include your search term that are geolocated (i.e., include a latitude and longitude).

food_tweets_geo = food_tweets[food_tweets['lon'].notnull() & food_tweets['lat'].notnull()]
len(food_tweets_geo)

#Only seven tweets are geolocated! Wild!
len(food_tweets)

# Use a scatter plot to make a quick visualization of the data points
# N.B., WHEN I DID THIS, I ONLY HAD SIX OUT OF ABOUT 100 TWEETS!
plt.scatter(food_tweets_geo['lon'], food_tweets_geo['lat'], s = 25)
plt.show
### Step 7

#Export your scraped Twitter datasets (one with a search term, one without) to two CSV files. We will be checking this CSV file for duplicates and for consistent location names, so make sure you clean carefully!

#I saved the cleaned datasets to CSVs for review - I hope they look alright!

tweets.to_csv('data/tweets.csv')
food_tweets.to_csv('data/food_tweets.csv')
## Extra Credit Opportunity

Build a scraper that downloads and parses the Wikipedia [List of Countries by Greenhouse Gas Emissions page](https://en.wikipedia.org/wiki/List_of_countries_by_greenhouse_gas_emissions) using BeautifulSoup and outputs the table of countries as as a CSV.
