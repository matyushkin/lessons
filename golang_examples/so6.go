// Часовая стрелка повернулась с начала суток на d градусов.
// Определите, сколько сейчас целых часов h и целых минут m.

package main

import "fmt"

func main(){

  var d, h, m int
  fmt.Scan(&d)
  h = d/30
  m = d%30

  fmt.Println("It is", h, "hours", m, "minutes.")
}