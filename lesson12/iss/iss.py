import requests
latitude_me=55.0357
longitude_me=82.9222
while True:
    req = requests.get("http://api.open-notify.org/iss-now.json")
    response = req.json()
    latitude = response['iss_position']['latitude']
    longitude = response['iss_position']['longitude']
    print('latitude =',response['iss_position']['latitude'])
    print('longitude =',response['iss_position']['longitude'])
    if latitude == latitude_me and longitude == longitude_me:
        print('улыбнись мкс')
    print('____________________________________________________')
