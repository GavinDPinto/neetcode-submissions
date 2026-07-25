class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        strs_len = len(strs)
        for i in range(strs_len):
            string = strs[i]
            string_len = len(string)
            for j in range(string_len):
                char = string[j]
                if char == '/':
                    encoded_string += "//"
                else:
                    encoded_string += char
            encoded_string += "/s"
        return encoded_string

    def decode(self, s: str) -> List[str]:
        s_len = len(s)
        ret = []
        cur_str = ""
        continue_flag = 0
        for i in range(s_len):
            if continue_flag:
                continue_flag = 0
                continue
            cur_char = s[i]
            if cur_char == '/':
                if s[i+1] == 's':
                    ret.append(cur_str)
                    cur_str = ""
                else:
                    cur_str += s[i+1]
                continue_flag = 1
            else:
                cur_str += cur_char
        return ret