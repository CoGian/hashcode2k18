import re
from ride import Ride
from vehicle import Vehicle

def main():
    # read file
    with open("c_no_hurry.in", "r") as f:
        # read info
        info = re.split("[ \n]", f.readline())[0:6]
        info = [int(i) for i in info]
        print(info)
        rows, columns, number_of_vehicles , number_of_rides , bonus, steps = info

        # read rides
        rides = []
        code = 0
        while True:
            line = f.readline()
            if not line:
                break
            ride_info = re.split("[ \n]", line)[0:6]
            ride_info = [int(i) for i in ride_info]
            start_loc = ride_info[0:2]

            finish_loc = ride_info[2:4]

            earliest_start = ride_info[4]

            latest_finish = ride_info[5]

            ride = Ride(code, start_loc, finish_loc, earliest_start, latest_finish)
            code += 1
            rides.append(ride)
        # sort rides
        rides.sort(key=lambda x: x.earliest_start, reverse=False)

        available_vehicles = []
        for i in range(number_of_vehicles):
            vehicle = Vehicle(i)
            available_vehicles.append(vehicle)
        canceled_rides = []
        unavailable_vehicles = []
        for t in range(steps+1):

            index = 0
            while index < len(unavailable_vehicles):
                vehicle = unavailable_vehicles[index]
                vehicle.move()
                if not vehicle.route:
                    available_vehicles.append(vehicle)
                    del unavailable_vehicles[index]
                else:
                    index += 1

            while True:
                if available_vehicles:
                    if rides:
                        ride = rides.pop(0)
                        if ride.is_doable(t):
                            available_vehicles.sort(key=lambda x: manhattan_dist(x.location, ride.start_loc),
                                                    reverse=False)

                            vehicle = available_vehicles[0]
                            if ride.is_still_doable(t, vehicle.location):
                                vehicle.get_assigned_to_ride(ride)
                                unavailable_vehicles.append(vehicle)
                                available_vehicles.remove(vehicle)

                        else:
                            canceled_rides.append(ride)
                    else:
                        break
                else:
                    break

        for vehicle in available_vehicles:
            print(vehicle.id, vehicle.history)

        print("\n Unavailable should be None")
        for vehicle in unavailable_vehicles:
            print(vehicle.id, vehicle.history, vehicle.route)

        print("\nCanceled rides: ", len(canceled_rides))
        for ride in canceled_rides:
            print(ride.code)

def manhattan_dist(x,y):
    return   abs(x[0]- y[0]) + abs(x[1] - y[1])


if __name__ == '__main__':
    main()
