class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_dict, col_dict, box_dict = {}, {}, {}
        for row in range(len(board)):
            for col in range(len(board[row])):
                element = board[row][col]
                # skip if blank
                if element != ".":
                    # check the surrounding 3x3 box
                    if (row // 3, col // 3) in box_dict:
                        box_elems = box_dict[(row // 3, col // 3)]
                        if element in box_elems:
                            return False
                        else:
                            box_elems.add(element)
                    else:
                        box_dict[(row // 3, col // 3)] = set([element])
                    
                    # check the row
                    if row in row_dict:
                        row_elems = row_dict[row]
                        if element in row_elems:
                            return False
                        else:
                            row_elems.add(element)
                    else:
                        row_dict[row] = set([element])

                    # check the column
                    if col in col_dict:
                        col_elems = col_dict[col]
                        if element in col_elems:
                            return False
                        else:
                            col_elems.add(element)
                    else:
                        col_dict[col] = set([element])

        return True
    
    
