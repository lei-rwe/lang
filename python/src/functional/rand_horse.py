# 我们有3辆车比赛，简单起见，我们分别给这3辆车有70%的概率可以
# 往前走一步，一共有5次机会，我们打出每一次这3辆车的前行状态。

from random import random
def run():
    time = 5
    car_positions = [1, 1, 1]
    for x in range(5):
        print('')
        for i in range(len(car_positions)):
            # move car
            if random() > 0.3:
                car_positions[i] += 1
            # draw car
            print('-' * car_positions[i])

def move_cars(car_positions):
    return map(lambda x: x + 1 if random() > 0.3 else x,
               car_positions)

def run_step_of_race(state):
    cp = list(move_cars(state['car_positions']))
    return {'time': state['time'] - 1,
            'car_positions': cp}

def output_car(car_position):
    return '-' * car_position

def draw(state):
    print('')
    print('\n'.join(map(output_car, state['car_positions'])))

def race(state):
    draw(state)
    if state['time']:
        race(run_step_of_race(state))

race({'time': 5,
      'car_positions': [1, 1, 1]})

