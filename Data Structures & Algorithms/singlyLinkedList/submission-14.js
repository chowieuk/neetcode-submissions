class LinkedList {
  constructor() {
    this.arr = new Array();
  }

  /**
   * @param {number} index
   * @return {number}
   */
  get(index) {
    return this.arr[index]?.value ?? -1;
  }

  /**
   * @param {number} val
   * @return {void}
   */
  insertHead(val) {
    this.arr.unshift({ value: val, next: this.arr[0] });
    return null;
  }

  /**
   * @param {number} val
   * @return {void}
   */
  insertTail(val) {
    this.arr.push({ value: val, next: null });
    this.arr[this.arr.length - 2] = {
      value: this.arr[this.arr.length - 2]?.value,
      next: this.arr[this.arr.length - 1],
    };
    return null;
  }

  /**
   * bool remove(int i) will remove the ith node (0-indexed).
   * If the index is out of bounds, return false, otherwise return true.
   * @param {number} index
   * @return {boolean}
   */
  remove(index) {
    if (index >= this.arr.length || index < 0) return false;
    this.arr.splice(index, 1);
    return true;
  }

  /**
   * @return {number[]}
   */
  getValues() {
    let i = 0;
    let result = [];
    while (i < this.arr.length) {
      result.push(this.arr[i].value);
      i++;
    }
    return result;
  }
}
