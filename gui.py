import functions

import PySimpleGUI as me

label=me.Text("Type in a to-do")
input_box=me.InputText(tooltip="Enter todo",key='todo')
add_button=me.Button("Add")

window=me.Window("My To-Do App",layout=[[label],
[input_box, add_button]],
font=('Helvetica',15))


while True:
    event,values=window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos=functions.get_todos()
            new_todo=values['todo']+ "\n"
            todos.append(new_todo)
            functions.write_todos(todos)

        case me.WINDOW_CLOSED:
            break



window.close()


