import random
import time

def get_list_average(list_of_results):
    list_sum = 0
    for result in list_of_results:
        list_sum += result
    average = list_sum / len(list_of_results)
    return average


def get_list_sum(list_of_results):
    sum_total = 0
    for result in list_of_results:
        sum_total += result
    return sum_total


def roll_a_die(_min=1, _max=6):
    values_of_active_die = list()
    for i in range(_min, _max, 1):
        values_of_active_die.append(i) 
    die_roll = random.choice(values_of_active_die)
    return die_roll


def roll_dice_x_times(times=216):
    all_dice_rolls = list()
    for i in range(times):
        all_dice_rolls.append(roll_n_dice(_min=1, _max=6, qty=2))
    return all_dice_rolls


def roll_n_dice(_min=1, _max=6, qty=2):
    result_of_n_dice = list()
    for i in range(qty):
        result_of_n_dice.append(roll_a_die(_min, _max))
    sum_of_dice_roll = get_list_sum(result_of_n_dice)
    return sum_of_dice_roll


def main():
    for i in range(999):
        list_of_roll_results = roll_dice_x_times()
        print(get_list_average(list_of_roll_results))
        time.sleep(0.25)


if __name__ == '__main__':
    main()
