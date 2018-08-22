
Start mysql with no volumes

```
docker run -d --env MYSQL_ROOT_PASSWORD=root mysql:5.5
```

Exec into the container and create a database

```
docker exec -ti <CONTAINER_ID> mysql -uroot -p
```

Kill the container, restart it and check that the database is still there

```
docker kill
docker restart
```

Remove the container and the database is gone

```
docker kill
docker rm
```

...
