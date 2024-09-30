# The Beginning Of The ToDos List
try:
    with open('todo.txt', 'r') as file:
        todos = [line.strip() for line in file.readlines()]
except FileNotFoundError:
    todos = ["Get money", "Spend money", "Cry out loud cause you got no money :("]

def save_todos():
    with open('todo.txt', 'w') as file:
        for todo in todos:
            file.write(todo + '\n')

while True:
    print("\nYour current todos are:")
    for index, todo in enumerate(todos, start=1):
        print(f"{index}) {todo}")

    # Ask the user if they want to add or remove a ToDo
    action = input("\nWould you like to add or remove a todo? (type 'add', 'remove', or 'quit' to exit): ").strip().lower()

    if action == 'add':
        new_todo = input("What is your new ToDo? ").strip()
        todos.append(new_todo)
        print(f"'{new_todo}' has been added to the ToDos list.")
        save_todos()  # Save to file
        print("________________________________________________")

    elif action == 'remove':
        try:
            todo_number = int(input("Which number ToDo would you like to remove from the list? ")) - 1
            if 0 <= todo_number < len(todos):
                removed_todo = todos.pop(todo_number)
                print(f"Removed todo: {removed_todo}")
                save_todos()  # Save to file
                print("____________________________________")
            else:
                print("Wrong ToDo number. Try again :(")
        except ValueError:
            print("Please enter a valid number.")

    elif action == 'quit':
        print("Exiting the Todo Tracker. Goodbye! See you later :)")
        break

    else:
        print("Invalid option. Please choose 'add', 'remove', or 'quit'.")
