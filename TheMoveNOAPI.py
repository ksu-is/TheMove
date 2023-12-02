# import requests module
import requests 

# Google Maps API key allowsautomated communication with the server
api_key = ''

# url base
url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"

#Create our lists here

#This will hold the names of our search results
results_list_pull = []
#This will hold the addresses of our search results
results_list_address = []
#This will hold what we save, both the names and addresses together
save_list = []



#our program is true
TheMove = True

#while it is running
while TheMove:
    
    #start with our search query "Whats the move today?"
    query = input('Whats the move today? ')
    if query != ("0"):
        
        #this takes our api key + the url base +our new search query and creates a functioning URL to pull data from the google maps API server
		#requests.get is what actually goes and gets our data
        request_url = requests.get(url + 'query=' + query +
                            '&key=' + api_key)
        
        #this was used when building the code to have a working variable to copy the URL and understand what data we were getting and how it was being received
        reference_request_url = url + 'query=' + query + '&key=' + api_key
        
        #json is a format that makes the data received from the Google Maps API able to be understood by Python and us
        json_url = request_url.json()
        
        #start a list from the json data 
        results_list = json_url['results'] 
        
        #for each result within the search...
        for single_result in range(len(results_list)): 
            
            #print the name of each result
            print(results_list[single_result]['name'])
            
            #create a new list of the names
			#I have no idea why I need to start .insert at 20 but it was the only way for me to keep the search results in order
            results_list_pull.insert(20,results_list[single_result]['name'])
            
            #and create a new list of addresses, this will only be showed at the end
            results_list_address.insert(20,results_list[single_result]['formatted_address'])
            
        #our next input will ask for the user for the result they want to save
        save_number =int(input("Enter corresponding number for item you wish to save"))  
        
        #this finds that input and saves the corresponding name
        save_list.append(results_list_pull[save_number])
        
        #this finds that input and saves the corresponding address
        save_list.append(results_list_address[save_number])
        
        #.clear is vital to build a save list that is compromised of multiple unique searches
        results_list_pull.clear()
        results_list_address.clear()
    else:
        
        #finally if the original search is 0, print the saved results of names and addresses and end the loop
        print(save_list)
        break
