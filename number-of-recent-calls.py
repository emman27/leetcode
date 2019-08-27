class RecentCounter:
    MAX_RECORD_TIME = 3000

    def __init__(self):
        self.pings = []

    def ping(self, t: int) -> int:
        self.pings.append(t)
        for (i, ping) in enumerate(self.pings):
            if self._should_be_remembered(ping, t):
                self.pings = self.pings[i:]
                break
        return len(self.pings)

    def _should_be_remembered(self, ping_time: int, current_time: int) -> bool:
        return ping_time >= current_time - self.MAX_RECORD_TIME
