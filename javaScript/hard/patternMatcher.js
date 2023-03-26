// pattern = "xxyxxy"
// string = "gogopowerrangergogopowerranger"
// output: ["go", "powerranger"]

function patternMatcher(pattern, string) {
  if (pattern.length > string.length) {
    return [];
  }

  const newPattern = getNewPattern(pattern);
  const hasPatternSwitched = pattern[0] !== newPattern[0];

  const counts = { x: 0, y: 0 };

  const firstYIndex = getCountsAndFirstYIndex(newPattern, counts);

  if (counts.y !== 0) {
    for (let lengOfX = 1; lengOfX <= string.length; lengOfX++) {
      const lengOfY = (string.length - lengOfX * counts.x) / counts.y;
      if (lengOfY <= 0 || lengOfY % 1 !== 0) {
        continue;
      }

      const x = string.slice(0, lengOfX);
      const yPosition = firstYIndex * lengOfX;
      const y = string.slice(yPosition, yPosition + lengOfY);

      const potentialMatch = newPattern
        .map((char) => (char === 'x' ? x : y))
        .join('');
      if (potentialMatch === string) {
        return hasPatternSwitched ? [y, x] : [x, y];
      }
    }
  } else {
    const lengOfX = string.length / counts.x;
    if (lengOfX % 1 !== 0) {
      return [];
    }

    const x = string.slice(0, lengOfX);

    const potentialMatch = newPattern.map(() => x).join('');

    if (potentialMatch === string) {
      return hasPatternSwitched ? ['', x] : [x, ''];
    }
  }

  return [];
}

function getNewPattern(pattern) {
  let patternArray = pattern.split('');
  if (patternArray[0] === 'x') {
    return patternArray;
  }

  return patternArray.map((item) => (item === 'x' ? 'y' : 'x'));
}

function getCountsAndFirstYIndex(newPattern, counts) {
  let firstYIndex = null;
  newPattern.map((item, i) => {
    if (item === 'y' && firstYIndex === null) {
      firstYIndex = i;
    }

    counts[item]++;
  });

  return firstYIndex;
}

const result = patternMatcher('xxyxxy', 'gogopowerrangergogopowerranger');
console.log(result);
