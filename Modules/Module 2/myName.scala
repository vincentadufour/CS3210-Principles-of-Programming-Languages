

object myName {
  def main(args: Array[String]): Unit = {
    println("Hello, my name is Vincent") //replace Red with your name
  }
}

object sc1 {
  def main(args: Array[String]): Unit = {
    val name: String = "Vincent" // Immutable
    var age: Int = 25          // Mutable
    age = 27 // This is allowed
    // name = "New name"  // This would cause an error because `val` is immutable
    println("Hello, my name is " +name+ " and my age is "+age) 
  }
}

object sc2{
  def main(args: Array[String]): Unit = {
    val number = 10
    if (number > 0) {
        println("Positive number")}
    else {
        println("Negative number or zero") }

    val day = "Wednesday"
    day match {
    case "Monday" => println("Start of the week!")
    case "Friday" => println("Almost weekend!")
    case _ => println("Mid-week day")
    }

    for (i <- 1 to 5) {
      println(s"Value of i: $i")
    }

    val fruits = List("Apple", "Banana", "Cherry")
    for (fruit <- fruits) {
      println(fruit)
    }

    for (i <- 1 to 10 if i % 2 == 0) {
      println(s"Even number: $i")
    }

    for (i <- 1 to 3; j <- 1 to 3) {
      println(s"i = $i, j = $j")
    }

    val squares = for (i <- 1 to 5) yield i * i
    println(squares) 
    // Output: Vector(1, 4, 9, 16, 25)

    // var i = 1
    // while (i <= 5) {
    //   println(s"i = $i")
    //   i += 1
    // }

    // var i = 1
    // do {
    //   println(s"i = $i")
    //   i += 1
    // } while (i <= 5)

    val myMap = Map(1 -> "One", 2 -> "Two", 3 -> "Three")
    for ((key, value) <- myMap) {
      println(s"Key: $key, Value: $value")
    }

    // def add(x: Int, y: Int): Int = {
    //   x + y
    // }

    // println(add(5, 3)) 
    // // Output: 8

    val add = (x: Int, y: Int) => x + y
    println(add(5, 3)) 
    // Output: 8

  }
}

  object qu{
    def test(x:Int): Boolean =
      {
        Math.abs(100-x) <= 20 || Math.abs(300-x) <= 20
  }
    def main(args: Array[String]): Unit =
      {
        println("Result: " + test(115));
      }


}
