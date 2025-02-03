#coding utf-8

import tkinter as tk
import cores as cr

janela = tk.Tk()

janela.title("Calc parte 1")
janela.geometry("240x350")



frame_visor = tk.Frame(janela, width = 240, height = 50, bg = cr.CorCinzaClaro)
frame_visor.grid(row = 0, column = 0)
valor_visor = tk.StringVar()
valor_visor.set("Calculadora Ligada")
visor_Label = tk.Label(frame_visor, textvariable= valor_visor , width=16, height=2)
visor_Label.place(x=0,y=0)

frame_botoes = tk.Frame(janela, width = 240, height = 300, bg = cr.CorBranco)
frame_botoes.grid(row = 1, column = 0)


botao_11 = tk.Button(frame_botoes , text = "Limpar", width = 11, height = 2)
botao_11.place(x=0,y=0)
botao_12 = tk.Button(frame_botoes , text = "mod", width = 4, height = 2)
botao_12.place(x=116,y=0)
botao_13 = tk.Button(frame_botoes , text = "div", width = 4, height = 2)
botao_13.place(x=176,y=0)

botao_21 = tk.Button(frame_botoes , text = "7", width = 4, height = 2)
botao_21.place(x=0,y=52)
botao_22 = tk.Button(frame_botoes , text = "8", width = 4, height = 2)
botao_22.place(x=60,y=52)
botao_23 = tk.Button(frame_botoes , text = "9", width = 4, height = 2)
botao_23.place(x=120,y=52)
botao_24 = tk.Button(frame_botoes , text = "*", width = 4, height = 2)
botao_24.place(x=180,y=52)

botao_31 = tk.Button(frame_botoes , text = "4", width = 4, height = 2)
botao_31.place(x=0,y=52*2)
botao_32 = tk.Button(frame_botoes , text = "5", width = 4, height = 2)
botao_32.place(x=60,y=52*2)
botao_33 = tk.Button(frame_botoes , text = "6", width = 4, height = 2)
botao_33.place(x=120,y=52*2)
botao_34 = tk.Button(frame_botoes , text = "/", width = 4, height = 2)
botao_34.place(x=180,y=52*2)

botao_41 = tk.Button(frame_botoes , text = "1", width = 4, height = 2)
botao_41.place(x=0,y=52*3)
botao_42 = tk.Button(frame_botoes , text = "2", width = 4, height = 2)
botao_42.place(x=60,y=52*3)
botao_43 = tk.Button(frame_botoes , text = "3", width = 4, height = 2)
botao_43.place(x=120,y=52*3)
botao_44 = tk.Button(frame_botoes , text = "-", width = 4, height = 2)
botao_44.place(x=180,y=52*3)

botao_51 = tk.Button(frame_botoes , text = "0", width = 4, height = 2)
botao_51.place(x=0,y=52*4)
botao_52 = tk.Button(frame_botoes , text = "00", width = 4, height = 2)
botao_52.place(x=60,y=52*4)
botao_53 = tk.Button(frame_botoes , text = ".", width = 4, height = 2)
botao_53.place(x=120,y=52*4)
botao_54 = tk.Button(frame_botoes , text = "+", width = 4, height = 2)
botao_54.place(x=180,y=52*4)

botao_64 = tk.Button(frame_botoes , text = "=", width = 25, height = 1)
botao_64.place(x=5,y=52*5)

janela.mainloop()