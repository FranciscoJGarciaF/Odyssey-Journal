from tkinter import *
from tkinter import filedialog
import os


root = Tk()

titulo = "Sin Título - Proyecto Pepino Pre-Alpha 0.1.0"
root.title(titulo)

root.iconbitmap('ico.ico')
root.geometry('1200x680')

global nombreAbierto
nombreAbierto = False

global seleccion
seleccion = False

# Funciones

# 1. Crear nuevo archivo

def nuevoArchivo():
    # Borrar el texto previamente escrito y actualizar el título y la barra de estado
    cajaTexto.delete("1.0", END)
    titulo = "Sin Título - Proyecto Pepino Pre-Alpha 0.1.0"
    root.title(titulo)
    barraEstado.config(text="Nuevo Archivo        ")

    global nombreAbierto
    nombreAbierto = False

# 1. Abrir archivo

def abrirArchivo():
    # Borrar el texto previamente escrito
    cajaTexto.delete("1.0", END)

    # Agarrar archivo de texto y cambiar el título y la barra de estado

    directorioInicial = os.path.expanduser('~')
    archivoTexto = filedialog.askopenfilename(initialdir= directorioInicial, title = "Abrir nuevo...", filetypes= (("Archivo de Texto", "*.txt"), ("Archivo HTML", "*.html"), ("Archivo de Python", "*.py") ))
    if archivoTexto:
        global nombreAbierto
        nombreAbierto = archivoTexto

    nombre = archivoTexto
    barraEstado.config(text=f"{nombre}        ")

    nombreLimpiar = nombre.rfind("/")
    nombre = nombre[nombreLimpiar+1:-4]

    root.title(f'{nombre} - Proyecto Pepino Pre-Alpha 0.1.0')

    # Abrir archivo

    archivoTexto = open(archivoTexto, 'r')
    colocarTexto = archivoTexto.read()

    cajaTexto.insert(END, colocarTexto)
    archivoTexto.close()


# 3. Guardar Como
def guardarComo():
    archivoTexto = filedialog.asksaveasfilename(defaultextension=".*", initialdir= os.path.expanduser('~'), title = 'Guardar cómo...', filetypes= (("Archivo de Texto", "*.txt"), ("Archivo HTML", "*.html"), ("Archivo de Python", "*.py") ))
    if archivoTexto:
        # Actualizar el título y la barra de status
        nombre = archivoTexto
        barraEstado.config(text=f"Guardado en: {nombre}        ")

        nombreLimpiar = nombre.rfind("/")
        nombre = nombre[nombreLimpiar+1:-4]

        root.title(f'{nombre} - Proyecto Pepino Pre-Alpha 0.1.0')
        # Guardar el archivo
        global nombreAbierto
        nombreAbierto = archivoTexto

        archivoTexto = open(archivoTexto, 'w')
        archivoTexto.write(cajaTexto.get(1.0, END))
        archivoTexto.close()

# 4. Guardar

def guardar():
    global nombreAbierto
    if nombreAbierto:
        archivoTexto = open(nombreAbierto, 'w')
        archivoTexto.write(cajaTexto.get(1.0, END))
        archivoTexto.close()    
        nombre = nombreAbierto
        barraEstado.config(text=f"Guardado en: {nombre}        ")
    else:
        guardarComo()

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

# Ventana principal para el texto

ventanaPrincipal = Frame(root)
ventanaPrincipal.pack(pady=5)

# Barra de Scroll

barraScroll = Scrollbar(ventanaPrincipal)
barraScroll.pack(side = RIGHT, fill = Y)

barraScrollHorizontal = Scrollbar(ventanaPrincipal, orient = 'horizontal')
barraScrollHorizontal.pack(side = BOTTOM, fill = X)

# Caja de texto

cajaTexto = Text(ventanaPrincipal, width = 97, height = 25, font=('Helvetica', 16), selectbackground="yellow", selectforeground='black', undo = True, yscrollcommand= barraScroll.set)
cajaTexto.pack()

# Configurar la barra de scroll

barraScroll.config(command=cajaTexto.yview)

barraScrollHorizontal.config(command=cajaTexto.xview)

# Menú de acciones

menuAcciones = Menu(root)
root.config(menu = menuAcciones)

# Botón de Archivo

menuAcciones_menuArchivos = Menu(menuAcciones, tearoff=False)
menuAcciones.add_cascade(label = 'Archivo', menu=menuAcciones_menuArchivos)
menuAcciones_menuArchivos.add_command(label = "Nuevo", command = nuevoArchivo)
menuAcciones_menuArchivos.add_command(label = "Abrir", command = abrirArchivo)
menuAcciones_menuArchivos.add_command(label = "Guardar", command = guardar)
menuAcciones_menuArchivos.add_command(label = "Guardar cómo", command = guardarComo)
menuAcciones_menuArchivos.add_separator()
menuAcciones_menuArchivos.add_command(label = "Salir", command = root.quit)

# Botón de Editar

menuAcciones_menuEditar = Menu(menuAcciones, tearoff=False)
menuAcciones.add_cascade(label="Editar", menu= menuAcciones_menuEditar)
menuAcciones_menuEditar.add_command(label = "Copiar", command= lambda: copiar(False), accelerator= "(Ctrl+C)")
menuAcciones_menuEditar.add_command(label = "Cortar ", command = lambda: cortar(False), accelerator= "(Ctrl+X)")
menuAcciones_menuEditar.add_command(label = "Pegar ", command = lambda: pegar(False), accelerator= "Ctrl+V")
menuAcciones_menuEditar.add_separator()
menuAcciones_menuEditar.add_command(label = "Deshacer", command = cajaTexto.edit_undo, accelerator= "(Ctrl+Z)")
menuAcciones_menuEditar.add_command(label = "Rehacer", command = cajaTexto.edit_redo, accelerator= "(Ctrl+Y)")

# Barra de Estado

barraEstado = Label(root, text="Listo        ", anchor = E)
barraEstado.pack(fill=X, side = BOTTOM, ipady = 15)


# Botón de Ventana

menuAcciones_menuVentana = Menu(menuAcciones, tearoff= False)
menuAcciones.add_cascade(label="Ventana", menu= menuAcciones_menuVentana)
menuAcciones_menuVentana.add_command(label = "Maximizar")
menuAcciones_menuVentana.add_command(label = "Minimizar")

# Botón de Ayuda

menuAcciones_menuAyuda = Menu(menuAcciones, tearoff= False)
menuAcciones.add_cascade(label="Ayuda", menu = menuAcciones_menuAyuda) 
menuAcciones_menuAyuda.add_command(label="Créditos y Contacto")
menuAcciones_menuAyuda.add_command(label="¿Cómo usar?")

# Editar atajos

root.bind('<Control-Key-x>', cortar)
root.bind('<Control-Key-x>', copiar)
root.bind('<Control-Key-x>', pegar)

root.mainloop()