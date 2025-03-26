file://<WORKSPACE>/Modules/Module%202/worksheetBookstoreMap.scala
### java.lang.AssertionError: assertion failed: position not set for nn(<empty>) # -1 of class dotty.tools.dotc.ast.Trees$Apply in <WORKSPACE>/Modules/Module 2/worksheetBookstoreMap.scala

occurred in the presentation compiler.

presentation compiler configuration:


action parameters:
offset: 689
uri: file://<WORKSPACE>/Modules/Module%202/worksheetBookstoreMap.scala
text:
```scala
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
        val expensiveBooks2 = books.filter(x => x._2 > 30)
        println(expensiveBooks2)


        books.updatedWith("Ender's Game")(_.@@)
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

java.lang.AssertionError: assertion failed: position not set for nn(<empty>) # -1 of class dotty.tools.dotc.ast.Trees$Apply in <WORKSPACE>/Modules/Module 2/worksheetBookstoreMap.scala