import tkinter
from tkinter import *  # Se importa la libreria tkinter que permite generar una interfaz gráfica
from tkinter import ttk

import matplotlib.pyplot as plt  # Se importa la libreria que permite generar el gráfico
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import numpy as np  # Se importa la libreria que permite dar valores númericos a las funciones matemáticas


def cilindro():
    try:
        borrar()
    except:
        pass
    grafico()
    color = color_grafico()
    ax = figure.add_subplot(111, projection="3d")
    ax.set_xlabel('Eje X')
    ax.set_ylabel('Eje Y')
    ax.set_zlabel('Eje Z')
    ax.set_title('Cilindro')
    x = np.linspace(-1, 1, 200)
    z = np.linspace(-2, 2, 200)
    Xc, Zc = np.meshgrid(x, z)
    Yc = np.sqrt(1 - Xc ** 2)
    ax.plot_surface(Xc, Yc, Zc, rstride=10, cstride=10, color=color)  # Mitad delantera
    ax.plot_surface(Xc, -Yc, Zc, rstride=10, cstride=10, color=color)  # Mitad trasera


def esfera():
    try:
        borrar()
    except:
        pass
    grafico()
    color = color_grafico()
    ax = figure.add_subplot(111, projection="3d")
    ax.set_xlabel('Eje X')
    ax.set_ylabel('Eje Y')
    ax.set_zlabel('Eje Z')
    ax.set_title('Esfera')
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = 2 * np.outer(np.cos(u), np.sin(v))
    y = 2 * np.outer(np.sin(u), np.sin(v))
    z = 2 * np.outer(np.ones(np.size(u)), np.cos(v))
    ax.plot_surface(x, y, z, rstride=4, cstride=4, color=color)


def elipsoide():
    try:
        borrar()
    except:
        pass
    grafico()
    color = color_grafico()
    ax = figure.add_subplot(111, projection="3d")
    ax.set_xlabel('Eje X')
    ax.set_ylabel('Eje Y')
    ax.set_zlabel('Eje Z')
    ax.set_title('Elipsoide')
    coefs = (1, 2, 2)
    rx, ry, rz = 1 / np.sqrt(coefs)
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = rx * np.outer(np.cos(u), np.sin(v))
    y = ry * np.outer(np.sin(u), np.sin(v))
    z = rz * np.outer(np.ones_like(u), np.cos(v))
    ax.plot_surface(x, y, z, rstride=4, cstride=4, color=color)
    max_radius = max(rx, ry, rz)
    for axis in 'xyz':
        getattr(ax, 'set_{}lim'.format(axis))((-max_radius, max_radius))


def hiperboloide_1h():
    try:
        borrar()
    except:
        pass
    grafico()
    color = color_grafico()
    x1 = np.linspace(-4, 4, 50)
    y1 = np.linspace(-4, 4, 50)
    X, Y = np.meshgrid(x1, y1)
    Z = np.sqrt(4 * (1 + X ** 2 + (Y ** 2) / 2))
    ax = figure.add_subplot(111, projection="3d")
    ax.set_xlabel('Eje X')
    ax.set_ylabel('Eje Y')
    ax.set_zlabel('Eje Z')
    ax.set_title('Hiperboloide de una hoja')
    ax.plot_surface(X, Y, Z, color=color)


def hiperboloide_2h():
    try:
        borrar()
    except:
        pass
    grafico()
    color = color_grafico()
    x1 = np.linspace(-4, 4, 50)
    y1 = np.linspace(-4, 4, 50)
    X, Y = np.meshgrid(x1, y1)
    Z = np.sqrt(4 * (1 + X ** 2 + (Y ** 2) / 2))
    ax = figure.add_subplot(111, projection="3d")
    ax.set_xlabel('Eje X')
    ax.set_ylabel('Eje Y')
    ax.set_zlabel('Eje Z')
    ax.set_title('Hiperboloide de dos hojas')
    ax.plot_surface(X, Y, Z, color=color)
    ax.plot_surface(X, Y, -Z, color=color)


def cono_eliptico():
    try:
        borrar()
    except:
        pass
    grafico()
    color = color_grafico()
    x1 = np.linspace(-2, 2, 50)
    y1 = np.linspace(-2, 2, 50)
    X, Y = np.meshgrid(x1, y1)
    Z = np.sqrt(4 * (X ** 2 + (Y ** 2) / 2))
    ax = figure.add_subplot(111, projection="3d")
    ax.set_xlabel('Eje X')
    ax.set_ylabel('Eje Y')
    ax.set_zlabel('Eje Z')
    ax.set_title('Cono Elíptico')
    ax.plot_surface(X, Y, Z, color=color)


def paraboloide_eliptico():
    try:
        borrar()
    except:
        pass
    grafico()
    color = color_grafico()
    x1 = np.linspace(-4, 4, 50)
    y1 = np.linspace(-4, 4, 50)
    X, Y = np.meshgrid(x1, y1)
    Z = X ** 2 + Y ** 2
    ax = figure.add_subplot(111, projection="3d")
    ax.set_xlabel('Eje X')
    ax.set_ylabel('Eje Y')
    ax.set_zlabel('Eje Z')
    ax.set_title('Paraboloide Elíptico')
    ax.plot_surface(X, Y, Z, color=color)


def paraboloide_hiperbólico():
    try:
        borrar()
    except:
        pass
    grafico()
    color = color_grafico()
    x1 = np.linspace(-4, 4, 500)
    y1 = np.linspace(-4, 4, 500)
    X, Y = np.meshgrid(x1, y1)
    Z = Y ** 2 - X ** 2
    ax = figure.add_subplot(111, projection="3d")
    ax.set_xlabel('Eje X')
    ax.set_ylabel('Eje Y')
    ax.set_zlabel('Eje Z')
    ax.set_title('Paraboloide Hiperbólico')
    ax.plot_surface(X, Y, Z, color=color)


# Grafico Funcion Z
def graficar():
    try:
        borrar()
    except:
        pass
    grafico()
    color = color_grafico()
    replacements = {
        'sin': 'np.sin',
        'cos': 'np.cos',
        'exp': 'np.exp',
        'sqrt': 'np.sqrt',
        '^': '**',
        'ln': 'np.log',
        'tan': 'np.tan',
    }
    z1 = parametros_z1.get()
    for old, new in replacements.items():
        z1 = z1.replace(old, new)
    x1 = np.linspace(-4, 4, 50)
    y1 = np.linspace(-4, 4, 50)
    X, Y = np.meshgrid(x1, y1)
    Z = eval(z1)
    ax = figure.add_subplot(111, projection="3d")
    ax.set_xlabel('Eje X')
    ax.set_ylabel('Eje Y')
    ax.set_zlabel('Eje Z')
    ax.set_title('Z= f(X,Y)')
    ax.plot_surface(X, Y, Z, color=color)


# Paramétrica
def graficar_parametrica():
    try:
        borrar()
    except:
        pass
    grafico()
    color = color_grafico()
    replacements = {
        'sin': 'np.sin',
        'cos': 'np.cos',
        'exp': 'np.exp',
        'sqrt': 'np.sqrt',
        '^': '**',
    }
    x1 = parametros_x.get()
    y1 = parametros_y.get()
    z1 = parametros_z.get()
    for old, new in replacements.items():
        x1 = x1.replace(old, new)
        y1 = y1.replace(old, new)
        z1 = z1.replace(old, new)
    ax = figure.add_subplot(111, projection="3d")
    ax.set_xlabel('Eje X')
    ax.set_ylabel('Eje Y')
    ax.set_zlabel('Eje Z')
    ax.set_title('Curva Paramétrica')
    u = np.linspace(0, 90, 100)
    v = np.linspace(0, 90, 100)
    u, v = np.meshgrid(u, v)
    x = eval(x1)
    y = eval(y1)
    z = eval(z1)
    ax.plot_surface(x, y, z, color=color)
    # ax.plot_surface(-x, -y, -z, color=color)


color_fondo = "light sky blue"
color_hover = "deep sky blue"


def on_leave(e):
    botonExp2["background"] = color_fondo
    botonExpn["background"] = color_fondo
    botonRaiz["background"] = color_fondo
    botonAbs["background"] = color_fondo
    botonLn["background"] = color_fondo
    botonLogn["background"] = color_fondo
    botonLog10["background"] = color_fondo
    botonEn["background"] = color_fondo
    botonGenerar["background"] = color_fondo
    botonGenerarP["background"] = color_fondo


ventana = Tk()  # Se le da un nombre al atributo TK de tkinter, ya que es el que ayudara a generar el resto de atributos
ventana.title("Gráficas en Python")  # Título de la ventana
ventana.resizable(0, 0)  # Opción para que la ventana no pueda cambiarse de tamaño.
ventana.geometry("1000x550")  # Dimensiones de la ventana
ventana.config(bg="white")  # Fondo de la interfaz

pestañas = ttk.Notebook(ventana)

FramePrincipal = Frame(pestañas, width=600, height=500, bg="white")
FramePrincipal.pack(expand='false', side='left', fill='both')
miFrame = Frame(FramePrincipal, width=600, height=500, bg="white")  # Contenedor frame
miFrame.pack(expand='false', side='left', fill='both')  # Empaqueta conetenedor para poder utilizarlo


pestañas.pack(expand='true', side='right', fill='both')
parametros_x = StringVar()
parametros_y = StringVar()
parametros_z = StringVar()
labelT1 = Label(miFrame, text="Curva paramétrica", font=20, bg="white")  # Label que contiene el texto función
labelT1.grid(row=0, column=1, columnspan=2)  # Se usa grid, filas columnas que ocupa el componente
labelX = Label(miFrame, text="X:", font=20, bg="white")  # Label que contiene el texto función
labelX.grid(row=1, column=0)  # Se usa grid, filas columnas que ocupa el componente
cuadroX = Entry(miFrame, font=20, highlightthickness=2, textvariable=parametros_x)  # Cuadro de texto de la función
cuadroX.grid(row=1, column=1, columnspan=2)  # Se usa grid, filas columnas que ocupa el componente
labelY = Label(miFrame, text="Y:", font=20, bg="white")  # Label que contiene el texto función
labelY.grid(row=2, column=0)  # Se usa grid, filas columnas que ocupa el componente
cuadroY = Entry(miFrame, font=20, highlightthickness=2, textvariable=parametros_y)  # Cuadro de texto de la función
cuadroY.grid(row=2, column=1, columnspan=2)  # Se usa grid, filas columnas que ocupa el componente
labelZ = Label(miFrame, text="Z:", font=20, bg="white")  # Label que contiene el texto función
labelZ.grid(row=3, column=0)  # Se usa grid, filas columnas que ocupa el componente
cuadroZ = Entry(miFrame, font=20, highlightthickness=2, textvariable=parametros_z)  # Cuadro de texto de la función
cuadroZ.grid(row=3, column=1, columnspan=2)  # Se usa grid, filas columnas que ocupa el componente


def on_enter_bgp(e):
    botonGenerarP["background"] = color_hover


botonGenerarP = Button(miFrame, text="Graficar", bg=color_fondo,
                       command=lambda: graficar_parametrica())  # Boton graficar
botonGenerarP.grid(row=2, column=3)  # Se usa grid, filas columnas que ocupa el componente
botonGenerarP.bind("<Enter>", on_enter_bgp)
botonGenerarP.bind("<Leave>", on_leave)

parametros_z1 = StringVar()
labelT2 = Label(miFrame, text="Z = f(X,Y)", font=20, bg="white")  # Label que contiene el texto función
labelT2.grid(row=4, column=1, columnspan=2)  # Se usa grid, filas columnas que ocupa el componente


def on_enter_bg(e):
    botonGenerar["background"] = color_hover


botonGenerar = Button(miFrame, text="Graficar", bg=color_fondo, command=lambda: graficar())  # Boton graficar
botonGenerar.grid(row=5, column=3)  # Se usa grid, filas columnas que ocupa el componente
botonGenerar.bind("<Enter>", on_enter_bg)
botonGenerar.bind("<Leave>", on_leave)
labelZ1 = Label(miFrame, text="Z:", font=20, bg="white")  # Label que contiene el texto función
labelZ1.grid(row=5, column=0)  # Se usa grid, filas columnas que ocupa el componente
cuadroZ1 = Entry(miFrame, font=20, highlightthickness=2, textvariable=parametros_z1)  # Cuadro de texto de la función
cuadroZ1.grid(row=5, column=1, columnspan=2)  # Se usa grid, filas columnas que ocupa el componente

miFrame2 = Frame(FramePrincipal, width=400, height=500, bg="white")  # Contenedor frame
miFrame2.pack(expand='true', side='right', fill='both')  # Empaqueta conetenedor para poder utilizarlo
labelTG = Label(miFrame2, text="Gráfico", font=20, bg="white")  # Label que contiene el texto función
labelTG.pack(side='top')


ventana2 = Frame(pestañas, width=100, height=100, bg="white")
imag = PhotoImage(file="logo_espe.png")
imag = imag.subsample(2)
imagen = Label(ventana2, image=imag)
imagen.config(background='white')
imagen.place(relx=0.34, rely=0)
Materia = Label(ventana2, text="Cálculo Vectorial", font=('Arial', 15),
                bg="white")  # Label que contiene el texto función
Materia.place(relx=0.42, rely=0.2)
Profesor = Label(ventana2, text="Ing. Nikolás Cobo J.", font=('Arial', 15),
                 bg="white")  # Label que contiene el texto función
Profesor.place(relx=0.42, rely=0.25)
TIntegrantes = Label(ventana2, text="Integrantes:", font=('Arial', 15),
                     bg="white")  # Label que contiene el texto función
TIntegrantes.place(relx=0.42, rely=0.35)
Integrantes = Label(ventana2, text="..... \n"

                    , font=('Arial', 12), bg="white")  # Label que contiene el texto función
Integrantes.place(relx=0.42, rely=0.42)

pestañas.add(ventana2, text="Presentación")
pestañas.add(FramePrincipal, text="Graficador")


def grafico():
    global canvas
    global figure
    global toolbar
    figure = plt.Figure(figsize=(5, 4), dpi=110)
    canvas = FigureCanvasTkAgg(figure, miFrame2)
    canvas.get_tk_widget().pack()
    toolbar = NavigationToolbar2Tk(canvas, miFrame2)
    toolbar.config(background='white')
    toolbar.update()
    toolbar.pack(side='left')


def borrar():
    canvas.get_tk_widget().destroy()
    toolbar.destroy()


def on_enter_exp2(e):
    botonExp2["background"] = color_hover


# Botones graficos
botonExp2 = Button(miFrame, text="Cilindro", bg=color_fondo, width=6, command=lambda: cilindro())
botonExp2.grid(row=6, column=0, pady=10)
botonExp2.bind("<Enter>", on_enter_exp2)
botonExp2.bind("<Leave>", on_leave)


def on_enter_expn(e):
    botonExpn["background"] = color_hover


botonExpn = Button(miFrame, text="Esfera", width=6, bg=color_fondo, command=lambda: esfera())
botonExpn.grid(row=6, column=1)
botonExpn.bind("<Enter>", on_enter_expn)
botonExpn.bind("<Leave>", on_leave)


def on_enter_raiz(e):
    botonRaiz["background"] = color_hover


botonRaiz = Button(miFrame, text="Elipsoide", bg=color_fondo, width=8, command=lambda: elipsoide())
botonRaiz.grid(row=6, column=2)
botonRaiz.bind("<Enter>", on_enter_raiz)
botonRaiz.bind("<Leave>", on_leave)


def on_enter(e):
    botonAbs["background"] = color_hover


botonAbs = Button(miFrame, text="Hiperboloide 1H", bg=color_fondo, width=14, command=lambda: hiperboloide_1h())
botonAbs.grid(row=6, column=3)
botonAbs.bind("<Enter>", on_enter)
botonAbs.bind("<Leave>", on_leave)


# Botones logaritmos
def on_enter_ln(e):
    botonLn["background"] = color_hover


botonLn = Button(miFrame, text="Hiperboloide 2H", bg=color_fondo, width=14, command=lambda: hiperboloide_2h())
botonLn.grid(row=7, column=0, padx=10)
botonLn.bind("<Enter>", on_enter_ln)
botonLn.bind("<Leave>", on_leave)


def on_enter_l10(e):
    botonLog10["background"] = color_hover


botonLog10 = Button(miFrame, text="Cono Eliptico", bg=color_fondo, width=12, command=lambda: cono_eliptico())
botonLog10.grid(row=7, column=1)
botonLog10.bind("<Enter>", on_enter_l10)
botonLog10.bind("<Leave>", on_leave)


def on_enter_logn(e):
    botonLogn["background"] = color_hover


botonLogn = Button(miFrame, text="Paraboloide Eliptico", bg=color_fondo, width=16,
                   command=lambda: paraboloide_eliptico())
botonLogn.grid(row=7, column=2)
botonLogn.bind("<Enter>", on_enter_logn)
botonLogn.bind("<Leave>", on_leave)


def on_enter_en(e):
    botonEn["background"] = color_hover


botonEn = Button(miFrame, text="Paraboloide Hiperbólico", bg=color_fondo, width=20,
                 command=lambda: paraboloide_hiperbólico())
botonEn.grid(row=7, column=3, padx=10)
botonEn.bind("<Enter>", on_enter_en)
botonEn.bind("<Leave>", on_leave)

labelCG = Label(miFrame, text="Color del gráfico:", font=("Arial", 12),
                bg="white")  # Label que contiene el texto función
labelCG.grid(column=2, row=9, pady=10)
comboExample = ttk.Combobox(miFrame,
                            values=[
                                "Azul",
                                "Amarillo",
                                "Verde",
                                "Naranja",
                                "Rojo"],
                            state="readonly")
comboExample.grid(column=3, row=9, pady=10)
comboExample.current(0)


def color_grafico():
    color_combo = comboExample.get()
    if color_combo == "Azul":
        color_grafico = 'blue'
    elif color_combo == "Amarillo":
        color_grafico = 'gold'
    elif color_combo == "Verde":
        color_grafico = 'green'
    elif color_combo == "Naranja":
        color_grafico = 'orange'
    elif color_combo == "Rojo":
        color_grafico = 'red'
    return color_grafico



ventana.mainloop()
