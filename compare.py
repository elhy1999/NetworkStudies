# importing the module
import json
 
# Opening JSON file
with open('desire_root.json') as json_file:
    data1 = json.load(json_file)
 

with open('music_root.json') as json_file:
    data2 = json.load(json_file)

with open('wood_root.json') as json_file:
    data3 = json.load(json_file)

with open('animal_root.json') as json_file:
    data4 = json.load(json_file)

similarity_count = 0
similar_words = []
for w in data1:
    if w in data2 and w in data3 and w in data4:
        similarity_count += 1
        similar_words.append(w)

print(similarity_count)