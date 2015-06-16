package main

import (
    "encoding/json"
    "flag"
    "net/http"
    "runtime"
    "log"

)

type Message struct {
    Message string `json:"message"`
}

const helloWorldString = "Hello, World!"

func main() {
    flag.Parse()
    runtime.GOMAXPROCS(runtime.NumCPU())

    http.HandleFunc("/json", jsonHandler)
    http.ListenAndServe(":9080", Log(http.DefaultServeMux))
}

func Log(handler http.Handler) http.Handler {
    return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
        log.Printf("%s %s %s", r.RemoteAddr, r.Method, r.URL)
        handler.ServeHTTP(w, r)
    })
}

func jsonHandler(w http.ResponseWriter, r *http.Request) {
    w.Header().Set("Content-Type", "application/json")
    json.NewEncoder(w).Encode(&Message{helloWorldString})
}