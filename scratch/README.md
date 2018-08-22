
Build the program in linux:

```
$ go build hello.go
```

Or do a cross build with [gox](https://github.com/mitchellh/gox):

```
gox -osarch="linux/amd64" --output="hello-linux"
```

Build the image

```
$ docker build -t hello .
```

Run the image

```
$ docker run hello
```
