class DynamicArray {
    /**
     * @constructor
     * @param {number} capacity
     */
    constructor(capacity) {
        this.capacity = capacity
        this.length = 0
        this.arr = Array.from({length: capacity}, ()=>{return null})
    }

    /**
     * @param {number} i
     * @returns {number}
     */
    get(i) {
        return this.arr[i]
    }

    /**
     * @param {number} i
     * @param {number} n
     * @returns {void}
     */
    set(i, n) {
        this.arr[i] = n
    }

    /**
     * @param {number} n
     * @returns {void}
     */
    pushback(n) {
        if (this.length >= this.arr.length) {
            this.resize()
        }
        this.arr[this.length] = n
        this.length++
    }

    /**
     * @returns {number}
     */
    popback() {
        this.length--
        return this.arr[this.length]
    }

    /**
     * @returns {void}
     */
    resize() {
        this.arr = [...this.arr, ...Array.from({length: this.length}, ()=>{return null})]
        this.capacity *= 2
    }

    /**
     * @returns {number}
     */
    getSize() {
        return this.length
    }

    /**
     * @returns {number}
     */
    getCapacity() {
        return this.capacity
    }
}
