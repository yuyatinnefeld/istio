package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"os"
	"sync"

	"golang.org/x/time/rate"
)

var limiter = rate.NewLimiter(rate.Limit(5), 1) // Adjust the rate limit as needed
var mu sync.Mutex

type Response struct {
	AppName    string `json:"appName"`
	Language   string `json:"language"`
	Version    string `json:"version"`
	Message    string `json:"message"`
	Enviroment string `json:"env"`
	PodID      string `json:"podID"`
}

func setEnvOrDefault(envName string, defaultValue string) string {
	if val, ok := os.LookupEnv(envName); ok {
		return val
	}
	return defaultValue
}

func fetchAPIResource(w http.ResponseWriter, r *http.Request) {
	appName := "reviews"
	language := "golang"

	version := setEnvOrDefault("VERSION", "0.0.0")
	message := setEnvOrDefault("MESSAGE", "MESSAGE_NOT_DEFINED")
	env := setEnvOrDefault("ENV", "ENV_NOT_DEFINED")
	podID := setEnvOrDefault("MY_POD_NAME", "PODID_NOT_DEFINED")

	mu.Lock()
	defer mu.Unlock()

	// Rate limiting
	if !limiter.Allow() {
		http.Error(w, "Too many requests. Please try again later.", http.StatusTooManyRequests)
		return
	}

	response := Response{
		AppName:  appName,
		Language: language,
		Version:  version,
		Message:  message,
		Enviroment: env,
		PodID:    podID,
	}

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(response)
}

func main() {
	http.HandleFunc("/", fetchAPIResource)
	port := 9999
	fmt.Printf("Serving on port %d..\n", port)
	log.Fatal(http.ListenAndServe(":9999", nil))
}