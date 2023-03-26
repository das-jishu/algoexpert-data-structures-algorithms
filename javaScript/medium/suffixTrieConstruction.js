class SuffixTrie {
  constructor(string) {
    this.root = {};
    this.endSymbol = '*';
    this.populateSuffixTrieFrom(string);
  }

  populateSuffixTrieFrom(string) {
    for (let i = 0; i < string.length; i++) {
      this.insertSubstringStartingAt(i, string);
    }
  }

  insertSubstringStartingAt(i, string) {
    let node = this.root;
    for (let j = i; j < string.length; j++) {
      const letter = string[j];
      if (!(letter in node)) {
        node[letter] = {};
      }

      node = node[letter];
    }

    node[this.endSymbol] = true;
  }

  contains(string) {
    let node = this.root;
    for (const letter of string) {
      if (!(letter in node)) {
        return false;
      }

      node = node[letter];
    }

    return this.endSymbol in node;
  }
}

const newSuffixTrie = new SuffixTrie('babcd');

console.log(newSuffixTrie.contains('bab')); // false
console.log(newSuffixTrie.contains('babcd')); // true
console.log(newSuffixTrie.contains('abcd')); // true
console.log(newSuffixTrie.contains('bcd')); // true
console.log(newSuffixTrie.contains('cd')); // true
console.log(newSuffixTrie.contains('d')); // true
