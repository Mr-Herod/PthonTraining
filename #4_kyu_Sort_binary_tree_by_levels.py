Description:

"""
You are given a binary tree:
class TreeNode
  attr_accessor :left
  attr_accessor :right
  attr_reader :value
end
data TreeNode a = TreeNode {
  left  :: Maybe (TreeNode a),
  right :: Maybe (TreeNode a),
  value :: a
  } deriving Show
class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n
class Node {
    Integer value
    Node left
    Node right

    Node(left, right, value) {
        this.value = value
        this.left = left
        this.right = right
    }
}
public class Node
{
    public Node Left;
    public Node Right;
    public int Value;

    public Node(Node l, Node r, int v)
    {
        Left = l;
        Right = r;
        Value = v;
    }
}
public class Node {
  public Node left;
  public Node right;
  public int value;

  public Node(Node l, Node r, int v) {
    left = l;
    right = r;
    value = v;
  }
}
Your task is to return the list with elements from tree sorted by levels, which means the root element goes first, then root children (from left to right) are second and third, and so on.
Return empty list if root is None.
Example 1 - following tree:
                 2
            8        9
          1  3     4   5Should return following list:
[2,8,9,1,3,4,5]Example 2 - following tree:
                 1
            8        4
              3        5
                         7Should return following list:
[1,8,4,3,5,7]
"""

My codes:

def tree_by_levels(node):
    li = []
    part_levels(node,1,li)
    return [y for x in li for y in x]

def part_levels(node,levels,li):
    if node == None:
        return
    if len(li) < levels:
        li.append([])
    li[levels-1].append(node.value)
    part_levels(node.left,levels+1,li)
    part_levels(node.right,levels+1,li)

Others codes:

from collections import deque


def tree_by_levels(node):
    if not node:
        return []
    res, queue = [], deque([node,])
    while queue:
        n = queue.popleft()
        res.append(n.value)
        if n.left is not None:
            queue.append(n.left)
        if n.right is not None:
            queue.append(n.right)
    return res

from collections import deque
def tree_by_levels(node):
    if not node:
        return []
    res, queue=[], deque([node,])
    while queue:
        n=queue.popleft()
        res.append(n.value)
        if n.left is not None:
            queue.append(n.left)
        if n.right is not None:
            queue.append(n.right)
    return res
