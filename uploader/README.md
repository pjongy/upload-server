# upload server

## start
```
$ pip install -r requirements.txt
$ UPLOAD_PATH=./files ACCESS_TOKEN=TOKEN uvicorn main:app --host 0.0.0.0 --port 8080
```

## test
```
curl 127.0.0.1:8080/files -F "files=@./README.md" -H "Authorization: Basic TOKEN"
```
