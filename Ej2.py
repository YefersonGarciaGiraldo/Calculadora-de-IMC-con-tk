import tkinter as tk 
import tkinter.messagebox as messagebox

# Funcion que comprueba que el valor ingresado sea numerico y mayor a 0 y si no lanza una ventana emergente
def Comprobar_valor(texto, etiqueta, titulo):
    try: 
        texto = float(texto)
        if texto <= 0:
            messagebox.showerror("Valor invalido", f"El valor no puede ser menor igual que 0 ({titulo.cget("text")})")
            return
        etiqueta.set(texto)
    except ValueError:
        messagebox.showerror("Valor invalido", f"Se esperaba un valor numerico ({titulo.cget("text")})")
   

# funcion para obtener los datos de entrada y ejecutar la funcion del imc
def Obtener_datos():
    def Obtener_peso():
        texto_peso = entrada_peso.get()
        Comprobar_valor(texto_peso,peso,titulo_peso)

    def Obtener_altura():
        texto_altura = entrada_altura.get()
        Comprobar_valor(texto_altura,altura,titulo_altura)
    Obtener_altura()
    Obtener_peso()
    valor_altura = altura.get()
    valor_peso = peso.get()
    Calcular_imc(valor_altura, valor_peso)

# funcion para calcular y categorizar segun el IMC
def Calcular_imc(altura,peso):
    imc = peso / (altura **2)
    imprimir_resultado.configure(bg="#efefef",bd=1,relief="solid", font=(10))
    if imc <= 18.5: categoria = "Bajo peso"
    elif 18.6 <= imc <= 24.9:
        categoria = "Peso normal"
    elif 25.0 <= imc <= 29.9:
        categoria = "Sobrepeso"
    elif 30.0 <= imc <= 34.9:
        categoria = "Obesidad grado 1"
    elif 35.0 <= imc <= 39.9:
        categoria = "Obesidad grado 2"
    elif imc >= 40.0:
        categoria = "Obesidad 3"
    imprimir_resultado.configure(text= f"Su IMC es: {round(imc,3)} ({categoria}) \n Peso: {peso} \n Altura: {altura}" )

# ventana principal
ventana = tk.Tk()
ventana.title ("Calculadora IMC")
ventana.geometry("500x500")

### contenedor principal ###
contenedor_principal = tk.Frame(ventana, width=300, height=200)
contenedor_principal.place(relx=0.5, rely=0.5, anchor="center")

### contenedor para los contenedores de peso y altura ###
contenedor_datos = tk.Frame(contenedor_principal)
contenedor_datos.pack()

### contenedor datos peso ###
contenedor_peso = tk.Frame(contenedor_datos)
contenedor_peso.configure()
contenedor_peso.pack(side="left", padx=10)

# titulo de contenedor de peso
titulo_peso = tk.Label(contenedor_peso, text="Peso en Kilo gramos", font=(30), pady=10)
titulo_peso.pack()

# etiqueta de peso
peso = tk.DoubleVar()
peso.set("--")
etiqueta_peso = tk.Label(contenedor_peso, font=(20))
etiqueta_peso.configure(textvariable=peso)
etiqueta_peso.pack()

# entrada peso
entrada_peso = tk.Entry(contenedor_peso, width=30)
entrada_peso.pack(pady=5)

### contenedor de altura ###
contenedor_altura = tk.Frame(contenedor_datos)
contenedor_altura.configure()
contenedor_altura.pack(side="left", padx=10)

# Titulo de contenedor altura
titulo_altura = tk.Label(contenedor_altura, text="Altura en metros", font=(30), pady=10)
titulo_altura.pack()

# etiqueta de valor altura
altura = tk.DoubleVar()
altura.set("--")
etiqueta_altura = tk.Label(contenedor_altura, font=(20))
etiqueta_altura.configure(textvariable=altura)
etiqueta_altura.pack()

# entrada altura
entrada_altura = tk.Entry(contenedor_altura, width=30)
entrada_altura.pack(pady=5)

# configurar enter 
ventana.bind("<Return>", lambda event: Obtener_datos())

# boton calcular imc
boton_calcularimc = tk.Button(contenedor_principal,pady=10, text="CALCULAR IMC", command=Obtener_datos)
boton_calcularimc.pack(side="bottom", pady=10)

# etiqueta de impresion de datos
imprimir_resultado = tk.Label(contenedor_principal, text="")
imprimir_resultado.pack(side="bottom")

# ciclo de ejecucion 
ventana.mainloop()