FROM golang:1.17.5 AS GO_BUILD
ENV CGO_ENABLED 0
WORKDIR /go-app
COPY . /go-app
RUN go mod init go-app
RUN go get golang.org/x/time/rate
RUN go build -o server

FROM alpine:3.15
WORKDIR /go-app
COPY --from=GO_BUILD /go-app/server /go-app/server
EXPOSE 9999
CMD ["./server"]