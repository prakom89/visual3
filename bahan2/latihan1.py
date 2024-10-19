import PySimpleGUI as sg

window = sg.Window(title="Profile",layout=[[sg.Text("NPM : 2110010615")],
                                           [sg.Text("Nama : M. BAMBANG TRI PRASODJO")],
                                           [sg.Text("Kelas : 5A NONREG BJM")],
                                           [sg.Text("Matkul : Pemrograman Visual 3")]],size=(400,200))
window()
window.close()