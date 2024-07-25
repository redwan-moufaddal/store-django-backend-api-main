
**For Windows:**

Install Python from this link:
[Python 3.11.7 for Windows (64-bit)](https://www.python.org/ftp/python/3.11.7/python-3.11.7-amd64.exe)

Click "Add Python to PATH" during installation.
![Installation](https://drive.google.com/uc?id=16vTamdftEamnadoVWt8YLPaSH4zI8XsF)

After installation, create a folder named 'backend' and add these files and folders into it.

Navigate to the 'backend' folder in your command prompt or terminal.

If you have Git installed, open Git Bash:
```bash
py -m venv env
source env/Scripts/activate
py manage.py runserver
```

If Git is not installed, open Command Prompt:
```cmd
python -m venv env
env\Scripts\activate.bat
python manage.py runserver
```

**For macOS:**

Install Python from this link:
[Python 3.11.7 for macOS](https://www.python.org/ftp/python/3.11.7/python-3.11.7-macosx10.9.pkg)

During installation, ensure "Add Python 3.11 to PATH" is selected.

After installation, create a folder named 'backend' and add your files and folders into it.

Navigate to the 'backend' folder in your terminal.

If you have Git installed, open Terminal:
```bash
python3 -m venv env
source env/bin/activate
python manage.py runserver
```

If Git is not installed, open Terminal:
```bash
python3 -m venv env
source env/bin/activate
python manage.py runserver
```

Now you can start using your API.
