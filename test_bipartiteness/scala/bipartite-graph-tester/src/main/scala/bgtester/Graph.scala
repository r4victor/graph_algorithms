package bgtester

import scala.collection.mutable.{Set, Queue}

class Graph(n: Int, rows: Seq[List[Int]]) {
  val adjacent = rows.map(_.toSet).toList

  def testForBipartite: Boolean = {
    val part1 = Set[Int]()
    val part2 = Set[Int]()
    var previousVertex = 0
    var previousPart = 0
    var currentVertex = 0
    val queue = Queue(1)

    while (!queue.isEmpty) {
      currentVertex = queue.dequeue
      for (v <- adjacent(currentVertex) if v != previousVertex) {
        if ((part1.contains(v) && previousPart == 2)
          || (part2.contains(v) && previousPart == 1)) return false
        else {
          queue += v
          if (previousPart == 1) {
            part2 += v
            previousPart = 2
          }
          else {
            part1 += v
            previousPart = 1
          }
        }
      }
      previousVertex = currentVertex
    }

    true
  }
}

object Graph {
  def getRows(lines: Seq[String]): Seq[List[Int]] = {
    lines.map(_.split(" ").map(_.toInt).toList)
  }
}