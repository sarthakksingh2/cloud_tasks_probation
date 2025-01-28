# Sayantan Das

This is a sample fastapi hello world app.

I suggest using Python Venv to install dependencies, so your OS will not be affected by the dependencies. (Python loves to break linux systems sometimes 😅)
Setup Venv with:

```sh
python3 -m venv venv
# On Linux/MacOS
source venv/bin/activate
# On Windows
venv\Scripts\activate
```

Then install the dependencies with:

```sh
pip install -r requirements.txt
```

---

## You always need to run the `activate` command to activate the virtual environment before running the app, whenever you open a new terminal.

After setting up everything, you should be able to run the app with:

```sh
fastapi dev main.py
```

This will open a dev server on `http://127.0.0.1:8000`
