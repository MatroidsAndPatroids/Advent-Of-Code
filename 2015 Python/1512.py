import utility # my own utility.pl file
import json # load

# Recursively iterate through the json object and return the sum of all numbers that are not skipped
def sumNumbers(json, skipped = None):
    if isinstance(json, int):
        return json
    elif isinstance(json, dict):
    	return 0 if skipped in json.values() else sumNumbers(list(json.values()), skipped)
    elif isinstance(json, list):
        return sum(map(sumNumbers, json, len(json) * [skipped]))
    else:
        return 0

assert sumNumbers(json.loads('[1,2,3]')) == 6
assert sumNumbers(json.loads('{"a":2,"b":4}')) == 6
assert sumNumbers(json.loads('[[[3]]]')) == 3
assert sumNumbers(json.loads('{"a":{"b":4},"c":-1}')) == 3
assert sumNumbers(json.loads('{"a":[-1,1]}')) == 0
assert sumNumbers(json.loads('[-1,{"a":1}]')) == 0
assert sumNumbers(json.loads('[]')) == 0
assert sumNumbers(json.loads('{}')) == 0

assert sumNumbers(json.loads('[1,2,3]'), 'red') == 6
assert sumNumbers(json.loads('[1,{"c":"red","b":2},3]'), 'red') == 4
assert sumNumbers(json.loads('{"d":"red","e":[1,2,3,4],"f":5}'), 'red') == 0
assert sumNumbers(json.loads('{"a":{"d":8},"e":[1,2,3,4],"d":"red","e":[1,2,3,4],"x":{"f":5}}'), 'red') == 0
assert sumNumbers(json.loads('[1,"red",5]'), 'red') == 6

# Display info message
print("Give a JSON document in text format:\n");
jsonObject = json.loads(utility.readInputList(joinedWith = ''))

# Display results
print (f'{sumNumbers(jsonObject) = }, {sumNumbers(jsonObject, "red") = }')
