import functions
import time
import PySimpleGUI as me
label=me.Text('',key='clock')

me.theme("DarkPurple4")


clock=me.Text("Type in a to-do")
input_box=me.InputText(tooltip="Enter todo",key='todo')
add_button=me.Button("Add",size=10)
list_box=me.Listbox(values=functions.get_todos(), key='todos',enable_events=True,
                    size=[45,10])

edit_button=me.Button("Edit")

complete_button=me.Button("Complete")

exit_button=me.Button("Exit")

window=me.Window("My To-Do App",layout=[[clock],
                                        [label],
[input_box, add_button],[list_box,edit_button,complete_button],
[exit_button]],
font=('Helvetica',15))


while True:
    event,values=window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    print(event)
    print(values)
    match event:
        case "Add":
            todos=functions.get_todos()
            new_todo=values['todo']+ "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            try:

                 todo_to_edit=values['todos'][0]
                 new_todo=values['todo']

                 todos=functions.get_todos()
                 index=todos.index(todo_to_edit)
                 todos[index]=new_todo
                 functions.write_todos(todos)
                 window['todos'].update(values=todos)
            except IndexError:
                me.popup("Select an item first",font=('Helvetica',15))



        case "Complete":

            try:
                todo_to_complete=values['todos'][0]
                todos=functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                me.popup("Select an item first", font=('Helvetica', 15))


        case "Exit":
            break



        case 'todos':
            window['todo'].update(value=values['todos'][0])












        case me.WINDOW_CLOSED:
            break









window.close()


