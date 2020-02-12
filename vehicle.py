
class Vehicle(object):

    def __init__(self, id):
        self.location = [0, 0]
        self.history = []
        self.route = []
        self.current_ride = None
        self.id = id
    def move(self):
        self.location = self.route.pop(0)

    def get_assigned_to_ride(self, ride):
        self.current_ride = ride
        self.route = self.calc_route_to_ride(ride)
        self.route = self.route + ride.route
        self.history.append(ride.code)

    def calc_route_to_ride(self, ride):
        temp_loc = [self.location[0], self.location[1]]
        route = []
        while temp_loc[0] != ride.finish_loc[0]:
            if temp_loc[0] < ride.finish_loc[0]:
                temp_loc[0] += 1
                route.append([temp_loc[0], temp_loc[1]])
            else:
                temp_loc[0] -= 1
                route.append([temp_loc[0], temp_loc[1]])

        while temp_loc[1] != ride.finish_loc[1]:
            if temp_loc[1] < ride.finish_loc[1]:
                temp_loc[1] += 1
                route.append([temp_loc[0], temp_loc[1]])
            else:
                temp_loc[1] -= 1
                route.append([temp_loc[0], temp_loc[1]])

        return route
