from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import colorchooser
import sys
import os
import webbrowser

if hasattr (sys, '_MEIPASS'):
    os.chdir(sys._MEIPASS)


root = Tk()


root.title("Sin Título - Proyecto Pepino Pre-Alpha 0.3.0")

root.iconbitmap("icon.ico")
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

def llamarNavegador(url):
    webbrowser.open_new(url)

def autorInfo(e):
    # Ventana de informaición de contacto y créditos al autor.

    ventanaAutor = Tk()
    ventanaAutor.title("Información y Contacto")
    ventanaAutor.iconbitmap('icon.ico')

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

    if estado == 0:
        # Minimizada

        root.wm_state("iconic")
    else:
        # Maximizada
        
        root.wm_state("zoomed")

def fuente(e):

    # Estilo Negrita
    fuenteNegrita = font.Font(cajaTexto, cajaTexto.cget("font"))
    fuenteNegrita.configure(weight="bold")

    # Estilo Cursiva
    fuenteCursiva = font.Font(cajaTexto, cajaTexto.cget("font"))
    fuenteCursiva.configure(slant="italic")

    # Estilo Subrayado
    fuenteSubrayado = font.Font(cajaTexto, cajaTexto.cget("font"))
    fuenteSubrayado.configure(underline = 1)

    # Estilo Sobrerayado
    fuenteSobrerayado = font.Font(cajaTexto, cajaTexto.cget("font"))
    fuenteSobrerayado.configure(overstrike= 1)

    # Combinaciones
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

        # Caso en el que se pulse el botón para el estilo Negrita
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
        
        # Caso en el que se pulse el botón para el estilo Cursiva
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

        # Caso en el que se pulse el botón para el estilo Subrayado
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

        # Caso en el que se pulse el botón para el estilo Sobrerayado
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

    # Este es para que al seleccionar una parte del texto, se diferencie del resto de textos
    global contadorEtiquetas

    # Este es para almacenar qué fuente posee el texto cuyo tamaño será modificado
    global contadorFuentes

    # Este es para almacenar qué tamaño posee el texto cuya fuente será modificada
    global contadorTamaños

    if contadorFuentes == None:
        contadorFuentes = 'Helvetica'
    if contadorTamaños == None:
        contadorTamaños = '11'


    # Cambiar fuente
    if e == 0:
        if cajaTexto.tag_ranges('sel'):
            cajaTexto.tag_add(f'etiquetaFamilia_{str(contadorEtiquetas)}', "sel.first", "sel.last")
            cajaTexto.tag_configure(f'etiquetaFamilia_{str(contadorEtiquetas)}', font= (cajaListaFuentes.get(cajaListaFuentes.curselection()), contadorTamaños))
            contadorFuentes = cajaListaFuentes.get(cajaListaFuentes.curselection())
            print(contadorFuentes)
            contadorEtiquetas += 1
        else:
            fuenteCajaTexto.config(family = cajaListaFuentes.get(cajaListaFuentes.curselection()))
            contadorFuentes = cajaListaFuentes.get(cajaListaFuentes.curselection())

    # Cambiar tamaño
    elif e == 1:
        if cajaTexto.tag_ranges('sel'):
            cajaTexto.tag_add(f'etiquetaTamaño_{str(contadorEtiquetas)}', "sel.first", "sel.last")
            print(contadorFuentes)
            cajaTexto.tag_configure(f'etiquetaTamaño_{str(contadorEtiquetas)}', font= (contadorFuentes, cajaListaFuentes_tamaño.get(cajaListaFuentes_tamaño.curselection())))
            contadorTamaños = cajaListaFuentes_tamaño.get(cajaListaFuentes_tamaño.curselection())
            contadorEtiquetas += 1
        else:
            fuenteCajaTexto.config(size = cajaListaFuentes_tamaño.get(cajaListaFuentes_tamaño.curselection()))
            contadorTamaños = cajaListaFuentes_tamaño.get(cajaListaFuentes_tamaño.curselection())

    # Cambiar color
    elif e == 2:
        color = colorchooser.askcolor()[1]

        if cajaTexto.tag_ranges('sel'):
            cajaTexto.tag_add(f'etiquetaColor_{str(contadorEtiquetas)}', "sel.first", "sel.last")
            cajaTexto.tag_configure(f'etiquetaColor_{str(contadorEtiquetas)}', foreground= color)
            contadorEtiquetas += 1
        else:
            cajaTexto.config(fg = color)

    
def estilos():


    # Si la ventana no está colocada, oculta la principal, configura la de estilos, la coloca y luego coloca la principal
    if ventanaHerramientas_ventanaFuentes.winfo_manager() != 'pack':

        ventanaPrincipal.pack_forget()

        ventanaHerramientas_ventanaFuentes.pack(fill= Y, side="left", anchor="w")

        ventanaHerramientas_ventanaFuentes.config(bd = 1, relief = "sunken")

        ventanaPrincipal.pack(pady=5, side="top", fill="both", expand=True)

        ventanaHerramientas_ventanaFuentes_ventanaBotones.grid(row = 3, column=0, columnspan = 3)

        botonNegrita.grid(row = 0, column = 1, padx = 2, pady= 10)

        botonCursiva.grid(row = 0, column = 2, padx = 2)

        botonSubrayado.grid(row = 0, column = 3, padx= 2, pady = 10)

        botonSobrerayado.grid(row= 0, column = 4, padx = 2)

        botonColor.grid(row = 0, column = 5, padx =5 )

        familiaFuentes.grid(row = 0, column = 0, sticky = N, padx = 5, pady= 10)

        familiaFuentes_tamaño.grid(row= 0, column = 1, padx = 5)

        cajaListaFuentes.grid(row=2, column = 0)
        cajaListaFuentes_tamaño.grid(row =2, column = 1)

        for f in font.families():
            cajaListaFuentes.insert('end', f)

        tamaño_Fuentes = [8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64]
        for tamaños in tamaño_Fuentes:
            cajaListaFuentes_tamaño.insert('end', tamaños)

    # En caso contrario la elimina
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


# Ventanas

# Ventana de herramientas

ventanaHerramientas = Frame(root)
ventanaHerramientas.pack(fill = Y, side = "left", anchor="nw")

# Ventana de fuentes y estilos

ventanaHerramientas_ventanaFuentes = Frame(root)
ventanaHerramientas_ventanaFuentes_ventanaBotones = Frame(ventanaHerramientas_ventanaFuentes)

# Ventana principal para el texto

ventanaPrincipal = Frame(root)
ventanaPrincipal.pack(pady=5, side="top", fill="both", expand=True)


# Barra de Scroll

barraScroll = Scrollbar(ventanaPrincipal)
barraScroll.pack(side = RIGHT, fill = Y)

barraScrollHorizontal = Scrollbar(ventanaPrincipal, orient = 'horizontal')
barraScrollHorizontal.pack(side = BOTTOM, fill = X)

# Caja de texto

contadorTamaños = None
contadorFuentes = None
contadorEtiquetas = 0
fuenteCajaTexto = font.Font(family='Helvetica', size="11")
cajaTexto = Text(ventanaPrincipal, width = 1, height = 1, font=fuenteCajaTexto, selectbackground="yellow", selectforeground='black', undo = True, yscrollcommand= barraScroll.set)
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

botonFuentes = Button(ventanaHerramientas, text = "Estilos", command = estilos)
botonFuentes.grid(row = 0, column = 0, sticky = N, padx= 5, pady= 10)

botonNegrita = Button(ventanaHerramientas_ventanaFuentes_ventanaBotones, text="B", command = lambda: fuente(0), width = 2, height = 1)
botonCursiva = Button(ventanaHerramientas_ventanaFuentes_ventanaBotones, text="I", command = lambda: fuente(1), width = 2, height = 1)
botonSubrayado = Button(ventanaHerramientas_ventanaFuentes_ventanaBotones, text= "U", command = lambda: fuente(2), width = 2, height = 1)
botonSobrerayado = Button(ventanaHerramientas_ventanaFuentes_ventanaBotones, text= "O", command = lambda: fuente(3), width = 2, height = 1)
botonColor = Button(ventanaHerramientas_ventanaFuentes_ventanaBotones, text="Color", command = lambda: cambiarFuente(2), width = 4, height = 1)

# Títulos para las cajas de lista de fuentes y la de tamaños respectivamente

familiaFuentes = Label(ventanaHerramientas_ventanaFuentes, text="Elegir Tipografía", font=("Helvetica", 14))
familiaFuentes_tamaño = Label(ventanaHerramientas_ventanaFuentes, text="Tamaño  ", font=("Helvetica", 14))

# Cajas de Lista para seleccionar la fuente y el tamaño

cajaListaFuentes = Listbox(ventanaHerramientas_ventanaFuentes, selectmode= SINGLE, width = 20)


cajaListaFuentes_tamaño = Listbox(ventanaHerramientas_ventanaFuentes, selectmode= SINGLE, width = 10)

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
cajaListaFuentes.bind("<ButtonRelease-1>", lambda e: cambiarFuente(0))
cajaListaFuentes_tamaño.bind("<ButtonRelease-1>", lambda e: cambiarFuente(1))

root.mainloop()
