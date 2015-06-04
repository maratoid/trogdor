package main

import (
    "encoding/json"
    "flag"
    "net/http"
    "runtime"

)

type Message struct {
    Message string `json:"message"`
}

const helloWorldString = "Hello, World!"

func main() {
    flag.Parse()
    runtime.GOMAXPROCS(runtime.NumCPU())

    http.HandleFunc("/json", jsonHandler)
    http.ListenAndServe(":8080", nil)
}

func jsonHandler(w http.ResponseWriter, r *http.Request) {
    w.Header().Set("Content-Type", "application/json")
    json.NewEncoder(w).Encode(&Message{helloWorldString})
}