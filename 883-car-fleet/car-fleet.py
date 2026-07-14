class Solution(object):
    def carFleet(self, target, position, speed):
        pairs = sorted(zip(position, speed))
        fleet = 0
        lastTime = 0
        for position, speed in reversed(pairs):
            time = (target - position) * 1.0 / speed
            if time > lastTime:
                fleet += 1
                lastTime = time
        return fleet
        