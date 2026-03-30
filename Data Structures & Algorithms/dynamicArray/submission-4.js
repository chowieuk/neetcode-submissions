/**
 * DynamicArray definition
 * @property {number} capacity - current capacity
 * @property {number} size - current size
 * @property {Array<number>} contents - current array contents
 */
class DynamicArray {
  capacity = 0;
  contents = new Array(0);
  /**
   * @constructor
   * @param {number} capacity
   */
  constructor(capacity) {
    if (capacity > 0) {
      this.capacity = capacity;
      this.contents = new Array(capacity);
      return null;
    } else {
      throw new Error("capacity must exceed 0");
    }
  }

  /**
   * @param {number} i
   * @returns {number}
   */
  get(i) {
    return this.contents[i];
  }

  /**
   * @param {number} i
   * @param {number} n
   * @returns {void}
   */
  set(i, n) {
    this.contents[i] = n;
  }

  /**
   * @param {number} n
   * @returns {void}
   */
  pushback(n) {
    if (this.getSize() >= this.getCapacity()) {
      this.resize();
    }
    this.contents[this.getSize()] = n;
  }

  /**
   * @returns {number}
   */
  popback() {
    let size = this.getSize();
    let v = this.contents[size];
    let i = 0;
    while (!v) {
      i++;
      v = this.contents[size - i];
    }
    delete this.contents[size - 1];
    return v;
  }

  /**
   * @returns {void}
   */
  resize() {
    this.capacity *= 2;
    console.log("resized", this.capacity);
    let newArray = new Array(this.capacity);
    this.contents.forEach((v, i) => {
      console.log({ v }, { i });
      newArray[i] = v;
    });
    console.log({ contents: this.contents }, { newArray });
    this.contents = newArray;
  }

  /**
   * @returns {number}
   */
  getSize() {
    let size = 0;
    this.contents.forEach(() => {
      size++;
    });
    return size;
  }

  /**
   * @returns {number}
   */
  getCapacity() {
    return this.capacity;
  }
}
