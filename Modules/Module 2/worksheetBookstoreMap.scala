object worksheetBookstoreMap {
  def main(args: Array[String]): Unit =
    {
        // Initializing the map and printing it
        val books = Map("Ender's Game" -> 15.99, "Compte de Monte Cristo" -> 19.99, "Berserk: Vol II" -> 39.99)
        
        // First method for filtering, using mapValues(), returns a new map with true and false statements
        // based on whether or not the condition was met
        val expensiveBooks = books.mapValues(_ > 30)
        println(expensiveBooks)


        // Second method for filtering using filter()
        val expensiveBooks2 = books.filter(book => book._2 > 30)
        println(expensiveBooks2)

        val removeBooks = books - ("Ender's Game")
        println(removeBooks)
        // books.updatedWith("Ender")(_.map(_ - 5))
        // println(books)
    }
}
