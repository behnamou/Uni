package main

import (
	"fmt"
	"io"
	"net/http"
	"os"
	"strings"
)

func main() {
	fmt.Println("Enter url: ")
	var url string
	fmt.Scanln(&url)
	url = strings.TrimSpace(url)
	if len(url) == 0 {
		fmt.Println("Please enter a valid url")
		return
	}
	
	fmt.Println("Enter file name: ")
	var fileName string
	fmt.Scanln(&fileName)
	fileName = strings.TrimSpace(fileName)
	if len(fileName) == 0 {
		fmt.Println("Please enter a valid file name")
		return
	}
	fmt.Println("Downloading...")
	resp, err := http.Get(url)
	if err != nil {
		fmt.Println("Error: ", err)
		return
	}
	defer resp.Body.Close()
	file, err := os.Create(fileName)
	if err != nil {
		fmt.Println("Error: ", err)
		return
	}
	defer file.Close()
	io.Copy(file, resp.Body)
	fmt.Println("Download complete")
}
