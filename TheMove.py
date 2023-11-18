
# import requests module
import requests 

# Google Maps API key allows communication with server
api_key = 'AIzaSyBVNOStj05653SnpTu4emjBJDi3zDlGA3Q'

# url base
url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"

# input will be input into the Google Maps seach API 
query = input('Search query: ') 


# build the new url with our search
#plugging this new url into a web browser shows us all sorts of data about the Google Maps API
#Like type of establishment, open or closed currently, size of building, rating, etc.
#also exact location(lat and lon), this will help us rank the results later on
request_url = requests.get(url + 'query=' + query +
						'&key=' + api_key) 

# convert into json
json_url = request_url.json() 


results_list = json_url['results'] 

# keep looping upto length of y 
#max result is 20, length is based on number of results
for single_result in range(len(results_list)): 
    # Print the list one result at a time
	print(results_list[single_result]['name']) 


