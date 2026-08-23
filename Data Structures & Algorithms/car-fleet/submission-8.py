class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position, speed), reverse=True)
        fleet_times = []
        for pos, speed in pairs:
            time = (target - pos) / speed
            if not fleet_times or time > fleet_times[-1]:
                fleet_times.append(time)
        
        return len(fleet_times)
