# import json
# f = open("data.json", "w", encoding="utf-8")
# salad = {
#     "Tomato": [5, "Cut"],
#     "Cucumber": [3, "Сheck cucumbers for bitterness", "Cut"],
#     "Salt": "add to taste",
#     "Sugar": False
# }
# text = [False, None, 3, 3.13, (1,2,3)]
# json.dump(salad, f)
# print(json.dumps(text))
# f.close()
# f = open("data.json","r", encoding="utf-8")
# content = json.load(f)
# f.close()
# print(content)

from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="specify_your_app_name_here")
location = geolocator.geocode("175 5th Avenue NYC")
print(location.raw)