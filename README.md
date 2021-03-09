# upload and static server

## start
```
$ docker-compose up -d
```

## upload test
```
curl 127.0.0.1:8080/files -F "files=@./README.md"
# Response:
# { files: [ {'original': 'README.md', 'stored': 'XXXX.md'} ] }
```

## serve test
```
curl 127.0.0.1:80/files/XXXX.md
```
