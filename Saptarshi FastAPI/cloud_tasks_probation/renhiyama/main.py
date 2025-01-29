from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

# Rest API example - posts CRUD.


posts = []


@app.get("/posts/{post_id}")
def read_post(post_id: int):
    for post in posts:
        if post["id"] == post_id:
            return post
    return {"error": "Post not found"}


@app.get("/posts")
def read_posts():
    return posts


@app.post("/posts/{post_id}")
def create_post(post_id: int, title: str):
    post = {"id": post_id, "title": title}
    # if post id already exists, return error
    for post in posts:
        if post["id"] == post_id:
            return {"status": "error"}
    posts.append(post)
    return {"status": "success", "post": post}


@app.delete("/posts/{post_id}")
def delete_post(post_id: int):
    global posts
    new_posts = [post for post in posts if post["id"] != post_id]
    if len(new_posts) == len(posts):
        return {"status": "error", "message": "Post not found"}
    posts = new_posts
    return {"status": "success"}