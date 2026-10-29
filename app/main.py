from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Hello Portal")


@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Hello Portal</title>
      </head>
      <body style="font-family: sans-serif; text-align: center; padding: 60px">
        <h1>Hello from my first app!</h1>
        <p>If you can see this page, the application is running.</p>
        <a href="/api/message">View API response</a>
      </body>
    </html>
    """


@app.get("/api/message")
def message():
    return {"message": "Hello from Aegis!", "application": "hello-portal"}


@app.get("/health")
def health():
    return {"status": "ok"}
