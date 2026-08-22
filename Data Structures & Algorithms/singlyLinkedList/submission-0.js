class LinkedList {
    constructor() {
        this.list = []
    }

    /**
     * @param {number} index
     * @return {number}
     */
    get(index) {
        if (index >= this.list.length) return -1
        return this.list[index]
    }

    /**
     * @param {number} val
     * @return {void}
     */
    insertHead(val) {
        this.list.unshift(val)
    }

    /**
     * @param {number} val
     * @return {void}
     */
    insertTail(val) {
        this.list.push(val)
    }

    /**
     * @param {number} index
     * @return {boolean}
     */
    remove(index) {
        if (index >= this.list.length)
            return false
        else {
            const newList = []
            for (let i = 0; i < this.list.length; i++) if (i !== index) newList.push(this.list[i])
            this.list = newList
            return true
        }
    }

    /**
     * @return {number[]}
     */
    getValues() {
        return this.list
    }
}
