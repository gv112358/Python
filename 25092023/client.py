import json, sys, requests
from jsonschema import validate

schema = {
    "type": "object",
    "properties": {
        "Tipo": {"type": "string"},
        "Valore": {"type": ["string","number"]},
    },
    "required": ["Tipo", "Valore"],
    "additionalProperties": False
}


api_url = "http://127.0.0.1:8080/interrogazione"
data = {"Tipo": "Cognome", "Valore": "Ros"}
validate(instance=data, schema=schema)
response = requests.get(api_url,json=data)
#print(response.json())
print(response.status_code)
print(response.headers["Content-Type"])
data1 = response.json()
print(data1)