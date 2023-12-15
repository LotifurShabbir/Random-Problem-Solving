class Solution(object):
    def destCity(self, paths):
        cities = set()
        for i in paths:
            cities.add(i[0])
        for path in paths:
            if path[1] not in cities:
                return path[1]
        