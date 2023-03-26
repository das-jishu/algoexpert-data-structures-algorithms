function solveSudoku(board) {
  // Write your code here.
  solveSudokuPartial(board, 0, 0);
  return board;
}

function solveSudokuPartial(board, row, col) {
  let currentRow = row;
  let currentCol = col;

  if (currentCol === board[currentRow].length) {
    currentRow++;
    currentCol = 0;

    if (currentRow === board.length) return true;
  }

  if (board[currentRow][currentCol] === 0) {
    return trialAllDigits(board, currentRow, currentCol);
  }

  return solveSudokuPartial(board, currentRow, currentCol + 1);
}

function trialAllDigits(board, row, col) {
  for (let digit = 1; digit < 10; digit++) {
    if (isNumberValidAtPosition(board, row, col, digit)) {
      board[row][col] = digit;
      if (solveSudokuPartial(board, row, col + 1)) return true;
    }
  }

  board[row][col] = 0;
  return false;
}

function isNumberValidAtPosition(board, row, col, value) {
  return !(
    hasNumberInRow(board, row, value) ||
    hasNumberInCol(board, col, value) ||
    hasNumberInBox(board, row, col, value)
  );
}

function hasNumberInRow(board, row, value) {
  return board[row].includes(value);
}

function hasNumberInCol(board, col, value) {
  return board.map((r) => r[col]).includes(value);
}

function hasNumberInBox(board, row, col, value) {
  const rowStart = Math.floor(row / 3) * 3;
  const colStart = Math.floor(col / 3) * 3;

  for (let rowIdx = 0; rowIdx < 3; rowIdx++) {
    for (let colIdx = 0; colIdx < 3; colIdx++) {
      const rowToCheck = rowStart + rowIdx;
      const colToCheck = colStart + colIdx;
      const currentValue = board[rowToCheck][colToCheck];
      if (currentValue === value) return true;
    }
  }

  return false;
}
// Do not edit the line below.
exports.solveSudoku = solveSudoku;
