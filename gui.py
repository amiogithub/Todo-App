import functions

import PySimpleGUI as me

label=me.Text("Type in a to-do")
input_box=me.InputText(tooltip="Enter todo")
add_button=me.Button("Add")

window=me.Window("My To-Do App",layout=[[label], [input_box, add_button]])

window.read()
window.close()


