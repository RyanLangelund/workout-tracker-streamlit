"""
-----------------------------------------------------------------------
ASSIGNMENT 13A: Object practice
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Define a class for a part of your project using PascalCase.
[ ] 3. Use __init__ to set private attributes (__variable).
[ ] 4. Write Setters and Getters for the attributes.
[ ] 5. Write a summary function that returns a formatted description.
[ ] 6. Instantiate two distinct objects and print their summaries.
-----------------------------------------------------------------------
"""


class Workout:
    def __init__(self, exercise, sets, reps, weight):
        self.__exercise = exercise
        self.__sets = sets
        self.__reps = reps
        self.__weight = weight

    def get_exercise(self):
        return self.__exercise

    def get_sets(self):
        return self.__sets

    def get_reps(self):
        return self.__reps

    def get_weight(self):
        return self.__weight

    def set_sets(self, sets):
        if sets > 0:
            self.__sets = sets

    def set_reps(self, reps):
        if reps > 0:
            self.__reps = reps

    def set_weight(self, weight):
        if weight >= 0:
            self.__weight = weight

    def get_summary(self):
        return (
            f"Exercise: {self.__exercise}\n"
            f"Sets: {self.__sets}\n"
            f"Reps: {self.__reps}\n"
            f"Weight: {self.__weight} lbs\n"
        )


def main():
    workout1 = Workout("Bench Press", 3, 10, 135)
    workout2 = Workout("Squat", 4, 8, 185)

    print("WORKOUT 1")
    print(workout1.get_summary())

    print("WORKOUT 2")
    print(workout2.get_summary())


main()
