FROM golang AS build
COPY hello.go /tmp/
RUN go build -o /tmp/hello /tmp/hello.go

FROM scratch
COPY --from=build /tmp/hello /
USER 1000
ENTRYPOINT ["/hello"]
