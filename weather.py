import requests

# city = input ("Enter name of City :")
def fetch_wea():
    url =f"http://api.weatherapi.com/v1/current.json?key=ed2461e259e34cb3894144510242311&q=London&aqi=no"

    response= requests.get(url)
    data=response.json();

    if "location" in data:
        wea_data=data["location"]
        country = wea_data["country"]
        return country

    else:
        raise Exception("data not found")

def main():
    try:
        country=fetch_wea()
        print(f"country :{country}")
    except Exception as e:
        print(e)

if __name__ == "__main__" :
    # if __name__ == "__main__"
    
    main()
    print("into main")


