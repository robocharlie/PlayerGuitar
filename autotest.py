import pywinauto

app = pywinauto.Application().start("notepad.exe")

app.UntiledNotepad.menu_select("Help->About Notepad")
app.AboutNotepad.OK.click()
app.UntitledNotepad.Edit.type_keys("pywinauto Works!", with_spaces = True)



