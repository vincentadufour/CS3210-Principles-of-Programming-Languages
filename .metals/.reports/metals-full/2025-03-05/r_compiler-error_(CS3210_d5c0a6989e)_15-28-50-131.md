file://<WORKSPACE>/Modules/Module%202/worksheetBookstoreMap.scala
### java.lang.AssertionError: assertion failed: NoType

occurred in the presentation compiler.

presentation compiler configuration:


action parameters:
offset: 690
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


        books.updatedWith("Ender's Game")(_.m@@)
    }
}

```



#### Error stacktrace:

```
scala.runtime.Scala3RunTime$.assertFailed(Scala3RunTime.scala:8)
	dotty.tools.dotc.core.Types$TypeBounds.<init>(Types.scala:5557)
	dotty.tools.dotc.core.Types$AliasingBounds.<init>(Types.scala:5636)
	dotty.tools.dotc.core.Types$TypeAlias.<init>(Types.scala:5661)
	dotty.tools.dotc.core.Types$TypeAlias$.apply(Types.scala:5700)
	dotty.tools.dotc.core.Types$Type.bounds(Types.scala:1857)
	dotty.tools.pc.completions.CaseKeywordCompletion$.matchContribute(MatchCaseCompletions.scala:280)
	dotty.tools.pc.completions.Completions.advancedCompletions(Completions.scala:349)
	dotty.tools.pc.completions.Completions.completions(Completions.scala:122)
	dotty.tools.pc.completions.CompletionProvider.completions(CompletionProvider.scala:139)
	dotty.tools.pc.ScalaPresentationCompiler.complete$$anonfun$1(ScalaPresentationCompiler.scala:150)
```
#### Short summary: 

java.lang.AssertionError: assertion failed: NoType