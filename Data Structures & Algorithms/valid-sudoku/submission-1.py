class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_dict, col_dict, box_dict = {}, {}, {}
        for row in range(len(board)):
            for col in range(len(board[row])):
                element = board[row][col]
                if element != ".":
                    if self.getBoxLocation(row, col) in box_dict:
                        box = box_dict[self.getBoxLocation(row, col)]
                        if element in box:
                            return False
                        else:
                            box.add(element)
                    else:
                        box_dict[self.getBoxLocation(row, col)] = set([element])
                    
                    if row in row_dict:
                        row_elems = row_dict[row]
                        if element in row_elems:
                            return False
                        else:
                            row_elems.add(element)
                    else:
                        row_dict[row] = set([element])

                    if col in col_dict:
                        col_elems = col_dict[col]
                        if element in col_elems:
                            return False
                        else:
                            col_elems.add(element)
                    else:
                        col_dict[col] = set([element])

        return True


    def getBoxLocation(self, row: int, col: int) -> Tuple[int, int]:
        return (row // 3, col // 3)
    
    
