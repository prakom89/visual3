import PySimpleGUI as sg
sg.theme("DarkGreen4")
sg.theme_text_color("#FFFF00")
window = sg.Window(title="Profile",layout=[[sg.Text("SELAMAT DATANG DI KELAS",font=("Arial",25,"italic","bold","underline"))],
                                           [sg.Text("NPM : 2110010615")],
                                           [sg.Text("Nama : M. BAMBANG TRI PRASODJO")],
                                           [sg.Text("Kelas : 5A NONREG BJM")]],size=(500,200),font=("Times", 18))
window()
window.close()