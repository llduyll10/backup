/**
 * @param {number[][]} grid
 * @return {number}
 */
var orangesRotting = function(grid) {
    let queue = []
    let minutes = 0
    let fresh = 0
    for (let i =0; i<grid.length; i++){
        for(let j=0; j<grid[0].length; j++){
            if(grid[i][j] == 1) fresh++
            if(grid[i][j] == 2) queue.push([i,j])
        }
    }

    while(queue.length != 0 && fresh){

        //These arrays are used to get row and column
        // numbers of 4 neighbours of a given cell
        let dR = [0,-1,0,1]
        let dC = [-1,0,1,0]

        let next = []

        while(queue.length != 0){
            let current = queue.shift()
            for(let i = 0; i<dR.length; i++){
                // nR & nC represents the calculated row and column
                let nR = current[0]+ dR[i] //nR <=> neighbor row
                let nC = current[1] + dC[i] // nC <=> neighbor column
                if(nR >= 0 && nC >= 0 && nR<grid.length && nC<grid[0].length){
                    if(grid[nR][nC] == 1){ //nếu là cam tươi
                        grid[nR][nC] = 2 // Chuyển thành cam hư
                        fresh--
                        next.push([nR,nC]) //Chuyển nó vào mảng next để tiếp tục xét hàng xóm 
                    }
                }
            }
        }
        minutes++
        queue = next //gán queue bằng mảng next
    }
    return fresh == 0 ? minutes : -1
};

var grid = [[2,1,1],[1,1,0],[0,1,1]]
console.log(orangesRotting(grid))