from tkinter import *
#mesajes emergentes 
from tkinter import messagebox
import sqlite3
import pymysql 
#---------------coneccion con base de datos mysql--------
class DataBase:
  def __init__(self):
    self.connection=pymysql.connect (
      host="localhost",
      user="root",
      db="Usuarios"
    )
    self.cursor= self.connection.cursor()
    print("conexion exitosa ")
    database=DataBase()
def conexionBBDD() :
    miConexion= sqlite3.connect("Usuarios")
  
    miCursor = miConexion.cursor()
    try:
 
     miCursor.execute ("""

        CREATE  TABLE DATOSUSUARIOS (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOMBRE_USUARIO VARCHAR (50),
        CEDULA INTEGER,
        TELEFONO1 INTEGER,
        TELEFONO2 INTEGER,
        DIRECCION VARCHAR)
        """)

     messagebox.showinfo("base de datos", "base de datos creada con exito ")


    except:
        messagebox.showwarning("Atencion", "la base de datos ya existe ")
     
   

def salirAplicasion() :
   valor=messagebox.askquestion("salir ", "¿Desea salir de la aplicasion? ")
   if  valor == "yes":
       root.destroy()


# ---------------funciones de  menu borrar ----------------

def limpiarCampos():
  miID.set("")
  miNomnbre.set("")
  miCedula.set ("")
  miTelefono1.set("")
  miTelefono2.set("")
  miDireccion.set("")
    

#------------------funcion de menu  CRUD----------------
#-------OPCION CREAR -------------

def crear():
    miConexion=sqlite3.connect("Usuarios")

    miCursor=miConexion.cursor()

    miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES (NULL,'"+ miNomnbre.get() + 
    "','" + miCedula.get()  +
    "','" + miTelefono1.get() +
    "','" + miTelefono2.get() +
    "','" + miDireccion.get() + "')" )
    miConexion.commit()
    messagebox.showinfo("base de datos ", "registro insetado con exito ")
  

 # -------------funcion de opcion leer-----------

def leer ():
  miConexion=sqlite3.connect("Usuarios")

  miCursor=miConexion.cursor()

  miCursor.execute("SELECT * FROM DATOSUSUARIOS WHERE ID ="+ miID.get())

  elUsuario=miCursor.fetchall()

  for usuario in elUsuario :

       miID.set(usuario[0])
       miNomnbre.set(usuario[1])
       miCedula.set(usuario[2])
       miTelefono1.set(usuario[3])
       miTelefono2.set(usuario[4])
       miDireccion.set(usuario[5])

  miConexion.commit()

  #--------------funcion actualizar ----------------

def actualizar():
    miConexion=sqlite3.connect("Usuarios")

    miCursor=miConexion.cursor()

    miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO = '" + miNomnbre.get()+
    "', CEDULA = '" + miCedula.get()+
    "', TELEFONO1 = '" + miTelefono1.get()+
    "', TELEFONO2 = '" + miTelefono2.get()+
    "', DIRECCION = '" + miDireccion.get()+
     "' WHERE ID = " + miID.get())
    miConexion.commit()
    messagebox.showinfo("base de datos ", "registro actualizado con exito ")

#--------------funcion eliminar -----------
def eliminar ():
     miConexion=sqlite3.connect("Usuarios")

     miCursor=miConexion.cursor()

     miCursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID = "+ miID.get())
     miConexion.commit()
     messagebox.showinfo("base de datos ", "registro borrado con exito ")









 
# crear una raiz 

root= Tk()

# crear barra menu

barraMenu = Menu(root)
root.config(menu=barraMenu,width= 300, height= 300)
# ingresar los elementos de la barra de menu 
bbddMenu = Menu(barraMenu, tearoff = 0)
bbddMenu.add_command(label= "Concetar",command=conexionBBDD)
bbddMenu.add_command(label= "Salir", command=salirAplicasion)

borrarMenu = Menu(barraMenu, tearoff = 0)
borrarMenu.add_command(label= "Borrar campos",command=limpiarCampos)


crudMenu = Menu(barraMenu, tearoff = 0)
crudMenu.add_command(label= "Crear", command=crear )
crudMenu.add_command(label= "leer", command=leer)
crudMenu.add_command(label= "Actualizar ", command = actualizar)
crudMenu.add_command(label= "Borrar  ",command=eliminar)

barraMenu.add_cascade(label= "base de datos ", menu=bbddMenu)
barraMenu.add_cascade(label= "borrar", menu=borrarMenu)
barraMenu.add_cascade(label= "CRUD", menu=crudMenu)

# --------------cominezo de campos de la aplicasion-----------

# frame de la parte superior 

miFrame= Frame(root)
miFrame.pack()

miID=StringVar()
miNomnbre=StringVar()
miCedula=StringVar()
miTelefono1=StringVar()
miTelefono2=StringVar()
miDireccion=StringVar()

cuadroID=Entry(miFrame,textvariable=miID)
cuadroID.grid(row=0,column= 1, padx=10 ,pady=10) # especifico el lugar 

cuadroNOMBRE=Entry(miFrame,textvariable=miNomnbre)
cuadroNOMBRE.grid(row=1,column= 1, padx=10 ,pady=10)

cuadroCEDULA=Entry(miFrame,textvariable=miCedula)
cuadroCEDULA.grid(row=2,column= 1, padx=10 ,pady=10)

cuadroTELEFONO1=Entry(miFrame,textvariable=miTelefono1)
cuadroTELEFONO1.grid(row=3,column= 1, padx=10 ,pady=10)

cuadroTELEFONO2=Entry(miFrame,textvariable=miTelefono2)
cuadroTELEFONO2.grid(row=4,column= 1, padx=10 ,pady=10)

cuadroDIRECCION=Entry(miFrame,textvariable=miDireccion)
cuadroDIRECCION.grid(row=5,column= 1, padx=10 ,pady=10)


# ---------------COMIENZAN LOS ETIQUETAS ---------------

idLabel= Label(miFrame, text= "ID :")
idLabel.grid(row=0,column=0,sticky= "e",padx= 10, pady= 10)

nombreLabel= Label(miFrame, text= "Nombre completo :")
nombreLabel.grid(row=1,column=0,sticky= "e",padx= 10, pady= 10)


cedulaLabel= Label(miFrame, text= "Cedula :")
cedulaLabel.grid(row=2,column=0,sticky= "e",padx= 10, pady= 10)


telefono1Label= Label(miFrame, text= "Telefono 1 :")
telefono1Label.grid(row=3,column=0,sticky= "e",padx= 10, pady= 10)



telefono2Label= Label(miFrame, text= "Telefono 2 :")
telefono2Label.grid(row=4,column=0,sticky= "e",padx= 10, pady= 10)

direccionLabel= Label(miFrame, text= "Direccion :")
direccionLabel.grid(row=5,column=0,sticky= "e",padx= 10, pady= 10)

#------------añadir botones en la parte inferior creando ootro frame----------------------

miFrame2= Frame(root)
miFrame2.pack()

botonCrear=Button(miFrame2, text= "Crear",command=crear)
botonCrear.grid(row=1,column= 0, sticky= "e", padx=10, pady=10)

botonLeer=Button(miFrame2, text= "Leer",command= leer)
botonLeer.grid(row=1,column= 1, sticky= "e", padx=10, pady=10)

botonActualizar=Button(miFrame2, text= "Actualizar", command=actualizar)
botonActualizar.grid(row=1,column= 2, sticky= "e", padx=10, pady=10)


botonBorrar=Button(miFrame2, text= "Borrar",command=eliminar)
botonBorrar.grid(row=1,column= 3, sticky= "e", padx=10, pady=10)


root.mainloop ()