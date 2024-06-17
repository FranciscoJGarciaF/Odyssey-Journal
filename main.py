from tkinter import *
from tkinter import font
from tkinter import messagebox
from PIL import Image, ImageTk
from customtkinter import *
import customtkinter
from customtkinter import CTkToplevel
from customtkinter import filedialog
from CTkListbox import *
from CTkMenuBar import *
import sys
import os
import webbrowser
import glob
import shutil
import sqlite3

if hasattr (sys, '_MEIPASS'):
    os.chdir(sys._MEIPASS)
else:
    os.chdir("C:/Users/FRANCISCO/Downloads/practicaprogramacion/unefamerida/tkinter/Fundamentos/EditordeTexto")

customtkinter.set_appearance_mode("System")  
customtkinter.set_default_color_theme("./themes/red.json")
root = CTk()

root.title("Sin Título - Odyssey Journal 1.1.0")

root.iconbitmap("./img/icon.ico")
root.geometry('1200x680')

imagenNegrita = customtkinter.CTkImage(Image.open('./img/negrita.png'), size=(25, 25))
imagenCursiva = customtkinter.CTkImage(Image.open('./img/cursiva.png'), size=(25, 25))
imagenSubrayado = customtkinter.CTkImage(Image.open('./img/S.png'), size=(25, 25))
imagenSobrerayado = customtkinter.CTkImage(Image.open('./img/U.png'), size=(25, 25))
imagenGestor = customtkinter.CTkImage(Image.open('./img/P.png'), size=(25, 25))
imagenFuentes = customtkinter.CTkImage(Image.open('./img/T.png'), size=(25, 25))



global nombreAbierto
nombreAbierto = False

global seleccion
seleccion = False

global proyectoAutor
global proyectoDesc
proyectoAutor = None
proyectoDesc = None

global nombreProyectoAbierto
nombreProyectoAbierto = None
global versionProyectoAbierto
versionProyectoAbierto = None
global actividadProyectoAbierto
actividadProyectoAbierto = None
global tagCount
tagCount = []
global cfont
global csize
global IDCount
global cajaTextoLabel
global guardado
guardado = False

# Funciones


# Crear Proyectos

class Project:
    def __init__(self, nombre):
        self.nombre = nombre
        self.id = 0
        self.folderpath = None
        self.versionsUpdtNum = 0
        self.versions = str(self.versionsUpdtNum)
        self.id_V = -1

        self.enlaceSig = None

class Projects:
    def __init__(self):
        if os.path.isfile('projects/projects.txt'):
            print('True')
            with open('projects/projects.txt', 'r') as file:
                data = file.readlines()
                print(f'{data}')
                for i in range (len(data)-1, -1, -1):
                    if data[i][0] == 'I':
                        dataID = data[i]
                        for elem in dataID:
                            if elem.isdigit():
                                self.id_Project = int(elem)
                                print(self.id_Project)
                                return

        else:
            print('False')
            self.id_Project = -1


    def crearProyecto(self, nombre):
        p = Project(nombre)

        self.id_Project = self.id_Project + 1
        p.id = self.id_Project

        if os.path.isdir('./projects') == False:
            os.mkdir('./projects')
            os.mkdir(f'projects/{nombre}')
            
            file = open(f'projects/projects.db', 'a')
            file.close()
            
            p.folderpath = f'projects/{nombre}'
            file = open(f'projects/projects.txt', 'a')
            file.write(f'ID: {p.id}\nName: {nombre}\nVersion: {p.versions}\nFolderpath: {p.folderpath}\n\n')
            file.close()

            os.mkdir(f'./projects/{nombre}/Versions')

            file = open(f'./projects/{nombre}/Versions/versions.db', 'a')
            file.close()

            with open(f'projects/projects.txt', 'r') as file:
                for line in file:
                    if f'Folderpath: projects/{nombre}' in line:
                        messagebox.showinfo('Éxito', f'Proyecto creado exitosamente en projects/{nombre}')

            return False
        else:
            try:
                os.mkdir(f'projects/{nombre}')
                p.folderpath = f'projects/{nombre}'

                file = open(f'projects/projects.txt', 'a')
                file.write(f'ID: {p.id}\nName: {nombre}\nVersion: {p.versions}\nFolderpath: {p.folderpath}\n\n')
                file.close()

                os.mkdir(f'./projects/{nombre}/Versions')

                file = open(f'./projects/{nombre}/Versions/versions.db', 'a')
                file.close()

                with open(f'projects/projects.txt', 'r') as file:
                    for line in file:
                        if f'Folderpath: projects/{nombre}' in line:
                            messagebox.showinfo('Éxito', f'Proyecto creado exitosamente en projects/{nombre}')

                return False
            except FileExistsError:
                messagebox.showinfo("Error", f"El proyecto ya existe")
                return True


    def nuevaVersion(self, nombre, ProyectoExiste = False):

        if ProyectoExiste == False:
            folderpath = None
            version = ''

            with open('./projects/projects.txt', 'r') as file:
                data = file.readlines()
                for line in range(0, len(data)):
                    if f'Folderpath: projects/{nombre}\n' == data[line]:
                        folderpath = f'projects/{nombre}'
                        i = line-1
                        break
            
            if folderpath == None:
                messagebox.showinfo('Error', 'Proyecto no encontrado.', icon = "cancel")
            else:
                with open('./projects/projects.txt', 'r') as file:
                    data = file.readlines()
                    dataV = data[i]
                    for e in range (0, len(data[i])):
                        if dataV[e].isdigit():
                            version += ''+dataV[e]   
                    if version == '0' and os.path.isdir(f'./projects/{nombre}/Versions/ver_0') == False:
                        os.mkdir(f'./projects/{nombre}/Versions/ver_{version}')        
                        fileVfolderpath =f'./projects/{nombre}/Versions/ver_{version}'

                        fileV = open(f'./projects/{nombre}/Versions/versions.txt', 'a')
                        fileV.write(f'ID: {version}\nFolderpath: {fileVfolderpath}\n')
                        fileV.close()
                        
                        messagebox.showinfo('Éxito', f'Versión: {version} creada exitosamente')
                    else:  
                        version = int(version)
                        version += 1
                        version = str(version)

                        os.mkdir(f'./projects/{nombre}/Versions/ver_{version}')        
                        fileVfolderpath =f'./projects/{nombre}/Versions/ver_{version}'

                        fileV = open(f'./projects/{nombre}/Versions/versions.txt', 'a')
                        fileV.write(f'ID: {version}\nFolderpath: {fileVfolderpath}\n')
                        fileV.close()
                        
                        messagebox.showinfo('Éxito', f'Versión: {version} creada exitosamente')

                data[i] = f'Version: {version}\n'
                
                with open('./projects/projects.txt', 'w') as file:
                    file.writelines(data)
                return int(version)
        else:
            return

    def nuevaActividad(self, nombre, ProyectoExiste = False):

        if ProyectoExiste == False:
            folderpath = None
            version = ''
            activity = ''


            with open('./projects/projects.txt', 'r') as file:
                data = file.readlines()
                for line in range(0, len(data)):
                    if f'Folderpath: projects/{nombre}\n' == data[line]:
                        folderpath = f'projects/{nombre}'
                        i = line
                        break
                

            if folderpath == None:
                messagebox.showerror('Error', 'Proyecto no encontrado.')
                return
            else:
                with open(f'./projects/{nombre}/Versions/versions.txt', 'r') as file:
                    data = file.readlines()
                    for e in range (len(data)-1, -1, -1):
                        if data[e][0] == 'I':
                            for elemV in data[e]:
                                if elemV.isdigit():
                                    version+= ''+elemV
                            break

                    for e in range (len(data)-1, -1, -1):
                        if data[e][0] == 'A':
                            for elem in data[e]:
                                if elem.isdigit():
                                    activity += ''+elem
                            activity = int(activity)

                            activity +=1 
                            activity = str(activity)
                            dataAux = data[:-1]
                            dataAux.append(f'Activities: {activity}\n')

                            with open(f'./projects/{nombre}/Versions/versions.txt', 'w') as file:
                                file.truncate()
                                file.writelines(dataAux)
                            break
                        else:
                            data.append(f"Activities: 0\n")
                            activity = '0'
                            with open(f'./projects/{nombre}/Versions/versions.txt', 'w') as file:
                                file.truncate()
                                file.writelines(data)
                            break
                       
            print(version)
            if os.path.isdir(f'./projects/{nombre}/Versions/ver_{version}/activities') == False:
                os.mkdir(f'./projects/{nombre}/Versions/ver_{version}/activities')

                file = open(f'./projects/{nombre}/Versions/ver_{version}/activities/activities.db', 'a')
                file.close()                

                file = open(f'./projects/{nombre}/Versions/ver_{version}/activities/Actividad {activity}.txt', 'a')
                file.close()
            else:
                file = open(f'./projects/{nombre}/Versions/ver_{version}/activities/Actividad {activity}.txt', 'a')
                file.close()
            


            return int(activity)
        else:
            return
        
    def buscarActividad(self, nombre):
        folderpath = None
        version = ''
        activity = ''

        with open('./projects/projects.txt', 'r') as file:
            data = file.readlines()
            for line in range(0, len(data)):
                if f'Folderpath: projects/{nombre}\n' == data[line]:
                    folderpath = f'projects/{nombre}'
                    i = line
                    break
                

        if folderpath == None:
            messagebox.showerror('Error', 'Proyecto no encontrado.')
            return
        else:
            with open(f'./projects/{nombre}/Versions/versions.txt', 'r') as file:
                data = file.readlines()
                for e in range (len(data)-1, -1, -1):
                    if data[e][0] == 'I':
                        for elemV in data[e]:
                            if elemV.isdigit():
                                 version+= ''+elemV
                        break
                    
                for e in range (len(data)-1, -1, -1):
                    if data[e][0] == 'A':
                        for elem in data[e]:
                            if elem.isdigit():
                                activity += ''+elem
                        break
        
        with open(f'./projects/{nombre}/Versions/ver_{version}/activities/Actividad {activity}.txt', 'r') as file:
            data = file.read()
        
        return data, int(activity)
        
    def buscarActividadEspecifica(self, nombre, actividad, version = ''):
        folderpath = None
        version = version
        activity = actividad

        with open('./projects/projects.txt', 'r') as file:
            data = file.readlines()
            for line in range(0, len(data)):
                if f'Folderpath: projects/{nombre}\n' == data[line]:
                    folderpath = f'./projects/{nombre}'
                    i = line
                    break
                

        if folderpath == None:
            messagebox.showerror('Error', 'Proyecto no encontrado.')
            return
        else:
            if version == '':
                with open(f'./projects/{nombre}/Versions/versions.txt', 'r') as file:
                    data = file.readlines()
                    for e in range (len(data)-1, -1, -1):
                        if data[e][0] == 'I':
                            for elemV in data[e]:
                                if elemV.isdigit():
                                    version+= ''+elemV
                            break
                    

        with open(f'./projects/{nombre}/Versions/ver_{version}/activities/{activity}.txt', 'r') as file:
            data = file.read()

        folderpath = f'./projects/{nombre}/Versions/ver_{version}/activities/{activity}.txt'

        return data, folderpath

    def eliminarActividad(self, nombre, actividad):
        g = self.buscarActividadEspecifica(nombre, actividad)[1]

        os.remove(g)

global p 
p = Projects()

def alSalir():
    global nombreProyectoAbierto
    global guardado

    if nombreProyectoAbierto != None and guardado != True:
        answer = messagebox.askyesno('No ha guardado el proyecto.', 'Si sale ahora el proyecto seguirá existiendo pero no podrá acceder a él.\n¿Desea guardarlo?')
        if answer != True:
            sys.exit()
        else:
            guardar()
            if cajaTexto.winfo_manager() == 'pack':
                if cajaTexto.edit_modified():
                    answer = messagebox.askyesno('No ha guardado los cambios', 'Una actividad del proyecto ha recibido modificaciones, si sale ahora no serán guardados.\n¿Desea proceder de todos modos?')
                    if answer != True:
                        sys.exit()
            root.quit()
    else:
        sys.exit()
            
    if cajaTexto.winfo_manager() == 'pack':
        if cajaTexto.edit_modified():

            answer = messagebox.askyesno('No ha guardado los cambios', 'Una actividad del proyecto ha recibido modificaciones, si sale ahora no serán guardados.\n¿Desea proceder de todos modos?')

            if answer != True:
                sys.exit()
    else:
        sys.exit()

def vaciarProyecto():
    global cajaTextoLabel
    global nombreAbierto
    nombreAbierto = False

    global seleccion
    seleccion = False

    global nombreProyectoAbierto
    nombreProyectoAbierto = None
    global versionProyectoAbierto
    versionProyectoAbierto = None
    global actividadProyectoAbierto
    actividadProyectoAbierto = None
    global tagCount
    tagCount = []
    global cfont
    cfont = None
    global csize
    csize = None
    global IDCount
    IDCount = 0
    global guardado
    guardado = False

    cajaTexto.delete("1.0", END)
    cajaTexto.pack_forget()
    if cajaTextoLabel.winfo_manager() == 'pack':
        cajaTextoLabel.pack_forget()

    listaActividades.delete(0, END)
    cajaListaVersiones.delete(0, END)

    if ventanaHerramientas_ventanaGestor.winfo_manager() == 'pack':
        ventanaHerramientas_ventanaGestor.pack_forget()
        ventanaHerramientas_ventanaGestor_ventanaActividades_Label.grid_forget()
        ventanaHerramientas_ventanaGestor_ventanaVersiones_Label.grid_forget()

def crearProyecto(a, e, i, o):
    global cajaTextoLabel
    global nombreProyectoAbierto
    global versionProyectoAbierto
    global actividadProyectoAbierto
    global proyectoAutor
    global proyectoDesc
    global guardado
    if a == 0:

        if nombreProyectoAbierto == None:
            nombreProyectoAbierto = e

            b = p.crearProyecto(e)
            versionProyectoAbierto = p.nuevaVersion(e, ProyectoExiste= b)
            actividadProyectoAbierto = p.nuevaActividad(e, ProyectoExiste= b)
            g = p.buscarActividad(e)[0]
            proyectoAutor = i
            proyectoDesc  = o

            print(f'{versionProyectoAbierto}, {actividadProyectoAbierto}')

            if b == False:
                ventanaPrincipal.pack_forget()
                ventanaPrincipal.pack(pady=5, side="top", fill="both", expand=True)
            
                cajaTextoLabel = CTkLabel(ventanaPrincipal, width = 5, text = f"Proyecto {nombreProyectoAbierto}, Versión {versionProyectoAbierto}, Actividad {actividadProyectoAbierto}, Autor {proyectoAutor}", font=('', 24))

                gestion()
                gestion()
                cajaListaActividadesFrame.grid_forget()
                listaActividades.grid_forget()
                cajaListaActividadesFrame.grid(row = 2, column = 0, columnspan = 3, pady= 5)
                listaActividades.pack(fill = BOTH, expand = True)

                listaActividades.delete(0, END)
                cajaListaVersiones.delete(0, END)

                a = -1
                for elem in glob.glob(f'./projects/{nombreProyectoAbierto}/Versions/ver_{versionProyectoAbierto}/activities/*.txt'):
                    a += 1
                    listaActividades.insert('end', f'Actividad {a}')

                a = -1
                for subdirs in os.listdir(f'./projects/{nombreProyectoAbierto}/Versions/'):
                    if os.path.isdir(f'./projects/{nombreProyectoAbierto}/Versions/{subdirs}'):
                        a+=1
                        cajaListaVersiones.insert('end', f'Version {a}')


                cajaTexto.insert("1.0", g)
                ventanaNuevo.destroy()
                return False
        elif nombreProyectoAbierto != None:
            vaciarProyecto()
            verificarVacio(e, i, o)
        
    elif a == 1:
        
        listaActividades.delete(0, END)
        cajaListaVersiones.delete(0, END)

        versionProyectoAbierto = p.nuevaVersion(e)
        actividadProyectoAbierto = p.nuevaActividad(e)

        try:
            conexionAbrirProyecto = sqlite3.connect('./projects/projects.db')

            cursor = conexionAbrirProyecto.cursor()

            IDCursor = cursor.execute(f'''SELECT Project_ID FROM projects WHERE Project_Title = '{nombreProyectoAbierto}'; ''')
            IDCursorRow = IDCursor.fetchall()
            IDCount = IDCursorRow[0][0]
            cursor.execute(f'''UPDATE projects SET Project_Current_Version = '{versionProyectoAbierto}' WHERE Project_ID = {IDCount}''')

            conexionAbrirProyecto.commit()
            cursor.close()
        
        except sqlite3.Error as error:
            messagebox.showerror('Error', f'Error {error} ocurrido')

        finally:
            if conexionAbrirProyecto:
                conexionAbrirProyecto.close()


        a = -1
        for subdirs in os.listdir(f'./projects/{nombreProyectoAbierto}/Versions/'):
            if os.path.isdir(f'./projects/{nombreProyectoAbierto}/Versions/{subdirs}'):
                a+=1
                cajaListaVersiones.insert('end', f'Version {a}')        

        a = -1
        for elem in glob.glob(f'./projects/{nombreProyectoAbierto}/Versions/ver_{versionProyectoAbierto}/activities/*.txt'):
            a += 1
            listaActividades.insert('end', f'Actividad {a}')

        cajaTextoLabel.pack_forget()
        cajaTexto.pack_forget()

        cajaTextoLabel = CTkLabel(ventanaPrincipal, width = 5, text = f"Proyecto {nombreProyectoAbierto}, Versión {versionProyectoAbierto}, Actividad {actividadProyectoAbierto}, Autor {proyectoAutor}", font=('', 24))
        cajaTextoLabel.pack(fill= X, expand = False)

        cajaTexto.pack(fill = BOTH, expand = True)
        cajaTexto.delete("1.0", END)
        guardado = False

    elif a == 2:
            actividadProyectoAbierto = p.nuevaActividad(e)

            listaActividades.delete(0, END)
            a = -1
            for elem in glob.glob(f'./projects/{nombreProyectoAbierto}/Versions/ver_{versionProyectoAbierto}/activities/*.txt'):
                a += 1
                listaActividades.insert('end', f'Actividad {a}')

            ventanaPrincipal.pack_forget()
            cajaTextoLabel.pack_forget()
            cajaTexto.pack_forget()
            ventanaPrincipal.pack(pady=5, side="top", fill="both", expand=True)

            cajaTextoLabel = CTkLabel(ventanaPrincipal, width = 5, text = f"Proyecto {nombreProyectoAbierto}, Versión {versionProyectoAbierto}, Actividad {actividadProyectoAbierto}, Autor {proyectoAutor}", font=('', 24))
            cajaTextoLabel.pack(fill= X, expand = False)

            cajaTexto.pack(fill="both", expand = True)
            cajaTexto.delete("1.0", END)



            messagebox.showinfo('Éxito', f'La actividad: {actividadProyectoAbierto} ha sido creada con éxito.')

def borrarProyecto(e):
    if nombreProyectoAbierto != None:
        answer = messagebox.askquestion('Advertencia', 'Esta acción eliminará al proyecto totalmente y es irreversible.\n¿Desea proceder?')

        if answer == 'yes':
            try:
                conexionCerrarProyecto = sqlite3.connect('./projects/projects.db')

                cursor = conexionCerrarProyecto.cursor()
                IDCursor = cursor.execute(f'''SELECT Project_ID FROM projects WHERE Project_Title = '{nombreProyectoAbierto}'; ''')
                IDCursorRow = IDCursor.fetchall()
                IDCount = IDCursorRow[0][0]
                cursor.execute(f'''DELETE FROM projects WHERE Project_ID = {IDCount}''')
            
                with open(f'./projects/projects.txt', 'r') as file:
                    data = file.readlines()
                dataAux = []
                with open(f'./projects/projects.txt', 'w') as file:
                    for elem in range (len(data)-1, -1, -1):
                        if data[elem] == f'ID: {int(IDCount)-1}':
                            if int(IDCount)-1 == 0:
                                dataAux = data[4:]
                                file.truncate()
                                file.writelines(dataAux)
                                break
                            else:
                                dataAux = data[:elem-1]
                                dataAux = data[elem+4:]
                                file.truncate()
                                file.writelines(dataAux)
                                break

                shutil.rmtree(f'./projects/{nombreProyectoAbierto}')

                conexionCerrarProyecto.commit()
                cursor.close()

                vaciarProyecto()
                cajaTextoInitLabel.pack(fill= X, expand = False)
            except sqlite3.Error as error:
                messagebox.showerror('Error', f'Error {error} ocurrido')

            finally:
                if conexionCerrarProyecto:
                    conexionCerrarProyecto.close()
    else:
        messagebox.showerror('Error', 'No ha abierto un proyecto.')

def borrarProyectoExistenteF(e):
    global nombreProyectoAbierto
    global ventanaBorrar

    if e[0] == nombreProyectoAbierto:
        borrarProyecto(e)
        ventanaBorrar.destroy()
        return
    answer = messagebox.askquestion('Advertencia', 'Esta acción eliminará al proyecto totalmente y es irreversible.\n¿Desea proceder?')

    if answer == 'yes':
        try:
            conexionCerrarProyecto = sqlite3.connect('./projects/projects.db')

            cursor = conexionCerrarProyecto.cursor()
            IDCursor = cursor.execute(f'''SELECT Project_ID FROM projects WHERE Project_Title = '{e[0]}'; ''')
            IDCursorRow = IDCursor.fetchall()
            IDCount = IDCursorRow[0][0]
            cursor.execute(f'''DELETE FROM projects WHERE Project_ID = {IDCount}''')

            with open(f'./projects/projects.txt', 'r') as file:
                data = file.readlines()
            dataAux = []
            with open(f'./projects/projects.txt', 'w') as file:
                for elem in range (len(data)-1, -1, -1):
                    if data[elem] == f'ID: {int(IDCount)-1}':
                        if int(IDCount)-1 == 0:
                            dataAux = data[4:]
                            file.truncate()
                            file.writelines(dataAux)
                            break
                        else:
                            dataAux = data[:elem-1]
                            dataAux = data[elem+4:]
                            file.truncate()
                            file.writelines(dataAux)
                            break

            shutil.rmtree(f'./projects/{e[0]}')

            conexionCerrarProyecto.commit()
            cursor.close()
            messagebox.showinfo('Éxito', 'Proyecto borrado exitosamente.')


        except sqlite3.Error as error:
            messagebox.showinfo('Error1', f'Error {error} ocurrido', icon = "cancel")

        finally:
            if conexionCerrarProyecto:
                conexionCerrarProyecto.close()
                ventanaBorrar.destroy()
                return

def borrarProyectoExistente():
    global ventanaBorrar



    if os.path.isdir('./projects'):
        ventanaBorrar = CTkToplevel()
        ventanaBorrar.grab_set()
        ventanaBorrar.title("Borrar un proyecto existente.")
        ventanaBorrar.after(250, lambda: ventanaBorrar.iconbitmap('./img/icon.ico'))

        ventanaBorrar.geometry('400x600')
        ventanaBorrar.minsize(400, 600)
        ventanaBorrar.maxsize(1280, 800)
        try:
            conexionBorrarProyectos = sqlite3.connect('./projects/projects.db')

            cursor = conexionBorrarProyectos.cursor()

            listaProyectos = cursor.execute('''SELECT Project_Title FROM projects;''')
            listaProyectosRow = listaProyectos.fetchall()

            cursor.close()
        
        except sqlite3.Error as error:
            messagebox.showerror('Error', f'Error {error} ha ocurrido.')
        
        finally:
            if conexionBorrarProyectos:
                conexionBorrarProyectos.close()


        seleccionLabel = CTkLabel(ventanaBorrar, text=f"Selecciona un proyecto para eliminar.", font= ('Helvetica', 16))
        seleccionLabel.pack(fill = X)

        cajaListaSeleccionFrame = CTkFrame(ventanaBorrar, width= 200)
        cajaListaSeleccionFrame.pack(fill= Y, expand = True, pady=(5, 25))

        cajaListaSeleccion = CTkListbox(cajaListaSeleccionFrame, width = 200, command = borrarProyectoExistenteF)
        for projects in listaProyectosRow:
            cajaListaSeleccion.insert('end', projects )
            

        cajaListaSeleccion.pack(fill = Y, expand= True)




    else:
        messagebox.showerror('Error', 'No existen proyectos.')

def verificarVacio(e, i, o):
    
    if len(e) == 0 or len(i) == 0 or len(o) == 0:
        messagebox.showerror('Error', 'Los campos no pueden estar vacíos')
        ventanaNuevo.destroy()
        return True
    else:
        if crearProyecto(
            a = 0, 
            e = e, 
            i = i, 
            o = o
            ) == False:
                cajaTextoInitLabel.pack_forget()
                cajaTextoLabel.pack_forget()
                ventanaPrincipal.pack_forget()
                ventanaPrincipal.pack(pady=5, side="top", fill="both", expand=True)
                cajaTextoLabel.pack(fill= X, expand = False)
                cajaTexto.pack(fill="both", expand = True)
                try:
                    conexionCrearProyecto = sqlite3.connect(f'./projects/projects.db')

                    cursor = conexionCrearProyecto.cursor()

                    cursor.execute('''CREATE TABLE IF NOT EXISTS projects(
                        Project_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        Project_Title TEXT NOT NULL,
                        Project_Folderpath TEXT NOT NULL,
                        Project_Current_Version INTEGER NOT NUll);''')

                    cursor.execute(f'''INSERT INTO projects (Project_Title, Project_Folderpath, Project_Current_Version) VALUES(
                        '{e}','./projects/{e}', '{versionProyectoAbierto}');''')
                    

                    conexionCrearProyecto.commit()
                    cursor.close()

                except sqlite3.Error as error:
                    messagebox.showerror('Error', f'Error {error} ocurrido')

                finally:

                    if conexionCrearProyecto:
                        conexionCrearProyecto.close()


        else:
            ventanaNuevo.destroy()

def obtenerTags(inicio, final):
    global cfont
    global csize

    index = inicio
    tags = []
    currTag = None
    data = []
    i = 0
    while cajaTexto.compare(index, '<=', final):
        tags.append(cajaTexto.tag_names(index))
        if len(tags) > 0:
            
            if len(data) >= 0: 
                if cajaTexto.tag_names(index) != currTag:
                    data.append(f'{tags[i]}, {index}\n')

            currTag = tags[i]
        index = cajaTexto.index(f'{index}+1c')
        i +=1

    if cfont == None:
        cfont = 'Helvetica'
    if csize == None:
        csize = '11'

    with open(f'./projects/{nombreProyectoAbierto}/Versions/ver_{versionProyectoAbierto}/act_{actividadProyectoAbierto}_tags.txt', 'w') as file:
        file.truncate()
        file.write(f'Folderpath: ./projects/{nombreProyectoAbierto}/Versions/ver_{versionProyectoAbierto}/activities/Actividad {actividadProyectoAbierto}.txt\n')
        file.write(f'Font: {cfont}\n')
        file.write(f'Size: {csize}\n')
        file.writelines(data)

# 1. Crear nuevo archivo

def nuevoArchivo():
    # Borrar el texto previamente escrito y actualizar el título y la barra de estado
    global nombreProyectoAbierto
    global versionProyectoAbierto
    global actividadProyectoAbierto
    global guardado

    if nombreProyectoAbierto != None and guardado != True:
        answer = messagebox.askyesno('No ha guardado el proyecto.', 'Si crea un proyecto nuevo sin guardar el actual, el proyecto seguirá existiendo pero no podrá acceder a él.\n¿Desea guardarlo?')
        if answer != True:
            pass
        else:
            if cajaTexto.winfo_manager() == 'pack':
                if cajaTexto.edit_modified():

                    answer = messagebox.askyesno('No ha guardado los cambios', 'Una actividad del proyecto ha recibido modificaciones, si sale ahora no serán guardados.\n¿Desea proceder de todos modos?')

                    if answer != True:
                        return
            guardar()
            
    if cajaTexto.winfo_manager() == 'pack':
        if cajaTexto.edit_modified():

            answer = messagebox.askyesno('No ha guardado los cambios', 'Una actividad del proyecto ha recibido modificaciones, si sale ahora no serán guardados.\n¿Desea proceder de todos modos?')

            if answer != True:
                return
            

    root.title("Sin Título - Odyssey Journal 1.1.0")
    barraEstado.configure(text="Nuevo Archivo        ")

    global ventanaNuevo
    ventanaNuevo = CTkToplevel(root)
    ventanaNuevo.grab_set()
    ventanaNuevo.title('Crea un nuevo proyecto')
    ventanaNuevo.after(250, lambda: ventanaNuevo.iconbitmap('./img/icon.ico'))
    ventanaNuevo.geometry('640x320')

    ventanaNuevo.minsize(640, 320)
    ventanaNuevo.maxsize(1280, 800)


    labelTitulo = CTkLabel(ventanaNuevo, text= "Título:   ", font=('Helvetica', 16))
    labelTitulo.grid(row = 0, column = 0, pady = 20)

    cajaTitulo = Text(ventanaNuevo, width = 30, height = 1, font= ('Helvetica', 16))
    cajaTitulo.grid(row= 0, column = 1, pady = 20, padx = 10)
    labelAutor = CTkLabel(ventanaNuevo, text= "Autor:   ", font=('Helvetica', 16))
    labelAutor.grid(row= 1, column = 0)

    cajaAutor = Text(ventanaNuevo, width = 30, height = 1, font= ('Helvetica', 16))
    cajaAutor.grid(row= 1, column = 1, padx = 10)

    labelDescripcion = CTkLabel(ventanaNuevo, text= "Descripción:", font=('Helvetica', 16))
    labelDescripcion.grid(row= 2, column = 1, padx = 10)

    cajaDescripcion = Text(ventanaNuevo, width = 30, height = 5, font= ('Helvetica', 16))
    cajaDescripcion.grid(row= 3, column = 0, columnspan=3, padx = 10)


    botonAceptar = CTkButton(ventanaNuevo, 
    width = 80, 
    height = 6, 
    text = "Aceptar", 
    font=('Helvetica', 14),
    command = lambda: verificarVacio(e = cajaTitulo.get("1.0", "end-1c"), 
    i = cajaAutor.get("1.0", "end-1c"), 
    o = cajaDescripcion.get("1.0", "end-1c")  
    )
    )

    botonAceptar.grid(row = 4, column = 3, sticky = S)

    botonCancelar = CTkButton(ventanaNuevo, width = 80, height = 6, font=('',14),text= "Cancelar", command = ventanaNuevo.destroy)
    botonCancelar.grid(row = 4, column = 2)

    global nombreAbierto
    nombreAbierto = False

# 1. Abrir archivo

def abrirArchivo():
    global nombreProyectoAbierto
    global versionProyectoAbierto
    global actividadProyectoAbierto
    global cajaTextoLabel
    global proyectoDesc
    global proyectoAutor
    global guardado
    # Borrar el texto previamente escrito
    # Agarrar archivo de texto y cambiar el título y la barra de estado

    if nombreProyectoAbierto != None and guardado != True:
        answer = messagebox.askyesno('No ha guardado el proyecto.', 'Si crea un proyecto nuevo sin guardar el actual, el proyecto seguirá existiendo pero no podrá acceder a él.\n¿Desea guardarlo?')
        if answer != True:
            pass
        else:
            if cajaTexto.winfo_manager() == 'pack':
                if cajaTexto.edit_modified():

                    answer = messagebox.askyesno('No ha guardado los cambios', 'Una actividad del proyecto ha recibido modificaciones, si sale ahora no serán guardados.\n¿Desea proceder de todos modos?')

                    if answer != True:
                        return
            guardar()
            
    if cajaTexto.winfo_manager() == 'pack':
        if cajaTexto.edit_modified():

            answer = messagebox.askyesno('No ha guardado los cambios', 'Una actividad del proyecto ha recibido modificaciones, si sale ahora no serán guardados.\n¿Desea proceder de todos modos?')

            if answer != True:
                return

    directorioInicial = os.path.expanduser('~')
    archivoTexto = filedialog.askopenfilename(initialdir= directorioInicial, title = "Abrir nuevo...", filetypes= [("Archivo de Proyecto", "*.odpr")])
    if archivoTexto:
        if nombreProyectoAbierto != None:
            vaciarProyecto()
        else:
            cajaTextoInitLabel.pack_forget()
        global nombreAbierto
        with open(archivoTexto, 'r') as file:
            data = file.readlines()
        proyectoAutor = ''
        for elem in range (7, len(data[3])):
            proyectoAutor += ''+data[3][elem]

        proyectoDesc = ''
        for elem in range(7, len(data)-1):
            proyectoDesc += ''+data[elem]
        
        IDStr = ''
        for elem in data[0]:
            if elem.isdigit():
                IDStr += ''+elem
        try:
            conexionAbrirProyecto = sqlite3.connect('./projects/projects.db')

            cursor = conexionAbrirProyecto.cursor()

            TitleCursor = cursor.execute(f'''SELECT Project_Title, Project_Current_Version FROM projects WHERE Project_ID = '{int(IDStr)}'; ''')
            TitleCursorRow = TitleCursor.fetchall()
            Title = TitleCursorRow[0][0]
            VersionCursor = TitleCursorRow[0][1]

            conexionAbrirProyecto.commit()
            cursor.close()
        
        except sqlite3.Error as error:
            messagebox.showerror('Error', f'Error {error} ocurrido')

        finally:
            if conexionAbrirProyecto:
                conexionAbrirProyecto.close()

        nombreProyectoAbierto = Title
        versionProyectoAbierto = VersionCursor
        actividadProyectoAbierto = 0

        cajaTextoLabel = CTkLabel(ventanaPrincipal, width = 5, text = f"Proyecto {nombreProyectoAbierto}, Versión {versionProyectoAbierto}, Actividad 0, Autor {proyectoAutor}", font=('', 24))
        cajaTextoLabel.pack(fill= X, expand = False)

        cajaTexto.pack(fill="both", expand = True)

        g = p.buscarActividadEspecifica(nombreProyectoAbierto, 'Actividad 0', version = versionProyectoAbierto)[0]

        listaActividades.delete(0, END)
        a = -1
        for elem in glob.glob(f'./projects/{nombreProyectoAbierto}/Versions/ver_{versionProyectoAbierto}/activities/*.txt'):
            a += 1
            listaActividades.insert('end', f'Actividad {a}')

        a = -1
        for subdirs in os.listdir(f'./projects/{nombreProyectoAbierto}/Versions/'):
            if os.path.isdir(f'./projects/{nombreProyectoAbierto}/Versions/{subdirs}'):
                a+=1
                cajaListaVersiones.insert('end', f'Version {a}')



        nombre = archivoTexto
        barraEstado.configure(text=f"{nombre}        ")
        titulo =f'{nombreProyectoAbierto} - Odyssey Journal 1.1.0'
        root.title(titulo)

    # Abrir archivo

        cajaTexto.delete("1.0", END)
        cajaTexto.insert("1.0", g)

        if os.path.isfile(f'./projects/{nombreProyectoAbierto}/Versions/ver_{versionProyectoAbierto}/act_{actividadProyectoAbierto}_tags.txt'):
            with open(f'./projects/{nombreProyectoAbierto}/Versions/ver_{versionProyectoAbierto}/act_{actividadProyectoAbierto}_tags.txt', 'r') as file:
                data = file.readlines()
            dataAux = ''
            posAux = ''
            posEnd = ''
            fontAux = ''
            sizeAux = ''

            for lines in range(1, 3):
                for elem in range(5, len(data[lines])):
                    if data[lines][elem].isalpha():
                        fontAux += ''+data[lines][elem]

                    if data[lines][elem].isdigit():
                        sizeAux += ''+data[lines][elem]

            cfont = fontAux
            csize = int(sizeAux)
            fuenteCajaTexto.configure(family = cfont, size = csize)

            for lines in range (3, len(data)-1):

                for elem in data[lines]:
                    if elem.isalpha():
                        dataAux += ''+elem
                    if elem.isdigit() or elem == '.':
                        posAux += ''+elem
                for elemV in data[lines+1]:
                    if elemV.isdigit() or elemV == '.':
                        posEnd += ''+elemV
                if 'sel' in dataAux:                        
                    cajaTexto.tag_add(f'{dataAux[3:]}', f'{posAux}', f'{posEnd}')
                    dataAux = ''
                    posAux = ''
                    posEnd = ''
                    fontAux = ''
                    sizeAux = ''
                else:
                    cajaTexto.tag_add(f'{dataAux}', f'{posAux}', f'{posEnd}')
                    dataAux = ''
                    posAux = ''
                    posEnd = ''
                    fontAux = ''
                    sizeAux = ''


# 3. Guardar Como
def guardarComo(e = False):
    global nombreAbierto
    global guardado

    if e == False and cajaTexto.winfo_manager() == 'pack':
        if cajaTexto.edit_modified():

            answer = messagebox.askyesno('No ha guardado los cambios', 'Una actividad del proyecto ha recibido modificaciones, guardar el proyecto como archivo no garantiza que se guarden las actividades, le recomendamos guardar primero las actividades.\n¿Desea proceder de todos modos?')

            if answer != True:
                return

    archivoTexto = filedialog.asksaveasfilename(defaultextension=".*", initialdir= os.path.expanduser('~'), title = 'Guardar cómo...', filetypes= [("Archivo de Proyecto", "*.odpr")])
    if archivoTexto:
        # Actualizar el título y la barra de status
        nombre = archivoTexto
        nombreAbierto = nombre
        barraEstado.configure(text=f"Guardado en: {nombre}        ")

        root.title(f'{nombreProyectoAbierto} - Odyssey Journal 1.1.0')
        # Guardar el archivo
        try:
            conexionAbrirProyecto = sqlite3.connect('./projects/projects.db')

            cursor = conexionAbrirProyecto.cursor()

            IDCursor = cursor.execute(f'''SELECT Project_ID, Project_Current_Version FROM projects WHERE Project_Title = '{nombreProyectoAbierto}'; ''')
            IDCursorRow = IDCursor.fetchall()
            IDCount = IDCursorRow[0][0]
            VersionCursorRow = IDCursorRow[0][1]

            conexionAbrirProyecto.commit()
            cursor.close()

            guardado = True
        
        except sqlite3.Error as error:
            messagebox.showerror('Error1', f'Error {error} ocurrido')

        finally:
            if conexionAbrirProyecto:
                conexionAbrirProyecto.close()

        archivoTexto = open(archivoTexto, 'w')
        archivoTexto.write(f'ID: {IDCount}\n')
        archivoTexto.write(f'Ruta: ./projects/{nombreProyectoAbierto}/\n')
        archivoTexto.write(f'Titulo: {nombreProyectoAbierto}\n')
        archivoTexto.write(f'Autor: {proyectoAutor}\n')
        archivoTexto.write(f'Version: {VersionCursorRow}\n')
        archivoTexto.write(f'Descripción:\n{proyectoDesc}\n')
        archivoTexto.close()

# 4. Guardar

def guardar():
    global nombreAbierto
    global guardado

    if cajaTexto.winfo_manager() == 'pack':
        if cajaTexto.edit_modified():

            answer = messagebox.askyesno('No ha guardado los cambios', 'Una actividad del proyecto ha recibido modificaciones, guardar el proyecto como archivo no garantiza que se guarden las actividades, le recomendamos guardar primero las actividades.\n¿Desea proceder de todos modos?')

            if answer != True:
                return

    if nombreAbierto:
        dataAux = []
        dataAux_Desc = []
        with open(nombreAbierto, 'r') as file:
            data = file.readlines()

        for elem in range(0, 3):
            dataAux.append(data[elem])

        for elem in range (5, len(data)):
            dataAux_Desc.append(data[elem])

        with open(nombreAbierto, 'w') as file:
            file.truncate()
            file.writelines(dataAux)
            file.write(f'Versión: {versionProyectoAbierto}\n')
            file.writelines(dataAux_Desc)
        nombre = nombreAbierto
        barraEstado.configure(text=f"Guardado en: {nombre}        ")
        guardado = True
    else:
        guardarComo(e = True)

# 5. Copiar, Cortar y Pegar

def cortar(e):
    global seleccion


    if e:
        seleccion= root.clipboard_get()
        cajaTexto.delete('sel.first', 'sel.last')


    else:

        if cajaTexto.selection_get():
            root.clipboard_clear()
            seleccion = cajaTexto.selection_get()
            root.clipboard_append(seleccion)
            cajaTexto.delete('sel.first', 'sel.last')

def copiar(e):
    global seleccion

    if e:
        seleccion = root.clipboard_get()

    else:
        if cajaTexto.selection_get():
            root.clipboard_clear()
            seleccion = cajaTexto.selection_get()
            root.clipboard_append(seleccion)

def pegar(e):
    global seleccion

    if e:
        seleccion = root.clipboard_get()
    else:
        if seleccion:
            posicion = cajaTexto.index(INSERT)
            cajaTexto.insert(posicion, seleccion)

# 6. Llamar al navegador predeterminado al hacer clic en un link.

def llamarNavegador(url):
    webbrowser.open_new(url)

# 7. Mostrar información sobre el autor

def autorInfo(e):
    # Ventana de información de contacto y créditos al autor.

    ventanaAutor = CTkToplevel()
    ventanaAutor.title("Información y Contacto")
    ventanaAutor.after(250, lambda: ventanaAutor.iconbitmap('./img/icon.ico'))

    ventanaAutor.geometry('300x200')
    ventanaAutor.minsize(300, 200)
    ventanaAutor.maxsize(1280, 800)

    infoAutor = CTkLabel(ventanaAutor, text="""
    Autor: Francisco García\n
    Correo: franciscojotagarciaefe@gmail.com\n
    Repositorio:""")
    infoAutor_Link = CTkLabel(ventanaAutor, text="github.com/FranciscoJGarciaF/Proyecto-Pepino", fg_color= '#3434f7', cursor="hand2")

    infoAutor.pack()
    infoAutor_Link.pack()
    infoAutor_Link.bind("<Button-1>", lambda: llamarNavegador("github.com/FranciscoJGarciaF/Proyecto-Pepino"))
    infoAutor_extra = CTkLabel(ventanaAutor, text="\n\n¡Gracias por usar!")
    infoAutor_extra.pack()

def verDesc():
    if proyectoDesc != None:
        ventanaDescripcion = CTkToplevel(root)
        ventanaDescripcion.grab_set()
        ventanaDescripcion.title("Descripción del Proyecto")
        ventanaDescripcion.after(250, lambda: ventanaDescripcion.iconbitmap('./img/icon.ico'))

        ventanaDescripcion.geometry('300x200')
        ventanaDescripcion.minsize(300, 200)
        ventanaDescripcion.maxsize(1280, 800)

        infoAutor = CTkLabel(ventanaDescripcion, text=f"{proyectoDesc}")

        infoAutor.pack()
    else:
        messagebox.showerror('Error', 'No ha seleccionado un proyecto.')

# 8. Maximizar o Minimizar la pantalla

def maxOmin(estado):


    if estado == 0:
        root.wm_state("iconic")
    else:
        root.wm_state("zoomed")

# 9. Negrita y Cursiva

def fuente(e):

    fuenteNegrita = font.Font(cajaTexto, cajaTexto.cget("font"))
    fuenteNegrita.configure(weight="bold")

    fuenteCursiva = font.Font(cajaTexto, cajaTexto.cget("font"))
    fuenteCursiva.configure(slant="italic")

    fuenteSubrayado = font.Font(cajaTexto, cajaTexto.cget("font"))
    fuenteSubrayado.configure(underline = 1)

    fuenteSobrerayado = font.Font(cajaTexto, cajaTexto.cget("font"))
    fuenteSobrerayado.configure(overstrike= 1)

    fuenteNegritaYCursiva = font.Font(cajaTexto, cajaTexto.cget("font"))
    fuenteNegritaYCursiva.configure(weight= "bold", slant = "italic")

    fuenteNegritaYSubrayada = font.Font(cajaTexto, cajaTexto.cget("font"))
    fuenteNegritaYSubrayada.configure(weight= "bold", underline=1)

    fuenteNegritaYSobrerayada = font.Font(cajaTexto, cajaTexto.cget("font"))
    fuenteNegritaYSobrerayada.configure(weight = "bold", overstrike= 1)

    fuenteCursivaYSubrayada = font.Font(cajaTexto, cajaTexto.cget("font"))
    fuenteCursivaYSubrayada.configure(slant="italic", underline=1)

    fuenteCursivaYSobrerayada = font.Font(cajaTexto, cajaTexto.cget("font"))
    fuenteCursivaYSobrerayada.configure(slant="italic", overstrike= 1)

    fuenteSubrayadaYSobrerayada = font.Font(cajaTexto, cajaTexto.cget("font"))
    fuenteSubrayadaYSobrerayada.configure(underline= 1, overstrike= 1)

    fuenteNegritaCursivaYSubrayada = font.Font(cajaTexto, cajaTexto.cget("font"))
    fuenteNegritaCursivaYSubrayada.configure(weight= "bold", slant = "italic", underline= 1)

    fuenteNegritaCursivaYSobrerayada = font.Font(cajaTexto, cajaTexto.cget("font"))
    fuenteNegritaCursivaYSobrerayada.configure(weight= "bold", slant = "italic", overstrike= 1)

    fuenteSubrayadaNegritaYSobrerayada = font.Font(cajaTexto, cajaTexto.cget("font"))
    fuenteSubrayadaNegritaYSobrerayada.configure(weight= "bold", underline= 1, overstrike= 1)

    fuenteSubrayadaCursivaYSobrerayada = font.Font(cajaTexto, cajaTexto.cget("font"))
    fuenteSubrayadaCursivaYSobrerayada.configure(slant = "italic", underline = 1, overstrike = 1)

    fuenteNegritaCursivaSubrayadaYSobrerayada = font.Font(cajaTexto, cajaTexto.cget("font"))
    fuenteNegritaCursivaSubrayadaYSobrerayada.configure(weight= "bold", slant = "italic", underline = 1, overstrike = 1)


    cajaTexto.tag_configure("negrita", font = fuenteNegrita)
    cajaTexto.tag_configure("cursiva", font = fuenteCursiva)
    cajaTexto.tag_configure("subrayada", font = fuenteSubrayado)
    cajaTexto.tag_configure("sobrerayada", font = fuenteSobrerayado)

    cajaTexto.tag_configure("negritaYcursiva", font = fuenteNegritaYCursiva)
    cajaTexto.tag_configure("negritaYsubrayada", font = fuenteNegritaYSubrayada)
    cajaTexto.tag_configure("negritaYsobrerayada", font = fuenteNegritaYSobrerayada)

    cajaTexto.tag_configure("cursivaYsubrayada", font = fuenteCursivaYSubrayada)
    cajaTexto.tag_configure("cursivaYsobrerayada", font = fuenteCursivaYSobrerayada)

    cajaTexto.tag_configure("subrayadaYsobrerayada", font = fuenteSubrayadaYSobrerayada)

    cajaTexto.tag_configure("negritaCursivaYsubrayada", font = fuenteNegritaCursivaYSubrayada)
    cajaTexto.tag_configure("negritaCursivaYsobrerayada", font = fuenteNegritaCursivaYSobrerayada)

    cajaTexto.tag_configure("subrayadaNegritaYsobrerayada", font = fuenteSubrayadaNegritaYSobrerayada)
    cajaTexto.tag_configure("subrayadaCursivaYsobrerayada", font = fuenteSubrayadaCursivaYSobrerayada)

    cajaTexto.tag_configure("negritaCursivaSubrayadaYsobrerayada", font = fuenteNegritaCursivaSubrayadaYSobrerayada)
    


    etiquetasActuales = cajaTexto.tag_names("sel.first")
    
    match e:
        case 0:
            if "negritaYcursiva" in etiquetasActuales:
                cajaTexto.tag_remove("negritaYcursiva", "sel.first", "sel.last")
                cajaTexto.tag_add("cursiva", "sel.first", "sel.last")
            
            elif "negritaYsubrayada" in etiquetasActuales:
                cajaTexto.tag_remove("negritaYsubrayada", "sel.first", "sel.last")
                cajaTexto.tag_add("subrayada", "sel.first", "sel.last")

            elif "negritaYsobrerayada" in etiquetasActuales:
                cajaTexto.tag_remove("negritaYsobrerayada", "sel.first", "sel.last")
                cajaTexto.tag_add("sobrerayada", "sel.first", "sel.last")

            elif "subrayadaNegritaYsobrerayada" in etiquetasActuales:
                cajaTexto.tag_remove("subrayadaNegritaYsobrerayada", "sel.first", "sel.last")
                cajaTexto.tag_add("subrayadaYsobrerayada", "sel.first", "sel.last")

            elif "negritaCursivaYsubrayada" in etiquetasActuales:
                cajaTexto.tag_remove("negritaCursivaYsubrayada", "sel.first", "sel.last")
                cajaTexto.tag_add("cursivaYsubrayada", "sel.first", "sel.last")

            elif "negritaCursivaYsobrerayada" in etiquetasActuales:
                cajaTexto.tag_remove("negritaCursivaYsobrerayada", "sel.first", "sel.last")
                cajaTexto.tag_add("cursivaYsobrerayada", "sel.first", "sel.last")

            elif "negritaCursivaSubrayadaYsobrerayada" in etiquetasActuales:
                cajaTexto.tag_remove("negritaCursivaSubrayadaYsobrerayada", "sel.first", "sel.last")
                cajaTexto.tag_add("subrayadaCursivaYsobrerayada", "sel.first", "sel.last")


            elif "negrita" in etiquetasActuales:
                cajaTexto.tag_remove("negrita", "sel.first", "sel.last")
            elif "negrita" not in etiquetasActuales:
                if "cursiva" in etiquetasActuales:
                    cajaTexto.tag_remove("cursiva", "sel.first", "sel.last")
                    cajaTexto.tag_add("negritaYcursiva", "sel.first", "sel.last")

                elif "subrayada" in etiquetasActuales:
                    cajaTexto.tag_remove("subrayada", "sel.first", "sel.last")
                    cajaTexto.tag_add("negritaYsubrayada", "sel.first", "sel.last")

                elif "sobrerayada" in etiquetasActuales:
                    cajaTexto.tag_remove("sobrerayada", "sel.first", "sel.last")
                    cajaTexto.tag_add("negritaYsobrerayada", "sel.first", "sel.last")
                
                elif "subrayadaYsobrerayada" in etiquetasActuales:
                    cajaTexto.tag_remove("subrayadaYsobrerayada", "sel.first", "sel.last")
                    cajaTexto.tag_add("subrayadaNegritaYsobrerayada", "sel.first", "sel.last")

                elif "cursivaYsubrayada" in etiquetasActuales:
                    cajaTexto.tag_remove("cursivaYsubrayada", "sel.first", "sel.last")
                    cajaTexto.tag_add("negritaCursivaYsubrayada", "sel.first", "sel.last")

                elif "cursivaYsobrerayada" in etiquetasActuales:
                    cajaTexto.tag_remove("cursivaYsobrerayada", "sel.first", "sel.last")
                    cajaTexto.tag_add("negritaCursivaYsobrerayada")

                elif "subrayadaCursivaYsobrerayada" in etiquetasActuales:
                    cajaTexto.tag_remove("subrayadaCursivaYsobrerayada", "sel.first", "sel.last")
                    cajaTexto.tag_add("negritaCursivaSubrayadaYsobrerayada", "sel.first", "sel.last")

                else:
                    cajaTexto.tag_add("negrita", "sel.first", "sel.last")

        case 1:
            if "negritaYcursiva" in etiquetasActuales:
                cajaTexto.tag_remove("negritaYcursiva", "sel.first", "sel.last")
                cajaTexto.tag_add("negrita", "sel.first", "sel.last")

            elif "cursivaYsubrayada" in etiquetasActuales:
                cajaTexto.tag_remove("cursivaYsubrayada", "sel.first", "sel.last")
                cajaTexto.tag_add("subrayada", "sel.first", "sel.last")

            elif "cursivaYsobrerayada" in etiquetasActuales:
                cajaTexto.tag_remove("cursivaYsobrerayada", "sel.first", "sel.last")
                cajaTexto.tag_add("sobrerayada", "sel.first", "sel.last")

            elif "subrayadaCursivaYsobrerayada" in etiquetasActuales:
                cajaTexto.tag_remove("subrayadaCursivaYsobrerayada", "sel.first", "sel.last")
                cajaTexto.tag_add("subrayadaYsobrerayada", "sel.first", "sel.last")

            elif "negritaCursivaYsubrayada" in etiquetasActuales:
                cajaTexto.tag_remove("negritaCursivaYsubrayada", "sel.first", "sel.last")
                cajaTexto.tag_add("negritaYsubrayada", "sel.first", "sel.last")

            elif "negritaCursivaYsobrerayada" in etiquetasActuales:
                cajaTexto.tag_remove("negritaCursivaYsobrerayada", "sel.first", "sel.last")
                cajaTexto.tag_add("negritaYsobrerayada", "sel.first", "sel.last")

            elif "negritaCursivaSubrayadaYsobrerayada" in etiquetasActuales:
                cajaTexto.tag_remove("negritaCursivaSubrayadaYsobrerayada", "sel.first", "sel.last")
                cajaTexto.tag_add("subrayadaNegritaYsobrerayada", "sel.first", "sel.last")


            elif "cursiva" in etiquetasActuales:
                cajaTexto.tag_remove("cursiva", "sel.first", "sel.last")

            elif "cursiva" not in etiquetasActuales:
                if "negrita" in etiquetasActuales:
                    cajaTexto.tag_remove("negrita", "sel.first", "sel.last")
                    cajaTexto.tag_remove("cursiva", "sel.first", "sel.last")
                    cajaTexto.tag_add("negritaYcursiva", "sel.first", "sel.last")
                
                elif "subrayada" in etiquetasActuales:
                    cajaTexto.tag_remove("subrayada", "sel.first", "sel.last")
                    cajaTexto.tag_add("cursivaYsubrayada", "sel.first", "sel.last")

                elif "sobrerayada" in etiquetasActuales:
                    cajaTexto.tag_remove("sobrerayada", "sel.first", "sel.last")
                    cajaTexto.tag_add("cursivaYsobrerayada", "sel.first", "sel.last")
                
                elif "subrayadaYsobrerayada" in etiquetasActuales:
                    cajaTexto.tag_remove("subrayadaYsobrerayada", "sel.first", "sel.last")
                    cajaTexto.tag_add("subrayadaCursivaYsobrerayada", "sel.first", "sel.last")

                elif "negritaYsubrayada" in etiquetasActuales:
                    cajaTexto.tag_remove("negritaYsubrayada", "sel.first", "sel.last")
                    cajaTexto.tag_add("negritaCursivaYsubrayada", "sel.first", "sel.last")

                elif "negritaYsobrerayada" in etiquetasActuales:
                    cajaTexto.tag_remove("negritaYsobrerayada", "sel.first", "sel.last")
                    cajaTexto.tag_add("negritaCursivaYsobrerayada")

                elif "subrayadaNegritaYsobrerayada" in etiquetasActuales:
                    cajaTexto.tag_remove("subrayadaNegritaYsobrerayada", "sel.first", "sel.last")
                    cajaTexto.tag_add("negritaCursivaSubrayadaYsobrerayada", "sel.first", "sel.last")


                else:
                    cajaTexto.tag_add("cursiva", "sel.first", "sel.last")           

        case 2: 

            if "subrayadaYsobrerayada" in etiquetasActuales:
                cajaTexto.tag_remove("subrayadaYsobrerayada", "sel.first", "sel.last")
                cajaTexto.tag_add("sobrerayada", "sel.first", "sel.last")

            elif "negritaYsubrayada" in etiquetasActuales:
                cajaTexto.tag_remove("negritaYsubrayada", "sel.first", "sel.last")
                cajaTexto.tag_add("negrita", "sel.first", "sel.last")

            elif "cursivaYsubrayada" in etiquetasActuales:
                cajaTexto.tag_remove("cursivaYsubrayada", "sel.first", "sel.last")
                cajaTexto.tag_add("cursiva", "sel.first", "sel.last")

            elif "negritaCursivaYsubrayada" in etiquetasActuales:
                cajaTexto.tag_remove("negritaCursivaYsubrayada", "sel.first", "sel.last")
                cajaTexto.tag_add("negritaYcursiva", "sel.first", "sel.last")

            elif "negritaCursivaSubrayadaYsobrerayada" in etiquetasActuales:
                cajaTexto.tag_remove("negritaCursivaSubrayadaYsobrerayada", "sel.first", "sel.last")
                cajaTexto.tag_add("negritaCursivaYsobrerayada", "sel.first", "sel.last")


            elif "subrayada" in etiquetasActuales:
                cajaTexto.tag_remove("subrayada", "sel.first", "sel.last")

            elif "subrayada" not in etiquetasActuales:
                if "negrita" in etiquetasActuales:
                    cajaTexto.tag_remove("negrita", "sel.first", "sel.last")
                    cajaTexto.tag_remove("subrayada", "sel.first", "sel.last")
                    cajaTexto.tag_add("negritaYsubrayada", "sel.first", "sel.last")
                
                elif "cursiva" in etiquetasActuales:
                    cajaTexto.tag_remove("cursiva", "sel.first", "sel.last")
                    cajaTexto.tag_add("cursivaYsubrayada", "sel.first", "sel.last")
                    
                elif "negritaYcursiva" in etiquetasActuales:
                    cajaTexto.tag_remove("negritaYcursiva", "sel.first", "sel.last")
                    cajaTexto.tag_add("negritaCursivaYsubrayada", "sel.first", "sel.last")

                elif "sobrerayada" in etiquetasActuales:
                    cajaTexto.tag_remove("sobrerayada", "sel.first", "sel.last")
                    cajaTexto.tag_add("subrayadaYsobrerayada", "sel.first", "sel.last")
                
                elif "negritaYsobrerayada" in etiquetasActuales:
                    cajaTexto.tag_remove("negritaYsobrerayada", "sel.first", "sel.last")
                    cajaTexto.tag_add("negritaYsubrayada", "sel.first", "sel.last")

                elif "cursivaYsobrerayada" in etiquetasActuales:
                    cajaTexto.tag_remove("cursivaYsobrerayada", "sel.first", "sel.last")
                    cajaTexto.tag_add("subrayadaCursivaYsobrerayada", "sel.first", "sel.last")

                elif "negritaCursivaYsobrerayada" in etiquetasActuales:
                    cajaTexto.tag_remove("negritaCursivaYsobrerayada", "sel.first", "sel.last")
                    cajaTexto.tag_add("negritaCursivaSubrayadaYsobrerayada", "sel.first", "sel.last")
                else:
                    cajaTexto.tag_add("subrayada", "sel.first", "sel.last")           

        case 3:

            if "subrayadaYsobrerayada" in etiquetasActuales:
                cajaTexto.tag_remove("subrayadaYsobrerayada", "sel.first", "sel.last")
                cajaTexto.tag_add("subrayada", "sel.first", "sel.last")

            elif "negritaYsobrerayada" in etiquetasActuales:
                cajaTexto.tag_remove("negritaYsobrerayada", "sel.first", "sel.last")
                cajaTexto.tag_add("negrita", "sel.first", "sel.last")

            elif "cursivaYsobrerayada" in etiquetasActuales:
                cajaTexto.tag_remove("cursivaYsobrerayada", "sel.first", "sel.last")
                cajaTexto.tag_add("cursiva", "sel.first", "sel.last")

            elif "negritaCursivaYsobrerayada" in etiquetasActuales:
                cajaTexto.tag_remove("negritaCursivaYsobrerayada", "sel.first", "sel.last")
                cajaTexto.tag_add("negritaYcursiva", "sel.first", "sel.last")

            elif "negritaCursivaSubrayadaYsobrerayada" in etiquetasActuales:
                cajaTexto.tag_remove("negritaCursivaSubrayadaYsobrerayada", "sel.first", "sel.last")
                cajaTexto.tag_add("negritaCursivaYsubrayada", "sel.first", "sel.last")


            elif "sobrerayada" in etiquetasActuales:
                cajaTexto.tag_remove("sobrerayada", "sel.first", "sel.last")

            elif "sobrerayada" not in etiquetasActuales:
                if "negrita" in etiquetasActuales:
                    cajaTexto.tag_remove("negrita", "sel.first", "sel.last")
                    cajaTexto.tag_remove("sobrerayada", "sel.first", "sel.last")
                    cajaTexto.tag_add("negritaYsobrerayada", "sel.first", "sel.last")
                
                elif "cursiva" in etiquetasActuales:
                    cajaTexto.tag_remove("cursiva", "sel.first", "sel.last")
                    cajaTexto.tag_add("cursivaYsobrerayada", "sel.first", "sel.last")
                    
                elif "negritaYcursiva" in etiquetasActuales:
                    cajaTexto.tag_remove("negritaYcursiva", "sel.first", "sel.last")
                    cajaTexto.tag_add("negritaCursivaYsobrerayada", "sel.first", "sel.last")

                elif "subrayada" in etiquetasActuales:
                    cajaTexto.tag_remove("subrayada", "sel.first", "sel.last")
                    cajaTexto.tag_add("subrayadaYsobrerayada", "sel.first", "sel.last")
                
                elif "negritaYsubrayada" in etiquetasActuales:
                    cajaTexto.tag_remove("negritaYsubrayada", "sel.first", "sel.last")
                    cajaTexto.tag_add("negritaYsobrerayada", "sel.first", "sel.last")

                elif "cursivaYsubrayada" in etiquetasActuales:
                    cajaTexto.tag_remove("cursivaYsubrayada", "sel.first", "sel.last")
                    cajaTexto.tag_add("subrayadaCursivaYsobrerayada", "sel.first", "sel.last")

                elif "negritaCursivaYsubrayada" in etiquetasActuales:
                    cajaTexto.tag_remove("negritaCursivaYsubrayada", "sel.first", "sel.last")
                    cajaTexto.tag_add("negritaCursivaSubrayadaYsobrerayada", "sel.first", "sel.last")
                else:
                    cajaTexto.tag_add("sobrerayada", "sel.first", "sel.last")
        
def cambiarFuente(e):
    global cfont
    global csize
    global tagCount


    if cfont == None:
        cfont = 'Helvetica'
    if csize == None:
        csize = '11'

    if e == 0:         
        tag = cajaTexto.tag_names()
        for tags in tag: 
            cajaTexto.tag_remove(tags, '1.0', END)
        cfont = cajaListaFuentes.get(cajaListaFuentes.curselection())
        fuenteCajaTexto.config(family = cfont)

    elif e == 1:
        fuenteCajaTexto.config(size = csize)
        csize = cajaListaFuentes_tamaño.get(cajaListaFuentes_tamaño.curselection())


#10. Estilos

def estilos():

    if ventanaHerramientas_ventanaFuentes.winfo_manager() != 'pack':

        ventanaPrincipal.pack_forget()

        ventanaHerramientas_ventanaFuentes.pack(fill= Y, side="left", anchor="w")

        ventanaHerramientas_ventanaFuentes.configure(border_width = 1, border_color = "#ffffff")

        ventanaPrincipal.pack(pady=5, side="top", fill="both", expand=True)

        ventanaHerramientas_ventanaFuentes_ventanaBotones.grid(row = 3, column=0, columnspan = 3, pady = 10)

        botonNegrita.grid(row = 0, column = 1, padx = 5, pady= 10, ipadx = 5, sticky = W)

        botonCursiva.grid(row = 0, column = 2, padx = 5, ipadx = 5, sticky = W+E)

        botonSubrayado.grid(row = 0, column = 3, padx= 5, pady = 10, ipadx = 5, sticky = E+W+S)

        botonSobrerayado.grid(row= 0, column = 4, padx = 5, ipadx = 5, sticky = E)
        familiaFuentes.grid(row = 0, column = 0, sticky = N, padx = 5, pady= 10, ipadx = 5)

        familiaFuentes_tamaño.grid(row= 0, column = 1, padx = 5)

        cajaListaFuentesFrame.grid(row=2, column = 0)
        cajaListaFuentesTamañoFrame.grid(row =2, column = 1)
        barraScrollListaFuentes.pack(side=RIGHT, fill= Y)
        barraScrollListaFuentes_tamaño.pack(side=RIGHT, fill=Y)

        cajaListaFuentes.pack(fill= BOTH, expand = True)
        cajaListaFuentes_tamaño.pack(fill= BOTH, expand = True)

        barraScrollListaFuentes.config(command= cajaListaFuentes.yview)
        barraScrollListaFuentes_tamaño.config(command= cajaListaFuentes_tamaño.yview)

        for f in font.families():
            cajaListaFuentes.insert('end', f)

        tamaño_Fuentes = [8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64]
        for tamaños in tamaño_Fuentes:
            cajaListaFuentes_tamaño.insert('end', tamaños)

    else:
        ventanaHerramientas_ventanaFuentes.pack_forget()
        botonNegrita.grid_forget()
        botonCursiva.grid_forget()
        botonSubrayado.grid_forget()
        botonSobrerayado.grid_forget()
        familiaFuentes.grid_forget()
        familiaFuentes_tamaño.grid_forget()
        cajaListaFuentes.grid_forget()
        cajaListaFuentes_tamaño.grid_forget()

def gestion():

    if ventanaHerramientas_ventanaGestor.winfo_manager() != 'pack':
        ventanaPrincipal.pack_forget()
        ventanaHerramientas_ventanaGestor.pack(fill= Y, side="left", anchor="w")

        ventanaHerramientas_ventanaGestor.configure(border_width = 1, border_color = "#d6d6ff")

        ventanaPrincipal.pack(pady=5, side="top", fill="both", expand=True)

        ventanaHerramientas_ventanaGestor_ventanaActividades.grid(row = 0, column = 0)

        ventanaHerramientas_ventanaGestor_ventanaActividades.configure(fg_color="transparent", width = 160)

        ventanaHerramientas_ventanaGestor_ventanaVersiones.grid(row = 2, column = 0)
        ventanaHerramientas_ventanaGestor_ventanaVersiones.configure(fg_color="transparent", width = 160)

        ventanaHerramientas_ventanaGestor_ventanaActividades_Label.grid(row = 0, column = 0, columnspan = 3 ,padx = 5, pady = 10)
        ventanaHerramientas_ventanaGestor_ventanaActividades_Label.configure(fg_color="transparent")

        botonVerDescripcion = CTkButton(ventanaHerramientas_ventanaGestor, text= 'Ver Descripción', command = verDesc, width = 80, height = 6, font=('Helvetica', 14))
        botonVerDescripcion.grid(row = 4, column = 0, columnspan = 3, pady = (10, 1))

        botonBorrarProyecto = CTkButton(ventanaHerramientas_ventanaGestor, text= "Borrar Proyecto Actual", command = lambda: borrarProyecto(nombreProyectoAbierto), width = 80, height = 6, font= ('Helvetica', 14))
        botonBorrarProyecto.grid(row = 5, column = 0, columnspan = 3, pady = 1)

        botonBorrarProyectos = CTkButton(ventanaHerramientas_ventanaGestor, text = "Borrar Proyecto Existente", command = borrarProyectoExistente, width = 80, height = 6, font= ('Helvetica', 14))
        botonBorrarProyectos.grid(row = 6, column = 0, columnspan= 3, pady = 1)

        cajaListaActividadesFrame.grid(row = 2, column = 0, columnspan = 3, pady = 5, sticky= N+W+S+E)
        ventanaHerramientas_ventanaGestor_ventanaVersiones_Label.grid(row = 0, column = 0, columnspan = 3 ,padx = 5)

        cajaListaVersionesFrame.grid(row = 2, column = 0, columnspan= 3, pady = 5, sticky = N+W+S+E)
        cajaListaVersionesFrame.configure(width= 10)

        botonNuevaVersion.grid(row = 1, column = 0)
        botonBorrarVersion.grid(row = 1, column = 1)

        botonNuevaActividad.grid(row = 1, column= 0)
        botonGuardarActividad.grid(row = 1, column = 1)
        botonBorrarActividad.grid(row = 1, column = 2)
        barraScrollListaActividades.pack(side = RIGHT, fill = Y)
        listaActividades.pack(fill = BOTH, expand = True)
        barraScrollListaVersiones.pack(side = RIGHT, fill = Y)
        cajaListaVersiones.pack(fill = BOTH, expand = True)

        barraScrollListaActividades.config(command = listaActividades.yview)
        barraScrollListaVersiones.config(command = cajaListaVersiones.yview)


    else:
        ventanaHerramientas_ventanaGestor.pack_forget()
        ventanaHerramientas_ventanaGestor_ventanaActividades_Label.grid_forget()
        ventanaHerramientas_ventanaGestor_ventanaVersiones_Label.grid_forget()

def gestion_buscarActividades(e):
    global nombreProyectoAbierto
    global actividadProyectoAbierto
    global versionProyectoAbierto
    global cajaTextoLabel
    global cfont
    global csize

    if cajaTexto.winfo_manager() == 'pack':
        if cajaTexto.edit_modified():

            answer = messagebox.askyesno('No ha guardado los cambios', 'El proyecto ha recibido modificaciones, crear uno eliminará los cambios hechos.\n¿Desea proceder de todos modos?')

            if answer != True:
                return

    if e == 0:
        nombre = nombreProyectoAbierto
        actividad = listaActividades.get(listaActividades.curselection())
        actividadAux = ''
        for elem in str(actividad):
            if elem.isdigit():
                actividadAux += ''+elem
        actividadAux = int(actividadAux)
        actividadProyectoAbierto = actividadAux
        ventanaPrincipal.pack_forget()
        cajaTextoLabel.pack_forget()
        cajaTexto.pack_forget()
        ventanaPrincipal.pack(pady=5, side="top", fill="both", expand=True)

        cajaTextoLabel = CTkLabel(ventanaPrincipal, width = 5, text = f"Proyecto {nombreProyectoAbierto}, Versión {versionProyectoAbierto}, {actividad}, Autor {proyectoAutor}", font=('', 24))
        cajaTextoLabel.pack(fill= X, expand = False)

        cajaTexto.pack(fill="both", expand = True)

        g = p.buscarActividadEspecifica(nombre, actividad)[0]

        cajaTexto.delete("1.0", END)
        cajaTexto.insert("1.0", g)

        if os.path.isfile(f'./projects/{nombreProyectoAbierto}/Versions/ver_{versionProyectoAbierto}/act_{actividadProyectoAbierto}_tags.txt'):
            with open(f'./projects/{nombreProyectoAbierto}/Versions/ver_{versionProyectoAbierto}/act_{actividadProyectoAbierto}_tags.txt', 'r') as file:
                data = file.readlines()
            dataAux = ''
            posAux = ''
            posEnd = ''
            fontAux = ''
            sizeAux = ''

            for lines in range(1, 3):
                for elem in range(5, len(data[lines])):
                    if data[lines][elem].isalpha():
                        fontAux += ''+data[lines][elem]

                    if data[lines][elem].isdigit():
                        sizeAux += ''+data[lines][elem]

            cfont = fontAux
            csize = int(sizeAux)
            fuenteCajaTexto.configure(family = cfont, size = csize)

            for lines in range (3, len(data)-1):

                for elem in data[lines]:
                    if elem.isalpha():
                        dataAux += ''+elem
                    if elem.isdigit() or elem == '.':
                        posAux += ''+elem
                for elemV in data[lines+1]:
                    if elemV.isdigit() or elemV == '.':
                        posEnd += ''+elemV
                if 'sel' in dataAux:                        
                    cajaTexto.tag_add(f'{dataAux[3:]}', f'{posAux}', f'{posEnd}')
                    dataAux = ''
                    posAux = ''
                    posEnd = ''
                    fontAux = ''
                    sizeAux = ''
                else:
                    cajaTexto.tag_add(f'{dataAux}', f'{posAux}', f'{posEnd}')
                    dataAux = ''
                    posAux = ''
                    posEnd = ''
                    fontAux = ''
                    sizeAux = ''
        else:
            messagebox.showerror('Error', 'Aún no ha guardado la actividad.')

    if e == 1:

        if listaActividades.size() > 1 or str(listaActividades.get(listaActividades.curselection())) != 'Actividad 0':
            if (messagebox.askokcancel('Advertencia', 'La actividad será borrada, esta acción es irreversible.\n¿Proceder?')):
                nombre = nombreProyectoAbierto
                actividadBorrar = ''
                actividadSelect = str(listaActividades.get(listaActividades.curselection()))
                for elem in actividadSelect:
                    if elem.isdigit():
                        actividadBorrar += ''+elem
                actividadBorrar = int(actividadBorrar)

                with open(f"./projects/{nombreProyectoAbierto}/Versions/versions.txt", "r") as f:
                    lines = f.readlines()
                    linesAux = lines[:2]
                with open(f"./projects/{nombreProyectoAbierto}/Versions/versions.txt", "w") as f:
                    linesAux.append(f'Activities: {actividadBorrar-1}')
                    f.truncate()
                    f.writelines(linesAux)
                        
                listaActividades.delete(0, END)

                p.eliminarActividad(nombreProyectoAbierto, f'Actividad {actividadBorrar}')
                if os.path.isfile(f'./projects/{nombreProyectoAbierto}/Versions/ver_{versionProyectoAbierto}/act_{actividadBorrar}_tags.txt'):
                    os.remove(f'./projects/{nombreProyectoAbierto}/Versions/ver_{versionProyectoAbierto}/act_{actividadBorrar}_tags.txt')
                a = -1
                for elem in glob.glob(f'./projects/{nombreProyectoAbierto}/Versions/ver_{versionProyectoAbierto}/activities/*.txt'):
                    a += 1
                    listaActividades.insert('end', f'Actividad {a}')
                if actividadBorrar == actividadProyectoAbierto:
                    actividadProyectoAbierto -= 1

                actividad = '0'

                ventanaPrincipal.pack_forget()
                cajaTextoLabel.pack_forget()
                cajaTexto.pack_forget()
                ventanaPrincipal.pack(pady=5, side="top", fill="both", expand=True)

                cajaTextoLabel = CTkLabel(ventanaPrincipal, width = 5, text = f"Proyecto {nombreProyectoAbierto}, Versión {versionProyectoAbierto}, {actividad}, Autor {proyectoAutor}", font=('', 24))
                cajaTextoLabel.pack(fill= X, expand = False)

                cajaTexto.pack(fill="both", expand = True)

                g = p.buscarActividadEspecifica(nombre, f'Actividad {actividad}')[0]

                cajaTexto.delete("1.0", END)
                cajaTexto.insert("1.0", g)
                
                if os.path.isfile(f'./projects/{nombreProyectoAbierto}/Versions/ver_{versionProyectoAbierto}/act_{actividadProyectoAbierto}_tags.txt'):
                    with open(f'./projects/{nombreProyectoAbierto}/Versions/ver_{versionProyectoAbierto}/act_{actividadProyectoAbierto}_tags.txt', 'r') as file:
                        data = file.readlines()
                    dataAux = ''
                    posAux = ''
                    posEnd = ''
                    fontAux = ''
                    sizeAux = ''

                    for lines in range(1, 3):
                        for elem in range(5, len(data[lines])):
                            if data[lines][elem].isalpha():
                                fontAux += ''+data[lines][elem]

                            if data[lines][elem].isdigit():
                                sizeAux += ''+data[lines][elem]

                    cfont = fontAux
                    csize = int(sizeAux)
                    fuenteCajaTexto.configure(family = cfont, size = csize)

                    for lines in range (3, len(data)-1):

                        for elem in data[lines]:
                            if elem.isalpha():
                                dataAux += ''+elem
                            if elem.isdigit() or elem == '.':
                                posAux += ''+elem
                        for elemV in data[lines+1]:
                            if elemV.isdigit() or elemV == '.':
                                posEnd += ''+elemV
                        if 'sel' in dataAux:                        
                            cajaTexto.tag_add(f'{dataAux[3:]}', f'{posAux}', f'{posEnd}')
                            dataAux = ''
                            posAux = ''
                            posEnd = ''
                            fontAux = ''
                            sizeAux = ''
                        else:
                            cajaTexto.tag_add(f'{dataAux}', f'{posAux}', f'{posEnd}')
                            dataAux = ''
                            posAux = ''
                            posEnd = ''
                            fontAux = ''
                            sizeAux = ''
            else:
                pass

        else:
            messagebox.showerror('Error', 'Los proyectos deben tener al menos una actividad 0.')

    elif e == 2:
        if cajaListaVersiones.size() > 1 and str(cajaListaVersiones.get(cajaListaVersiones.curselection())) != 'Version 0':
            if (messagebox.askokcancel('Advertencia', 'La versión seleccionada y todas sus actividades serán borradas, esta acción es irreversible.\n¿Proceder?')):
                versionBorrar = ''


                with open(f'./projects/{nombreProyectoAbierto}/Versions/versions.txt', 'r') as file:
                    data = file.readlines()
                    for elem in str(cajaListaVersiones.get(cajaListaVersiones.curselection())):
                        if elem.isdigit():
                            versionBorrar += ''+elem
                            
                    for lines in range(len(data)-1, -1, -1):
                        if f'ID: {versionBorrar}' in data[lines]:
                            if int(versionBorrar) == versionProyectoAbierto:
                                dataAux = data[:lines]
                            else:
                                dataAux = data[:lines]
                                dataAux.extend(data[lines+3:])

                            with open(f'./projects/{nombreProyectoAbierto}/Versions/versions.txt', 'w') as file:
                                file.truncate()
                                file.writelines(dataAux)
                            break

                if int(versionBorrar) == versionProyectoAbierto:
                    with open(f'./projects/{nombreProyectoAbierto}/Versions/versions.txt', 'r') as file:
                        data = file.readlines()
                        versionAux = ''
                        for lines in range (len(data)-1, -1, -1):
                            if 'ID: ' in data[lines]:
                                dataAux = data[lines]
                                for elem in dataAux:
                                    if elem.isdigit():
                                        versionAux += ''+elem
                                break
                                        
                        with open(f'./projects/projects.txt', 'r') as fileP:
                            dataP = fileP.readlines()
                            for linesP in range (len(dataP)-1, -1, -1):
                                if f'Name: {nombreProyectoAbierto}' in dataP[linesP]:
                                    if f'Version: {versionBorrar}' in dataP[linesP+1]:
                                        dataPAux = dataP[:linesP+1]
                                        dataPAux.append(f'Version: {versionAux}\n')
                                        dataPAux.extend(dataP[linesP+2:])
                                        break
                        
                            with open(f'./projects/projects.txt', 'w') as fileP:
                                fileP.truncate()
                                fileP.writelines(dataPAux)
                
                shutil.rmtree(f'./projects/{nombreProyectoAbierto}/Versions/ver_{versionBorrar}')

                cajaListaVersiones.delete(0, END)

                for subdirs in os.listdir(f'./projects/{nombreProyectoAbierto}/Versions/'):
                    if os.path.isdir(f'./projects/{nombreProyectoAbierto}/Versions/{subdirs}'):
                        elemSubdir = subdirs
                        for elemSubdirV in elemSubdir:
                            if elemSubdirV.isdigit():
                                cajaListaVersiones.insert('end', f'Version {elemSubdirV}')   

                if int(versionBorrar) == versionProyectoAbierto:
                    with open(f'./projects/{nombreProyectoAbierto}/Versions/versions.txt') as file:
                        data = file.readlines()
                        versionProyectoAbierto = ''
                        for elem in range(len(data)-1, -1, -1):
                            if "ID: " in data[elem]:
                                for elemV in data[elem]:
                                    if elemV.isdigit():
                                        versionProyectoAbierto += ''+elemV
                                break
                        
                        versionProyectoAbierto = int(versionProyectoAbierto)
                        
                        try:
                            conexionAbrirProyecto = sqlite3.connect('./projects/projects.db')

                            cursor = conexionAbrirProyecto.cursor()

                            IDCursor = cursor.execute(f'''SELECT Project_ID FROM projects WHERE Project_Title = '{nombreProyectoAbierto}'; ''')
                            IDCursorRow = IDCursor.fetchall()
                            IDCount = IDCursorRow[0][0]
                            cursor.execute(f'''UPDATE projects SET Project_Current_Version = '{versionProyectoAbierto}' WHERE Project_ID = {IDCount}''')

                            conexionAbrirProyecto.commit()
                            cursor.close()
                        
                        except sqlite3.Error as error:
                            messagebox.showerror('Error', f'Error {error} ocurrido')

                        finally:
                            if conexionAbrirProyecto:
                                conexionAbrirProyecto.close()

                actividadProyectoAbierto = 0
                g = p.buscarActividadEspecifica(nombreProyectoAbierto, 'Actividad 0')[0]
                listaActividades.delete(0, END)

                a = -1
                for elem in glob.glob(f'./projects/{nombreProyectoAbierto}/Versions/ver_{versionProyectoAbierto}/activities/*.txt'):
                    a += 1
                    listaActividades.insert('end', f'Actividad {a}')

                cajaTextoLabel.pack_forget()
                cajaTexto.pack_forget()

                cajaTextoLabel = CTkLabel(ventanaPrincipal, width = 5, text = f"Proyecto {nombreProyectoAbierto}, Versión {versionProyectoAbierto}, Actividad {actividadProyectoAbierto}, Autor {proyectoAutor}", font=('', 24))
                cajaTextoLabel.pack(fill= X, expand = False)

                cajaTexto.pack(fill = BOTH, expand = True)
                cajaTexto.delete("1.0", END)
                cajaTexto.insert("1.0", g)


                if os.path.isfile(f'./projects/{nombreProyectoAbierto}/Versions/ver_{versionProyectoAbierto}/act_{actividadProyectoAbierto}_tags.txt'):
                    with open(f'./projects/{nombreProyectoAbierto}/Versions/ver_{versionProyectoAbierto}/act_{actividadProyectoAbierto}_tags.txt', 'r') as file:
                        data = file.readlines()
                    dataAux = ''
                    posAux = ''
                    posEnd = ''
                    fontAux = ''
                    sizeAux = ''

                    for lines in range(1, 3):
                        for elem in range(5, len(data[lines])):
                            if data[lines][elem].isalpha():
                                fontAux += ''+data[lines][elem]

                            if data[lines][elem].isdigit():
                                sizeAux += ''+data[lines][elem]

                    cfont = fontAux
                    csize = int(sizeAux)
                    fuenteCajaTexto.configure(family = cfont, size = csize)

                    for lines in range (3, len(data)-1):

                        for elem in data[lines]:
                            if elem.isalpha():
                                dataAux += ''+elem
                            if elem.isdigit() or elem == '.':
                                posAux += ''+elem
                        for elemV in data[lines+1]:
                            if elemV.isdigit() or elemV == '.':
                                posEnd += ''+elemV
                        if 'sel' in dataAux:                        
                            cajaTexto.tag_add(f'{dataAux[3:]}', f'{posAux}', f'{posEnd}')
                            dataAux = ''
                            posAux = ''
                            posEnd = ''
                            fontAux = ''
                            sizeAux = ''
                        else:
                            cajaTexto.tag_add(f'{dataAux}', f'{posAux}', f'{posEnd}')
                            dataAux = ''
                            posAux = ''
                            posEnd = ''
                            fontAux = ''
                            sizeAux = ''
            else:
                pass
        else:
            messagebox.showerror('Error', 'Los proyectos deben tener al menos una versión 0.')

    elif e == 3:
        nombre = nombreProyectoAbierto
        version = cajaListaVersiones.get(cajaListaVersiones.curselection())
        versionAux = ''
        for elem in str(version):
            if elem.isdigit():
                versionAux += ''+elem

        versionAux = int(versionAux)
        versionProyectoAbierto = versionAux
        ventanaPrincipal.pack_forget()
        cajaTextoLabel.pack_forget()
        cajaTexto.pack_forget()
        ventanaPrincipal.pack(pady=5, side="top", fill="both", expand=True)

        g, n = p.buscarActividad(nombre)

        actividadProyectoAbierto = n

        cajaTextoLabel = CTkLabel(ventanaPrincipal, width = 5, text = f"Proyecto {nombreProyectoAbierto}, Versión {versionProyectoAbierto}, Actividad {actividadProyectoAbierto}, Autor {proyectoAutor}", font=('', 24))
        cajaTextoLabel.pack(fill= X, expand = False)

        cajaTexto.pack(fill="both", expand = True)


        listaActividades.delete(0, END)
        a = -1
        for elem in glob.glob(f'./projects/{nombreProyectoAbierto}/Versions/ver_{versionProyectoAbierto}/activities/*.txt'):
            a += 1
            listaActividades.insert('end', f'Actividad {a}')

        cajaTexto.delete("1.0", END)
        cajaTexto.insert("1.0", g)

        if os.path.isfile(f'./projects/{nombreProyectoAbierto}/Versions/ver_{versionProyectoAbierto}/act_{actividadProyectoAbierto}_tags.txt'):
            with open(f'./projects/{nombreProyectoAbierto}/Versions/ver_{versionProyectoAbierto}/act_{actividadProyectoAbierto}_tags.txt', 'r') as file:
                data = file.readlines()
            dataAux = ''
            posAux = ''
            posEnd = ''
            fontAux = ''
            sizeAux = ''

            for lines in range(1, 3):
                for elem in range(5, len(data[lines])):
                    if data[lines][elem].isalpha():
                        fontAux += ''+data[lines][elem]

                    if data[lines][elem].isdigit():
                        sizeAux += ''+data[lines][elem]

            cfont = fontAux
            csize = int(sizeAux)
            fuenteCajaTexto.configure(family = cfont, size = csize)

            for lines in range (3, len(data)-1):

                for elem in data[lines]:
                    if elem.isalpha():
                        dataAux += ''+elem
                    if elem.isdigit() or elem == '.':
                        posAux += ''+elem
                for elemV in data[lines+1]:
                    if elemV.isdigit() or elemV == '.':
                        posEnd += ''+elemV
                if 'sel' in dataAux:                        
                    cajaTexto.tag_add(f'{dataAux[3:]}', f'{posAux}', f'{posEnd}')
                    dataAux = ''
                    posAux = ''
                    posEnd = ''
                    fontAux = ''
                    sizeAux = ''
                else:
                    cajaTexto.tag_add(f'{dataAux}', f'{posAux}', f'{posEnd}')
                    dataAux = ''
                    posAux = ''
                    posEnd = ''
                    fontAux = ''
                    sizeAux = ''

def gestion_guardarCambiosActividades(e):
    if os.path.isfile(f'./projects/{nombreProyectoAbierto}/Versions/ver_{versionProyectoAbierto}/act_{actividadProyectoAbierto}_tags.txt'):
        pass
    else:
        act_tags = open(f'./projects/{nombreProyectoAbierto}/Versions/ver_{versionProyectoAbierto}/act_{actividadProyectoAbierto}_tags.txt', 'w')
        act_tags.write(f'Folderpath: ./projects/{nombreProyectoAbierto}/Versions/ver_{versionProyectoAbierto}/activities/Actividad {actividadProyectoAbierto}.txt\n')
        act_tags.close()
    obtenerTags("1.0", "end-1c")

    if len(listaActividades.curselection()) != 0:
        actividadSelect = listaActividades.get(listaActividades.curselection())
        actividadSave = f'Actividad {actividadProyectoAbierto}'

        if actividadSave == 'Actividad 0' and actividadSave == actividadSelect:
            actividadTexto = open(f'./projects/{nombreProyectoAbierto}/Versions/ver_{versionProyectoAbierto}/activities/Actividad 0.txt', 'w')
            actividadTexto.write(cajaTexto.get(1.0, END))
            actividadTexto.close()

            messagebox.showinfo('Éxito', 'Actividad guardada exitosamente.')

            barraEstado.configure(text=f"Guardado en: {f'/projects/{nombreProyectoAbierto}/Versions/ver_{versionProyectoAbierto}/activities/Actividad 0.txt'}        ")

        elif actividadSave == actividadSelect:
            
            actividadTexto = open (f'./projects/{nombreProyectoAbierto}/Versions/ver_{versionProyectoAbierto}/activities/{actividadSelect}.txt', 'w')
            actividadTexto.write(cajaTexto.get(1.0, END))
            actividadTexto.close()

            messagebox.showinfo('Éxito', 'Actividad guardada exitosamente.')

            barraEstado.configure(text=f"Guardado en: {f'/projects/{nombreProyectoAbierto}/Versions/ver_{versionProyectoAbierto}/activities/{actividadSelect}.txt'}        ")
        else:
            messagebox.showerror('Error', 'La actividad que ha seleccionado no es correcta.')

        if cajaTexto.edit_modified():
            cajaTexto.edit_modified(False)


    else:
        messagebox.showerror('Error', 'No ha seleccionado una actividad.')

# Ventanas

# Ventana de herramientas
menuPrincipal = CTkMenuBar(root)

ventanaHerramientas = CTkFrame(root)
ventanaHerramientas.pack(fill = Y, side = "left", anchor="nw")


# Ventana de fuentes y estilos

ventanaHerramientas_ventanaFuentes = CTkFrame(root, fg_color="#424447")
ventanaHerramientas_ventanaFuentes_ventanaBotones = CTkFrame(ventanaHerramientas_ventanaFuentes)

# Ventana principal para el texto


ventanaPrincipal = CTkFrame(root, fg_color="#313336")
ventanaPrincipal.pack(pady=5, side="top", fill="both", expand=True)

# Ventana para el gestor

ventanaHerramientas_ventanaGestor = CTkFrame(root, fg_color="#424447")
ventanaHerramientas_ventanaGestor_ventanaActividades = CTkFrame(ventanaHerramientas_ventanaGestor)
ventanaHerramientas_ventanaGestor_ventanaVersiones = CTkFrame(ventanaHerramientas_ventanaGestor, width = 100)



# Caja de texto
barraScroll = Scrollbar(ventanaPrincipal)
barraScroll.pack(side = RIGHT, fill = Y)

cajaTextoInitLabel = CTkLabel(ventanaPrincipal, width = 5, text = "Crea un Nuevo Proyecto para empezar", font= ('./fonts/BRLNSR.TTF', 32))
cajaTextoInitLabel.pack(fill= X, expand = False)

csize = None
cfont = None
fuenteCajaTexto = font.Font(family='Helvetica', size="11")
cajaTexto = Text(ventanaPrincipal, width = 1, height = 1, font=fuenteCajaTexto, selectbackground="#ffcc00", selectforeground='#12110e', undo = True, background="#424447", foreground="#ffffff")

ventanaHerramientas_ventanaGestor_ventanaActividades_Label = CTkLabel(ventanaHerramientas_ventanaGestor_ventanaActividades, width = 160, text= "Actividades", font=('Helvetica', 16))
ventanaHerramientas_ventanaGestor_ventanaVersiones_Label = CTkLabel(ventanaHerramientas_ventanaGestor_ventanaVersiones, width = 120, text= "Versiones", font=('Helvetica', 16))

cajaListaActividadesFrame = CTkFrame(ventanaHerramientas_ventanaGestor_ventanaActividades)


# Menú de acciones

botonArchivo = menuPrincipal.add_cascade("Archivo")
botonEditar = menuPrincipal.add_cascade("Editar")
botonVentana = menuPrincipal.add_cascade("Ventana")
botonAyuda = menuPrincipal.add_cascade("Ayuda")

# Botón de Archivo

menuAcciones_menuArchivos = CustomDropdownMenu(widget = botonArchivo)
menuAcciones_menuArchivos.add_option(option= "Nuevo", command = nuevoArchivo)
menuAcciones_menuArchivos.add_option(option = "Abrir", command = abrirArchivo)
menuAcciones_menuArchivos.add_option(option = "Guardar", command = guardar)
menuAcciones_menuArchivos.add_option(option = "Guardar cómo", command = guardarComo)
menuAcciones_menuArchivos.add_separator()
menuAcciones_menuArchivos.add_option(option = "Salir", command = root.quit)

# Botón de Editar

menuAcciones_menuEditar = CustomDropdownMenu(widget = botonEditar)
menuAcciones_menuEditar.add_option(option = "Copiar", command= lambda: copiar(False))
menuAcciones_menuEditar.add_option(option = "Cortar ", command = lambda: cortar(False))
menuAcciones_menuEditar.add_option(option = "Pegar ", command = lambda: pegar(False))
menuAcciones_menuEditar.add_separator()
menuAcciones_menuEditar.add_option(option = "Deshacer", command = cajaTexto.edit_undo)
menuAcciones_menuEditar.add_option(option = "Rehacer", command = cajaTexto.edit_redo)

# Botón de Ventana

menuAcciones_menuVentana = CustomDropdownMenu(widget = botonVentana)
menuAcciones_menuVentana.add_option(option = "Maximizar", command = lambda: maxOmin(1))
menuAcciones_menuVentana.add_option(option = "Minimizar", command = lambda: maxOmin(0))


# Botón de Ayuda

menuAcciones_menuAyuda = CustomDropdownMenu(widget= botonAyuda)
menuAcciones_menuAyuda.add_option(option="Créditos y Contacto", command = lambda: autorInfo(True) )

# Botones de la ventana de herramientas

botonFuentes = CTkButton(ventanaHerramientas, image = imagenFuentes,text = "", command = estilos)
botonFuentes.grid(row = 0, column = 0, sticky = N,padx= 5, pady= 10)

botonNegrita = CTkButton(ventanaHerramientas_ventanaFuentes_ventanaBotones, image=imagenNegrita,text="", command = lambda: fuente(0), width = 20, height = 5)
botonCursiva = CTkButton(ventanaHerramientas_ventanaFuentes_ventanaBotones, image=imagenCursiva,text="", command = lambda: fuente(1), width = 20, height = 5)
botonSubrayado = CTkButton(ventanaHerramientas_ventanaFuentes_ventanaBotones, image=imagenSubrayado,text="", command = lambda: fuente(2), width = 50, height = 5)
botonSobrerayado = CTkButton(ventanaHerramientas_ventanaFuentes_ventanaBotones, image=imagenSobrerayado,text="", command = lambda: fuente(3), width = 10, height = 5)

botonGestor = CTkButton(ventanaHerramientas, image = imagenGestor,text = "", command = gestion)
botonGestor.grid (row = 1, column = 0, padx = 5, pady = 10)


botonNuevaActividad = CTkButton(ventanaHerramientas_ventanaGestor_ventanaActividades, text="Nueva", command = lambda: crearProyecto(2, nombreProyectoAbierto, versionProyectoAbierto, actividadProyectoAbierto) ,width = 80, height = 6, font=('Helvetica', 14))
botonGuardarActividad = CTkButton(ventanaHerramientas_ventanaGestor_ventanaActividades, text="Guardar", command = lambda: gestion_guardarCambiosActividades(True), width = 80, height = 6, font=('Helvetica', 14))
botonBorrarActividad = CTkButton(ventanaHerramientas_ventanaGestor_ventanaActividades, text= "Borrar", command = lambda: gestion_buscarActividades(1), width = 80, height = 6, font=('Helvetica', 14))

botonNuevaVersion = CTkButton(ventanaHerramientas_ventanaGestor_ventanaVersiones, text = "Nueva", command = lambda: crearProyecto(1, nombreProyectoAbierto, versionProyectoAbierto, actividadProyectoAbierto), width = 80, height = 6, font=('Helvetica', 14))
botonBorrarVersion = CTkButton(ventanaHerramientas_ventanaGestor_ventanaVersiones, text = "Borrar", command = lambda: gestion_buscarActividades(2), width = 80, height = 6, font=('Helvetica', 14))


barraScrollListaActividades = Scrollbar(cajaListaActividadesFrame)

listaActividades = Listbox(cajaListaActividadesFrame, selectmode = SINGLE, width = 20, yscrollcommand= barraScrollListaActividades.set)

# Labels

familiaFuentes = CTkLabel(ventanaHerramientas_ventanaFuentes, text="Elegir Tipografía", font=("Helvetica", 14))
familiaFuentes_tamaño = CTkLabel(ventanaHerramientas_ventanaFuentes, text="Tamaño  ", font=("Helvetica", 14))

# Cajas de Lista

cajaListaFuentesFrame = CTkFrame(ventanaHerramientas_ventanaFuentes)
cajaListaFuentesTamañoFrame = CTkFrame(ventanaHerramientas_ventanaFuentes, width = 500)

cajaListaVersionesFrame = CTkFrame(ventanaHerramientas_ventanaGestor_ventanaVersiones, width = 100)


barraScrollListaFuentes = Scrollbar(cajaListaFuentesFrame, orient ="vertical")
barraScrollListaFuentes_tamaño = Scrollbar(cajaListaFuentesTamañoFrame, orient ="vertical")
barraScrollListaVersiones = Scrollbar(cajaListaVersionesFrame, orient ="vertical")


cajaListaFuentes = Listbox(cajaListaFuentesFrame, selectmode= SINGLE, width = 20, yscrollcommand = barraScrollListaFuentes.set)


cajaListaFuentes_tamaño = Listbox(cajaListaFuentesTamañoFrame, selectmode= SINGLE, width = 10, yscrollcommand = barraScrollListaFuentes_tamaño.set)

cajaListaVersiones = Listbox(cajaListaVersionesFrame, selectmode= SINGLE, width = 20, yscrollcommand = barraScrollListaVersiones.set)


# Barra de Estado

barraEstado = CTkLabel(root, text="Listo        ", anchor = E)
barraEstado.pack(fill=X, side = BOTTOM, ipady = 15)


# Atajos

root.protocol("WM_DELETE_WINDOW", alSalir)
root.bind('<Control-Key-x>', cortar)
root.bind('<Control-Key-x>', copiar)
root.bind('<Control-Key-x>', pegar)
root.bind("<F1>", autorInfo)
root.bind("<Control-Key-b>", lambda e: fuente(0))
root.bind("<Alt-Key-i>", lambda e: fuente(1))
cajaListaFuentes.bind("<Double-Button-1>", lambda e: cambiarFuente(0))
cajaListaFuentes_tamaño.bind("<Double-Button-1>", lambda e: cambiarFuente(1))
listaActividades.bind("<Double-Button-1>", lambda e: gestion_buscarActividades(0))
cajaListaVersiones.bind("<Double-Button-1>", lambda e: gestion_buscarActividades(3))

root.mainloop()
