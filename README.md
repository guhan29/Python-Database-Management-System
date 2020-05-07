```
Requisites:
	1. TKinter.
	2. Pillow.
	* I have used pillow for the icon in the title bar you can just comment the lines if you don't need it.
```
```python
# Line 2
from PIL import ImageTk, Image
# Line 7
win.iconbitmap("icons/dbms.ico")

def showTable():
	# Line 131 in this finction
	tab.iconbitmap("icons/table.ico")
```

# Python-Student-Database-System
Simple python Database-Management-System

# To-Add-Records
* Give an id (primary key) to the new record.
* Make sure you enter integers for Age, Date of Birth, Mobile etc.,
* **If you enter anything wrong it will not accept the data so, it will not clear the data even if you click `Add Records To Database` button.**

# Show Records
* The **Show Records** button will show the `id` and `name` in the bottom box.

# Edit Record
* Enter the `id` to edit the records

# Update Record
* The `Update Record` button will be enabled if you click `Edit Record` with an `id`

# Delete Record
* The procedure is similar to updating the records

# Show Table
* The `Show Table` button opens the table in a new window