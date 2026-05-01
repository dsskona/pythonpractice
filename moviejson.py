import json

movies = ["Inception", "Titanic", "Avatar"]

# Save
json_file = open("movies.json", "w")
json.dump(movies, json_file)
json_file.close()

print("Saved")  

# Load
json_file = open("movies.json", "r")
data = json.load(json_file)
json_file.close()

print("Loaded:", data)