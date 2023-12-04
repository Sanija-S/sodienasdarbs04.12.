#uzd tiks pildits mazliet savadak!!!(kopij peistoju uzdevums.py kodu)

import json 

file_name=input("Ievadi danes nosaukumu:")

try:
  with open(file_name, "r", encoding= "utf-8") as file:
    data=json.load(file)

except FileNotFoundError:
  print("file not found")

except json.JSONDecodeError:
  print("file format is wrong for jonson")


# pārvērst jonsona datni par vārdnīcu
people_dict=[]# izveido tukšu vārdnīcu 
for person in data:
  person_id=person.get("id")
  person.info={
    "vards": person.get{"vards"},
    "uzvards": person.get{"uzvards"},
    "vecums": person.get{"vecums"},


  }
  people_dict[person_id]=person_id
  print("Vārdnīca ar personu informāciju")


  for person_id, person_info in people_dict.items(): #nebija tada mainigaa "person_id"
    print(f"ID:{person_id}, Vārds: {person_info["vards"]}, Uzvārds: {person_info["uzvards"]}, Vecums: {person_info["vecums"]}")
