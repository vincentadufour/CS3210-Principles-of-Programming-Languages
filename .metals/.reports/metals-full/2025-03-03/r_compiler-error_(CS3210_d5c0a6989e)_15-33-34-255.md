file://<WORKSPACE>/Modules/Module%202/EmpOutline.scala
### java.lang.AssertionError: assertion failed: position not set for fromNullable(<empty>) # -1 of class dotty.tools.dotc.ast.Trees$Apply in <WORKSPACE>/Modules/Module 2/EmpOutline.scala

occurred in the presentation compiler.

presentation compiler configuration:


action parameters:
offset: 1528
uri: file://<WORKSPACE>/Modules/Module%202/EmpOutline.scala
text:
```scala
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
    val sortedEmps = employees.sortBy(_.@@)
   
 
    
  }
}

```



#### Error stacktrace:

```
scala.runtime.Scala3RunTime$.assertFailed(Scala3RunTime.scala:8)
	dotty.tools.dotc.typer.Typer$.assertPositioned(Typer.scala:76)
	dotty.tools.dotc.typer.Typer.typed(Typer.scala:3657)
	dotty.tools.dotc.typer.Applications.extMethodApply(Applications.scala:2642)
	dotty.tools.dotc.typer.Applications.extMethodApply$(Applications.scala:434)
	dotty.tools.dotc.typer.Typer.extMethodApply(Typer.scala:148)
	dotty.tools.dotc.typer.Applications.tryApplyingExtensionMethod(Applications.scala:2687)
	dotty.tools.dotc.typer.Applications.tryApplyingExtensionMethod$(Applications.scala:434)
	dotty.tools.dotc.typer.Typer.tryApplyingExtensionMethod(Typer.scala:148)
	dotty.tools.dotc.interactive.Completion$Completer.tryApplyingReceiverToExtension$1(Completion.scala:561)
	dotty.tools.dotc.interactive.Completion$Completer.$anonfun$23(Completion.scala:604)
	scala.collection.immutable.List.flatMap(List.scala:294)
	scala.collection.immutable.List.flatMap(List.scala:79)
	dotty.tools.dotc.interactive.Completion$Completer.extensionCompletions(Completion.scala:601)
	dotty.tools.dotc.interactive.Completion$Completer.selectionCompletions(Completion.scala:449)
	dotty.tools.dotc.interactive.Completion$.computeCompletions(Completion.scala:221)
	dotty.tools.dotc.interactive.Completion$.rawCompletions(Completion.scala:80)
	dotty.tools.pc.completions.Completions.enrichedCompilerCompletions(Completions.scala:114)
	dotty.tools.pc.completions.Completions.completions(Completions.scala:136)
	dotty.tools.pc.completions.CompletionProvider.completions(CompletionProvider.scala:139)
	dotty.tools.pc.ScalaPresentationCompiler.complete$$anonfun$1(ScalaPresentationCompiler.scala:150)
```
#### Short summary: 

java.lang.AssertionError: assertion failed: position not set for fromNullable(<empty>) # -1 of class dotty.tools.dotc.ast.Trees$Apply in <WORKSPACE>/Modules/Module 2/EmpOutline.scala