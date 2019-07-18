
from Classes.Evolution import Evolution

population = 10
evolution = Evolution(population)
i = 0
while 0 < population < 50:
    print("step", i, ": population of", population, "\n", evolution, "\n")
    evolution.step_reproduce()
    evolution.step_feed()
    population = evolution.step_survive()
    i += 1

print("step", i, ": population of", population, "\n", evolution, "\n")
