# Card generator

Generate social media cards for glasnt.com sites. 


## Run server

```
FLASK_ENV=development FLASK_APP=app.py flask run
```

## Run server in docker container

```
docker build . -t cards && docker run --rm -e "PORT=8080" -p 8080:8080
```

## Sample invocations

### For PNG

```
open http://HOST/blog/hot-cold-wet-smoke.png
```

### For HTML (debugging)

```
open http://HOST/blog/hot-cold-wet-smoke.html
```

## Licence

See LICENCE.md
