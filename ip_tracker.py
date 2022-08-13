#I want to learn how to track the location of a machine using the IP address

#Useful libraries that I would be working with -->
try:
    from geolite2 import geolite2 
    from geopy.geocoders import Nominatim
    import urllib.request
    import traceback
except Exception as e:
    print(f"An error occurred in imported libraries due to [{e}]")



#Commencing the code
def locate(ipAddress: str = None):
    #This checks if an IP Address was given
    if ipAddress == None:
        ipAddress = urllib.request.urlopen('https://api.ipify.org/').read().decode('utf8')
    else:
        pass
    print("IP Address", ipAddress)

    try:
        reader = geolite2.reader()
        location = reader.get(ipAddress) #This gets the various information from our IP address
        #print(f"Location: {location}")
        geolocator = Nominatim(user_agent = "geoapiExercises")

        if location:
            #The geolite database dict values and fine tunning
            if (location["continent"]["names"]["en"]):
                continent = (location["continent"]["names"]["en"])
            else:
                continent = "Null"
            if (location["country"]["names"]["en"]):
                country = (location["country"]["names"]["en"])
            else:
                country = "Null"
            if (location["location"]):
                area = (location["location"])
            else:
                area = "Null"
            if "accuracy_radius" in area:
                accuracyRadius = area["accuracy_radius"]
            else:
                accuracyRadius = "Null"
            if "latitude" in area:
                latitude = area["latitude"]
            else:
                latitude = "Null"
            if "longitude" in area:
                longitude = area["longitude"]
            else:
                longitude = "Null"
            if "metro_code" in area:
                metroCode = area["metro_code"]
            else:
                metroCode = "Null"
            if "time_zone" in area: 
                timeZone = area["time_zone"]
            else:
                timeZone = "Null"

            if (location["registered_country"]["names"]["en"]):
                regCountry = (location["registered_country"]["names"]["en"])
            else:
                regCountry = "Null"
            geoLocation = geolocator.reverse(f"{latitude},{longitude}")
   
            address = geoLocation.raw['address']
            #print(f"Address: {address}")
            if "house_number" in address:
                houseNumber = address["house_number"]
            else:
                houseNumber = "Null"
            if "postcode" in address:
                postal = (address["postcode"])
            else:
                postal = "Null"
            if "road" in address:
                road = address["road"]
            else:
                road = "Null"
            if "village" in address:
                village = address["village"]
            else:
                village = "Null"
            if "city" in address:
                city = address["city"]
            else:
                city = "Null"
            if "suburb" in address:
                suburb = address["suburb"]
            else:
                suburb = "Null"
            if "building" in address:
                building = address["building"]
            else:
                building = "Null"
            if "neighbourhood" in address:
                hood = address["neighbourhood"]
            else:
                hood = "Null"
            if "state" in address:
                state = address["state"]
            else:
                state = "Null"
            if "county" in address:
                county = address["county"]
            else:
                county = "Null"
            if "country_code" in address:
                countryCode = address["country_code"].upper()
            else:
                countryCode = "Null"

            report = f"""IP ADDRESS INFORMATION for {ipAddress} -->
    House Number: {houseNumber}
    Building: {building}
    Street: {road}
    Village: {village}
    Neighbourhood: {hood}
    Suburb: {suburb}
    City: {city}
    County: {county}
    State: {state}
    Country: {country}({countryCode})
    Continent: {continent}
    Accuracy Radius: {accuracyRadius}km
    Latitude: {latitude}
    Longitude: {longitude}
    Metro Code: {metroCode}
    Time Zone: {timeZone}
    Postal Code: {postal}
    Registered Country: {regCountry}
    """
        
        else:
            report = f"Null"

        #Specifically getting country value
        if location:
            if country == "Null":
                country = regCountry
            else:
                pass
        else:
            country = "Null"
        return report, country
    except:
        print(f"An error occurred due to [{traceback.format_exc()}]")

    


if __name__ == "__main__":
    ip = r"104.243.35.168"
    locate, country = locate(ip)
    print(f"Country: {country}")
    print("Location", locate)

