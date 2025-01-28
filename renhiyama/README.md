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

---

## API Endpoints

- GET `/` - Returns a simple hello world message.
- GET `/posts/` - Returns a list of posts.
- GET `/posts/{post_id}` - Returns a single post by ID.
- POST `/posts/{post_id}` - Create a new post. Provide `title` in the request body.
- DELETE `/posts/{post_id}` - Delete a post by ID.

---

## Testing

You can test the API with the provided `test.py` script. Run the script with:

```sh
pytest
```

It will show something like this if everything is working fine:

```sh
=========================================================================== test session starts ===========================================================================
platform linux -- Python 3.13.1, pytest-8.3.4, pluggy-1.5.0
rootdir: /home/ren/coding/cloud-computing/cloud_tasks_probation/renhiyama
plugins: anyio-4.8.0
collected 5 items                                                                                                                                                         

test_main.py .....                                                                                                                                                  [100%]

============================================================================ 5 passed in 0.31s ============================================================================
```