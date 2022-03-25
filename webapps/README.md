# Redis superb web app

```
docker build -t webapp .
```

## Network and start containers

By default, creates network of type bridge

```
docker network create foobar
```

start containers

```
docker run -d --name redis -p 6379:6379 --net foobar redis
docker run -d --net foobar -p 5000:5000 webapp
```



