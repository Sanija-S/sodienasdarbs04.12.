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
#izvadi visas vertibas 
print(f"3.) Vārdnīcas vērtības:")
for i in ziema.values():
    print(i)
#izvadit atslegu un parbaudit vai tada atslega pastav
ievade_atslega=input("Ievadi atslegu, lai atrastu vērtību:")

if ievade_atslega in ziema:
  print(f"{ievade_atslega}: {ziema[ievade_atslega]}")
else:
  print(f"tāda atslēga nav atrasta vārdnīcā")