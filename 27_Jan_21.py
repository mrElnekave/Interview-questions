# golf balls are chucked out of a 1000 storie building,
# at what height do these golf balls start breaking (floor)
# to throw each golf ball it costs 1 dollar
# if we have infinite balls what is the most cost-efficient way to find the "x" floor
# if we only have 2 balls, what is the most cost-efficient method to find "x" floor

def nice_algorithm(
        building_height=1000
        , golf_balls=2
        , payperfloor=1
        , magic_floor=500):
    current_cost = 0
    current_floor = 0

    def get_best_number():
        closest_above = 0
        numbers_passed = 0
        for i in range(building_height):
            if (closest_above >= building_height):
                numbers_passed = i
                break
            else:
                closest_above += i

        return numbers_passed

    best_number = get_best_number()

    for i in range(best_number, 1, -1):
        current_floor += i
        current_cost += payperfloor

        if current_floor >= magic_floor:
            # 1 golf ball breaks
            golf_balls -= 1
            # back sequence
            # first we go down to our previous floor
            current_floor -= i
            # have to go one by one throwing
            for j in range(i):
                current_floor += 1
                current_cost += payperfloor
                if current_floor == magic_floor:
                    return (current_floor, current_cost)
            # note: if we had three balls before the 1by1 step we could repeat the "best number" step
            # with the extra golf ball we have in our new range

            pass


print(nice_algorithm())

# notes for improvement:
"""
don't let your function know the magic_floor have a black box program that takes in a floor and says break or not
inside the main function I should have two steps, 
step 1 is find the magic number and test using it
step 2 is going linearly one by one
then a main loop which continues doing step one in smaller and smaller intervals until we only have one golf ball left
which we would then need to go to step 2

curr_range(min, max)
while (golf_balls > 1){
    step 1(max-min)
}
step 2
"""
