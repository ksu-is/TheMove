# import requests module
import requests 

# Google Maps API key allowsautomated communication with the server
api_key = ''

# url base
url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"

# input will be input into the Google Maps seach API 
query = input('Search query: ') 


# build the new url with our input
#plugging this new url into a web browser shows us all sorts of data about the Google Maps API
#Like type of establishment, open or closed currently, size of building, rating, etc.
#also exact location(lat and lon), this will help us rank the results later on
request_url = requests.get(url + 'query=' + query +
						'&key=' + api_key) 

#this makes getting the request url easy, so I can plug it into my broswer for reference
reference_request_url = url + 'query=' + query + '&key=' + api_key

#printing the url here lets me double check my work on a browser
print(reference_request_url)

# convert into json
json_url = request_url.json() 

results_list_pull = []
save_list = []

results_list = json_url['results'] 

# keep looping up to length of the results
#max result is 20, length is based on number of results in google maps
for single_result in range(len(results_list)): 
    # Print the list one result at a time
	print(results_list[single_result]['name'])
	#along with their types
	print(results_list[single_result]['types'])
	#Also create a new list from the results of the search
	results_list_pull.append(results_list[single_result]['name'])

#ask for which item they would like to save
save_number =int(input("Enter corresponding number for item you wish to save"))
#throw it onto a new list
save_list.append(results_list_pull[save_number])
#print save list
print(save_list)
