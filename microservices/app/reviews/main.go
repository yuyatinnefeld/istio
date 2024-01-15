package main

import (
	"fmt"
	"io"
	"net/http"
	"sync"

	"golang.org/x/time/rate"
)

var limiter = rate.NewLimiter(rate.Limit(5), 1) // Adjust the rate limit as needed
var mu sync.Mutex

func main() {
	port := 9999
	http.HandleFunc("/", MyHandler)
	fmt.Printf("Serving on port %d..\n", port)
	http.ListenAndServe(fmt.Sprintf(":%d", port), nil)
}

func MyHandler(w http.ResponseWriter, r *http.Request) {
	mu.Lock()
	defer mu.Unlock()

	// Rate limiting
	if !limiter.Allow() {
		http.Error(w, "Too many requests. Please try again later.", http.StatusTooManyRequests)
		return
	}

	// Logging IP address of request to stdout
	fmt.Println("Request received from:", r.RemoteAddr)

	// Displaying JSON string
	response := `{"app": "reviews", "version": "1.0.0", "language": "golang"}`

	// Sending response
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusOK)
	io.WriteString(w, response)
}
