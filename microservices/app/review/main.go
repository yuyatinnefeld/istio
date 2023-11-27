package main

import (
    "fmt"
    "log"
    "net/http"
)

func main() {
    http.HandleFunc("/", hello)
    fmt.Println("Server started")
    log.Fatal(http.ListenAndServe(":9999", nil))
}

func hello(w http.ResponseWriter, r *http.Request) {
    w.WriteHeader(http.StatusOK)
    w.Header().Set("Content-Type", "application/json")
    w.Write([]byte(`{"app":"review-app", "version": "3.0.0"}`))
}