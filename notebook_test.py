from notebook import Notebook, Note
from menu import Menu

menu = Menu()
print('type of Menu object:', type(menu))

print('checking if choices in menu is dictionary:',
      isinstance(menu.choices, dict))
print('type of display_menu function result:', type(menu.display_menu()))
print('possible attributes for Menu object:', dir(menu))
print('menu as a dictionary:', menu.__dict__)

print()
note1 = Note('text of the first note', 'tag1')
note2 = Note('text of the second note', 'tag1 tag2')
note3 = Note('text of the third note', 'tag2')

print('type of the Note object:', type(note1))
print('possible attributes for Note object:', dir(note3))
print('note1 as a dictionary:', note1.__dict__)
print('note2 as a dictionary:', note2.__dict__)

print()
note1_match = note1.match('second note')
note2_match = note2.match('second note')
print('type of result of note.match() function:', type(note1_match))
print('results of match():', note1_match)
print(note2_match)

print()
notebook = menu.notebook
print('type of Notebook object:', type(notebook))
print('possible attributes for Notebook object:', dir(notebook))
print('all the notes in notebook:', notebook.notes)

print()
notebook.new_note(note1.memo, note1.tags)
notebook.new_note(note2.memo, note2.tags)
print('notebook as a dictionary:', notebook.__dict__)
print('type of notes in notebook:', type(notebook.notes))
print('type of a single note in notebook:', type(notebook.notes[0]))
print('all the notes in notebook', notebook.notes)

print()
print('all the notes in notebook as a dictionaries before modifying:')
print([note.__dict__ for note in notebook.notes])
notebook.modify_memo(notebook.notes[0].id, 'modified text of the first note')
notebook.modify_memo(notebook.notes[1].id, 'modified text of the second note')
print('all the notes in notebook as a dictionaries after modifying:')
print([note.__dict__ for note in notebook.notes])
print('type of result of modify() function:', type(notebook.modify_memo(
    notebook.notes[0].id, 'modified text of the first note')))

print()
notebook.modify_tags(notebook.notes[1].id, 'tag1 tag2_modified')
print('all the notes in notebook after modifying tags:',
      [note.__dict__ for note in notebook.notes])

print()
print('result of searching for modified notes:')
print(notebook.search('modified'))
for note in notebook.search('modified'):
    print(note.id, note.memo)
print('type of search() function result:', type(notebook.search('modified')))
