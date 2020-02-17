import json

data = [
    {
        "id": 1,
        "first_name": "Robena",
        "last_name": "Sellek",
        "gender": "Female",
        "replayTo": None
    },
    {
        "id": 2,
        "first_name": "Alvira",
        "last_name": "Elias",
        "gender": "Female",
        "replayTo": None
    },
    {
        "id": 3,
        "first_name": "Marie-ann",
        "last_name": "Linn",
        "gender": "Female",
        "replayTo": 1
    },
    {
        "id": 4,
        "first_name": "Merrill",
        "last_name": "Jursch",
        "gender": "Male",
        "replayTo": None
    },
    {
        "id": 5,
        "first_name": "Anatole",
        "last_name": "Leming",
        "gender": "Male",
        "replayTo": None
    },
    {
        "id": 6,
        "first_name": "Jobey",
        "last_name": "Gallimore",
        "gender": "Female",
        "replayTo": 3
    },
    {
        "id": 7,
        "first_name": "Ikey",
        "last_name": "Bisterfeld",
        "gender": "Male",
        "replayTo": None
    },
    {
        "id": 8,
        "first_name": "Gonzales",
        "last_name": "Kneller",
        "gender": "Male",
        "replayTo": None
    },
    {
        "id": 9,
        "first_name": "Sancho",
        "last_name": "Jakoviljevic",
        "gender": "Male",
        "replayTo": 7
    },
    {
        "id": 10,
        "first_name": "Harriot",
        "last_name": "Merrikin",
        "gender": "Female",
        "replayTo": None
    },
    {
        "id": 11,
        "first_name": "Maggee",
        "last_name": "Wyrall",
        "gender": "Female",
        "replayTo": 9
    },
    {
        "id": 12,
        "first_name": "Abrahan",
        "last_name": "Skerme",
        "gender": "Male",
        "replayTo": None
    },
    {
        "id": 13,
        "first_name": "Carlee",
        "last_name": "McCritichie",
        "gender": "Female",
        "replayTo": None
    },
    {
        "id": 14,
        "first_name": "Piotr",
        "last_name": "Leyson",
        "gender": "Male",
        "replayTo": 13
    },
    {
        "id": 15,
        "first_name": "Lauree",
        "last_name": "Piscopiello",
        "gender": "Female",
        "replayTo": None
    },
    {
        "id": 16,
        "first_name": "Grover",
        "last_name": "Dudmarsh",
        "gender": "Male",
        "replayTo": 11
    },
    {
        "id": 17,
        "first_name": "Rozalie",
        "last_name": "Ivatts",
        "gender": "Female",
        "replayTo": None
    },
    {
        "id": 18,
        "first_name": "Dot",
        "last_name": "Bundock",
        "gender": "Female",
        "replayTo": 100
    },
    {
        "id": 19,
        "first_name": "Nedda",
        "last_name": "Howell",
        "gender": "Female",
        "replayTo": 18
    },
    {
        "id": 20,
        "first_name": "Lloyd",
        "last_name": "Oscroft",
        "gender": "Male",
        "replayTo": None
    }
]
strMap = {}


def main():
    for d in data:
        obj = {d['id']: d}

        strMap.update(obj)

    setContentType()


def setContentType():
    print("Length: " + str(len(strMap)))

    for key in strMap:
        isReplayMsgExist = strMap.get(key)['replayTo'] in strMap
        print(isReplayMsgExist)
        if strMap.get(key)['replayTo'] is None or not isReplayMsgExist:
            strMap.get(key)['contentType'] = 'post'
            strMap.get(key)['esId'] = strMap.get(key)['first_name'] + '_' + str(strMap.get(key)['id'])
            strMap.get(key)['replayTo'] = None
        else:
            strMap.get(key)['contentType'] = 'comment'
            strMap.get(key)['esId'] = strMap.get(key)['first_name'] + '_' + str(strMap.get(key)['id'])

    # print(strMap)

    for key in strMap:
        element = strMap.get(key)

        if element['contentType'] is 'comment':
            parentId = recursive(element['replayTo'])
            element['parentId'] = parentId

    res = json.dumps(strMap)
    print(res)


def recursive(msgId):
    if strMap.get(msgId)['replayTo'] is None:
        return strMap.get(msgId)['esId']
    else:
        return recursive(strMap.get(msgId)['replayTo'])


main()
