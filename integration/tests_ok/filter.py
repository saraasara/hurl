from app import app


@app.route("/filter")
def filter():
    return """{
  "list": [1,2,3],
  "message": "Hello Bob!",
  "url": "https://mozilla.org/?x=шеллы",
  "encoded_url": "https://mozilla.org/?x=%D1%88%D0%B5%D0%BB%D0%BB%D1%8B",
  "id": "123",
  "score": 1.6
}"""
