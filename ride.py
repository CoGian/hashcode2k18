
class Ride(object):

    def __init__(self, code, start_loc, finish_loc, earliest_start, latest_finish):
        self.code = code
        self.start_loc = start_loc
        self.finish_loc = finish_loc
        self.earliest_start = earliest_start
        self.latest_finish = latest_finish
        self.distance = self.manhattan_dist(start_loc,finish_loc)
        self.route = self.calc_route()

    def calc_route(self):

        temp_loc = [self.start_loc[0], self.start_loc[1]]
        route = []
        while temp_loc[0] != self.finish_loc[0]:
            if temp_loc[0] < self.finish_loc[0]:
                temp_loc[0] += 1
                route.append([temp_loc[0], temp_loc[1]])
            else:
                temp_loc[0] -= 1
                route.append([temp_loc[0], temp_loc[1]])

        while temp_loc[1] != self.finish_loc[1]:
            if temp_loc[1] < self.finish_loc[1]:
                temp_loc[1] += 1
                route.append([temp_loc[0], temp_loc[1]])
            else:
                temp_loc[1] -= 1
                route.append([temp_loc[0], temp_loc[1]])

        return route

    def is_doable(self, step):
        return step + self.distance <= self.latest_finish

    def is_still_doable(self,step, vehicle_loc):
        return  step + self.distance + self.manhattan_dist(vehicle_loc, self.start_loc) <= self.latest_finish

    def manhattan_dist(self,x, y):
        return abs(x[0] - y[0]) + abs(x[1] - y[1])