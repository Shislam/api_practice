import requests

'''
general steps:
1. get response with url
2. load data variable with response (json metadata)
3. extract data from the metadata

Use NWS.gov api in two steps 
get data point url,
then take that url and get requests from that url,
then print data form the second request 

code assisted by gemini

'''

def get_data_point_url():

    #coordinates of statue of liberty
    latitude = 40.689247
    longitude = -74.044502

    #declare url
    url = f"https://api.weather.gov/points/{latitude},{longitude}"
    
    #1. get response
    response = requests.get(url)

    # if we get response, proceed with next steps
    if response.status_code == 200:

        #2. load data with metadata
        data = response.json()

        #3. extract data
        forecast = data["properties"]["forecast"]
        return forecast
    else:
        return None


def get_forecast(input_url):

    response = requests.get(input_url)

    data = response.json()
    return data["properties"]["periods"][0]

data_point_url = get_data_point_url()
data = get_forecast(data_point_url)

if data is not None:
    print(f"{data['name']}: {data['detailedForecast']}")
else:
    print("Failed to retrieve data.")