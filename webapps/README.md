# Redis superb web app

```
docker build -t webapp .
```

## With Link

```
docker run -d --name redis -p 6379:6379 redis
docker run -d --link redis -p 5000:5000 webapp
```

## Without links, using networks

By default, creates network of type bridge

```
docker network create foobar
```

start containers

```
docker run -d --name redis -p 6379:6379 --net foobar redis
docker run -d --net foobar -p 5000:5000 webapp
```



