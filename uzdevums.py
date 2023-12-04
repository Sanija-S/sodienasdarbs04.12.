import json 
#ievadit datnes nosaukumu kuru velas apstradat
file_name=input("Ievadi danes nosaukumu:")
#meginat atvert un nolasit JSOn datni

try:
  with open(file_name, "r", encoding= "utf-8") as file:


    data=json.load(file)
except FileNotFoundError:

  print("file not found")

except json.JSONDecodeError:

  print("file format is wrong for jonson")


  ziema=dict(data)

  print(f"1.) Vardnicas garums ir:{len(ziema)}")

  print(f"2) vardnicas atslegas:")

  for key in ziema.keys():
    print(key)
