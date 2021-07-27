# Imports
import json

with open("cristian.json") as cristian:
    cristian_dict = json.load(cristian)

with open("cristian.json","w") as cristian:
    json.dump(person_dict, cristian)

with open("Articulos.json") as client:
    client_dict = json.loads(client.read())
    
    
print(client_dict)
print(client_dict["name"])
print(client_dict["intereses"])
print(client_dict["intereses"][2])
print(client_dict["ultimos articulos"])
print(client_dict["ultimos articulos"]["ropa"])

person_dict = {"name": "Cristian"
                "last name": "Rosas"
                "sobrenombre": "Chino"
                }

print(cristian_dict)
