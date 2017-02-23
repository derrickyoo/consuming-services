import json

text_json = '''{
    "demo": "Processing JSON in Python"
}'''

print(type(text_json), text_json)

data = json.loads(text_json)
print(type(data), data)

# data['instructor']
# use this incase instructor key does not exist
data.get('instructor', '')