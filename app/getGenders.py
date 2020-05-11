def getGenders(genders):
    import json
    json_string = genders
    parsed_json = json.loads(json_string)

    genders = []

    gender1 = parsed_json['gender1']
    genders.append(gender1)
    gender2 = parsed_json['gender2']
    genders.append(gender2)
    gender3 = parsed_json['gender3']
    genders.append(gender3)

    return genders
