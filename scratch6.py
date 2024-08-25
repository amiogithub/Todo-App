import functions
import time

now=time.strftime("%b %d, %Y %H:%M:%S")
print("it is", now)
print("Routine checkup")

while True:
    user_action = input('Sir/Maam, please type add, show, edit, complete or exit: ')
    user_action = user_action.strip()  # removes additional spaces

    if user_action.startswith('add'):
        todo = user_action[4:]  # Add a newline character at the end

        todos=functions.get_todos()

        todos.append(todo+'\n')

        functions.write_todos(todos)

    elif user_action.startswith('show'):

        todos=functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')  # Remove the newline character when displaying
            row = f'{index + 1} - {item}'
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1  # Adjust for zero-based indexing

            todos=functions.get_todos()

            new_todo = input("Enter new todo: ") + '\n'  # Add a newline character at the end
            todos[number] = new_todo

            functions.write_todos(todos)

        except ValueError:
            print("Oops Your command is valid")
            continue


    elif user_action.startswith('complete'):

        try:
            number =int(user_action[9:])

            todos=functions.get_todos()

            index = number - 1  # Adjust for zero-based indexing
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            print(f'Todo "{todo_to_remove}" was successfully removed from the list.')

        except IndexError:
            print("The task number you are trying to access is not in your to do list")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print(f'The input is not valid at the moment! Please try again -_-')

print('Oyasuminasai Mastermind, Take care!')
