import simplejson as json

test = [
    {
        'id': '1',
        'name': 'kahee',
        'age': '24'
    },
    {
        'id': '2',
        'name': 'u-na',
        'age': '22'
    },
    {
        'id': '3',
        'name': 'minyoung',
        'age': '28'
    },
]

print(json.dumps(test))