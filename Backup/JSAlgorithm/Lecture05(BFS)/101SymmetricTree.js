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
 * @return {boolean}
 */
var isSymmetric = function(root) {
    if(!root){
        return true
    }
    const leftStack = [root.left], rightStack = [root.right]

    while(leftStack.length && rightStack.length){
        const l = leftStack.pop(), r = rightStack.pop()
        
        if(!l && !r) continue
        if(!l || !r) return false
        if(l.val !== r.val) return false

        leftStack.push(l.left);
        leftStack.push(l.right);

        rightStack.push(r.right);
        rightStack.push(r.left)
    }
    return true
};