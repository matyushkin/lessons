// Дано неотрицательное целое число.
// Найдите число десятков. 

package main

import "fmt"

func main(){

  var a, b, c, d int
  fmt.Scan(&a)
  b = a % 100
  c = b % 10
  d = (b - c)/10

  fmt.Println(d)
}