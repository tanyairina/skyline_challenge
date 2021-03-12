class Maxpq:
    def __init__(self):
      self.container = []

    def front(self):
      if not self.container: return 0, 2**32
      t = self.container[0]
      return (-t[0], t[1])

    def push(self, t):
      heapq.heappush(self.container, (-t[0], t[1]))

    def pop(self):
      heapq.heappop(self.container)


class Solution:
    def getSkyline(self, buildings):
        events = []
        closing_events = set()
        for l, r, h in buildings:
            events.append((l, h, r))
            closing_events.add((r, 0, 0))
        events += list(closing_events)
        events.sort(key=lambda x: [x[0], -x[1]])

        skyline, pq = [], Maxpq()
        for x, h, r in events:
            while x >= pq.front()[1]: pq.pop()
            if h: pq.push((h, r))
            if not skyline or skyline[-1][1] != pq.front()[0]:
                skyline.append([x, pq.front()[0]])
        return skyline

        print(skyline)