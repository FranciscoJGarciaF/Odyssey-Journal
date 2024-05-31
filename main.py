from tkinter import *
from tkinter import filedialog
from tkinter import font
import sys
import os
import webbrowser


if hasattr (sys, '_MEIPASS'):
    os.chdir(sys._MEIPASS)

root = Tk()


root.title("Sin Título - Proyecto Pepino Pre-Alpha 0.2.0")

root.iconbitmap("ico.ico")
root.geometry('1200x680')

global nombreAbierto
nombreAbierto = False

global seleccion
seleccion = False


# Funciones

def nuevoArchivo():
    # Borrar el texto previamente escrito y actualizar el título y la barra de estado
    cajaTexto.delete("1.0", END)
    root.title("Sin Título - Proyecto Pepino Pre-Alpha 0.2.0")
    barraEstado.config(text="Nuevo Archivo        ")

    global nombreAbierto
    nombreAbierto = False


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
        titulo =f'{nombre} - Proyecto Pepino Pre-Alpha 0.2.0'
        root.title(titulo)

    # Abrir archivo

    archivoTexto = open(archivoTexto, 'r')
    colocarTexto = archivoTexto.read()

    cajaTexto.insert(END, colocarTexto)
    archivoTexto.close()

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

def cortar(e):
    global seleccion
# Verificar si fue llamada por un atajo o por el botón y asignar al portapapeles
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
# Verificar si fue llamada por un atajo o por el botón y asignar al portapapeles
    if e:
        seleccion = root.clipboard_get()

    else:
        if cajaTexto.selection_get():
            root.clipboard_clear()
            seleccion = cajaTexto.selection_get()
            root.clipboard_append(seleccion)

def pegar(e):
    global seleccion
# Verificar si fue llamada por un atajo o por el botón y asignar al portapapeles
    if e:
        seleccion = root.clipboard_get()
    else:
        if seleccion:
            posicion = cajaTexto.index(INSERT)
            cajaTexto.insert(posicion, seleccion)



def llamarNavegador(url):
    webbrowser.open_new(url)

def autorInfo(e):
    # Ventana de información de contacto y créditos al autor.

    ventanaAutor = Tk()
    ventanaAutor.title("Información y Contacto")
    ventanaAutor.iconbitmap('ico.ico')

    ventanaAutor.geometry('300x200')
    ventanaAutor.minsize(300, 200)
    ventanaAutor.maxsize(1280, 800)

    infoAutor = Label(ventanaAutor, text="""
    Autor: Francisco García\n
    Correo: franciscojotagarciaefe@gmail.com\n
    Repositorio:""")
    infoAutor_Link = Label(ventanaAutor, text="github.com/FranciscoJGarciaF/Proyecto-Pepino", fg= 'blue', cursor="hand2")

    infoAutor.pack()
    infoAutor_Link.pack()
    infoAutor_Link.bind("<Button-1>", lambda: llamarNavegador("github.com/FranciscoJGarciaF/Proyecto-Pepino"))
    infoAutor_extra = Label(ventanaAutor, text="\n\n¡Gracias por usar!")
    infoAutor_extra.pack()

def maxOmin(estado):

    global pantallaCompleta

    if estado == 0:
        root.wm_state("iconic")
    else:
        root.wm_state("zoomed")


def fuente(e):
    fuenteNegrita = font.Font(cajaTexto, cajaTexto.cget("font"))
    fuenteNegrita.configure(weight="bold")

    fuenteCursiva = font.Font(cajaTexto, cajaTexto.cget("font"))
    fuenteCursiva.configure(slant="italic")

    fuenteCursivaYNegrita = font.Font(cajaTexto, cajaTexto.cget("font"))
    fuenteCursivaYNegrita.configure(weight= "bold", slant = "italic")


    cajaTexto.tag_configure("negrita", font = fuenteNegrita)
    cajaTexto.tag_configure("cursiva", font = fuenteCursiva)
    cajaTexto.tag_configure("negritaYcursiva", font = fuenteCursivaYNegrita)


    etiquetasActuales = cajaTexto.tag_names("sel.first")
    
    match e:
        case 0:
            if "negritaYcursiva" in etiquetasActuales:
                cajaTexto.tag_remove("negritaYcursiva", "sel.first", "sel.last")
                cajaTexto.tag_add("cursiva", "sel.first", "sel.last")
                

            elif "negrita" in etiquetasActuales:
                cajaTexto.tag_remove("negrita", "sel.first", "sel.last")
            elif "negrita" not in etiquetasActuales:
                if "cursiva" in etiquetasActuales:
                    cajaTexto.tag_remove("cursiva", "sel.first", "sel.last")
                    cajaTexto.tag_add("negritaYcursiva", "sel.first", "sel.last")
                else:
                    cajaTexto.tag_add("negrita", "sel.first", "sel.last")


        case 1:
            if "negritaYcursiva" in etiquetasActuales:
                cajaTexto.tag_remove("negritaYcursiva", "sel.first", "sel.last")
                cajaTexto.tag_add("negrita", "sel.first", "sel.last")

            elif "cursiva" in etiquetasActuales:
                cajaTexto.tag_remove("cursiva", "sel.first", "sel.last")
            elif "cursiva" not in etiquetasActuales:
                if "negrita" in etiquetasActuales:
                    cajaTexto.tag_remove("negrita", "sel.first", "sel.last")
                    cajaTexto.tag_remove("cursiva", "sel.first", "sel.last")
                    cajaTexto.tag_add("negritaYcursiva", "sel.first", "sel.last")
                else:
                    cajaTexto.tag_add("cursiva", "sel.first", "sel.last")           
          

# Ventana de herramientas

ventanaHerramientas = Frame(root)
ventanaHerramientas.pack(fill = Y, side = "left", anchor="nw")


# Ventana principal para el texto

ventanaPrincipal = Frame(root)
ventanaPrincipal.pack(pady=5, side="top", fill="both", expand=True)


# Barra de Scroll

barraScroll = Scrollbar(ventanaPrincipal)
barraScroll.pack(side = RIGHT, fill = Y)

barraScrollHorizontal = Scrollbar(ventanaPrincipal, orient = 'horizontal')
barraScrollHorizontal.pack(side = BOTTOM, fill = X)

# Caja de texto

cajaTexto = Text(ventanaPrincipal, width = 1, height = 1, font=('Helvetica', 16), selectbackground="yellow", selectforeground='black', undo = True, yscrollcommand= barraScroll.set)
cajaTexto.pack(fill="both", expand = True)

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

# Botón de Ventana

menuAcciones_menuVentana = Menu(menuAcciones, tearoff= False)
menuAcciones.add_cascade(label="Ventana", menu= menuAcciones_menuVentana)
menuAcciones_menuVentana.add_command(label = "Maximizar", command = lambda: maxOmin(1))
menuAcciones_menuVentana.add_command(label = "Minimizar", command = lambda: maxOmin(0))


# Botón de Ayuda

menuAcciones_menuAyuda = Menu(menuAcciones, tearoff= False)
menuAcciones.add_cascade(label="Ayuda", menu = menuAcciones_menuAyuda) 
menuAcciones_menuAyuda.add_command(label="Créditos y Contacto", command = lambda: autorInfo(True), accelerator="F1")
menuAcciones_menuAyuda.add_command(label="¿Cómo usar?")

# Botones de la ventana de herramientas

botonNegrita = Button(ventanaHerramientas, text="Negrita", command = lambda: fuente(0))
botonNegrita.grid(row = 0, column = 0, sticky = N, padx = 5)
botonCursiva = Button(ventanaHerramientas, text="Cursiva", command = lambda: fuente(1))
botonCursiva.grid(row = 1, column = 0, padx = 5)


# Barra de Estado

barraEstado = Label(root, text="Listo        ", anchor = E)
barraEstado.pack(fill=X, side = BOTTOM, ipady = 15)


# Atajos

root.bind('<Control-Key-x>', cortar)
root.bind('<Control-Key-x>', copiar)
root.bind('<Control-Key-x>', pegar)
root.bind("<F1>", autorInfo)
root.bind("<Control-Key-b>", lambda e: fuente(0))
root.bind("<Alt-Key-i>", lambda e: fuente(1))

print(os.getcwd())

root.mainloop()
