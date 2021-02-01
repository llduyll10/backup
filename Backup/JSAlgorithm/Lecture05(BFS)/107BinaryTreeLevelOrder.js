/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[][]}
 */

var levelOrderBottom = function(root) {
    var queue = [{node:root, level:0}],
        crt,
        stack = [],
        maxLevel,
        result = []
    if(!root) return result

    while(queue.length > 0){
        crt  = queue.shift(); //Dequeue
        stack.push(crt)
        if(crt.node.right){
            queue.push({node:crt.node.right, level:crt.level +1})
        }
        if(crt.node.left){
            queue.push({node:crt.node.left, level: crt.level + 1})
        }
        maxLevel = crt.level + 1
    }

    while(stack.length > 0){
        crt = stack.pop()
        if(crt.level < maxLevel){
            result.push([])
            maxLevel--
        }
        result[result.length-1].push(crt.node.val)
    }
    return result
};

