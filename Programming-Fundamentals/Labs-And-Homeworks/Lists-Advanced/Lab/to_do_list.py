#def process_todo_notes():
  #  todo_notes = []

  #  while True:
        #note = input()

  #      if note == "End":
            #break

 #       todo_notes.append(note)

#        sorted_notes = sorted(todo_notes, key=lambda x: int(x.split("-")[0]))
#        return [note.split("-")[1] for note in sorted_notes]

#result = process_todo_notes()
#print(result)

notes = [0] * 10

while True:
    command = input()

    if command == "End":
        break

    tokens = command.split("-")
    priority = int(tokens[0]) - 1
    note = tokens[1]
    notes.pop(priority)
    notes.insert(priority, note)

result = [element for element in notes if element != 0]
print(result)