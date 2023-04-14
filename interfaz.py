import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
import sqlite3



#F1 DOCUMENTACIÓN

class Interfaz:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.title("Base de Datos")
        self.ventana1.iconbitmap('img/sistema.ico')
        self.ventana1.geometry("915x410")
        self.ventana1.resizable(0,0)
        self.cuaderno1 = ttk.Notebook(self.ventana1,width=905, height=400)
        self.empresa()
        self.articulos()
        self.vendedores()
        self.clientes()
        self.cuaderno1.grid(column=0, row=0, padx=10, pady=10)
        self.ventana1.mainloop()

    def empresa(self):
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="  Empresa  ")
        self.img=tk.PhotoImage(file='img/empresaXL.png')
        self.panel = tk.Label(self.pagina1, image = self.img)
        self.panel.pack(side='left',fill='both',expand='true')
            


    def articulos(self):
        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2, text="  Articulos ")
        #LabelFrame"Datos"
        self.labelframeFiltros=ttk.LabelFrame(self.pagina2, text="Datos")        
        self.labelframeFiltros.grid(row=0, column=0, sticky="nw",padx=5,pady=10)
        #LabelID
        self.labelID = ttk.Label(self.labelframeFiltros, text="ID")
        self.labelID.grid(column=0,row=1,pady=5)
        #EntryLabelID
        self.ID=tk.StringVar()
        self.entryID=ttk.Entry(self.labelframeFiltros, textvariable=self.ID)
        self.entryID.grid(row=1, column=1)
        #LabelArticulo
        self.labelArticulo = ttk.Label(self.labelframeFiltros, text="Articulo")
        self.labelArticulo.grid(column=2,row=1, padx=4)
        #EntryLabelArticulo
        self.Articulo=tk.StringVar()
        self.entryArticulo=ttk.Entry(self.labelframeFiltros, textvariable=self.Articulo)
        self.entryArticulo.grid(row=1, column=3)
        #LabelCategoria
        self.labelCategoria = ttk.Label(self.labelframeFiltros, text="Categoria")
        self.labelCategoria.grid(column=4,row=1)
        #EntryLabelCategoria
        self.Categoria=tk.StringVar()
        self.entryCategoria=ttk.Entry(self.labelframeFiltros, textvariable=self.Categoria)
        self.entryCategoria.grid(row=1, column=5, padx=4)
        #LabelMarca
        self.labelMarca = ttk.Label(self.labelframeFiltros, text="Marca")
        self.labelMarca.grid(column=0,row=2)
        #EntryLabelMarca
        self.Marca=tk.StringVar()
        self.entryMarca=ttk.Entry(self.labelframeFiltros, textvariable=self.Marca)
        self.entryMarca.grid(row=2, column=1)
        #LabelPrecio
        self.labelPrecio = ttk.Label(self.labelframeFiltros, text="Precio")
        self.labelPrecio.grid(column=2,row=2)
        #EntryLabelPrecio
        self.Precio=tk.StringVar()
        self.entryPrecio=ttk.Entry(self.labelframeFiltros, textvariable=self.Precio)
        self.entryPrecio.grid(row=2, column=3,pady=5)
        #LabelFrame"CRUD"
        self.labelframeCRUD=ttk.LabelFrame(self.pagina2, text="CRUD")        
        self.labelframeCRUD.grid(row=0, column=2, pady=5)
        #Botón Listar
        self.listarA = ttk.Button(self.labelframeCRUD, text="Listar", command=self.mostrarA)
        self.listarA.grid(column=2, row=0, padx=5)
        #Botón Crear
        self.crearA = ttk.Button(self.labelframeCRUD, text="Crear", command=self.crearA)
        self.crearA.grid(column=3, row=0,padx=3)
        
        #Botón Eliminar
        self.eliminarA = ttk.Button(self.labelframeCRUD, text="Eliminar", command=self.eliminarA)
        self.eliminarA.grid(column=2, row=1,pady=5)
        #Botón Actualizar
        self.actualizarA = ttk.Button(self.labelframeCRUD, text="Actualizar", command=self.actualizarA)
        self.actualizarA.grid(column=3, row=1)
       
        
        #Tabla
        self.tablaA=ttk.Treeview(self.pagina2, columns=('#0','#1','#2','#3'))
        self.tablaA.place(x=80, y=110)
        self.tablaA.column('#0',width=80 )
        self.tablaA.heading('#0', text="ID")
        self.tablaA.column('#1',width=150 )
        self.tablaA.heading('#1', text="Nombre")
        self.tablaA.heading('#2', text="Categoría")
        self.tablaA.column('#2',width=150 )
        self.tablaA.heading('#3', text="Marca")
        self.tablaA.column('#3',width=150)
        self.tablaA.heading('#4', text="Precio")
        self.tablaA.column('#4',width=150)
        
   


    def vendedores(self):
        #Style
        #Bloques
        self.pagina3 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina3, text="  Vendedores  ")
        #LabelFrame"Datos"
        self.labelframeDatosV=ttk.LabelFrame(self.pagina3, text="Datos")        
        self.labelframeDatosV.grid(row=0, column=0, sticky="nw",padx=10,pady=10)
        #LabelID
        self.labelID = ttk.Label(self.labelframeDatosV, text="ID")
        self.labelID.grid(column=0,row=1,pady=5)
        #EntryLabelID
        self.IDV=tk.StringVar()
        self.entryIDV=ttk.Entry(self.labelframeDatosV, textvariable=self.IDV)
        self.entryIDV.grid(row=1, column=1)
        #LabelNombre
        self.labelNombre = ttk.Label(self.labelframeDatosV, text="Nombre")
        self.labelNombre.grid(column=2,row=1, padx=4)
        #EntryLabelNombre
        self.NombreV=tk.StringVar()
        self.entryNombreV=ttk.Entry(self.labelframeDatosV, textvariable=self.NombreV)
        self.entryNombreV.grid(row=1, column=3)
        #LabelDNI
        self.labelDNI = ttk.Label(self.labelframeDatosV, text="DNI")
        self.labelDNI.grid(column=4,row=1, padx=3)
        #EntryLabelDNI
        self.DNIV=tk.StringVar()
        self.entryDNIV=ttk.Entry(self.labelframeDatosV, textvariable=self.DNIV)
        self.entryDNIV.grid(row=1, column=5, padx=4)
        #LabelCelular
        self.labelCelular = ttk.Label(self.labelframeDatosV, text="Celular")
        self.labelCelular.grid(column=0,row=2)
        #EntryLabelCelular
        self.Celular=tk.StringVar()
        self.entryCelular=ttk.Entry(self.labelframeDatosV, textvariable=self.Celular)
        self.entryCelular.grid(row=2, column=1)
        #LabelIngreso
        self.labelfingreso = ttk.Label(self.labelframeDatosV, text="Ingreso")
        self.labelfingreso.grid(column=2,row=2)
        #EntryLabelIngreso
        self.fingreso=tk.StringVar()
        self.entryfingreso=ttk.Entry(self.labelframeDatosV, textvariable=self.fingreso)
        self.entryfingreso.grid(row=2, column=3,pady=7)
        #----------------------------------------------------------------------------------------#
        #LabelFrame"CRUD"
        self.labelframeCRUDV=ttk.LabelFrame(self.pagina3, text="CRUD")        
        self.labelframeCRUDV.grid(row=0, column=2, pady=5, padx=5)
        #Botón Crear
        self.crearV = ttk.Button(self.labelframeCRUDV, text="Crear", command=self.crearV)
        self.crearV.grid(column=3, row=0,padx=3)
        #Botón Eliminar
        self.eliminarV= ttk.Button(self.labelframeCRUDV, text="Eliminar", command=self.eliminarV )
        self.eliminarV.grid(column=2, row=1,pady=5)
        #Botón Actualizar
        self.actualizarV = ttk.Button(self.labelframeCRUDV, text="Actualizar", command=self.actualizarV)
        self.actualizarV.grid(column=3, row=1)
        #Botón Listar
        self.listarV = ttk.Button(self.labelframeCRUDV, text="Listar", command=self.mostrarV)
        self.listarV.grid(column=2, row=0, padx=5)
        #Tabla
        self.tablaV=ttk.Treeview(self.pagina3, columns=('#0','#1','#2','#3'))
        self.tablaV.place(x=80, y=110)
        self.tablaV.column('#0',width=50 )
        self.tablaV.heading('#0', text="ID")
        self.tablaV.heading('#1', text="Nombre")
        self.tablaV.heading('#2', text="DNI")
        self.tablaV.heading('#3', text="Celular")
        self.tablaV.heading('#4', text="FechaI")
        self.tablaV.column('#0',width=80 )
        self.tablaV.column('#1',width=150 )
        self.tablaV.column('#2',width=150 )
        self.tablaV.column('#3',width=150)
        self.tablaV.column('#4',width=150)

    def clientes(self):
        #Style
        #Bloques
        self.pagina4 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina4, text="  Clientes  ")
        #LabelFrame"Datos"
        self.labelframeDatosC=ttk.LabelFrame(self.pagina4, text="Datos")        
        self.labelframeDatosC.grid(row=0, column=0, sticky="nw",padx=10,pady=10)
        #LabelID
        self.labelID = ttk.Label(self.labelframeDatosC, text="ID")
        self.labelID.grid(column=0,row=1,pady=5)
        #EntryLabelID
        self.codC=tk.StringVar()
        self.codC=ttk.Entry(self.labelframeDatosC, textvariable=self.codC)
        self.codC.grid(row=1, column=1)
        #LabelNombre
        self.labelNombre = ttk.Label(self.labelframeDatosC, text="Nombre")
        self.labelNombre.grid(column=2,row=1, padx=4)
        #EntryLabelNombre
        self.Nombrec=tk.StringVar()
        self.entryNombrec=ttk.Entry(self.labelframeDatosC, textvariable=self.Nombrec)
        self.entryNombrec.grid(row=1, column=3)
        #LabelDNI
        self.labelDNI = ttk.Label(self.labelframeDatosC, text="DNI")
        self.labelDNI.grid(column=4,row=1, padx=3)
        #EntryLabelDNI
        self.DNIc=tk.StringVar()
        self.entryDNIc=ttk.Entry(self.labelframeDatosC, textvariable=self.DNIc)
        self.entryDNIc.grid(row=1, column=5, padx=4)
        #LabelDistrito
        self.labelDistrito = ttk.Label(self.labelframeDatosC, text="Distrito")
        self.labelDistrito.grid(column=0,row=2)
        #EntryLabelDistrito
        self.Distrito=tk.StringVar()
        self.entryDistrito=ttk.Entry(self.labelframeDatosC, textvariable=self.Distrito)
        self.entryDistrito.grid(row=2, column=1)
        #LabelEmail
        self.labelemail = ttk.Label(self.labelframeDatosC, text="Email")
        self.labelemail.grid(column=2,row=2)
        #EntryLabelEmail
        self.email=tk.StringVar()
        self.entryemail=ttk.Entry(self.labelframeDatosC, textvariable=self.email)
        self.entryemail.grid(row=2, column=3,pady=7)
        #----------------------------------------------------------------------------------------#
        #LabelFrame"CRUD"
        self.labelframeCRUDC=ttk.LabelFrame(self.pagina4, text="CRUD")        
        self.labelframeCRUDC.grid(row=0, column=2, pady=5, padx=5)
        #Botón Crear
        self.crearC = ttk.Button(self.labelframeCRUDC, text="Crear", command=self.crearC)
        self.crearC.grid(column=3, row=0,padx=3)
        #Botón Eliminar
        self.eliminarC= ttk.Button(self.labelframeCRUDC, text="Eliminar", command=self.eliminarC )
        self.eliminarC.grid(column=2, row=1,pady=5)
        #Botón Actualizar
        self.actualizarC = ttk.Button(self.labelframeCRUDC, text="Actualizar", command=self.actualizarC)
        self.actualizarC.grid(column=3, row=1)
        #Botón Listar
        self.listarC = ttk.Button(self.labelframeCRUDC, text="Listar",command=self.mostrarC)
        self.listarC.grid(column=2, row=0, padx=5)
    
        #TablaC
        self.tablaC=ttk.Treeview(self.pagina4, columns=('#0','#1','#2','#3'))
        self.tablaC.place(x=80, y=110)
        self.tablaC.column('#0',width=50 )
        self.tablaC.heading('#0', text="ID")
        self.tablaC.heading('#1', text="Nombre")
        self.tablaC.heading('#2', text="DNI")
        self.tablaC.heading('#3', text="Dsitrito")
        self.tablaC.heading('#4', text="Email")
        self.tablaC.column('#0',width=80 )
        self.tablaC.column('#1',width=150 )
        self.tablaC.column('#2',width=150 )
        self.tablaC.column('#3',width=150)
        self.tablaC.column('#4',width=150)

#----------------------------------------------------------------------------------------
    #ListaArticulos
    def mostrarA(self):
        conexion=sqlite3.connect("BDINVENTARIO.db")
        tabla=self.tablaA
        cursor=conexion.cursor()
        registros=tabla.get_children()
        for elemento in registros:
                tabla.delete(elemento)

        try:
            cursor.execute("SELECT * FROM articulo")
            for row in cursor:
                    tabla.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4]))
        except:
                pass

    #ListaVendedor
    def mostrarV(self):
        conexion=sqlite3.connect("BDINVENTARIO.db")
        tabla=self.tablaV
        cursor=conexion.cursor()
        registros=tabla.get_children()
        for elemento in registros:
                tabla.delete(elemento)

        try:
                cursor.execute("SELECT * FROM vendedor")
                for row in cursor:
                        tabla.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4]))
        except:
                pass
   #ListaCliente
    def mostrarC(self):
        conexion=sqlite3.connect("BDINVENTARIO.db")
        tabla=self.tablaC
        cursor=conexion.cursor()
        registros=tabla.get_children()
        for elemento in registros:
                tabla.delete(elemento)

        try:
                cursor.execute("SELECT * FROM cliente")
                for row in cursor:
                        tabla.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4]))
        except:
                pass

    #Limpia Campos 
    def LimpiarCamposA(self):
        self.ID.set("")
        self.Articulo.set("")
        self.Categoria.set("")
        self.Marca.set("")
        self.Precio.set("")

    def LimpiarCamposV(self):
        self.IDV.set("")
        self.NombreV.set("")
        self.DNIV.set("")
        self.Celular.set("")
        self.fingreso.set("")

    

    
        
    #Borrar elementos de tablaA
    def borrarListaA(self):
        conexion=sqlite3.connect('BDINVENTARIO.db')
        tabla=self.tablaA
        cursor=conexion.cursor()
        registros=tabla.get_children()
        for elemento in registros:
            tabla.delete(elemento)
    
    #Consulta por nombre
    def consultarA(self):
        self.borrarListaA()
        conexion=sqlite3.connect("BDINVENTARIO.db")
        datos=self.Articulo.get() 
        tabla=self.tablaA
        cursor=conexion.cursor()
        cursor=conexion.execute("select * from articulo where Nombre=?", (datos,))
        row=cursor.fetchone()
        filas=cursor.fetchall()
        if row!=None:
            for filas in row:
                tabla.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4]))
        else:
            mb.showinfo("Información", "No existe un artículo con dicho nombre")
        conexion.close()


    #Crear datosA
    def crearA(self):
        miConexion=sqlite3.connect("BDINVENTARIO.db")
        miCursor=miConexion.cursor()
        datos=self.Articulo.get(),self.Categoria.get(), self.Marca.get(),self.Precio.get()
        miCursor.execute("INSERT INTO articulo VALUES(NULL,?,?,?,?)", (datos))
        miConexion.commit()
        mb.showinfo(title="Información",message="Se creó el resgitro")
        self.mostrarA()
        self.LimpiarCamposA()

    def crearV(self):
            conex=sqlite3.connect('BDINVENTARIO.db')
            cursor=conex.cursor() 
            datos=self.NombreV.get(),self.DNIV.get(),self.Celular.get(),self.fingreso.get()
            cursor.execute("INSERT INTO vendedor VALUES(NULL,?,?,?,?)", (datos))
            conex.commit()
            mb.showinfo(title="Información",message="Se creó el resgitro")
            self.mostrarV()
            self.LimpiarCamposV()

    #no borra
    def crearC(self):
            conex=sqlite3.connect('BDINVENTARIO.db')
            cursor=conex.cursor() 
            datos=self.Nombrec.get(),self.DNIc.get(),self.Distrito.get(),self.email.get()
            cursor.execute("INSERT INTO cliente VALUES(NULL,?,?,?,?)", (datos))
            conex.commit()
            mb.showinfo(title="Información",message="Se creó el resgitro")
            self.mostrarC()
            self.Limpiar()
            
    #-------#
    def Limpiar(self):
        #self.codC.set("")
        self.Nombrec.set("")
        self.DNIc.set("")
        self.Distrito.set("")
        self.email.set("")


    #Eliminar
    def eliminarA(self):
            conex=sqlite3.connect('BDINVENTARIO.db')
            cursor=conex.cursor() 
            if mb.askyesno(message="¿Realmente desea eliminar el registro?", title="ADVERTENCIA"):
                            cursor.execute("DELETE FROM articulo WHERE codA="+self.ID.get())
                            conex.commit()
                            mb.showinfo(title="Información",message="Se elimino correctamente")
                            self.mostrarA()
            else:
               mb.showwarning("ADVERTENCIA","Ocurrió un error al tratar de eliminar el registro")
               pass

    def eliminarV(self):
            conex=sqlite3.connect('BDINVENTARIO.db')
            cursor=conex.cursor() 
            if mb.askyesno(message="¿Realmente desea eliminar el registro?", title="ADVERTENCIA"):
                            cursor.execute("DELETE FROM vendedor WHERE codV="+self.IDV.get())
                            conex.commit()
                            mb.showinfo(title="Información",message="Se elimino correctamente")
                            self.mostrarV()
            else:
               mb.showwarning("ADVERTENCIA","Ocurrió un error al tratar de eliminar el registro")
               pass

    def eliminarC(self):
            conex=sqlite3.connect('BDINVENTARIO.db')
            cursor=conex.cursor() 
            if mb.askyesno(message="¿Realmente desea eliminar el registro?", title="ADVERTENCIA"):
                            cursor.execute("DELETE FROM cliente WHERE codC="+self.codC.get())
                            conex.commit()
                            mb.showinfo(title="Información",message="Se elimino correctamente")
                            self.mostrarC()
            else:
               mb.showwarning("ADVERTENCIA","Ocurrió un error al tratar de eliminar el registro")
               pass


   #UPdate
    def actualizarA(self):
            conex=sqlite3.connect('BDINVENTARIO.db')
            cursor=conex.cursor()
            datos=self.Articulo.get(),self.Categoria.get(), self.Marca.get(),self.Precio.get()
            if mb.askyesno(message="¿Realmente desea actualizar el registro?", title="ADVERTENCIA"):
                            cursor.execute("UPDATE articulo SET Nombre=?, categoria=?, marca=?, precio=? WHERE codA="+self.ID.get(), (datos))
                            conex.commit()
                            mb.showinfo(title="Información",message="Se actualizo correctamente")
                            self.mostrarA()
                            self.LimpiarCamposA()
            else:
               mb.showwarning("ADVERTENCIA","Ocurrió un error al tratar de actualizar el registro")
               pass

    def actualizarV(self):
            conex=sqlite3.connect('BDINVENTARIO.db')
            cursor=conex.cursor()
            datos=self.NombreV.get(),self.DNIV.get(),self.Celular.get(),self.fingreso.get()
            if mb.askyesno(message="¿Realmente desea actualizar el registro?", title="ADVERTENCIA"):
                    cursor.execute("UPDATE vendedor SET Nombre=?, dni=?, celular=?, fingreso=? WHERE codV="+self.IDV.get(), (datos))
                    conex.commit()
                    mb.showinfo(title="Información", message="Se actualizo correctamente")
                    self.mostrarV()
                    self.LimpiarCamposV()
            else:
                mb.showwarning("ADVERTENCIA","Ocurrió un error al tratar de actualizar el registro")
                pass


    def actualizarC(self):
            conex=sqlite3.connect("BDINVENTARIO.db")
            cursor=conex.cursor()
            datos=self.Nombrec.get(),self.DNIc.get(),self.Distrito.get(),self.email.get()
            if mb.askyesno(message="¿Realmente desea actualizar el registro?", title="ADVERTENCIA"):
                    cursor.execute("UPDATE cliente SET Nombre=?, dni=?, distrito=?, email=? WHERE codC="+self.codC.get(), (datos))
                    conex.commit()
                    mb.showinfo(title="Información", message="Se actualizo correctamente")
                    self.mostrarC()
                    self.Limpiar()
            else:
                   mb.showwarning("ADVERTENCIA","Ocurrió un error al tratar de actualizar el registro")
                   pass
                


    
            
            
  

        

   
            

    

    


            

aplicacion1=Interfaz()

