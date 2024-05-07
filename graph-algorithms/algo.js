class Node {
  constructor(val) {
    this.val = val;
    this.left = null;
    this.right = null;
  }
}

// treeSum --> Depth First traversal, alteratively
function treeSum(root) {
  if (root == null) return 0;
  let sum = 0;
  const stack = [root];
  while (stack.length > 0) {
    const current = stack.pop();
    sum += current.val;
    if (current.right) stack.push(current.right);
    if (current.left) stack.push(current.left);
  }
  return sum;
}

// treeSum --> Breadth First traversal, alteratively
function treeSum(root) {
  if (root == null) return 0;
  let sum = 0;
  const queue = [root];
  while (stack.length > 0) {
    const current = queue.shift();
    sum += current.val;
    if (current.right) queue.push(current.right);
    if (current.left) queue.push(current.left);
  }
  return sum;
}

// treeSum --> Depth First Traversal, Recursively
function treeSumRecursive(root) {
  if (root == null) return 0;
  const sumRight = treeSumRecursive(root.right);
  const sumLeft = treeSumRecursive(root.left);
  return root.val + sumRight + sumLeft;
}

// HasTarget --> Breadth First search, an alterative way
function treeHasTarget(root, target) {
  if (root == null) return false;
  const queue = [root];
  while (stack.length > 0) {
    const current = queue.shift();
    if (current.val == target) return true;
    if (current.right) queue.push(current.right);
    if (current.left) queue.push(current.left);
  }
  return false;
}

// HasTarget --> Depth First search, Recursively
function treeHasTargetRecursively(root, target) {
  if (root == null) return false;
  if (root.val == target) return true;
  const rightHasTarget = treeHasTargetRecursively(root.right, target);
  const leftHasTarget = treeHasTargetRecursively(root.left, target);
  return rightHasTarget || leftHasTarget;
}

// Tree min value problem

// 1. breadth first seach
function treeMinValue(root) {
  if (root == null) return null;
  let min = root.val;
  const queue = [root];
  while (queue.length > 0) {
    const current = queue.shift();
    if (current.val < min) min = current.val;
    if (current.right) queue.push(current.right);
    if (current.left) queue.push(current.left);
  }
  return min;
}

// 1. recursively
function treeMinValueRec(root) {
  if (root == null) return null;

  const leftMin = root.left ? treeMinValueRec(root.left) : Number.MAX_VALUE;
  const rightMin = root.right ? treeMinValueRec(root.right) : Number.MAX_VALUE;

  return Math.min(root.val, rightMin, leftMin);
}

// Max root to leaf path sum
function maxRootToLeafPathSum(root){
    if(root == null) return -Number.MAX_VALUE;
    if(root.right == null && root.left == null) return root.val;
    const maxChild = Math.max(maxRootToLeafPathSum(root.right), maxRootToLeafPathSum(root.left));
    return root.val + maxChild;
}


// average value of nodes at each level

function averageOfNodeAtEachLevel(root) {
  if (root == null) return [];
  const averages = [];
  const queue = [[root]];
  while (queue.length > 0) {
    const currentLevelNodes = queue.shift();
    const currentLevelNodesAverage =
      currentLevelNodes.map((node) => node.val).sum() /
      currentLevelNodes.length;
    averages.push(currentLevelNodesAverage);

    const nextLevelNodes = [];

    currentLevelNodes.forEach((node) => {
      if (node.right != null) nextLevelNodes.push(node.right);
      if (node.left != null) nextLevelNodes.push(node.left);
    });

    queue.push(nextLevelNodes);
  }

  return averages;
}
