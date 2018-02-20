package bgtester

import scala.io.Source
import java.io.{FileNotFoundException, IOException}


object BibartiteGraphTester extends App {

  val lines = FileReader.getLines(args(0))
  val n: Int = lines.next().toInt
  val graph = new Graph(n, Graph.getRows(lines.toSeq))
  println(graph.testForBipartite)
}

object FileReader {
  def getLines(filename: String): Iterator[String] = {
      Source.fromFile(filename).getLines
  }
}


