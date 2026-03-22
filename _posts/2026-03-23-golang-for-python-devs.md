---
title: GoLang for Python Devs
---


This post is a text version of the code samples and resources from [Golang for Python Devs](https://www.youtube.com/watch?v=AVxosSFzq5s) by Dana Garifullina from Kiwi PyCon 2016. 

Some resources no longer work, so I've updated to the most accurate thing I can find. 

Some Python samples were Python 2, updated to Python 3. 

Most code OCR'd, may contain translation issues


## Hello World

Python

```python
print("Hello World!")
```

Golang


```go
package main

import "fmt"

func main() {
	fmt.Println("Hello, KiwiPycon!")
}

```

## Lists

Python

```python
# initialise a list
arr = []
# initialise sized List
arr = [0]*12
# add one element
arr.append(20)
arr[0] = 21
# Length of list
len(arr) # 13
# List extending
arr.extend([4, 5, 6])
# get element by index
arr[2] # 0
```

Golang

```go
func main() {
	// initialise a list
	var arr [3]int // ［9, e, 9］
	// change element via index
	arr[0] = 125
	// SLICES - when you don't know size
	// of List
	colours := []string{"red", "blue"}
	// append == recreation
	colours = append(colours, "purple")
	// Length, capacity
	fmt.Println(len(colours))
	fmt.Println(cap(colours))
}
```

## Dictionaries (maps)

Python

```python
#initialisation of dictionary
py_map = {}
# add element
py_map["first_key"] = 25
# delete element
py_map.pop("first_key")
# re-fill
py_map = {"first_key": 26}
# print element
if "first_key" in py_map:
	print(py_map["first_key"])
# or just
print(py_map.get("first_key"))
```

Golang

```go
func main() {
	// initialisation
	go_map := make(map[string]int)
	go_map["first_key"] = 25
	fmt.Println(go_map["first_key"])

	// remove by key
	delete(go_map, "first_key")

	// print element
	if element, ok := go_map["random_key"]; ok {
		fmt.Println(element) // won't be printed
	}
	if element, ok := go_map["first_key"]; ok {
		fmt.Println(element) // 25
	}
}
```



## While Loop
Python
```python
# while Loop
i = 1
while i <= 10:
	print(i)
	i += 1
```
Golang
```go
func main() {
	// Loop from 0 until 10 is reached.
	for i := 1; i <= 10; i++ {
		// Display integer.
		fmt.Println(i)
	}
}
```

## Infinite Loop
Python

```python
# no condition
id = 10
while True:
	if id > 20:
		break
	print(id)
	id +=5
```

Golang
```go
func main() {
	id := 10
	// This Loop continues infinitely until broken.
	for {
		// Break if id is past a certain number.
		if id > 20 {
			break
		}
		fmt.Println(id)
		id += 5
	}
}
```

## Range Loop

Python

```python
#for Loop
for i in range (0, 25):
	print(i)
# other way
names = ["Peter", "Anders", "Bengt"]
for i, name in enumerate (names):
	print("%d. %s" % (i + 1, name))
```

Golang 
```go
func main() {
	names := []string{
		"Peter",
		"Anders",
		"Bengt",
	}
	/* This will print
	1. Peter
	2. Anders
	3. Bengt
	*/
	for i, name := range names {
		fmt.Printf("%d. %s\n", i+1, name)
	}
}
```

## If Statements

Python 
```python
# if-elif-else switches
value = 1.0
if value == 1.0:
	print("This is 1.0 but I will print...")
	value = value + 0.5
if value == 1.5:
	print("One point five")
elif value == 2.5:
	print("Two point five")
else:
	print("Anything else")
```

Golang
```go
func main() {
	value := 1.0
	// Switch on a floating-point value.
	switch value {
	case 1.0:
		fmt.Println("This is 1.0, but i will print...")
		fallthrough
	case 1.5:
		fmt.Println("One point five")
	case 2.5:
		fmt.Println("Two point five")
	default:
		fmt.Println("Anything else")
	}
}
```


## Exceptions

Python

```python
try:
# An error occurs.
	x = 1 / 0
except:
	# Except clause:
	print("Error encountered")
finally:
	# Finally clause:
	print("Finally clause reached")

# another example
while True:
	# Read int from console.
	denominator = int(input())
	# Use int as denominator.
	try:
		i = 1 / denominator
	except:
		print("Error")
	else:
		print("OK")
```

## Error handling

Golang

```go
func explode() {
	// Cause a panic.
	panic("WRONG")
}

func main() {
	// Handle errors in defer func with recover.
	defer func() {
		if err := recover(); err != nil {
			// Handle our error.
			fmt.Println("FIX")
			fmt.Println(" ERR", err)
		}
	}()
	// This causes an error.
	explode()
}
```

```go
Open (name string) (file *File, err error)
f, err := os.Open("filename.ext")
if err != nil {
	log. Fatal(err)
}
// do something with the open *File f
```

## OOP in Go

```go
package main

import "fmt"

type Attendee struct {
	Topic  string
	Person Person
}
type Person struct {
	Name    string
	City    string
	Company string
}

func (a Attendee) SayHi() {
	fmt.Printf("Hi, my name is %s and today I will talk about %s! \n", a.Person.Name, a.Topic)
}

func (a Attendee) About() {
	fmt.Printf("I'm from %s and currently working in %s by the way. \n", a.Person.City, a.Person.Company)
}

func main() {
	guy := Attendee{
		Topic: "Meetings with cookies: never have less then 10",
		Person: Person{
			Name:    "John Doe",
			City:    "Doeville",
			Company: "WeCodes Inc",
		},
	}
	guy.SayHi()
	guy.About()
}
```

## Empty Interfaces

```go
package main
import (
	"fmt"
	"strconv" // for conversions to and from string
)

type Person struct {
	name  string
	age   int
	phone string
}

// Returns a nice string representing a Person
// With this method, Person implements fmt.Stringer

func (p Person) String() string {
	return "<<" + p.name + " - " + strconv.Itoa(p.age) + " years - @" + p.phone + ">>"
}

func main() {
	John := Person{"John", 29, "022-4XX-66X"}
	fmt.Println("This Person is: ", John)
}
```


## Concurrency

```go
import (
	"fmt"
	"time"
)

func main() {
	go sayHello()
	fmt.Println("Going to sleep....ZZzzzzzZZ")
	//make main last a little bit more
	time.Sleep(6 * time.Second)
}
func sayHello() {
	fmt.Println("Waking up....")
	time.Sleep(3 * time.Second)
	fmt.Println("Hello KiwiPycon!")
}

// Going to sleep...ZZzzzzzZZ
// Waking up....
// Hello KiwiPycon!
```

## Channels and Defers

(complicated, see talk)

## Resources

Books:

 * http://www.golang-book.com/books/intro
   * no longer works. Try https://github.com/ashleymcnamara/an-introduction-to-programming-in-go
 * Introducing Go by Caleb Doxsey http://shop.oreilly.com/product/0636920046516.do

Official docs:

 * A tour of Go: https://tour.golang.org/welcome/1
 * Effective Go: https://golang.org/doc/effective_go.html
 * Blog: https://blog.golang.org/

Talks:

 * The Evolution of Go https://youtu.be/0ReKdcpNyQg
 * Concurrency Is Not Parallelism https://youtu.be/cN_DpYBzKso
   * Probably https://go.dev/blog/waza-talk
 * Simplicity is complicated: https://youtu.be/rFejpH_tAHM
	
Articles:

 * Traps, Gotchas, etc for New Golang Devs: http://goo.gl/ijZVrw
   * http://devs.cloudimmunity.com/gotchas-and-common-mistakes-in-go-golang/
 * Five things that make Go fast: http://goo.gl/WYPJ8K
   * Probably https://dave.cheney.net/2014/06/07/five-things-that-make-go-fast