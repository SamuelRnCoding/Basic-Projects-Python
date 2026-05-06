import json
datos_os={
    "Nombre OS":"Flow OS",
    "Resolucion":"Full HD"
}
option=input("1 Escribir  2 Leer 3 Cambiar")
if option=="1":
  with open("datos_os.json","w") as file:
    json.dump(datos_os,file)
    print("Guardado correcto")
elif option=="2":
  with open("datos_os.json","r") as file:
    lectura=json.load(file)
    print(f"Sistema Operativo:{lectura['Nombre OS']}")
    print(f"Resolucion Actual:{lectura['Resolucion']}")
elif option == 3:
  print(f"Resolucion Actual {datos_os['Resolucion']}")
  nueva_resolucion=input("A que resolucion cambiaras")
  datos_os['Resolucion']=nueva_resolucion
  with open(datos_os.json,'w') as file:
    json.dump(datos_os,file)
    print("Resolucion Cambiada!")
