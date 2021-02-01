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
var zigzagLevelOrder = function(root) {
    if(!root) return []
    let queue = [root]
    let output = []
    let deep = 0 //xác định nó ở cấp nào mà cho data vào đầu hay vào cuối
    while(queue.length > 0){
        const size = queue.length
        const level = []
        for(let i=0; i<size; i++){
            const node = queue.shift()
            if(deep % 2 === 0) level.push(node.val) //Thêm vào cuói mảng
            else level.unshift(node.val) // Thêm vào đầu mảng

            if(node.left) queue.push(node.left)
            if(node.right) queue.push(node.right)
        }
        output.push(level)
        deep++
    }
    return output
};
