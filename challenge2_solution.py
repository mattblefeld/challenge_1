import json


def remove_element_from_json(element_name):
    """
    Purpose: To accept an element name and remove it from the json file
    :param element_name: this is the text of the element you want to delete
    :type str
    """
    with open('test_payload.json', 'r') as json_file:
        data = json.load(json_file)

    for k, v in list(data.items()):
        if element_name in k:
            data.pop(element_name)
        elif v is not None and element_name in v:
            for key in list(v.keys()):
                if element_name == key:
                    v.pop(key)

    with open('test_payload.json', 'w') as json_file:
        json.dump(data, json_file)


if __name__ == '__main__':
    remove_element_from_json("statecode")
