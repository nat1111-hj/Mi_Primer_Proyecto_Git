import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Contador de Clics")
ancho_ventana = 720
alto_ventana = 480
ancho_pantalla = ventana.winfo_screenwidth() //3
largo_pantalla = ventana.winfo_screenheight() //3
ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{ancho_pantalla}+{largo_pantalla}")

def configurar_interfaz():
    global etiqueta_clics, etiqueta_tiempo, boton_clic, boton_empezar

    # Etiqueta para el contador de clics
    etiqueta_clics = tk.Label(ventana, text="Número de clics: 0")
    etiqueta_clics.pack(pady=10)
    
    # Etiqueta para el tiempo restante
    etiqueta_tiempo = tk.Label(ventana, text="Tiempo restante: 30s")
    etiqueta_tiempo.pack(pady=10)
    
    # Botón para hacer clic
    boton_clic = tk.Button(ventana, text="¡Haz clic aquí!", command=incrementar_clic, state=tk.DISABLED)
    boton_clic.pack(pady=20)
    
    # Botón para empezar
    boton_empezar = tk.Button(ventana, text="Empezar", command=iniciar_contador)
    boton_empezar.pack(pady=20)

def iniciar_contador():
    global contador_de_clics, tiempo_restante, temporizador_en_curso

    if not temporizador_en_curso:
        contador_de_clics = 0
        tiempo_restante = 30
        etiqueta_clics.config(text=f"Número de clics: {contador_de_clics}")
        etiqueta_tiempo.config(text=f"Tiempo restante: {tiempo_restante}s")
        boton_clic.config(state=tk.NORMAL)
        boton_empezar.config(state=tk.DISABLED)
        temporizador_en_curso = True
        actualizar_temporizador()

def incrementar_clic():
    global contador_de_clics

    if tiempo_restante > 0:
        contador_de_clics += 1
        etiqueta_clics.config(text=f"Número de clics: {contador_de_clics}")

def actualizar_temporizador():
    global tiempo_restante, temporizador_en_curso

    if tiempo_restante > 0:
        tiempo_restante -= 1
        etiqueta_tiempo.config(text=f"Tiempo restante: {tiempo_restante}s")
        ventana.after(1000, actualizar_temporizador)  # Llama a actualizar_temporizador cada 1000ms (1s)
    else:
        boton_clic.config(state=tk.DISABLED)
        boton_empezar.config(state=tk.NORMAL)
        temporizador_en_curso = False
        messagebox.showinfo("Tiempo terminado", f"El tiempo ha terminado. Número final de clics: {contador_de_clics}")



contador_de_clics = 0
tiempo_restante = 30
temporizador_en_curso = False


configurar_interfaz()


ventana.mainloop()
