from workout_sprint6 import Workout


def main():
    workout1 = Workout("Bench Press", 3, 10, 135)

    workout1.set_weight(150)

    print(workout1.get_summary())


main()
