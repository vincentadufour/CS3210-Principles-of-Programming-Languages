object worksheetStudentsMap {
  def main(args: Array[String]): Unit =
    {
        // Initializing the map and printing it
        val studentMap = Map("Ren" -> 0.87, "Maria" -> 0.92, "Avonlea" -> 0.82)
        println(studentMap)

        // Creating a new map and adding a new student to it
        val updatedStudentMap = studentMap + ("George" -> 0.73)
        println(updatedStudentMap)

        // Making a student variable (not necessary, but is much cleaner code)
        val student = "Maria"

        // I didn't want to use .get because the returned value has "Some()"
        // To work around this, I first check if the student is in the list with an if statement, then just access the list using the
        // student variable which has Maria stored in it.
        if (updatedStudentMap.contains(student))
        {
            println("Maria's grade: " + updatedStudentMap(student));

        }
        else    // Error message prints that desired student is not in the class
        {
            println(student + "is not in the class.")
        }

    }
}
