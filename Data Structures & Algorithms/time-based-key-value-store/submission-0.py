class TimeMap:

    def __init__(self):
        self.keys = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keys[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        value_arr = self.keys[key]
        # binary search
        left, right = 0, len(value_arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if value_arr[mid][0] == timestamp:
                return value_arr[mid][1]
            elif value_arr[mid][0] < timestamp:
                left = mid + 1
            else:
                right = mid - 1
        if left - 1 >= 0:
            return value_arr[left - 1][1]
        else:
            return ""
    
