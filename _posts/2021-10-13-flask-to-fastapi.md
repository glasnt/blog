---
title: Migrating from Flask to FastAPI
---

<style>
.highlight span { white-space: unset !important; }
</style>

I recently had the urge to try out FastAPI, and reading the docs I saw how similar it looked to Flask. So I thought, since I have this small demo I'm working on that is basically an API with a nice HTML front-end, how hard would it be to migrate? 

*Note*: this was for a **demo**, so while the below works, *it may not be the best solution in all cases*.

*This post uses the `diff` format. If you're unfamiliar: lines starting `-` were removed, lines starting with `+` were added*.

The tips I've picked up: 


## Web Server

Because you're going to be dealing with `async` by default, if you're using `gunicorn` you're going to have to replace that with `uvicorn`. Same format though: 

```diff
-$ gunicorn app:app --reload

+$ uvicorn app:app --reload
```

## Application object

This one is fairly simple: just replace Flask with FastAPI: 

```diff
-app = Flask(__name__)
+app = FastAPI()
```

## Route methods

FastAPI is pedantic. Well, that is to say it's **py**dantic, making use of the `pydantic` package for data validation through type annotations. 

If you haven't use type annotations before, checkout the [`typing` docs](https://docs.python.org/3/library/typing.html).

In a practical sense, if you've been relying on Flask's `request` without declaring it in your method signatures, you'll have to do that. You'll also have to declare your methods as `async`. 

```diff
@app.get("/")
- def index():
+ async def index(request: Request):
     if request: 

```

## Json responses

You can drop the `jsonify`, if you want to return a dict to the user.

```diff
- return jsonify(response)
+ return response
```

## Templates

You can use [Jinja2 in FastAPI](https://fastapi.tiangolo.com/advanced/templates/), you just need to be a bit more specific: 

Loading templates: explicitly tell it where to pull files: 

```diff
+ from fastapi.templating import Jinja2Templates
+ templates = Jinja2Templates(directory="templates")
```  

Linking static in templates: you just need to replace `filename` with `path`: 

```diff
- url_for('static', filename='theming.js')
+ url_for('static', path='theming.js')
```

Be wary here, though! While this function reads the same, this will generate absolute URLs, and may not correctly pick up your scheme (HTTP vs HTTPS). In my case, I got "mixed content" errors. I worked around this temporarily by hardcoding the URLs, which may not be the best solution long term.

## Uploads

This one is going to be harder. 

Because of the type annotation earlier, you need to be very explicit with what you want the user to provide. You will also be questioned on the values used in your HTML form before you proceed. 

In my case, I wanted to allow either a file upload or a curl of a JSON file, so these are the changes I needed to make. 

For the form itself, I originally had: 

```
<input type="file" id="upload_file" name="upload">
```

So `upload` must be in the method signature. 

I also needed to change the way I redirect. You can do [redirect responses](https://fastapi.tiangolo.com/advanced/custom-response/?h=redirectresponse#redirectresponse), but in my case I'm using a GET-only route as a failure case for a POST-only route, so I need to explicitly set the status code here to not pass-through the POST method and get a routing error.

```diff
@app.post("/upload")
-def upload():
-    if "upload" not in request.files:
-        return redirect(request.url)
-    upload = request.files["upload"]
-    data = json.loads(upload.read())
+async def preapprove_upload(request: Request, upload: bytes = File(...)):
+    if not upload:
+       return RedirectResponse('/', status_code=303)
+    data = json.loads(upload)
```

You'll also need to include the `multipart-upload` package if you're doing complex upload things.


## Curl Endpoint

This also required some changes, but it also did some processing for me. 

By specifying `Body` it pre-processed the data for me, so I didn't have to worry about JSON processing: 

```diff
 @app.post("/preapprove")
-def preapprove():
-    if request.data:
-        response = apply_business_logic(json.loads(request.data))
+async def preapprove(data: dict = Body(...)):
+    if data:
+        response = apply_business_logic(data)
```

# Thoughts

This wasn't as bad as it could be. Having frameworks follow similar patterns helps, but it's those nuances that'll get you every time. 

Though now I have fancy API documentation for free, so it's probably worth it :)

