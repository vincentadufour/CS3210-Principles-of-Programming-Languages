error id: `<none>`.
file://<WORKSPACE>/Modules/Module%202/myName.scala
empty definition using pc, found symbol in pc: `<none>`.
empty definition using semanticdb
|empty definition using fallback
non-local guesses:
	 -

Document text:

```scala


object myName {
  def main(args: Array[String]): Unit = {
    println("Hello, my name is Vincent") //replace Red with your name
  }
}

object sc1 {
  def main(args: Array[String]): Unit = {
    val name: String = "Red" // Immutable
    var age: Int = 25          // Mutable
    age = 36 // This is allowed
    // name = "New name"  // This would cause an error because `val` is immutable
    println("Hello, my name is " +name+ " and my age is "+age) 
  }
}

```

#### Short summary: 

empty definition using pc, found symbol in pc: `<none>`.