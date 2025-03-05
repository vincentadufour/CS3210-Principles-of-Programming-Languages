case class Employee(name: String, age: Int, department: String, salary: Double)

object EmpOutline {
  def main(args: Array[String]): Unit = {
    val employees = List(
      Employee("Alice", 30, "HR", 50000),
      Employee("Bob", 25, "Engineering", 70000),
      Employee("Charlie", 35, "Sales", 45000),
      Employee("David", 28, "Engineering", 75000),
      Employee("Emma", 40, "HR", 60000)
    )
    // Display all employees
    println("All Employees:")
    employees.foreach(emp => println(s"${emp.name}, ${emp.age}, ${emp.department}, ${emp.salary}"))

    // 1. Filter employees by department
    val engineeringEmployees = employees.filter(_.department == "Engineering")
    //display filtered data
    println("\nAll Engineering Employees:")
    engineeringEmployees.foreach(emp => println(s"${emp.name}, ${emp.age}, ${emp.department}, ${emp.salary}"))

    // 2. Calculate total and average salary
    var total: Double = 0
    for (emp <- employees)
    {
      total = total + emp.salary
    }
    println("\nTotal Salary:")
    println(total)
    println("\nAverage Salary:")
    println(total/5)
   

    // 3. Find the highest-paid employee
    println("\nHighest Paid Employee:")
    var highestPaid: Double = 0
    for (emp <- employees)
    {
      if (emp.salary > highestPaid)
        {
          highestPaid = emp.salary
        }
    }
    println(highestPaid)
    

    // 4. Categorize employees based on salary
    val sortedEmps = employees.sortBy(_.salary)
    print(sortedEmps)
    sortedEmps.foreach(emp => println(s"${emp.name}, ${emp.age}, ${emp.department}, ${emp.salary}"))

 
    
  }
}
