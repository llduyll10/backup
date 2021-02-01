class Stack{
    constructor(){
        this.stack = []
    }

    push(item){
        return this.stack.push(item)
    }
    //Lấy ra giá trị đỉnh của stack và xoá khỏi stack
    pop(){
        return this.stack.pop() 
    }
    //Lấy ra giá trị đầu tiên của stack và xoá khỏi stack
    peek(){
        return this.stack.shift()
    }

    isEmpty(){
        return this.length === 0
    }

}

