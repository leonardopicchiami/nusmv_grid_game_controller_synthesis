def Legal(state, action):

    if (state[0] < 0 or state[0] >= 49) or (state[1] < 0 or state[1] >= 52):
        raise Exception("The input state is not among the grid states.")

    if action.lower() not in ["up", "left-up", "right-up", "right", "right-down", "down", "left-down", "left"]:
        raise Exception("The input action is not among the actions that can be performed.")

    if state == (0, 0) and action.lower() == "down":
        return True

    if state == (0, 2) and action.lower() == "right-down":
        return True

    if state == (0, 5) and action.lower() == "right":
        return True

    if state == (0, 5) and action.lower() == "down":
        return True

    if state == (0, 5) and action.lower() == "left-down":
        return True

    if state == (0, 6) and action.lower() == "right":
        return True

    if state == (0, 6) and action.lower() == "right-down":
        return True

    if state == (0, 6) and action.lower() == "left-down":
        return True

    if state == (0, 6) and action.lower() == "left":
        return True

    if state == (0, 7) and action.lower() == "down":
        return True

    if state == (0, 7) and action.lower() == "left":
        return True

    if state == (0, 10) and action.lower() == "down":
        return True

    if state == (0, 10) and action.lower() == "left-down":
        return True

    if state == (0, 14) and action.lower() == "right-down":
        return True

    if state == (0, 14) and action.lower() == "down":
        return True

    if state == (0, 16) and action.lower() == "right":
        return True

    if state == (0, 16) and action.lower() == "left-down":
        return True

    if state == (0, 17) and action.lower() == "right-down":
        return True

    if state == (0, 17) and action.lower() == "left":
        return True

    if state == (0, 19) and action.lower() == "right":
        return True

    if state == (0, 19) and action.lower() == "right-down":
        return True

    if state == (0, 19) and action.lower() == "down":
        return True

    if state == (0, 19) and action.lower() == "left-down":
        return True

    if state == (0, 20) and action.lower() == "right":
        return True

    if state == (0, 20) and action.lower() == "down":
        return True

    if state == (0, 20) and action.lower() == "left-down":
        return True

    if state == (0, 20) and action.lower() == "left":
        return True

    if state == (0, 21) and action.lower() == "right":
        return True

    if state == (0, 21) and action.lower() == "right-down":
        return True

    if state == (0, 21) and action.lower() == "left-down":
        return True

    if state == (0, 21) and action.lower() == "left":
        return True

    if state == (0, 22) and action.lower() == "right-down":
        return True

    if state == (0, 22) and action.lower() == "down":
        return True

    if state == (0, 22) and action.lower() == "left":
        return True

    if state == (0, 24) and action.lower() == "down":
        return True

    if state == (0, 24) and action.lower() == "left-down":
        return True

    if state == (0, 28) and action.lower() == "right":
        return True

    if state == (0, 28) and action.lower() == "down":
        return True

    if state == (0, 28) and action.lower() == "left-down":
        return True

    if state == (0, 29) and action.lower() == "right":
        return True

    if state == (0, 29) and action.lower() == "left-down":
        return True

    if state == (0, 29) and action.lower() == "left":
        return True

    if state == (0, 30) and action.lower() == "right-down":
        return True

    if state == (0, 30) and action.lower() == "left":
        return True

    if state == (0, 33) and action.lower() == "down":
        return True

    if state == (0, 33) and action.lower() == "left-down":
        return True

    if state == (0, 35) and action.lower() == "right-down":
        return True

    if state == (0, 35) and action.lower() == "down":
        return True

    if state == (0, 42) and action.lower() == "right":
        return True

    if state == (0, 42) and action.lower() == "right-down":
        return True

    if state == (0, 42) and action.lower() == "down":
        return True

    if state == (0, 42) and action.lower() == "left-down":
        return True

    if state == (0, 43) and action.lower() == "right":
        return True

    if state == (0, 43) and action.lower() == "down":
        return True

    if state == (0, 43) and action.lower() == "left-down":
        return True

    if state == (0, 43) and action.lower() == "left":
        return True

    if state == (0, 44) and action.lower() == "right":
        return True

    if state == (0, 44) and action.lower() == "left-down":
        return True

    if state == (0, 44) and action.lower() == "left":
        return True

    if state == (0, 45) and action.lower() == "right-down":
        return True

    if state == (0, 45) and action.lower() == "left":
        return True

    if state == (0, 47) and action.lower() == "left-down":
        return True

    if state == (0, 50) and action.lower() == "right":
        return True

    if state == (0, 50) and action.lower() == "right-down":
        return True

    if state == (0, 50) and action.lower() == "down":
        return True

    if state == (0, 50) and action.lower() == "left-down":
        return True

    if state == (0, 51) and action.lower() == "down":
        return True

    if state == (0, 51) and action.lower() == "left-down":
        return True

    if state == (0, 51) and action.lower() == "left":
        return True

    if state == (1, 0) and action.lower() == "up":
        return True

    if state == (1, 3) and action.lower() == "left-up":
        return True

    if state == (1, 3) and action.lower() == "right":
        return True

    if state == (1, 3) and action.lower() == "right-down":
        return True

    if state == (1, 4) and action.lower() == "right-up":
        return True

    if state == (1, 4) and action.lower() == "right":
        return True

    if state == (1, 4) and action.lower() == "down":
        return True

    if state == (1, 4) and action.lower() == "left":
        return True

    if state == (1, 5) and action.lower() == "up":
        return True

    if state == (1, 5) and action.lower() == "right-up":
        return True

    if state == (1, 5) and action.lower() == "right-down":
        return True

    if state == (1, 5) and action.lower() == "left-down":
        return True

    if state == (1, 5) and action.lower() == "left":
        return True

    if state == (1, 7) and action.lower() == "left-up":
        return True

    if state == (1, 7) and action.lower() == "up":
        return True

    if state == (1, 7) and action.lower() == "left-down":
        return True

    if state == (1, 9) and action.lower() == "right-up":
        return True

    if state == (1, 9) and action.lower() == "right":
        return True

    if state == (1, 9) and action.lower() == "right-down":
        return True

    if state == (1, 10) and action.lower() == "up":
        return True

    if state == (1, 10) and action.lower() == "right-down":
        return True

    if state == (1, 10) and action.lower() == "down":
        return True

    if state == (1, 10) and action.lower() == "left":
        return True

    if state == (1, 14) and action.lower() == "up":
        return True

    if state == (1, 14) and action.lower() == "right":
        return True

    if state == (1, 14) and action.lower() == "down":
        return True

    if state == (1, 14) and action.lower() == "left-down":
        return True

    if state == (1, 15) and action.lower() == "left-up":
        return True

    if state == (1, 15) and action.lower() == "right-up":
        return True

    if state == (1, 15) and action.lower() == "right-down":
        return True

    if state == (1, 15) and action.lower() == "left-down":
        return True

    if state == (1, 15) and action.lower() == "left":
        return True

    if state == (1, 18) and action.lower() == "left-up":
        return True

    if state == (1, 18) and action.lower() == "right-up":
        return True

    if state == (1, 18) and action.lower() == "right":
        return True

    if state == (1, 18) and action.lower() == "down":
        return True

    if state == (1, 18) and action.lower() == "left-down":
        return True

    if state == (1, 19) and action.lower() == "up":
        return True

    if state == (1, 19) and action.lower() == "right-up":
        return True

    if state == (1, 19) and action.lower() == "right":
        return True

    if state == (1, 19) and action.lower() == "right-down":
        return True

    if state == (1, 19) and action.lower() == "left-down":
        return True

    if state == (1, 19) and action.lower() == "left":
        return True

    if state == (1, 20) and action.lower() == "left-up":
        return True

    if state == (1, 20) and action.lower() == "up":
        return True

    if state == (1, 20) and action.lower() == "right-up":
        return True

    if state == (1, 20) and action.lower() == "right-down":
        return True

    if state == (1, 20) and action.lower() == "down":
        return True

    if state == (1, 20) and action.lower() == "left":
        return True

    if state == (1, 22) and action.lower() == "left-up":
        return True

    if state == (1, 22) and action.lower() == "up":
        return True

    if state == (1, 22) and action.lower() == "right":
        return True

    if state == (1, 22) and action.lower() == "right-down":
        return True

    if state == (1, 22) and action.lower() == "down":
        return True

    if state == (1, 22) and action.lower() == "left-down":
        return True

    if state == (1, 23) and action.lower() == "left-up":
        return True

    if state == (1, 23) and action.lower() == "right-up":
        return True

    if state == (1, 23) and action.lower() == "right":
        return True

    if state == (1, 23) and action.lower() == "down":
        return True

    if state == (1, 23) and action.lower() == "left-down":
        return True

    if state == (1, 23) and action.lower() == "left":
        return True

    if state == (1, 24) and action.lower() == "up":
        return True

    if state == (1, 24) and action.lower() == "left-down":
        return True

    if state == (1, 24) and action.lower() == "left":
        return True

    if state == (1, 27) and action.lower() == "right-up":
        return True

    if state == (1, 27) and action.lower() == "right":
        return True

    if state == (1, 27) and action.lower() == "right-down":
        return True

    if state == (1, 28) and action.lower() == "up":
        return True

    if state == (1, 28) and action.lower() == "right-up":
        return True

    if state == (1, 28) and action.lower() == "right-down":
        return True

    if state == (1, 28) and action.lower() == "down":
        return True

    if state == (1, 28) and action.lower() == "left":
        return True

    if state == (1, 31) and action.lower() == "left-up":
        return True

    if state == (1, 31) and action.lower() == "right":
        return True

    if state == (1, 31) and action.lower() == "down":
        return True

    if state == (1, 32) and action.lower() == "right-up":
        return True

    if state == (1, 32) and action.lower() == "right":
        return True

    if state == (1, 32) and action.lower() == "left-down":
        return True

    if state == (1, 32) and action.lower() == "left":
        return True

    if state == (1, 33) and action.lower() == "up":
        return True

    if state == (1, 33) and action.lower() == "right-down":
        return True

    if state == (1, 33) and action.lower() == "left":
        return True

    if state == (1, 35) and action.lower() == "up":
        return True

    if state == (1, 35) and action.lower() == "right":
        return True

    if state == (1, 35) and action.lower() == "right-down":
        return True

    if state == (1, 35) and action.lower() == "left-down":
        return True

    if state == (1, 36) and action.lower() == "left-up":
        return True

    if state == (1, 36) and action.lower() == "right":
        return True

    if state == (1, 36) and action.lower() == "right-down":
        return True

    if state == (1, 36) and action.lower() == "down":
        return True

    if state == (1, 36) and action.lower() == "left":
        return True

    if state == (1, 37) and action.lower() == "right":
        return True

    if state == (1, 37) and action.lower() == "right-down":
        return True

    if state == (1, 37) and action.lower() == "down":
        return True

    if state == (1, 37) and action.lower() == "left-down":
        return True

    if state == (1, 37) and action.lower() == "left":
        return True

    if state == (1, 38) and action.lower() == "right":
        return True

    if state == (1, 38) and action.lower() == "right-down":
        return True

    if state == (1, 38) and action.lower() == "down":
        return True

    if state == (1, 38) and action.lower() == "left-down":
        return True

    if state == (1, 38) and action.lower() == "left":
        return True

    if state == (1, 39) and action.lower() == "right":
        return True

    if state == (1, 39) and action.lower() == "down":
        return True

    if state == (1, 39) and action.lower() == "left-down":
        return True

    if state == (1, 39) and action.lower() == "left":
        return True

    if state == (1, 40) and action.lower() == "right":
        return True

    if state == (1, 40) and action.lower() == "right-down":
        return True

    if state == (1, 40) and action.lower() == "left-down":
        return True

    if state == (1, 40) and action.lower() == "left":
        return True

    if state == (1, 41) and action.lower() == "right-up":
        return True

    if state == (1, 41) and action.lower() == "right":
        return True

    if state == (1, 41) and action.lower() == "right-down":
        return True

    if state == (1, 41) and action.lower() == "down":
        return True

    if state == (1, 41) and action.lower() == "left":
        return True

    if state == (1, 42) and action.lower() == "up":
        return True

    if state == (1, 42) and action.lower() == "right-up":
        return True

    if state == (1, 42) and action.lower() == "right":
        return True

    if state == (1, 42) and action.lower() == "down":
        return True

    if state == (1, 42) and action.lower() == "left-down":
        return True

    if state == (1, 42) and action.lower() == "left":
        return True

    if state == (1, 43) and action.lower() == "left-up":
        return True

    if state == (1, 43) and action.lower() == "up":
        return True

    if state == (1, 43) and action.lower() == "right-up":
        return True

    if state == (1, 43) and action.lower() == "left-down":
        return True

    if state == (1, 43) and action.lower() == "left":
        return True

    if state == (1, 46) and action.lower() == "left-up":
        return True

    if state == (1, 46) and action.lower() == "right-up":
        return True

    if state == (1, 46) and action.lower() == "down":
        return True

    if state == (1, 49) and action.lower() == "right-up":
        return True

    if state == (1, 49) and action.lower() == "right":
        return True

    if state == (1, 49) and action.lower() == "right-down":
        return True

    if state == (1, 49) and action.lower() == "down":
        return True

    if state == (1, 49) and action.lower() == "left-down":
        return True

    if state == (1, 50) and action.lower() == "up":
        return True

    if state == (1, 50) and action.lower() == "right-up":
        return True

    if state == (1, 50) and action.lower() == "right":
        return True

    if state == (1, 50) and action.lower() == "right-down":
        return True

    if state == (1, 50) and action.lower() == "down":
        return True

    if state == (1, 50) and action.lower() == "left-down":
        return True

    if state == (1, 50) and action.lower() == "left":
        return True

    if state == (1, 51) and action.lower() == "left-up":
        return True

    if state == (1, 51) and action.lower() == "up":
        return True

    if state == (1, 51) and action.lower() == "down":
        return True

    if state == (1, 51) and action.lower() == "left-down":
        return True

    if state == (1, 51) and action.lower() == "left":
        return True

    if state == (2, 4) and action.lower() == "left-up":
        return True

    if state == (2, 4) and action.lower() == "up":
        return True

    if state == (2, 4) and action.lower() == "right-up":
        return True

    if state == (2, 6) and action.lower() == "left-up":
        return True

    if state == (2, 6) and action.lower() == "right-up":
        return True

    if state == (2, 10) and action.lower() == "left-up":
        return True

    if state == (2, 10) and action.lower() == "up":
        return True

    if state == (2, 10) and action.lower() == "right":
        return True

    if state == (2, 10) and action.lower() == "down":
        return True

    if state == (2, 10) and action.lower() == "left-down":
        return True

    if state == (2, 11) and action.lower() == "left-up":
        return True

    if state == (2, 11) and action.lower() == "right-down":
        return True

    if state == (2, 11) and action.lower() == "left-down":
        return True

    if state == (2, 11) and action.lower() == "left":
        return True

    if state == (2, 13) and action.lower() == "right-up":
        return True

    if state == (2, 13) and action.lower() == "right":
        return True

    if state == (2, 13) and action.lower() == "left-down":
        return True

    if state == (2, 14) and action.lower() == "up":
        return True

    if state == (2, 14) and action.lower() == "right-up":
        return True

    if state == (2, 14) and action.lower() == "right-down":
        return True

    if state == (2, 14) and action.lower() == "left":
        return True

    if state == (2, 16) and action.lower() == "left-up":
        return True

    if state == (2, 16) and action.lower() == "right":
        return True

    if state == (2, 16) and action.lower() == "down":
        return True

    if state == (2, 16) and action.lower() == "left-down":
        return True

    if state == (2, 17) and action.lower() == "right-up":
        return True

    if state == (2, 17) and action.lower() == "right":
        return True

    if state == (2, 17) and action.lower() == "left-down":
        return True

    if state == (2, 17) and action.lower() == "left":
        return True

    if state == (2, 18) and action.lower() == "up":
        return True

    if state == (2, 18) and action.lower() == "right-up":
        return True

    if state == (2, 18) and action.lower() == "left":
        return True

    if state == (2, 20) and action.lower() == "left-up":
        return True

    if state == (2, 20) and action.lower() == "up":
        return True

    if state == (2, 20) and action.lower() == "right":
        return True

    if state == (2, 20) and action.lower() == "right-down":
        return True

    if state == (2, 20) and action.lower() == "down":
        return True

    if state == (2, 21) and action.lower() == "left-up":
        return True

    if state == (2, 21) and action.lower() == "right-up":
        return True

    if state == (2, 21) and action.lower() == "right":
        return True

    if state == (2, 21) and action.lower() == "down":
        return True

    if state == (2, 21) and action.lower() == "left-down":
        return True

    if state == (2, 21) and action.lower() == "left":
        return True

    if state == (2, 22) and action.lower() == "up":
        return True

    if state == (2, 22) and action.lower() == "right-up":
        return True

    if state == (2, 22) and action.lower() == "right":
        return True

    if state == (2, 22) and action.lower() == "right-down":
        return True

    if state == (2, 22) and action.lower() == "left-down":
        return True

    if state == (2, 22) and action.lower() == "left":
        return True

    if state == (2, 23) and action.lower() == "left-up":
        return True

    if state == (2, 23) and action.lower() == "up":
        return True

    if state == (2, 23) and action.lower() == "right-up":
        return True

    if state == (2, 23) and action.lower() == "right-down":
        return True

    if state == (2, 23) and action.lower() == "down":
        return True

    if state == (2, 23) and action.lower() == "left":
        return True

    if state == (2, 28) and action.lower() == "left-up":
        return True

    if state == (2, 28) and action.lower() == "up":
        return True

    if state == (2, 28) and action.lower() == "right":
        return True

    if state == (2, 28) and action.lower() == "right-down":
        return True

    if state == (2, 28) and action.lower() == "down":
        return True

    if state == (2, 28) and action.lower() == "left-down":
        return True

    if state == (2, 29) and action.lower() == "left-up":
        return True

    if state == (2, 29) and action.lower() == "down":
        return True

    if state == (2, 29) and action.lower() == "left-down":
        return True

    if state == (2, 29) and action.lower() == "left":
        return True

    if state == (2, 31) and action.lower() == "up":
        return True

    if state == (2, 31) and action.lower() == "right-up":
        return True

    if state == (2, 34) and action.lower() == "left-up":
        return True

    if state == (2, 34) and action.lower() == "right-up":
        return True

    if state == (2, 34) and action.lower() == "right-down":
        return True

    if state == (2, 34) and action.lower() == "down":
        return True

    if state == (2, 34) and action.lower() == "left-down":
        return True

    if state == (2, 36) and action.lower() == "left-up":
        return True

    if state == (2, 36) and action.lower() == "up":
        return True

    if state == (2, 36) and action.lower() == "right-up":
        return True

    if state == (2, 36) and action.lower() == "right":
        return True

    if state == (2, 36) and action.lower() == "left-down":
        return True

    if state == (2, 37) and action.lower() == "left-up":
        return True

    if state == (2, 37) and action.lower() == "up":
        return True

    if state == (2, 37) and action.lower() == "right-up":
        return True

    if state == (2, 37) and action.lower() == "right":
        return True

    if state == (2, 37) and action.lower() == "left":
        return True

    if state == (2, 38) and action.lower() == "left-up":
        return True

    if state == (2, 38) and action.lower() == "up":
        return True

    if state == (2, 38) and action.lower() == "right-up":
        return True

    if state == (2, 38) and action.lower() == "right":
        return True

    if state == (2, 38) and action.lower() == "right-down":
        return True

    if state == (2, 38) and action.lower() == "left":
        return True

    if state == (2, 39) and action.lower() == "left-up":
        return True

    if state == (2, 39) and action.lower() == "up":
        return True

    if state == (2, 39) and action.lower() == "right-up":
        return True

    if state == (2, 39) and action.lower() == "down":
        return True

    if state == (2, 39) and action.lower() == "left":
        return True

    if state == (2, 41) and action.lower() == "left-up":
        return True

    if state == (2, 41) and action.lower() == "up":
        return True

    if state == (2, 41) and action.lower() == "right-up":
        return True

    if state == (2, 41) and action.lower() == "right":
        return True

    if state == (2, 41) and action.lower() == "right-down":
        return True

    if state == (2, 41) and action.lower() == "down":
        return True

    if state == (2, 42) and action.lower() == "left-up":
        return True

    if state == (2, 42) and action.lower() == "up":
        return True

    if state == (2, 42) and action.lower() == "right-up":
        return True

    if state == (2, 42) and action.lower() == "right-down":
        return True

    if state == (2, 42) and action.lower() == "down":
        return True

    if state == (2, 42) and action.lower() == "left-down":
        return True

    if state == (2, 42) and action.lower() == "left":
        return True

    if state == (2, 46) and action.lower() == "up":
        return True

    if state == (2, 46) and action.lower() == "left-down":
        return True

    if state == (2, 48) and action.lower() == "right-up":
        return True

    if state == (2, 48) and action.lower() == "right":
        return True

    if state == (2, 48) and action.lower() == "right-down":
        return True

    if state == (2, 49) and action.lower() == "up":
        return True

    if state == (2, 49) and action.lower() == "right-up":
        return True

    if state == (2, 49) and action.lower() == "right":
        return True

    if state == (2, 49) and action.lower() == "down":
        return True

    if state == (2, 49) and action.lower() == "left":
        return True

    if state == (2, 50) and action.lower() == "left-up":
        return True

    if state == (2, 50) and action.lower() == "up":
        return True

    if state == (2, 50) and action.lower() == "right-up":
        return True

    if state == (2, 50) and action.lower() == "right":
        return True

    if state == (2, 50) and action.lower() == "left-down":
        return True

    if state == (2, 50) and action.lower() == "left":
        return True

    if state == (2, 51) and action.lower() == "left-up":
        return True

    if state == (2, 51) and action.lower() == "up":
        return True

    if state == (2, 51) and action.lower() == "left":
        return True

    if state == (3, 0) and action.lower() == "right":
        return True

    if state == (3, 0) and action.lower() == "down":
        return True

    if state == (3, 1) and action.lower() == "right":
        return True

    if state == (3, 1) and action.lower() == "left-down":
        return True

    if state == (3, 1) and action.lower() == "left":
        return True

    if state == (3, 2) and action.lower() == "left":
        return True

    if state == (3, 8) and action.lower() == "right":
        return True

    if state == (3, 8) and action.lower() == "right-down":
        return True

    if state == (3, 8) and action.lower() == "down":
        return True

    if state == (3, 9) and action.lower() == "right-up":
        return True

    if state == (3, 9) and action.lower() == "right":
        return True

    if state == (3, 9) and action.lower() == "right-down":
        return True

    if state == (3, 9) and action.lower() == "down":
        return True

    if state == (3, 9) and action.lower() == "left-down":
        return True

    if state == (3, 9) and action.lower() == "left":
        return True

    if state == (3, 10) and action.lower() == "up":
        return True

    if state == (3, 10) and action.lower() == "right-up":
        return True

    if state == (3, 10) and action.lower() == "right-down":
        return True

    if state == (3, 10) and action.lower() == "down":
        return True

    if state == (3, 10) and action.lower() == "left-down":
        return True

    if state == (3, 10) and action.lower() == "left":
        return True

    if state == (3, 12) and action.lower() == "left-up":
        return True

    if state == (3, 12) and action.lower() == "right-up":
        return True

    if state == (3, 12) and action.lower() == "right-down":
        return True

    if state == (3, 12) and action.lower() == "down":
        return True

    if state == (3, 12) and action.lower() == "left-down":
        return True

    if state == (3, 15) and action.lower() == "left-up":
        return True

    if state == (3, 15) and action.lower() == "right-up":
        return True

    if state == (3, 15) and action.lower() == "right":
        return True

    if state == (3, 15) and action.lower() == "right-down":
        return True

    if state == (3, 15) and action.lower() == "down":
        return True

    if state == (3, 16) and action.lower() == "up":
        return True

    if state == (3, 16) and action.lower() == "right-up":
        return True

    if state == (3, 16) and action.lower() == "right-down":
        return True

    if state == (3, 16) and action.lower() == "down":
        return True

    if state == (3, 16) and action.lower() == "left-down":
        return True

    if state == (3, 16) and action.lower() == "left":
        return True

    if state == (3, 20) and action.lower() == "up":
        return True

    if state == (3, 20) and action.lower() == "right-up":
        return True

    if state == (3, 20) and action.lower() == "right":
        return True

    if state == (3, 20) and action.lower() == "right-down":
        return True

    if state == (3, 20) and action.lower() == "down":
        return True

    if state == (3, 20) and action.lower() == "left-down":
        return True

    if state == (3, 21) and action.lower() == "left-up":
        return True

    if state == (3, 21) and action.lower() == "up":
        return True

    if state == (3, 21) and action.lower() == "right-up":
        return True

    if state == (3, 21) and action.lower() == "down":
        return True

    if state == (3, 21) and action.lower() == "left-down":
        return True

    if state == (3, 21) and action.lower() == "left":
        return True

    if state == (3, 23) and action.lower() == "left-up":
        return True

    if state == (3, 23) and action.lower() == "up":
        return True

    if state == (3, 23) and action.lower() == "right":
        return True

    if state == (3, 23) and action.lower() == "right-down":
        return True

    if state == (3, 24) and action.lower() == "left-up":
        return True

    if state == (3, 24) and action.lower() == "right-down":
        return True

    if state == (3, 24) and action.lower() == "down":
        return True

    if state == (3, 24) and action.lower() == "left":
        return True

    if state == (3, 27) and action.lower() == "right-up":
        return True

    if state == (3, 27) and action.lower() == "right":
        return True

    if state == (3, 27) and action.lower() == "right-down":
        return True

    if state == (3, 28) and action.lower() == "up":
        return True

    if state == (3, 28) and action.lower() == "right-up":
        return True

    if state == (3, 28) and action.lower() == "right":
        return True

    if state == (3, 28) and action.lower() == "right-down":
        return True

    if state == (3, 28) and action.lower() == "down":
        return True

    if state == (3, 28) and action.lower() == "left":
        return True

    if state == (3, 29) and action.lower() == "left-up":
        return True

    if state == (3, 29) and action.lower() == "up":
        return True

    if state == (3, 29) and action.lower() == "down":
        return True

    if state == (3, 29) and action.lower() == "left-down":
        return True

    if state == (3, 29) and action.lower() == "left":
        return True

    if state == (3, 33) and action.lower() == "right-up":
        return True

    if state == (3, 33) and action.lower() == "right":
        return True

    if state == (3, 33) and action.lower() == "down":
        return True

    if state == (3, 34) and action.lower() == "up":
        return True

    if state == (3, 34) and action.lower() == "right":
        return True

    if state == (3, 34) and action.lower() == "right-down":
        return True

    if state == (3, 34) and action.lower() == "left-down":
        return True

    if state == (3, 34) and action.lower() == "left":
        return True

    if state == (3, 35) and action.lower() == "left-up":
        return True

    if state == (3, 35) and action.lower() == "right-up":
        return True

    if state == (3, 35) and action.lower() == "down":
        return True

    if state == (3, 35) and action.lower() == "left":
        return True

    if state == (3, 39) and action.lower() == "left-up":
        return True

    if state == (3, 39) and action.lower() == "up":
        return True

    if state == (3, 39) and action.lower() == "right-down":
        return True

    if state == (3, 39) and action.lower() == "down":
        return True

    if state == (3, 41) and action.lower() == "up":
        return True

    if state == (3, 41) and action.lower() == "right-up":
        return True

    if state == (3, 41) and action.lower() == "right":
        return True

    if state == (3, 41) and action.lower() == "right-down":
        return True

    if state == (3, 41) and action.lower() == "down":
        return True

    if state == (3, 41) and action.lower() == "left-down":
        return True

    if state == (3, 42) and action.lower() == "left-up":
        return True

    if state == (3, 42) and action.lower() == "up":
        return True

    if state == (3, 42) and action.lower() == "right":
        return True

    if state == (3, 42) and action.lower() == "right-down":
        return True

    if state == (3, 42) and action.lower() == "down":
        return True

    if state == (3, 42) and action.lower() == "left-down":
        return True

    if state == (3, 42) and action.lower() == "left":
        return True

    if state == (3, 43) and action.lower() == "left-up":
        return True

    if state == (3, 43) and action.lower() == "right":
        return True

    if state == (3, 43) and action.lower() == "down":
        return True

    if state == (3, 43) and action.lower() == "left-down":
        return True

    if state == (3, 43) and action.lower() == "left":
        return True

    if state == (3, 44) and action.lower() == "right":
        return True

    if state == (3, 44) and action.lower() == "left-down":
        return True

    if state == (3, 44) and action.lower() == "left":
        return True

    if state == (3, 45) and action.lower() == "right-up":
        return True

    if state == (3, 45) and action.lower() == "right-down":
        return True

    if state == (3, 45) and action.lower() == "left":
        return True

    if state == (3, 49) and action.lower() == "left-up":
        return True

    if state == (3, 49) and action.lower() == "up":
        return True

    if state == (3, 49) and action.lower() == "right-up":
        return True

    if state == (3, 49) and action.lower() == "right-down":
        return True

    if state == (3, 49) and action.lower() == "down":
        return True

    if state == (3, 49) and action.lower() == "left-down":
        return True

    if state == (4, 0) and action.lower() == "up":
        return True

    if state == (4, 0) and action.lower() == "right-up":
        return True

    if state == (4, 0) and action.lower() == "down":
        return True

    if state == (4, 5) and action.lower() == "right-down":
        return True

    if state == (4, 8) and action.lower() == "up":
        return True

    if state == (4, 8) and action.lower() == "right-up":
        return True

    if state == (4, 8) and action.lower() == "right":
        return True

    if state == (4, 8) and action.lower() == "right-down":
        return True

    if state == (4, 8) and action.lower() == "down":
        return True

    if state == (4, 8) and action.lower() == "left-down":
        return True

    if state == (4, 9) and action.lower() == "left-up":
        return True

    if state == (4, 9) and action.lower() == "up":
        return True

    if state == (4, 9) and action.lower() == "right-up":
        return True

    if state == (4, 9) and action.lower() == "right":
        return True

    if state == (4, 9) and action.lower() == "down":
        return True

    if state == (4, 9) and action.lower() == "left-down":
        return True

    if state == (4, 9) and action.lower() == "left":
        return True

    if state == (4, 10) and action.lower() == "left-up":
        return True

    if state == (4, 10) and action.lower() == "up":
        return True

    if state == (4, 10) and action.lower() == "right":
        return True

    if state == (4, 10) and action.lower() == "left-down":
        return True

    if state == (4, 10) and action.lower() == "left":
        return True

    if state == (4, 11) and action.lower() == "left-up":
        return True

    if state == (4, 11) and action.lower() == "right-up":
        return True

    if state == (4, 11) and action.lower() == "right":
        return True

    if state == (4, 11) and action.lower() == "right-down":
        return True

    if state == (4, 11) and action.lower() == "left":
        return True

    if state == (4, 12) and action.lower() == "up":
        return True

    if state == (4, 12) and action.lower() == "right":
        return True

    if state == (4, 12) and action.lower() == "right-down":
        return True

    if state == (4, 12) and action.lower() == "down":
        return True

    if state == (4, 12) and action.lower() == "left":
        return True

    if state == (4, 13) and action.lower() == "left-up":
        return True

    if state == (4, 13) and action.lower() == "right-down":
        return True

    if state == (4, 13) and action.lower() == "down":
        return True

    if state == (4, 13) and action.lower() == "left-down":
        return True

    if state == (4, 13) and action.lower() == "left":
        return True

    if state == (4, 15) and action.lower() == "up":
        return True

    if state == (4, 15) and action.lower() == "right-up":
        return True

    if state == (4, 15) and action.lower() == "right":
        return True

    if state == (4, 15) and action.lower() == "right-down":
        return True

    if state == (4, 15) and action.lower() == "left-down":
        return True

    if state == (4, 16) and action.lower() == "left-up":
        return True

    if state == (4, 16) and action.lower() == "up":
        return True

    if state == (4, 16) and action.lower() == "right":
        return True

    if state == (4, 16) and action.lower() == "right-down":
        return True

    if state == (4, 16) and action.lower() == "down":
        return True

    if state == (4, 16) and action.lower() == "left":
        return True

    if state == (4, 17) and action.lower() == "left-up":
        return True

    if state == (4, 17) and action.lower() == "right-down":
        return True

    if state == (4, 17) and action.lower() == "down":
        return True

    if state == (4, 17) and action.lower() == "left-down":
        return True

    if state == (4, 17) and action.lower() == "left":
        return True

    if state == (4, 19) and action.lower() == "right-up":
        return True

    if state == (4, 19) and action.lower() == "right":
        return True

    if state == (4, 19) and action.lower() == "right-down":
        return True

    if state == (4, 19) and action.lower() == "down":
        return True

    if state == (4, 19) and action.lower() == "left-down":
        return True

    if state == (4, 20) and action.lower() == "up":
        return True

    if state == (4, 20) and action.lower() == "right-up":
        return True

    if state == (4, 20) and action.lower() == "right":
        return True

    if state == (4, 20) and action.lower() == "right-down":
        return True

    if state == (4, 20) and action.lower() == "down":
        return True

    if state == (4, 20) and action.lower() == "left-down":
        return True

    if state == (4, 20) and action.lower() == "left":
        return True

    if state == (4, 21) and action.lower() == "left-up":
        return True

    if state == (4, 21) and action.lower() == "up":
        return True

    if state == (4, 21) and action.lower() == "right-down":
        return True

    if state == (4, 21) and action.lower() == "down":
        return True

    if state == (4, 21) and action.lower() == "left-down":
        return True

    if state == (4, 21) and action.lower() == "left":
        return True

    if state == (4, 24) and action.lower() == "left-up":
        return True

    if state == (4, 24) and action.lower() == "up":
        return True

    if state == (4, 24) and action.lower() == "right":
        return True

    if state == (4, 24) and action.lower() == "right-down":
        return True

    if state == (4, 24) and action.lower() == "down":
        return True

    if state == (4, 24) and action.lower() == "left-down":
        return True

    if state == (4, 25) and action.lower() == "left-up":
        return True

    if state == (4, 25) and action.lower() == "down":
        return True

    if state == (4, 25) and action.lower() == "left-down":
        return True

    if state == (4, 25) and action.lower() == "left":
        return True

    if state == (4, 28) and action.lower() == "left-up":
        return True

    if state == (4, 28) and action.lower() == "up":
        return True

    if state == (4, 28) and action.lower() == "right-up":
        return True

    if state == (4, 28) and action.lower() == "right":
        return True

    if state == (4, 28) and action.lower() == "right-down":
        return True

    if state == (4, 28) and action.lower() == "down":
        return True

    if state == (4, 29) and action.lower() == "left-up":
        return True

    if state == (4, 29) and action.lower() == "up":
        return True

    if state == (4, 29) and action.lower() == "right-down":
        return True

    if state == (4, 29) and action.lower() == "down":
        return True

    if state == (4, 29) and action.lower() == "left-down":
        return True

    if state == (4, 29) and action.lower() == "left":
        return True

    if state == (4, 33) and action.lower() == "up":
        return True

    if state == (4, 33) and action.lower() == "right-up":
        return True

    if state == (4, 33) and action.lower() == "right-down":
        return True

    if state == (4, 33) and action.lower() == "down":
        return True

    if state == (4, 33) and action.lower() == "left-down":
        return True

    if state == (4, 35) and action.lower() == "left-up":
        return True

    if state == (4, 35) and action.lower() == "up":
        return True

    if state == (4, 35) and action.lower() == "left-down":
        return True

    if state == (4, 39) and action.lower() == "up":
        return True

    if state == (4, 39) and action.lower() == "right":
        return True

    if state == (4, 39) and action.lower() == "down":
        return True

    if state == (4, 40) and action.lower() == "left-up":
        return True

    if state == (4, 40) and action.lower() == "right-up":
        return True

    if state == (4, 40) and action.lower() == "right":
        return True

    if state == (4, 40) and action.lower() == "left-down":
        return True

    if state == (4, 40) and action.lower() == "left":
        return True

    if state == (4, 41) and action.lower() == "up":
        return True

    if state == (4, 41) and action.lower() == "right-up":
        return True

    if state == (4, 41) and action.lower() == "right":
        return True

    if state == (4, 41) and action.lower() == "left":
        return True

    if state == (4, 42) and action.lower() == "left-up":
        return True

    if state == (4, 42) and action.lower() == "up":
        return True

    if state == (4, 42) and action.lower() == "right-up":
        return True

    if state == (4, 42) and action.lower() == "right":
        return True

    if state == (4, 42) and action.lower() == "right-down":
        return True

    if state == (4, 42) and action.lower() == "left":
        return True

    if state == (4, 43) and action.lower() == "left-up":
        return True

    if state == (4, 43) and action.lower() == "up":
        return True

    if state == (4, 43) and action.lower() == "right-up":
        return True

    if state == (4, 43) and action.lower() == "down":
        return True

    if state == (4, 43) and action.lower() == "left":
        return True

    if state == (4, 46) and action.lower() == "left-up":
        return True

    if state == (4, 46) and action.lower() == "right":
        return True

    if state == (4, 46) and action.lower() == "down":
        return True

    if state == (4, 46) and action.lower() == "left-down":
        return True

    if state == (4, 47) and action.lower() == "right":
        return True

    if state == (4, 47) and action.lower() == "left-down":
        return True

    if state == (4, 47) and action.lower() == "left":
        return True

    if state == (4, 48) and action.lower() == "right-up":
        return True

    if state == (4, 48) and action.lower() == "right":
        return True

    if state == (4, 48) and action.lower() == "right-down":
        return True

    if state == (4, 48) and action.lower() == "left":
        return True

    if state == (4, 49) and action.lower() == "up":
        return True

    if state == (4, 49) and action.lower() == "right":
        return True

    if state == (4, 49) and action.lower() == "right-down":
        return True

    if state == (4, 49) and action.lower() == "down":
        return True

    if state == (4, 49) and action.lower() == "left":
        return True

    if state == (4, 50) and action.lower() == "left-up":
        return True

    if state == (4, 50) and action.lower() == "right":
        return True

    if state == (4, 50) and action.lower() == "right-down":
        return True

    if state == (4, 50) and action.lower() == "down":
        return True

    if state == (4, 50) and action.lower() == "left-down":
        return True

    if state == (4, 50) and action.lower() == "left":
        return True

    if state == (4, 51) and action.lower() == "down":
        return True

    if state == (4, 51) and action.lower() == "left-down":
        return True

    if state == (4, 51) and action.lower() == "left":
        return True

    if state == (5, 0) and action.lower() == "up":
        return True

    if state == (5, 0) and action.lower() == "right-down":
        return True

    if state == (5, 0) and action.lower() == "down":
        return True

    if state == (5, 2) and action.lower() == "right":
        return True

    if state == (5, 2) and action.lower() == "down":
        return True

    if state == (5, 2) and action.lower() == "left-down":
        return True

    if state == (5, 3) and action.lower() == "right-down":
        return True

    if state == (5, 3) and action.lower() == "left-down":
        return True

    if state == (5, 3) and action.lower() == "left":
        return True

    if state == (5, 6) and action.lower() == "left-up":
        return True

    if state == (5, 6) and action.lower() == "right":
        return True

    if state == (5, 6) and action.lower() == "right-down":
        return True

    if state == (5, 6) and action.lower() == "down":
        return True

    if state == (5, 7) and action.lower() == "right-up":
        return True

    if state == (5, 7) and action.lower() == "right":
        return True

    if state == (5, 7) and action.lower() == "down":
        return True

    if state == (5, 7) and action.lower() == "left-down":
        return True

    if state == (5, 7) and action.lower() == "left":
        return True

    if state == (5, 8) and action.lower() == "up":
        return True

    if state == (5, 8) and action.lower() == "right-up":
        return True

    if state == (5, 8) and action.lower() == "right":
        return True

    if state == (5, 8) and action.lower() == "left-down":
        return True

    if state == (5, 8) and action.lower() == "left":
        return True

    if state == (5, 9) and action.lower() == "left-up":
        return True

    if state == (5, 9) and action.lower() == "up":
        return True

    if state == (5, 9) and action.lower() == "right-up":
        return True

    if state == (5, 9) and action.lower() == "right-down":
        return True

    if state == (5, 9) and action.lower() == "left":
        return True

    if state == (5, 12) and action.lower() == "left-up":
        return True

    if state == (5, 12) and action.lower() == "up":
        return True

    if state == (5, 12) and action.lower() == "right-up":
        return True

    if state == (5, 12) and action.lower() == "right":
        return True

    if state == (5, 13) and action.lower() == "left-up":
        return True

    if state == (5, 13) and action.lower() == "up":
        return True

    if state == (5, 13) and action.lower() == "right":
        return True

    if state == (5, 13) and action.lower() == "left":
        return True

    if state == (5, 14) and action.lower() == "left-up":
        return True

    if state == (5, 14) and action.lower() == "right-up":
        return True

    if state == (5, 14) and action.lower() == "right-down":
        return True

    if state == (5, 14) and action.lower() == "left":
        return True

    if state == (5, 16) and action.lower() == "left-up":
        return True

    if state == (5, 16) and action.lower() == "up":
        return True

    if state == (5, 16) and action.lower() == "right-up":
        return True

    if state == (5, 16) and action.lower() == "right":
        return True

    if state == (5, 16) and action.lower() == "right-down":
        return True

    if state == (5, 16) and action.lower() == "down":
        return True

    if state == (5, 16) and action.lower() == "left-down":
        return True

    if state == (5, 17) and action.lower() == "left-up":
        return True

    if state == (5, 17) and action.lower() == "up":
        return True

    if state == (5, 17) and action.lower() == "right":
        return True

    if state == (5, 17) and action.lower() == "down":
        return True

    if state == (5, 17) and action.lower() == "left-down":
        return True

    if state == (5, 17) and action.lower() == "left":
        return True

    if state == (5, 18) and action.lower() == "left-up":
        return True

    if state == (5, 18) and action.lower() == "right-up":
        return True

    if state == (5, 18) and action.lower() == "right":
        return True

    if state == (5, 18) and action.lower() == "left-down":
        return True

    if state == (5, 18) and action.lower() == "left":
        return True

    if state == (5, 19) and action.lower() == "up":
        return True

    if state == (5, 19) and action.lower() == "right-up":
        return True

    if state == (5, 19) and action.lower() == "right":
        return True

    if state == (5, 19) and action.lower() == "right-down":
        return True

    if state == (5, 19) and action.lower() == "left":
        return True

    if state == (5, 20) and action.lower() == "left-up":
        return True

    if state == (5, 20) and action.lower() == "up":
        return True

    if state == (5, 20) and action.lower() == "right-up":
        return True

    if state == (5, 20) and action.lower() == "right":
        return True

    if state == (5, 20) and action.lower() == "down":
        return True

    if state == (5, 20) and action.lower() == "left":
        return True

    if state == (5, 21) and action.lower() == "left-up":
        return True

    if state == (5, 21) and action.lower() == "up":
        return True

    if state == (5, 21) and action.lower() == "right":
        return True

    if state == (5, 21) and action.lower() == "right-down":
        return True

    if state == (5, 21) and action.lower() == "left-down":
        return True

    if state == (5, 21) and action.lower() == "left":
        return True

    if state == (5, 22) and action.lower() == "left-up":
        return True

    if state == (5, 22) and action.lower() == "right":
        return True

    if state == (5, 22) and action.lower() == "down":
        return True

    if state == (5, 22) and action.lower() == "left":
        return True

    if state == (5, 23) and action.lower() == "right-up":
        return True

    if state == (5, 23) and action.lower() == "right":
        return True

    if state == (5, 23) and action.lower() == "left-down":
        return True

    if state == (5, 23) and action.lower() == "left":
        return True

    if state == (5, 24) and action.lower() == "up":
        return True

    if state == (5, 24) and action.lower() == "right-up":
        return True

    if state == (5, 24) and action.lower() == "right":
        return True

    if state == (5, 24) and action.lower() == "right-down":
        return True

    if state == (5, 24) and action.lower() == "left":
        return True

    if state == (5, 25) and action.lower() == "left-up":
        return True

    if state == (5, 25) and action.lower() == "up":
        return True

    if state == (5, 25) and action.lower() == "down":
        return True

    if state == (5, 25) and action.lower() == "left":
        return True

    if state == (5, 28) and action.lower() == "up":
        return True

    if state == (5, 28) and action.lower() == "right-up":
        return True

    if state == (5, 28) and action.lower() == "right":
        return True

    if state == (5, 28) and action.lower() == "right-down":
        return True

    if state == (5, 28) and action.lower() == "down":
        return True

    if state == (5, 28) and action.lower() == "left-down":
        return True

    if state == (5, 29) and action.lower() == "left-up":
        return True

    if state == (5, 29) and action.lower() == "up":
        return True

    if state == (5, 29) and action.lower() == "right":
        return True

    if state == (5, 29) and action.lower() == "down":
        return True

    if state == (5, 29) and action.lower() == "left-down":
        return True

    if state == (5, 29) and action.lower() == "left":
        return True

    if state == (5, 30) and action.lower() == "left-up":
        return True

    if state == (5, 30) and action.lower() == "right":
        return True

    if state == (5, 30) and action.lower() == "left-down":
        return True

    if state == (5, 30) and action.lower() == "left":
        return True

    if state == (5, 31) and action.lower() == "right":
        return True

    if state == (5, 31) and action.lower() == "right-down":
        return True

    if state == (5, 31) and action.lower() == "left":
        return True

    if state == (5, 32) and action.lower() == "right-up":
        return True

    if state == (5, 32) and action.lower() == "right":
        return True

    if state == (5, 32) and action.lower() == "down":
        return True

    if state == (5, 32) and action.lower() == "left":
        return True

    if state == (5, 33) and action.lower() == "up":
        return True

    if state == (5, 33) and action.lower() == "right":
        return True

    if state == (5, 33) and action.lower() == "left-down":
        return True

    if state == (5, 33) and action.lower() == "left":
        return True

    if state == (5, 34) and action.lower() == "left-up":
        return True

    if state == (5, 34) and action.lower() == "right-up":
        return True

    if state == (5, 34) and action.lower() == "right-down":
        return True

    if state == (5, 34) and action.lower() == "left":
        return True

    if state == (5, 37) and action.lower() == "right-down":
        return True

    if state == (5, 37) and action.lower() == "left-down":
        return True

    if state == (5, 39) and action.lower() == "up":
        return True

    if state == (5, 39) and action.lower() == "right-up":
        return True

    if state == (5, 39) and action.lower() == "left-down":
        return True

    if state == (5, 43) and action.lower() == "left-up":
        return True

    if state == (5, 43) and action.lower() == "up":
        return True

    if state == (5, 43) and action.lower() == "right-down":
        return True

    if state == (5, 43) and action.lower() == "left-down":
        return True

    if state == (5, 45) and action.lower() == "right-up":
        return True

    if state == (5, 45) and action.lower() == "right":
        return True

    if state == (5, 45) and action.lower() == "left-down":
        return True

    if state == (5, 46) and action.lower() == "up":
        return True

    if state == (5, 46) and action.lower() == "right-up":
        return True

    if state == (5, 46) and action.lower() == "right-down":
        return True

    if state == (5, 46) and action.lower() == "left":
        return True

    if state == (5, 49) and action.lower() == "left-up":
        return True

    if state == (5, 49) and action.lower() == "up":
        return True

    if state == (5, 49) and action.lower() == "right-up":
        return True

    if state == (5, 49) and action.lower() == "right":
        return True

    if state == (5, 49) and action.lower() == "down":
        return True

    if state == (5, 50) and action.lower() == "left-up":
        return True

    if state == (5, 50) and action.lower() == "up":
        return True

    if state == (5, 50) and action.lower() == "right-up":
        return True

    if state == (5, 50) and action.lower() == "right":
        return True

    if state == (5, 50) and action.lower() == "right-down":
        return True

    if state == (5, 50) and action.lower() == "left-down":
        return True

    if state == (5, 50) and action.lower() == "left":
        return True

    if state == (5, 51) and action.lower() == "left-up":
        return True

    if state == (5, 51) and action.lower() == "up":
        return True

    if state == (5, 51) and action.lower() == "down":
        return True

    if state == (5, 51) and action.lower() == "left":
        return True

    if state == (6, 0) and action.lower() == "up":
        return True

    if state == (6, 0) and action.lower() == "right":
        return True

    if state == (6, 0) and action.lower() == "down":
        return True

    if state == (6, 1) and action.lower() == "left-up":
        return True

    if state == (6, 1) and action.lower() == "right-up":
        return True

    if state == (6, 1) and action.lower() == "right":
        return True

    if state == (6, 1) and action.lower() == "left-down":
        return True

    if state == (6, 1) and action.lower() == "left":
        return True

    if state == (6, 2) and action.lower() == "up":
        return True

    if state == (6, 2) and action.lower() == "right-up":
        return True

    if state == (6, 2) and action.lower() == "left":
        return True

    if state == (6, 4) and action.lower() == "left-up":
        return True

    if state == (6, 4) and action.lower() == "right-down":
        return True

    if state == (6, 4) and action.lower() == "down":
        return True

    if state == (6, 6) and action.lower() == "up":
        return True

    if state == (6, 6) and action.lower() == "right-up":
        return True

    if state == (6, 6) and action.lower() == "right":
        return True

    if state == (6, 6) and action.lower() == "left-down":
        return True

    if state == (6, 7) and action.lower() == "left-up":
        return True

    if state == (6, 7) and action.lower() == "up":
        return True

    if state == (6, 7) and action.lower() == "right-up":
        return True

    if state == (6, 7) and action.lower() == "left":
        return True

    if state == (6, 10) and action.lower() == "left-up":
        return True

    if state == (6, 10) and action.lower() == "right-down":
        return True

    if state == (6, 10) and action.lower() == "left-down":
        return True

    if state == (6, 15) and action.lower() == "left-up":
        return True

    if state == (6, 15) and action.lower() == "right-up":
        return True

    if state == (6, 15) and action.lower() == "right":
        return True

    if state == (6, 15) and action.lower() == "left-down":
        return True

    if state == (6, 16) and action.lower() == "up":
        return True

    if state == (6, 16) and action.lower() == "right-up":
        return True

    if state == (6, 16) and action.lower() == "right":
        return True

    if state == (6, 16) and action.lower() == "left":
        return True

    if state == (6, 17) and action.lower() == "left-up":
        return True

    if state == (6, 17) and action.lower() == "up":
        return True

    if state == (6, 17) and action.lower() == "right-up":
        return True

    if state == (6, 17) and action.lower() == "right-down":
        return True

    if state == (6, 17) and action.lower() == "left":
        return True

    if state == (6, 20) and action.lower() == "left-up":
        return True

    if state == (6, 20) and action.lower() == "up":
        return True

    if state == (6, 20) and action.lower() == "right-up":
        return True

    if state == (6, 20) and action.lower() == "right-down":
        return True

    if state == (6, 22) and action.lower() == "left-up":
        return True

    if state == (6, 22) and action.lower() == "up":
        return True

    if state == (6, 22) and action.lower() == "right-up":
        return True

    if state == (6, 22) and action.lower() == "left-down":
        return True

    if state == (6, 25) and action.lower() == "left-up":
        return True

    if state == (6, 25) and action.lower() == "up":
        return True

    if state == (6, 25) and action.lower() == "down":
        return True

    if state == (6, 25) and action.lower() == "left-down":
        return True

    if state == (6, 27) and action.lower() == "right-up":
        return True

    if state == (6, 27) and action.lower() == "right":
        return True

    if state == (6, 27) and action.lower() == "down":
        return True

    if state == (6, 28) and action.lower() == "up":
        return True

    if state == (6, 28) and action.lower() == "right-up":
        return True

    if state == (6, 28) and action.lower() == "right":
        return True

    if state == (6, 28) and action.lower() == "left-down":
        return True

    if state == (6, 28) and action.lower() == "left":
        return True

    if state == (6, 29) and action.lower() == "left-up":
        return True

    if state == (6, 29) and action.lower() == "up":
        return True

    if state == (6, 29) and action.lower() == "right-up":
        return True

    if state == (6, 29) and action.lower() == "left":
        return True

    if state == (6, 32) and action.lower() == "left-up":
        return True

    if state == (6, 32) and action.lower() == "up":
        return True

    if state == (6, 32) and action.lower() == "right-up":
        return True

    if state == (6, 32) and action.lower() == "right-down":
        return True

    if state == (6, 32) and action.lower() == "down":
        return True

    if state == (6, 35) and action.lower() == "left-up":
        return True

    if state == (6, 35) and action.lower() == "right":
        return True

    if state == (6, 35) and action.lower() == "right-down":
        return True

    if state == (6, 35) and action.lower() == "down":
        return True

    if state == (6, 35) and action.lower() == "left-down":
        return True

    if state == (6, 36) and action.lower() == "right-up":
        return True

    if state == (6, 36) and action.lower() == "right-down":
        return True

    if state == (6, 36) and action.lower() == "down":
        return True

    if state == (6, 36) and action.lower() == "left-down":
        return True

    if state == (6, 36) and action.lower() == "left":
        return True

    if state == (6, 38) and action.lower() == "left-up":
        return True

    if state == (6, 38) and action.lower() == "right-up":
        return True

    if state == (6, 38) and action.lower() == "right-down":
        return True

    if state == (6, 38) and action.lower() == "left-down":
        return True

    if state == (6, 42) and action.lower() == "right-up":
        return True

    if state == (6, 42) and action.lower() == "down":
        return True

    if state == (6, 44) and action.lower() == "left-up":
        return True

    if state == (6, 44) and action.lower() == "right-up":
        return True

    if state == (6, 44) and action.lower() == "down":
        return True

    if state == (6, 47) and action.lower() == "left-up":
        return True

    if state == (6, 47) and action.lower() == "right-down":
        return True

    if state == (6, 49) and action.lower() == "up":
        return True

    if state == (6, 49) and action.lower() == "right-up":
        return True

    if state == (6, 49) and action.lower() == "right-down":
        return True

    if state == (6, 49) and action.lower() == "down":
        return True

    if state == (6, 49) and action.lower() == "left-down":
        return True

    if state == (6, 51) and action.lower() == "left-up":
        return True

    if state == (6, 51) and action.lower() == "up":
        return True

    if state == (6, 51) and action.lower() == "down":
        return True

    if state == (6, 51) and action.lower() == "left-down":
        return True

    if state == (7, 0) and action.lower() == "up":
        return True

    if state == (7, 0) and action.lower() == "right-up":
        return True

    if state == (7, 4) and action.lower() == "up":
        return True

    if state == (7, 4) and action.lower() == "right":
        return True

    if state == (7, 4) and action.lower() == "down":
        return True

    if state == (7, 5) and action.lower() == "left-up":
        return True

    if state == (7, 5) and action.lower() == "right-up":
        return True

    if state == (7, 5) and action.lower() == "left-down":
        return True

    if state == (7, 5) and action.lower() == "left":
        return True

    if state == (7, 9) and action.lower() == "right-up":
        return True

    if state == (7, 11) and action.lower() == "left-up":
        return True

    if state == (7, 11) and action.lower() == "right":
        return True

    if state == (7, 12) and action.lower() == "left":
        return True

    if state == (7, 14) and action.lower() == "right-up":
        return True

    if state == (7, 18) and action.lower() == "left-up":
        return True

    if state == (7, 21) and action.lower() == "left-up":
        return True

    if state == (7, 21) and action.lower() == "right-up":
        return True

    if state == (7, 21) and action.lower() == "right-down":
        return True

    if state == (7, 24) and action.lower() == "right-up":
        return True

    if state == (7, 24) and action.lower() == "right":
        return True

    if state == (7, 24) and action.lower() == "left-down":
        return True

    if state == (7, 25) and action.lower() == "up":
        return True

    if state == (7, 25) and action.lower() == "right-down":
        return True

    if state == (7, 25) and action.lower() == "left":
        return True

    if state == (7, 27) and action.lower() == "up":
        return True

    if state == (7, 27) and action.lower() == "right-up":
        return True

    if state == (7, 27) and action.lower() == "right-down":
        return True

    if state == (7, 27) and action.lower() == "left-down":
        return True

    if state == (7, 32) and action.lower() == "up":
        return True

    if state == (7, 32) and action.lower() == "right":
        return True

    if state == (7, 32) and action.lower() == "down":
        return True

    if state == (7, 32) and action.lower() == "left-down":
        return True

    if state == (7, 33) and action.lower() == "left-up":
        return True

    if state == (7, 33) and action.lower() == "right":
        return True

    if state == (7, 33) and action.lower() == "left-down":
        return True

    if state == (7, 33) and action.lower() == "left":
        return True

    if state == (7, 34) and action.lower() == "right-up":
        return True

    if state == (7, 34) and action.lower() == "right":
        return True

    if state == (7, 34) and action.lower() == "left":
        return True

    if state == (7, 35) and action.lower() == "up":
        return True

    if state == (7, 35) and action.lower() == "right-up":
        return True

    if state == (7, 35) and action.lower() == "right":
        return True

    if state == (7, 35) and action.lower() == "right-down":
        return True

    if state == (7, 35) and action.lower() == "left":
        return True

    if state == (7, 36) and action.lower() == "left-up":
        return True

    if state == (7, 36) and action.lower() == "up":
        return True

    if state == (7, 36) and action.lower() == "right":
        return True

    if state == (7, 36) and action.lower() == "right-down":
        return True

    if state == (7, 36) and action.lower() == "down":
        return True

    if state == (7, 36) and action.lower() == "left":
        return True

    if state == (7, 37) and action.lower() == "left-up":
        return True

    if state == (7, 37) and action.lower() == "right-up":
        return True

    if state == (7, 37) and action.lower() == "right-down":
        return True

    if state == (7, 37) and action.lower() == "down":
        return True

    if state == (7, 37) and action.lower() == "left-down":
        return True

    if state == (7, 37) and action.lower() == "left":
        return True

    if state == (7, 39) and action.lower() == "left-up":
        return True

    if state == (7, 39) and action.lower() == "right":
        return True

    if state == (7, 39) and action.lower() == "right-down":
        return True

    if state == (7, 39) and action.lower() == "left-down":
        return True

    if state == (7, 40) and action.lower() == "down":
        return True

    if state == (7, 40) and action.lower() == "left":
        return True

    if state == (7, 42) and action.lower() == "up":
        return True

    if state == (7, 42) and action.lower() == "right-down":
        return True

    if state == (7, 42) and action.lower() == "down":
        return True

    if state == (7, 44) and action.lower() == "up":
        return True

    if state == (7, 44) and action.lower() == "left-down":
        return True

    if state == (7, 48) and action.lower() == "left-up":
        return True

    if state == (7, 48) and action.lower() == "right-up":
        return True

    if state == (7, 48) and action.lower() == "right":
        return True

    if state == (7, 48) and action.lower() == "right-down":
        return True

    if state == (7, 48) and action.lower() == "down":
        return True

    if state == (7, 49) and action.lower() == "up":
        return True

    if state == (7, 49) and action.lower() == "right":
        return True

    if state == (7, 49) and action.lower() == "right-down":
        return True

    if state == (7, 49) and action.lower() == "down":
        return True

    if state == (7, 49) and action.lower() == "left-down":
        return True

    if state == (7, 49) and action.lower() == "left":
        return True

    if state == (7, 50) and action.lower() == "left-up":
        return True

    if state == (7, 50) and action.lower() == "right-up":
        return True

    if state == (7, 50) and action.lower() == "right":
        return True

    if state == (7, 50) and action.lower() == "down":
        return True

    if state == (7, 50) and action.lower() == "left-down":
        return True

    if state == (7, 50) and action.lower() == "left":
        return True

    if state == (7, 51) and action.lower() == "up":
        return True

    if state == (7, 51) and action.lower() == "left-down":
        return True

    if state == (7, 51) and action.lower() == "left":
        return True

    if state == (8, 2) and action.lower() == "right-down":
        return True

    if state == (8, 2) and action.lower() == "down":
        return True

    if state == (8, 2) and action.lower() == "left-down":
        return True

    if state == (8, 4) and action.lower() == "up":
        return True

    if state == (8, 4) and action.lower() == "right-up":
        return True

    if state == (8, 4) and action.lower() == "right-down":
        return True

    if state == (8, 4) and action.lower() == "left-down":
        return True

    if state == (8, 7) and action.lower() == "right-down":
        return True

    if state == (8, 7) and action.lower() == "left-down":
        return True

    if state == (8, 22) and action.lower() == "left-up":
        return True

    if state == (8, 22) and action.lower() == "right":
        return True

    if state == (8, 22) and action.lower() == "down":
        return True

    if state == (8, 22) and action.lower() == "left-down":
        return True

    if state == (8, 23) and action.lower() == "right-up":
        return True

    if state == (8, 23) and action.lower() == "right-down":
        return True

    if state == (8, 23) and action.lower() == "left-down":
        return True

    if state == (8, 23) and action.lower() == "left":
        return True

    if state == (8, 26) and action.lower() == "left-up":
        return True

    if state == (8, 26) and action.lower() == "right-up":
        return True

    if state == (8, 26) and action.lower() == "right-down":
        return True

    if state == (8, 26) and action.lower() == "down":
        return True

    if state == (8, 28) and action.lower() == "left-up":
        return True

    if state == (8, 28) and action.lower() == "right":
        return True

    if state == (8, 28) and action.lower() == "right-down":
        return True

    if state == (8, 28) and action.lower() == "left-down":
        return True

    if state == (8, 29) and action.lower() == "down":
        return True

    if state == (8, 29) and action.lower() == "left":
        return True

    if state == (8, 31) and action.lower() == "right-up":
        return True

    if state == (8, 31) and action.lower() == "right":
        return True

    if state == (8, 31) and action.lower() == "down":
        return True

    if state == (8, 32) and action.lower() == "up":
        return True

    if state == (8, 32) and action.lower() == "right-up":
        return True

    if state == (8, 32) and action.lower() == "right-down":
        return True

    if state == (8, 32) and action.lower() == "left-down":
        return True

    if state == (8, 32) and action.lower() == "left":
        return True

    if state == (8, 36) and action.lower() == "left-up":
        return True

    if state == (8, 36) and action.lower() == "up":
        return True

    if state == (8, 36) and action.lower() == "right-up":
        return True

    if state == (8, 36) and action.lower() == "right":
        return True

    if state == (8, 36) and action.lower() == "right-down":
        return True

    if state == (8, 36) and action.lower() == "down":
        return True

    if state == (8, 37) and action.lower() == "left-up":
        return True

    if state == (8, 37) and action.lower() == "up":
        return True

    if state == (8, 37) and action.lower() == "right":
        return True

    if state == (8, 37) and action.lower() == "right-down":
        return True

    if state == (8, 37) and action.lower() == "down":
        return True

    if state == (8, 37) and action.lower() == "left-down":
        return True

    if state == (8, 37) and action.lower() == "left":
        return True

    if state == (8, 38) and action.lower() == "left-up":
        return True

    if state == (8, 38) and action.lower() == "right-up":
        return True

    if state == (8, 38) and action.lower() == "down":
        return True

    if state == (8, 38) and action.lower() == "left-down":
        return True

    if state == (8, 38) and action.lower() == "left":
        return True

    if state == (8, 40) and action.lower() == "left-up":
        return True

    if state == (8, 40) and action.lower() == "up":
        return True

    if state == (8, 40) and action.lower() == "down":
        return True

    if state == (8, 42) and action.lower() == "up":
        return True

    if state == (8, 42) and action.lower() == "right":
        return True

    if state == (8, 42) and action.lower() == "down":
        return True

    if state == (8, 43) and action.lower() == "left-up":
        return True

    if state == (8, 43) and action.lower() == "right-up":
        return True

    if state == (8, 43) and action.lower() == "right-down":
        return True

    if state == (8, 43) and action.lower() == "left-down":
        return True

    if state == (8, 43) and action.lower() == "left":
        return True

    if state == (8, 46) and action.lower() == "right-down":
        return True

    if state == (8, 48) and action.lower() == "up":
        return True

    if state == (8, 48) and action.lower() == "right-up":
        return True

    if state == (8, 48) and action.lower() == "right":
        return True

    if state == (8, 48) and action.lower() == "left-down":
        return True

    if state == (8, 49) and action.lower() == "left-up":
        return True

    if state == (8, 49) and action.lower() == "up":
        return True

    if state == (8, 49) and action.lower() == "right-up":
        return True

    if state == (8, 49) and action.lower() == "right":
        return True

    if state == (8, 49) and action.lower() == "right-down":
        return True

    if state == (8, 49) and action.lower() == "left":
        return True

    if state == (8, 50) and action.lower() == "left-up":
        return True

    if state == (8, 50) and action.lower() == "up":
        return True

    if state == (8, 50) and action.lower() == "right-up":
        return True

    if state == (8, 50) and action.lower() == "down":
        return True

    if state == (8, 50) and action.lower() == "left":
        return True

    if state == (9, 0) and action.lower() == "right":
        return True

    if state == (9, 0) and action.lower() == "down":
        return True

    if state == (9, 1) and action.lower() == "right-up":
        return True

    if state == (9, 1) and action.lower() == "right":
        return True

    if state == (9, 1) and action.lower() == "left-down":
        return True

    if state == (9, 1) and action.lower() == "left":
        return True

    if state == (9, 2) and action.lower() == "up":
        return True

    if state == (9, 2) and action.lower() == "right":
        return True

    if state == (9, 2) and action.lower() == "left":
        return True

    if state == (9, 3) and action.lower() == "left-up":
        return True

    if state == (9, 3) and action.lower() == "right-up":
        return True

    if state == (9, 3) and action.lower() == "left":
        return True

    if state == (9, 5) and action.lower() == "left-up":
        return True

    if state == (9, 5) and action.lower() == "right":
        return True

    if state == (9, 5) and action.lower() == "right-down":
        return True

    if state == (9, 5) and action.lower() == "down":
        return True

    if state == (9, 6) and action.lower() == "right-up":
        return True

    if state == (9, 6) and action.lower() == "down":
        return True

    if state == (9, 6) and action.lower() == "left-down":
        return True

    if state == (9, 6) and action.lower() == "left":
        return True

    if state == (9, 8) and action.lower() == "left-up":
        return True

    if state == (9, 8) and action.lower() == "right-down":
        return True

    if state == (9, 11) and action.lower() == "right":
        return True

    if state == (9, 11) and action.lower() == "down":
        return True

    if state == (9, 12) and action.lower() == "right":
        return True

    if state == (9, 12) and action.lower() == "right-down":
        return True

    if state == (9, 12) and action.lower() == "left-down":
        return True

    if state == (9, 12) and action.lower() == "left":
        return True

    if state == (9, 13) and action.lower() == "right":
        return True

    if state == (9, 13) and action.lower() == "right-down":
        return True

    if state == (9, 13) and action.lower() == "down":
        return True

    if state == (9, 13) and action.lower() == "left":
        return True

    if state == (9, 14) and action.lower() == "down":
        return True

    if state == (9, 14) and action.lower() == "left-down":
        return True

    if state == (9, 14) and action.lower() == "left":
        return True

    if state == (9, 17) and action.lower() == "right":
        return True

    if state == (9, 17) and action.lower() == "down":
        return True

    if state == (9, 17) and action.lower() == "left-down":
        return True

    if state == (9, 18) and action.lower() == "right-down":
        return True

    if state == (9, 18) and action.lower() == "left-down":
        return True

    if state == (9, 18) and action.lower() == "left":
        return True

    if state == (9, 20) and action.lower() == "right":
        return True

    if state == (9, 20) and action.lower() == "left-down":
        return True

    if state == (9, 21) and action.lower() == "right-up":
        return True

    if state == (9, 21) and action.lower() == "right":
        return True

    if state == (9, 21) and action.lower() == "left":
        return True

    if state == (9, 22) and action.lower() == "up":
        return True

    if state == (9, 22) and action.lower() == "right-up":
        return True

    if state == (9, 22) and action.lower() == "left":
        return True

    if state == (9, 24) and action.lower() == "left-up":
        return True

    if state == (9, 24) and action.lower() == "down":
        return True

    if state == (9, 26) and action.lower() == "up":
        return True

    if state == (9, 26) and action.lower() == "right":
        return True

    if state == (9, 26) and action.lower() == "right-down":
        return True

    if state == (9, 27) and action.lower() == "left-up":
        return True

    if state == (9, 27) and action.lower() == "right-up":
        return True

    if state == (9, 27) and action.lower() == "right-down":
        return True

    if state == (9, 27) and action.lower() == "down":
        return True

    if state == (9, 27) and action.lower() == "left":
        return True

    if state == (9, 29) and action.lower() == "left-up":
        return True

    if state == (9, 29) and action.lower() == "up":
        return True

    if state == (9, 29) and action.lower() == "left-down":
        return True

    if state == (9, 31) and action.lower() == "up":
        return True

    if state == (9, 31) and action.lower() == "right-up":
        return True

    if state == (9, 31) and action.lower() == "down":
        return True

    if state == (9, 33) and action.lower() == "left-up":
        return True

    if state == (9, 33) and action.lower() == "right":
        return True

    if state == (9, 33) and action.lower() == "right-down":
        return True

    if state == (9, 34) and action.lower() == "right-down":
        return True

    if state == (9, 34) and action.lower() == "down":
        return True

    if state == (9, 34) and action.lower() == "left":
        return True

    if state == (9, 36) and action.lower() == "up":
        return True

    if state == (9, 36) and action.lower() == "right-up":
        return True

    if state == (9, 36) and action.lower() == "right":
        return True

    if state == (9, 36) and action.lower() == "right-down":
        return True

    if state == (9, 36) and action.lower() == "left-down":
        return True

    if state == (9, 37) and action.lower() == "left-up":
        return True

    if state == (9, 37) and action.lower() == "up":
        return True

    if state == (9, 37) and action.lower() == "right-up":
        return True

    if state == (9, 37) and action.lower() == "right":
        return True

    if state == (9, 37) and action.lower() == "right-down":
        return True

    if state == (9, 37) and action.lower() == "down":
        return True

    if state == (9, 37) and action.lower() == "left":
        return True

    if state == (9, 38) and action.lower() == "left-up":
        return True

    if state == (9, 38) and action.lower() == "up":
        return True

    if state == (9, 38) and action.lower() == "right-down":
        return True

    if state == (9, 38) and action.lower() == "down":
        return True

    if state == (9, 38) and action.lower() == "left-down":
        return True

    if state == (9, 38) and action.lower() == "left":
        return True

    if state == (9, 40) and action.lower() == "up":
        return True

    if state == (9, 40) and action.lower() == "right-down":
        return True

    if state == (9, 40) and action.lower() == "left-down":
        return True

    if state == (9, 42) and action.lower() == "up":
        return True

    if state == (9, 42) and action.lower() == "right-up":
        return True

    if state == (9, 42) and action.lower() == "right-down":
        return True

    if state == (9, 42) and action.lower() == "down":
        return True

    if state == (9, 42) and action.lower() == "left-down":
        return True

    if state == (9, 44) and action.lower() == "left-up":
        return True

    if state == (9, 44) and action.lower() == "down":
        return True

    if state == (9, 44) and action.lower() == "left-down":
        return True

    if state == (9, 47) and action.lower() == "left-up":
        return True

    if state == (9, 47) and action.lower() == "right-up":
        return True

    if state == (9, 47) and action.lower() == "down":
        return True

    if state == (9, 50) and action.lower() == "left-up":
        return True

    if state == (9, 50) and action.lower() == "up":
        return True

    if state == (9, 50) and action.lower() == "right-down":
        return True

    if state == (9, 50) and action.lower() == "down":
        return True

    if state == (10, 0) and action.lower() == "up":
        return True

    if state == (10, 0) and action.lower() == "right-up":
        return True

    if state == (10, 0) and action.lower() == "right-down":
        return True

    if state == (10, 0) and action.lower() == "down":
        return True

    if state == (10, 5) and action.lower() == "up":
        return True

    if state == (10, 5) and action.lower() == "right-up":
        return True

    if state == (10, 5) and action.lower() == "right":
        return True

    if state == (10, 5) and action.lower() == "left-down":
        return True

    if state == (10, 6) and action.lower() == "left-up":
        return True

    if state == (10, 6) and action.lower() == "up":
        return True

    if state == (10, 6) and action.lower() == "right-down":
        return True

    if state == (10, 6) and action.lower() == "left":
        return True

    if state == (10, 9) and action.lower() == "left-up":
        return True

    if state == (10, 9) and action.lower() == "down":
        return True

    if state == (10, 9) and action.lower() == "left-down":
        return True

    if state == (10, 11) and action.lower() == "up":
        return True

    if state == (10, 11) and action.lower() == "right-up":
        return True

    if state == (10, 11) and action.lower() == "right-down":
        return True

    if state == (10, 13) and action.lower() == "left-up":
        return True

    if state == (10, 13) and action.lower() == "up":
        return True

    if state == (10, 13) and action.lower() == "right-up":
        return True

    if state == (10, 13) and action.lower() == "right":
        return True

    if state == (10, 13) and action.lower() == "right-down":
        return True

    if state == (10, 13) and action.lower() == "left-down":
        return True

    if state == (10, 14) and action.lower() == "left-up":
        return True

    if state == (10, 14) and action.lower() == "up":
        return True

    if state == (10, 14) and action.lower() == "right-down":
        return True

    if state == (10, 14) and action.lower() == "down":
        return True

    if state == (10, 14) and action.lower() == "left":
        return True

    if state == (10, 16) and action.lower() == "right-up":
        return True

    if state == (10, 16) and action.lower() == "right":
        return True

    if state == (10, 16) and action.lower() == "left-down":
        return True

    if state == (10, 17) and action.lower() == "up":
        return True

    if state == (10, 17) and action.lower() == "right-up":
        return True

    if state == (10, 17) and action.lower() == "right-down":
        return True

    if state == (10, 17) and action.lower() == "left":
        return True

    if state == (10, 19) and action.lower() == "left-up":
        return True

    if state == (10, 19) and action.lower() == "right-up":
        return True

    if state == (10, 19) and action.lower() == "right-down":
        return True

    if state == (10, 19) and action.lower() == "left-down":
        return True

    if state == (10, 24) and action.lower() == "up":
        return True

    if state == (10, 24) and action.lower() == "down":
        return True

    if state == (10, 27) and action.lower() == "left-up":
        return True

    if state == (10, 27) and action.lower() == "up":
        return True

    if state == (10, 27) and action.lower() == "right":
        return True

    if state == (10, 27) and action.lower() == "right-down":
        return True

    if state == (10, 28) and action.lower() == "left-up":
        return True

    if state == (10, 28) and action.lower() == "right-up":
        return True

    if state == (10, 28) and action.lower() == "down":
        return True

    if state == (10, 28) and action.lower() == "left":
        return True

    if state == (10, 31) and action.lower() == "up":
        return True

    if state == (10, 31) and action.lower() == "right-down":
        return True

    if state == (10, 31) and action.lower() == "left-down":
        return True

    if state == (10, 34) and action.lower() == "left-up":
        return True

    if state == (10, 34) and action.lower() == "up":
        return True

    if state == (10, 34) and action.lower() == "right":
        return True

    if state == (10, 34) and action.lower() == "down":
        return True

    if state == (10, 35) and action.lower() == "left-up":
        return True

    if state == (10, 35) and action.lower() == "right-up":
        return True

    if state == (10, 35) and action.lower() == "right-down":
        return True

    if state == (10, 35) and action.lower() == "left-down":
        return True

    if state == (10, 35) and action.lower() == "left":
        return True

    if state == (10, 37) and action.lower() == "left-up":
        return True

    if state == (10, 37) and action.lower() == "up":
        return True

    if state == (10, 37) and action.lower() == "right-up":
        return True

    if state == (10, 37) and action.lower() == "right":
        return True

    if state == (10, 37) and action.lower() == "left-down":
        return True

    if state == (10, 38) and action.lower() == "left-up":
        return True

    if state == (10, 38) and action.lower() == "up":
        return True

    if state == (10, 38) and action.lower() == "right":
        return True

    if state == (10, 38) and action.lower() == "right-down":
        return True

    if state == (10, 38) and action.lower() == "left":
        return True

    if state == (10, 39) and action.lower() == "left-up":
        return True

    if state == (10, 39) and action.lower() == "right-up":
        return True

    if state == (10, 39) and action.lower() == "right-down":
        return True

    if state == (10, 39) and action.lower() == "down":
        return True

    if state == (10, 39) and action.lower() == "left":
        return True

    if state == (10, 41) and action.lower() == "left-up":
        return True

    if state == (10, 41) and action.lower() == "right-up":
        return True

    if state == (10, 41) and action.lower() == "right":
        return True

    if state == (10, 41) and action.lower() == "down":
        return True

    if state == (10, 41) and action.lower() == "left-down":
        return True

    if state == (10, 42) and action.lower() == "up":
        return True

    if state == (10, 42) and action.lower() == "right":
        return True

    if state == (10, 42) and action.lower() == "left-down":
        return True

    if state == (10, 42) and action.lower() == "left":
        return True

    if state == (10, 43) and action.lower() == "left-up":
        return True

    if state == (10, 43) and action.lower() == "right-up":
        return True

    if state == (10, 43) and action.lower() == "right":
        return True

    if state == (10, 43) and action.lower() == "right-down":
        return True

    if state == (10, 43) and action.lower() == "left":
        return True

    if state == (10, 44) and action.lower() == "up":
        return True

    if state == (10, 44) and action.lower() == "right-down":
        return True

    if state == (10, 44) and action.lower() == "down":
        return True

    if state == (10, 44) and action.lower() == "left":
        return True

    if state == (10, 47) and action.lower() == "up":
        return True

    if state == (10, 47) and action.lower() == "left-down":
        return True

    if state == (10, 50) and action.lower() == "up":
        return True

    if state == (10, 50) and action.lower() == "right":
        return True

    if state == (10, 50) and action.lower() == "right-down":
        return True

    if state == (10, 50) and action.lower() == "down":
        return True

    if state == (10, 50) and action.lower() == "left-down":
        return True

    if state == (10, 51) and action.lower() == "left-up":
        return True

    if state == (10, 51) and action.lower() == "down":
        return True

    if state == (10, 51) and action.lower() == "left-down":
        return True

    if state == (10, 51) and action.lower() == "left":
        return True

    if state == (11, 0) and action.lower() == "up":
        return True

    if state == (11, 0) and action.lower() == "right":
        return True

    if state == (11, 1) and action.lower() == "left-up":
        return True

    if state == (11, 1) and action.lower() == "right-down":
        return True

    if state == (11, 1) and action.lower() == "left":
        return True

    if state == (11, 4) and action.lower() == "right-up":
        return True

    if state == (11, 4) and action.lower() == "right-down":
        return True

    if state == (11, 4) and action.lower() == "down":
        return True

    if state == (11, 4) and action.lower() == "left-down":
        return True

    if state == (11, 7) and action.lower() == "left-up":
        return True

    if state == (11, 7) and action.lower() == "right":
        return True

    if state == (11, 7) and action.lower() == "right-down":
        return True

    if state == (11, 7) and action.lower() == "down":
        return True

    if state == (11, 8) and action.lower() == "right-up":
        return True

    if state == (11, 8) and action.lower() == "right":
        return True

    if state == (11, 8) and action.lower() == "down":
        return True

    if state == (11, 8) and action.lower() == "left-down":
        return True

    if state == (11, 8) and action.lower() == "left":
        return True

    if state == (11, 9) and action.lower() == "up":
        return True

    if state == (11, 9) and action.lower() == "left-down":
        return True

    if state == (11, 9) and action.lower() == "left":
        return True

    if state == (11, 12) and action.lower() == "left-up":
        return True

    if state == (11, 12) and action.lower() == "right-up":
        return True

    if state == (11, 12) and action.lower() == "down":
        return True

    if state == (11, 12) and action.lower() == "left-down":
        return True

    if state == (11, 14) and action.lower() == "left-up":
        return True

    if state == (11, 14) and action.lower() == "up":
        return True

    if state == (11, 14) and action.lower() == "right":
        return True

    if state == (11, 14) and action.lower() == "down":
        return True

    if state == (11, 15) and action.lower() == "left-up":
        return True

    if state == (11, 15) and action.lower() == "right-up":
        return True

    if state == (11, 15) and action.lower() == "left-down":
        return True

    if state == (11, 15) and action.lower() == "left":
        return True

    if state == (11, 18) and action.lower() == "left-up":
        return True

    if state == (11, 18) and action.lower() == "right-up":
        return True

    if state == (11, 18) and action.lower() == "right-down":
        return True

    if state == (11, 20) and action.lower() == "left-up":
        return True

    if state == (11, 20) and action.lower() == "right-down":
        return True

    if state == (11, 20) and action.lower() == "down":
        return True

    if state == (11, 20) and action.lower() == "left-down":
        return True

    if state == (11, 24) and action.lower() == "up":
        return True

    if state == (11, 28) and action.lower() == "left-up":
        return True

    if state == (11, 28) and action.lower() == "up":
        return True

    if state == (11, 28) and action.lower() == "left-down":
        return True

    if state == (11, 30) and action.lower() == "right-up":
        return True

    if state == (11, 30) and action.lower() == "right-down":
        return True

    if state == (11, 30) and action.lower() == "down":
        return True

    if state == (11, 32) and action.lower() == "left-up":
        return True

    if state == (11, 32) and action.lower() == "left-down":
        return True

    if state == (11, 34) and action.lower() == "up":
        return True

    if state == (11, 34) and action.lower() == "right-up":
        return True

    if state == (11, 34) and action.lower() == "down":
        return True

    if state == (11, 36) and action.lower() == "left-up":
        return True

    if state == (11, 36) and action.lower() == "right-up":
        return True

    if state == (11, 36) and action.lower() == "right-down":
        return True

    if state == (11, 39) and action.lower() == "left-up":
        return True

    if state == (11, 39) and action.lower() == "up":
        return True

    if state == (11, 39) and action.lower() == "right":
        return True

    if state == (11, 39) and action.lower() == "left-down":
        return True

    if state == (11, 40) and action.lower() == "left-up":
        return True

    if state == (11, 40) and action.lower() == "right-up":
        return True

    if state == (11, 40) and action.lower() == "right":
        return True

    if state == (11, 40) and action.lower() == "left":
        return True

    if state == (11, 41) and action.lower() == "up":
        return True

    if state == (11, 41) and action.lower() == "right-up":
        return True

    if state == (11, 41) and action.lower() == "left":
        return True

    if state == (11, 44) and action.lower() == "left-up":
        return True

    if state == (11, 44) and action.lower() == "up":
        return True

    if state == (11, 44) and action.lower() == "right":
        return True

    if state == (11, 44) and action.lower() == "right-down":
        return True

    if state == (11, 45) and action.lower() == "left-up":
        return True

    if state == (11, 45) and action.lower() == "right":
        return True

    if state == (11, 45) and action.lower() == "down":
        return True

    if state == (11, 45) and action.lower() == "left":
        return True

    if state == (11, 46) and action.lower() == "right-up":
        return True

    if state == (11, 46) and action.lower() == "left-down":
        return True

    if state == (11, 46) and action.lower() == "left":
        return True

    if state == (11, 49) and action.lower() == "right-up":
        return True

    if state == (11, 49) and action.lower() == "right":
        return True

    if state == (11, 49) and action.lower() == "right-down":
        return True

    if state == (11, 49) and action.lower() == "down":
        return True

    if state == (11, 49) and action.lower() == "left-down":
        return True

    if state == (11, 50) and action.lower() == "up":
        return True

    if state == (11, 50) and action.lower() == "right-up":
        return True

    if state == (11, 50) and action.lower() == "right":
        return True

    if state == (11, 50) and action.lower() == "right-down":
        return True

    if state == (11, 50) and action.lower() == "down":
        return True

    if state == (11, 50) and action.lower() == "left-down":
        return True

    if state == (11, 50) and action.lower() == "left":
        return True

    if state == (11, 51) and action.lower() == "left-up":
        return True

    if state == (11, 51) and action.lower() == "up":
        return True

    if state == (11, 51) and action.lower() == "down":
        return True

    if state == (11, 51) and action.lower() == "left-down":
        return True

    if state == (11, 51) and action.lower() == "left":
        return True

    if state == (12, 2) and action.lower() == "left-up":
        return True

    if state == (12, 2) and action.lower() == "right":
        return True

    if state == (12, 2) and action.lower() == "right-down":
        return True

    if state == (12, 3) and action.lower() == "right-up":
        return True

    if state == (12, 3) and action.lower() == "right":
        return True

    if state == (12, 3) and action.lower() == "right-down":
        return True

    if state == (12, 3) and action.lower() == "down":
        return True

    if state == (12, 3) and action.lower() == "left":
        return True

    if state == (12, 4) and action.lower() == "up":
        return True

    if state == (12, 4) and action.lower() == "right":
        return True

    if state == (12, 4) and action.lower() == "right-down":
        return True

    if state == (12, 4) and action.lower() == "down":
        return True

    if state == (12, 4) and action.lower() == "left-down":
        return True

    if state == (12, 4) and action.lower() == "left":
        return True

    if state == (12, 5) and action.lower() == "left-up":
        return True

    if state == (12, 5) and action.lower() == "down":
        return True

    if state == (12, 5) and action.lower() == "left-down":
        return True

    if state == (12, 5) and action.lower() == "left":
        return True

    if state == (12, 7) and action.lower() == "up":
        return True

    if state == (12, 7) and action.lower() == "right-up":
        return True

    if state == (12, 7) and action.lower() == "right":
        return True

    if state == (12, 8) and action.lower() == "left-up":
        return True

    if state == (12, 8) and action.lower() == "up":
        return True

    if state == (12, 8) and action.lower() == "right-up":
        return True

    if state == (12, 8) and action.lower() == "right-down":
        return True

    if state == (12, 8) and action.lower() == "left":
        return True

    if state == (12, 11) and action.lower() == "right-up":
        return True

    if state == (12, 11) and action.lower() == "right":
        return True

    if state == (12, 11) and action.lower() == "down":
        return True

    if state == (12, 12) and action.lower() == "up":
        return True

    if state == (12, 12) and action.lower() == "left-down":
        return True

    if state == (12, 12) and action.lower() == "left":
        return True

    if state == (12, 14) and action.lower() == "up":
        return True

    if state == (12, 14) and action.lower() == "right-up":
        return True

    if state == (12, 14) and action.lower() == "right-down":
        return True

    if state == (12, 19) and action.lower() == "left-up":
        return True

    if state == (12, 19) and action.lower() == "right-up":
        return True

    if state == (12, 19) and action.lower() == "right":
        return True

    if state == (12, 20) and action.lower() == "up":
        return True

    if state == (12, 20) and action.lower() == "right":
        return True

    if state == (12, 20) and action.lower() == "right-down":
        return True

    if state == (12, 20) and action.lower() == "left":
        return True

    if state == (12, 21) and action.lower() == "left-up":
        return True

    if state == (12, 21) and action.lower() == "right":
        return True

    if state == (12, 21) and action.lower() == "down":
        return True

    if state == (12, 21) and action.lower() == "left":
        return True

    if state == (12, 22) and action.lower() == "left-down":
        return True

    if state == (12, 22) and action.lower() == "left":
        return True

    if state == (12, 27) and action.lower() == "right-up":
        return True

    if state == (12, 27) and action.lower() == "right-down":
        return True

    if state == (12, 30) and action.lower() == "up":
        return True

    if state == (12, 30) and action.lower() == "right":
        return True

    if state == (12, 30) and action.lower() == "right-down":
        return True

    if state == (12, 31) and action.lower() == "left-up":
        return True

    if state == (12, 31) and action.lower() == "right-up":
        return True

    if state == (12, 31) and action.lower() == "right-down":
        return True

    if state == (12, 31) and action.lower() == "down":
        return True

    if state == (12, 31) and action.lower() == "left":
        return True

    if state == (12, 34) and action.lower() == "up":
        return True

    if state == (12, 34) and action.lower() == "right-down":
        return True

    if state == (12, 37) and action.lower() == "left-up":
        return True

    if state == (12, 37) and action.lower() == "right":
        return True

    if state == (12, 38) and action.lower() == "right-up":
        return True

    if state == (12, 38) and action.lower() == "right-down":
        return True

    if state == (12, 38) and action.lower() == "left":
        return True

    if state == (12, 45) and action.lower() == "left-up":
        return True

    if state == (12, 45) and action.lower() == "up":
        return True

    if state == (12, 45) and action.lower() == "right-up":
        return True

    if state == (12, 45) and action.lower() == "right-down":
        return True

    if state == (12, 45) and action.lower() == "down":
        return True

    if state == (12, 45) and action.lower() == "left-down":
        return True

    if state == (12, 48) and action.lower() == "right-up":
        return True

    if state == (12, 48) and action.lower() == "right":
        return True

    if state == (12, 48) and action.lower() == "right-down":
        return True

    if state == (12, 49) and action.lower() == "up":
        return True

    if state == (12, 49) and action.lower() == "right-up":
        return True

    if state == (12, 49) and action.lower() == "right":
        return True

    if state == (12, 49) and action.lower() == "right-down":
        return True

    if state == (12, 49) and action.lower() == "down":
        return True

    if state == (12, 49) and action.lower() == "left":
        return True

    if state == (12, 50) and action.lower() == "left-up":
        return True

    if state == (12, 50) and action.lower() == "up":
        return True

    if state == (12, 50) and action.lower() == "right-up":
        return True

    if state == (12, 50) and action.lower() == "right":
        return True

    if state == (12, 50) and action.lower() == "right-down":
        return True

    if state == (12, 50) and action.lower() == "down":
        return True

    if state == (12, 50) and action.lower() == "left-down":
        return True

    if state == (12, 50) and action.lower() == "left":
        return True

    if state == (12, 51) and action.lower() == "left-up":
        return True

    if state == (12, 51) and action.lower() == "up":
        return True

    if state == (12, 51) and action.lower() == "down":
        return True

    if state == (12, 51) and action.lower() == "left-down":
        return True

    if state == (12, 51) and action.lower() == "left":
        return True

    if state == (13, 3) and action.lower() == "left-up":
        return True

    if state == (13, 3) and action.lower() == "up":
        return True

    if state == (13, 3) and action.lower() == "right-up":
        return True

    if state == (13, 3) and action.lower() == "right":
        return True

    if state == (13, 3) and action.lower() == "right-down":
        return True

    if state == (13, 3) and action.lower() == "down":
        return True

    if state == (13, 3) and action.lower() == "left-down":
        return True

    if state == (13, 4) and action.lower() == "left-up":
        return True

    if state == (13, 4) and action.lower() == "up":
        return True

    if state == (13, 4) and action.lower() == "right-up":
        return True

    if state == (13, 4) and action.lower() == "right":
        return True

    if state == (13, 4) and action.lower() == "right-down":
        return True

    if state == (13, 4) and action.lower() == "down":
        return True

    if state == (13, 4) and action.lower() == "left-down":
        return True

    if state == (13, 4) and action.lower() == "left":
        return True

    if state == (13, 5) and action.lower() == "left-up":
        return True

    if state == (13, 5) and action.lower() == "up":
        return True

    if state == (13, 5) and action.lower() == "right-down":
        return True

    if state == (13, 5) and action.lower() == "down":
        return True

    if state == (13, 5) and action.lower() == "left-down":
        return True

    if state == (13, 5) and action.lower() == "left":
        return True

    if state == (13, 9) and action.lower() == "left-up":
        return True

    if state == (13, 9) and action.lower() == "right-down":
        return True

    if state == (13, 11) and action.lower() == "up":
        return True

    if state == (13, 11) and action.lower() == "right-up":
        return True

    if state == (13, 11) and action.lower() == "down":
        return True

    if state == (13, 11) and action.lower() == "left-down":
        return True

    if state == (13, 15) and action.lower() == "left-up":
        return True

    if state == (13, 15) and action.lower() == "right":
        return True

    if state == (13, 15) and action.lower() == "right-down":
        return True

    if state == (13, 16) and action.lower() == "down":
        return True

    if state == (13, 16) and action.lower() == "left":
        return True

    if state == (13, 21) and action.lower() == "left-up":
        return True

    if state == (13, 21) and action.lower() == "up":
        return True

    if state == (13, 21) and action.lower() == "right-up":
        return True

    if state == (13, 21) and action.lower() == "right-down":
        return True

    if state == (13, 28) and action.lower() == "left-up":
        return True

    if state == (13, 28) and action.lower() == "left-down":
        return True

    if state == (13, 31) and action.lower() == "left-up":
        return True

    if state == (13, 31) and action.lower() == "up":
        return True

    if state == (13, 31) and action.lower() == "right":
        return True

    if state == (13, 31) and action.lower() == "down":
        return True

    if state == (13, 32) and action.lower() == "left-up":
        return True

    if state == (13, 32) and action.lower() == "right-down":
        return True

    if state == (13, 32) and action.lower() == "left-down":
        return True

    if state == (13, 32) and action.lower() == "left":
        return True

    if state == (13, 35) and action.lower() == "left-up":
        return True

    if state == (13, 35) and action.lower() == "down":
        return True

    if state == (13, 35) and action.lower() == "left-down":
        return True

    if state == (13, 39) and action.lower() == "left-up":
        return True

    if state == (13, 39) and action.lower() == "right-down":
        return True

    if state == (13, 43) and action.lower() == "right":
        return True

    if state == (13, 43) and action.lower() == "down":
        return True

    if state == (13, 43) and action.lower() == "left-down":
        return True

    if state == (13, 44) and action.lower() == "right-up":
        return True

    if state == (13, 44) and action.lower() == "right":
        return True

    if state == (13, 44) and action.lower() == "left-down":
        return True

    if state == (13, 44) and action.lower() == "left":
        return True

    if state == (13, 45) and action.lower() == "up":
        return True

    if state == (13, 45) and action.lower() == "right":
        return True

    if state == (13, 45) and action.lower() == "right-down":
        return True

    if state == (13, 45) and action.lower() == "left":
        return True

    if state == (13, 46) and action.lower() == "left-up":
        return True

    if state == (13, 46) and action.lower() == "right-down":
        return True

    if state == (13, 46) and action.lower() == "down":
        return True

    if state == (13, 46) and action.lower() == "left":
        return True

    if state == (13, 49) and action.lower() == "left-up":
        return True

    if state == (13, 49) and action.lower() == "up":
        return True

    if state == (13, 49) and action.lower() == "right-up":
        return True

    if state == (13, 49) and action.lower() == "right":
        return True

    if state == (13, 49) and action.lower() == "right-down":
        return True

    if state == (13, 49) and action.lower() == "left-down":
        return True

    if state == (13, 50) and action.lower() == "left-up":
        return True

    if state == (13, 50) and action.lower() == "up":
        return True

    if state == (13, 50) and action.lower() == "right-up":
        return True

    if state == (13, 50) and action.lower() == "right":
        return True

    if state == (13, 50) and action.lower() == "right-down":
        return True

    if state == (13, 50) and action.lower() == "down":
        return True

    if state == (13, 50) and action.lower() == "left":
        return True

    if state == (13, 51) and action.lower() == "left-up":
        return True

    if state == (13, 51) and action.lower() == "up":
        return True

    if state == (13, 51) and action.lower() == "down":
        return True

    if state == (13, 51) and action.lower() == "left-down":
        return True

    if state == (13, 51) and action.lower() == "left":
        return True

    if state == (14, 1) and action.lower() == "right":
        return True

    if state == (14, 1) and action.lower() == "down":
        return True

    if state == (14, 1) and action.lower() == "left-down":
        return True

    if state == (14, 2) and action.lower() == "right-up":
        return True

    if state == (14, 2) and action.lower() == "right":
        return True

    if state == (14, 2) and action.lower() == "left-down":
        return True

    if state == (14, 2) and action.lower() == "left":
        return True

    if state == (14, 3) and action.lower() == "up":
        return True

    if state == (14, 3) and action.lower() == "right-up":
        return True

    if state == (14, 3) and action.lower() == "right":
        return True

    if state == (14, 3) and action.lower() == "right-down":
        return True

    if state == (14, 3) and action.lower() == "left":
        return True

    if state == (14, 4) and action.lower() == "left-up":
        return True

    if state == (14, 4) and action.lower() == "up":
        return True

    if state == (14, 4) and action.lower() == "right-up":
        return True

    if state == (14, 4) and action.lower() == "right":
        return True

    if state == (14, 4) and action.lower() == "right-down":
        return True

    if state == (14, 4) and action.lower() == "down":
        return True

    if state == (14, 4) and action.lower() == "left":
        return True

    if state == (14, 5) and action.lower() == "left-up":
        return True

    if state == (14, 5) and action.lower() == "up":
        return True

    if state == (14, 5) and action.lower() == "right":
        return True

    if state == (14, 5) and action.lower() == "right-down":
        return True

    if state == (14, 5) and action.lower() == "down":
        return True

    if state == (14, 5) and action.lower() == "left-down":
        return True

    if state == (14, 5) and action.lower() == "left":
        return True

    if state == (14, 6) and action.lower() == "left-up":
        return True

    if state == (14, 6) and action.lower() == "down":
        return True

    if state == (14, 6) and action.lower() == "left-down":
        return True

    if state == (14, 6) and action.lower() == "left":
        return True

    if state == (14, 10) and action.lower() == "left-up":
        return True

    if state == (14, 10) and action.lower() == "right-up":
        return True

    if state == (14, 10) and action.lower() == "right":
        return True

    if state == (14, 10) and action.lower() == "right-down":
        return True

    if state == (14, 10) and action.lower() == "down":
        return True

    if state == (14, 10) and action.lower() == "left-down":
        return True

    if state == (14, 11) and action.lower() == "up":
        return True

    if state == (14, 11) and action.lower() == "right-down":
        return True

    if state == (14, 11) and action.lower() == "down":
        return True

    if state == (14, 11) and action.lower() == "left-down":
        return True

    if state == (14, 11) and action.lower() == "left":
        return True

    if state == (14, 13) and action.lower() == "right-down":
        return True

    if state == (14, 13) and action.lower() == "left-down":
        return True

    if state == (14, 16) and action.lower() == "left-up":
        return True

    if state == (14, 16) and action.lower() == "up":
        return True

    if state == (14, 16) and action.lower() == "left-down":
        return True

    if state == (14, 18) and action.lower() == "right":
        return True

    if state == (14, 18) and action.lower() == "down":
        return True

    if state == (14, 19) and action.lower() == "left-down":
        return True

    if state == (14, 19) and action.lower() == "left":
        return True

    if state == (14, 22) and action.lower() == "left-up":
        return True

    if state == (14, 22) and action.lower() == "left-down":
        return True

    if state == (14, 24) and action.lower() == "right":
        return True

    if state == (14, 24) and action.lower() == "right-down":
        return True

    if state == (14, 24) and action.lower() == "down":
        return True

    if state == (14, 25) and action.lower() == "right":
        return True

    if state == (14, 25) and action.lower() == "right-down":
        return True

    if state == (14, 25) and action.lower() == "down":
        return True

    if state == (14, 25) and action.lower() == "left-down":
        return True

    if state == (14, 25) and action.lower() == "left":
        return True

    if state == (14, 26) and action.lower() == "right":
        return True

    if state == (14, 26) and action.lower() == "down":
        return True

    if state == (14, 26) and action.lower() == "left-down":
        return True

    if state == (14, 26) and action.lower() == "left":
        return True

    if state == (14, 27) and action.lower() == "right-up":
        return True

    if state == (14, 27) and action.lower() == "left-down":
        return True

    if state == (14, 27) and action.lower() == "left":
        return True

    if state == (14, 31) and action.lower() == "up":
        return True

    if state == (14, 31) and action.lower() == "right-up":
        return True

    if state == (14, 31) and action.lower() == "right-down":
        return True

    if state == (14, 31) and action.lower() == "down":
        return True

    if state == (14, 33) and action.lower() == "left-up":
        return True

    if state == (14, 33) and action.lower() == "right":
        return True

    if state == (14, 33) and action.lower() == "down":
        return True

    if state == (14, 33) and action.lower() == "left-down":
        return True

    if state == (14, 34) and action.lower() == "right-up":
        return True

    if state == (14, 34) and action.lower() == "right":
        return True

    if state == (14, 34) and action.lower() == "left-down":
        return True

    if state == (14, 34) and action.lower() == "left":
        return True

    if state == (14, 35) and action.lower() == "up":
        return True

    if state == (14, 35) and action.lower() == "right-down":
        return True

    if state == (14, 35) and action.lower() == "left":
        return True

    if state == (14, 37) and action.lower() == "right-down":
        return True

    if state == (14, 37) and action.lower() == "left-down":
        return True

    if state == (14, 40) and action.lower() == "left-up":
        return True

    if state == (14, 40) and action.lower() == "right-down":
        return True

    if state == (14, 40) and action.lower() == "down":
        return True

    if state == (14, 42) and action.lower() == "right-up":
        return True

    if state == (14, 42) and action.lower() == "right":
        return True

    if state == (14, 42) and action.lower() == "down":
        return True

    if state == (14, 42) and action.lower() == "left-down":
        return True

    if state == (14, 43) and action.lower() == "up":
        return True

    if state == (14, 43) and action.lower() == "right-up":
        return True

    if state == (14, 43) and action.lower() == "right-down":
        return True

    if state == (14, 43) and action.lower() == "left-down":
        return True

    if state == (14, 43) and action.lower() == "left":
        return True

    if state == (14, 46) and action.lower() == "left-up":
        return True

    if state == (14, 46) and action.lower() == "up":
        return True

    if state == (14, 46) and action.lower() == "right":
        return True

    if state == (14, 46) and action.lower() == "left-down":
        return True

    if state == (14, 47) and action.lower() == "left-up":
        return True

    if state == (14, 47) and action.lower() == "right":
        return True

    if state == (14, 47) and action.lower() == "left":
        return True

    if state == (14, 48) and action.lower() == "right-up":
        return True

    if state == (14, 48) and action.lower() == "left":
        return True

    if state == (14, 50) and action.lower() == "left-up":
        return True

    if state == (14, 50) and action.lower() == "up":
        return True

    if state == (14, 50) and action.lower() == "right-up":
        return True

    if state == (14, 50) and action.lower() == "right":
        return True

    if state == (14, 51) and action.lower() == "left-up":
        return True

    if state == (14, 51) and action.lower() == "up":
        return True

    if state == (14, 51) and action.lower() == "left":
        return True

    if state == (15, 0) and action.lower() == "right-up":
        return True

    if state == (15, 0) and action.lower() == "right":
        return True

    if state == (15, 0) and action.lower() == "right-down":
        return True

    if state == (15, 1) and action.lower() == "up":
        return True

    if state == (15, 1) and action.lower() == "right-up":
        return True

    if state == (15, 1) and action.lower() == "right-down":
        return True

    if state == (15, 1) and action.lower() == "down":
        return True

    if state == (15, 1) and action.lower() == "left":
        return True

    if state == (15, 4) and action.lower() == "left-up":
        return True

    if state == (15, 4) and action.lower() == "up":
        return True

    if state == (15, 4) and action.lower() == "right-up":
        return True

    if state == (15, 4) and action.lower() == "right":
        return True

    if state == (15, 4) and action.lower() == "right-down":
        return True

    if state == (15, 4) and action.lower() == "left-down":
        return True

    if state == (15, 5) and action.lower() == "left-up":
        return True

    if state == (15, 5) and action.lower() == "up":
        return True

    if state == (15, 5) and action.lower() == "right-up":
        return True

    if state == (15, 5) and action.lower() == "right":
        return True

    if state == (15, 5) and action.lower() == "down":
        return True

    if state == (15, 5) and action.lower() == "left":
        return True

    if state == (15, 6) and action.lower() == "left-up":
        return True

    if state == (15, 6) and action.lower() == "up":
        return True

    if state == (15, 6) and action.lower() == "left-down":
        return True

    if state == (15, 6) and action.lower() == "left":
        return True

    if state == (15, 9) and action.lower() == "right-up":
        return True

    if state == (15, 9) and action.lower() == "right":
        return True

    if state == (15, 9) and action.lower() == "down":
        return True

    if state == (15, 10) and action.lower() == "up":
        return True

    if state == (15, 10) and action.lower() == "right-up":
        return True

    if state == (15, 10) and action.lower() == "right":
        return True

    if state == (15, 10) and action.lower() == "left-down":
        return True

    if state == (15, 10) and action.lower() == "left":
        return True

    if state == (15, 11) and action.lower() == "left-up":
        return True

    if state == (15, 11) and action.lower() == "up":
        return True

    if state == (15, 11) and action.lower() == "right":
        return True

    if state == (15, 11) and action.lower() == "left":
        return True

    if state == (15, 12) and action.lower() == "left-up":
        return True

    if state == (15, 12) and action.lower() == "right-up":
        return True

    if state == (15, 12) and action.lower() == "left":
        return True

    if state == (15, 14) and action.lower() == "left-up":
        return True

    if state == (15, 14) and action.lower() == "right":
        return True

    if state == (15, 14) and action.lower() == "down":
        return True

    if state == (15, 15) and action.lower() == "right-up":
        return True

    if state == (15, 15) and action.lower() == "left-down":
        return True

    if state == (15, 15) and action.lower() == "left":
        return True

    if state == (15, 18) and action.lower() == "up":
        return True

    if state == (15, 18) and action.lower() == "right-up":
        return True

    if state == (15, 18) and action.lower() == "left-down":
        return True

    if state == (15, 21) and action.lower() == "right-up":
        return True

    if state == (15, 21) and action.lower() == "down":
        return True

    if state == (15, 24) and action.lower() == "up":
        return True

    if state == (15, 24) and action.lower() == "right-up":
        return True

    if state == (15, 24) and action.lower() == "right":
        return True

    if state == (15, 24) and action.lower() == "left-down":
        return True

    if state == (15, 25) and action.lower() == "left-up":
        return True

    if state == (15, 25) and action.lower() == "up":
        return True

    if state == (15, 25) and action.lower() == "right-up":
        return True

    if state == (15, 25) and action.lower() == "right":
        return True

    if state == (15, 25) and action.lower() == "right-down":
        return True

    if state == (15, 25) and action.lower() == "left":
        return True

    if state == (15, 26) and action.lower() == "left-up":
        return True

    if state == (15, 26) and action.lower() == "up":
        return True

    if state == (15, 26) and action.lower() == "right-up":
        return True

    if state == (15, 26) and action.lower() == "down":
        return True

    if state == (15, 26) and action.lower() == "left":
        return True

    if state == (15, 31) and action.lower() == "up":
        return True

    if state == (15, 31) and action.lower() == "right":
        return True

    if state == (15, 31) and action.lower() == "right-down":
        return True

    if state == (15, 32) and action.lower() == "left-up":
        return True

    if state == (15, 32) and action.lower() == "right-up":
        return True

    if state == (15, 32) and action.lower() == "right":
        return True

    if state == (15, 32) and action.lower() == "down":
        return True

    if state == (15, 32) and action.lower() == "left":
        return True

    if state == (15, 33) and action.lower() == "up":
        return True

    if state == (15, 33) and action.lower() == "right-up":
        return True

    if state == (15, 33) and action.lower() == "right-down":
        return True

    if state == (15, 33) and action.lower() == "left-down":
        return True

    if state == (15, 33) and action.lower() == "left":
        return True

    if state == (15, 36) and action.lower() == "left-up":
        return True

    if state == (15, 36) and action.lower() == "right-up":
        return True

    if state == (15, 36) and action.lower() == "down":
        return True

    if state == (15, 36) and action.lower() == "left-down":
        return True

    if state == (15, 38) and action.lower() == "left-up":
        return True

    if state == (15, 38) and action.lower() == "right-down":
        return True

    if state == (15, 38) and action.lower() == "down":
        return True

    if state == (15, 40) and action.lower() == "up":
        return True

    if state == (15, 40) and action.lower() == "right":
        return True

    if state == (15, 40) and action.lower() == "right-down":
        return True

    if state == (15, 40) and action.lower() == "down":
        return True

    if state == (15, 40) and action.lower() == "left-down":
        return True

    if state == (15, 41) and action.lower() == "left-up":
        return True

    if state == (15, 41) and action.lower() == "right-up":
        return True

    if state == (15, 41) and action.lower() == "right":
        return True

    if state == (15, 41) and action.lower() == "right-down":
        return True

    if state == (15, 41) and action.lower() == "down":
        return True

    if state == (15, 41) and action.lower() == "left-down":
        return True

    if state == (15, 41) and action.lower() == "left":
        return True

    if state == (15, 42) and action.lower() == "up":
        return True

    if state == (15, 42) and action.lower() == "right-up":
        return True

    if state == (15, 42) and action.lower() == "down":
        return True

    if state == (15, 42) and action.lower() == "left-down":
        return True

    if state == (15, 42) and action.lower() == "left":
        return True

    if state == (15, 44) and action.lower() == "left-up":
        return True

    if state == (15, 44) and action.lower() == "right":
        return True

    if state == (15, 45) and action.lower() == "right-up":
        return True

    if state == (15, 45) and action.lower() == "right-down":
        return True

    if state == (15, 45) and action.lower() == "left":
        return True

    if state == (16, 1) and action.lower() == "left-up":
        return True

    if state == (16, 1) and action.lower() == "up":
        return True

    if state == (16, 1) and action.lower() == "right":
        return True

    if state == (16, 1) and action.lower() == "down":
        return True

    if state == (16, 1) and action.lower() == "left-down":
        return True

    if state == (16, 2) and action.lower() == "left-up":
        return True

    if state == (16, 2) and action.lower() == "right":
        return True

    if state == (16, 2) and action.lower() == "right-down":
        return True

    if state == (16, 2) and action.lower() == "left-down":
        return True

    if state == (16, 2) and action.lower() == "left":
        return True

    if state == (16, 3) and action.lower() == "right-up":
        return True

    if state == (16, 3) and action.lower() == "down":
        return True

    if state == (16, 3) and action.lower() == "left":
        return True

    if state == (16, 5) and action.lower() == "left-up":
        return True

    if state == (16, 5) and action.lower() == "up":
        return True

    if state == (16, 5) and action.lower() == "right-up":
        return True

    if state == (16, 9) and action.lower() == "up":
        return True

    if state == (16, 9) and action.lower() == "right-up":
        return True

    if state == (16, 14) and action.lower() == "up":
        return True

    if state == (16, 14) and action.lower() == "right-up":
        return True

    if state == (16, 17) and action.lower() == "right-up":
        return True

    if state == (16, 17) and action.lower() == "right-down":
        return True

    if state == (16, 21) and action.lower() == "up":
        return True

    if state == (16, 21) and action.lower() == "right-down":
        return True

    if state == (16, 21) and action.lower() == "left-down":
        return True

    if state == (16, 23) and action.lower() == "right-up":
        return True

    if state == (16, 23) and action.lower() == "left-down":
        return True

    if state == (16, 26) and action.lower() == "left-up":
        return True

    if state == (16, 26) and action.lower() == "up":
        return True

    if state == (16, 26) and action.lower() == "right-down":
        return True

    if state == (16, 26) and action.lower() == "down":
        return True

    if state == (16, 28) and action.lower() == "right-down":
        return True

    if state == (16, 28) and action.lower() == "down":
        return True

    if state == (16, 28) and action.lower() == "left-down":
        return True

    if state == (16, 32) and action.lower() == "left-up":
        return True

    if state == (16, 32) and action.lower() == "up":
        return True

    if state == (16, 32) and action.lower() == "right-up":
        return True

    if state == (16, 32) and action.lower() == "left-down":
        return True

    if state == (16, 34) and action.lower() == "left-up":
        return True

    if state == (16, 34) and action.lower() == "right":
        return True

    if state == (16, 34) and action.lower() == "down":
        return True

    if state == (16, 35) and action.lower() == "right-up":
        return True

    if state == (16, 35) and action.lower() == "right":
        return True

    if state == (16, 35) and action.lower() == "left-down":
        return True

    if state == (16, 35) and action.lower() == "left":
        return True

    if state == (16, 36) and action.lower() == "up":
        return True

    if state == (16, 36) and action.lower() == "right-down":
        return True

    if state == (16, 36) and action.lower() == "left":
        return True

    if state == (16, 38) and action.lower() == "up":
        return True

    if state == (16, 38) and action.lower() == "right":
        return True

    if state == (16, 38) and action.lower() == "right-down":
        return True

    if state == (16, 38) and action.lower() == "down":
        return True

    if state == (16, 38) and action.lower() == "left-down":
        return True

    if state == (16, 39) and action.lower() == "left-up":
        return True

    if state == (16, 39) and action.lower() == "right-up":
        return True

    if state == (16, 39) and action.lower() == "right":
        return True

    if state == (16, 39) and action.lower() == "down":
        return True

    if state == (16, 39) and action.lower() == "left-down":
        return True

    if state == (16, 39) and action.lower() == "left":
        return True

    if state == (16, 40) and action.lower() == "up":
        return True

    if state == (16, 40) and action.lower() == "right-up":
        return True

    if state == (16, 40) and action.lower() == "right":
        return True

    if state == (16, 40) and action.lower() == "right-down":
        return True

    if state == (16, 40) and action.lower() == "left-down":
        return True

    if state == (16, 40) and action.lower() == "left":
        return True

    if state == (16, 41) and action.lower() == "left-up":
        return True

    if state == (16, 41) and action.lower() == "up":
        return True

    if state == (16, 41) and action.lower() == "right-up":
        return True

    if state == (16, 41) and action.lower() == "right":
        return True

    if state == (16, 41) and action.lower() == "right-down":
        return True

    if state == (16, 41) and action.lower() == "down":
        return True

    if state == (16, 41) and action.lower() == "left":
        return True

    if state == (16, 42) and action.lower() == "left-up":
        return True

    if state == (16, 42) and action.lower() == "up":
        return True

    if state == (16, 42) and action.lower() == "right-down":
        return True

    if state == (16, 42) and action.lower() == "down":
        return True

    if state == (16, 42) and action.lower() == "left-down":
        return True

    if state == (16, 42) and action.lower() == "left":
        return True

    if state == (16, 46) and action.lower() == "left-up":
        return True

    if state == (16, 46) and action.lower() == "right":
        return True

    if state == (16, 46) and action.lower() == "down":
        return True

    if state == (16, 46) and action.lower() == "left-down":
        return True

    if state == (16, 47) and action.lower() == "right":
        return True

    if state == (16, 47) and action.lower() == "left-down":
        return True

    if state == (16, 47) and action.lower() == "left":
        return True

    if state == (16, 48) and action.lower() == "right-down":
        return True

    if state == (16, 48) and action.lower() == "left":
        return True

    if state == (16, 50) and action.lower() == "right-down":
        return True

    if state == (16, 50) and action.lower() == "down":
        return True

    if state == (16, 50) and action.lower() == "left-down":
        return True

    if state == (17, 0) and action.lower() == "right-up":
        return True

    if state == (17, 0) and action.lower() == "right":
        return True

    if state == (17, 0) and action.lower() == "right-down":
        return True

    if state == (17, 0) and action.lower() == "down":
        return True

    if state == (17, 1) and action.lower() == "up":
        return True

    if state == (17, 1) and action.lower() == "right-up":
        return True

    if state == (17, 1) and action.lower() == "down":
        return True

    if state == (17, 1) and action.lower() == "left-down":
        return True

    if state == (17, 1) and action.lower() == "left":
        return True

    if state == (17, 3) and action.lower() == "left-up":
        return True

    if state == (17, 3) and action.lower() == "up":
        return True

    if state == (17, 3) and action.lower() == "right-down":
        return True

    if state == (17, 3) and action.lower() == "down":
        return True

    if state == (17, 7) and action.lower() == "left-down":
        return True

    if state == (17, 11) and action.lower() == "right":
        return True

    if state == (17, 11) and action.lower() == "down":
        return True

    if state == (17, 12) and action.lower() == "left-down":
        return True

    if state == (17, 12) and action.lower() == "left":
        return True

    if state == (17, 18) and action.lower() == "left-up":
        return True

    if state == (17, 18) and action.lower() == "right":
        return True

    if state == (17, 18) and action.lower() == "down":
        return True

    if state == (17, 18) and action.lower() == "left-down":
        return True

    if state == (17, 19) and action.lower() == "right":
        return True

    if state == (17, 19) and action.lower() == "right-down":
        return True

    if state == (17, 19) and action.lower() == "left-down":
        return True

    if state == (17, 19) and action.lower() == "left":
        return True

    if state == (17, 20) and action.lower() == "right-up":
        return True

    if state == (17, 20) and action.lower() == "down":
        return True

    if state == (17, 20) and action.lower() == "left":
        return True

    if state == (17, 22) and action.lower() == "left-up":
        return True

    if state == (17, 22) and action.lower() == "right-up":
        return True

    if state == (17, 22) and action.lower() == "right-down":
        return True

    if state == (17, 26) and action.lower() == "up":
        return True

    if state == (17, 26) and action.lower() == "right":
        return True

    if state == (17, 26) and action.lower() == "right-down":
        return True

    if state == (17, 26) and action.lower() == "left-down":
        return True

    if state == (17, 27) and action.lower() == "left-up":
        return True

    if state == (17, 27) and action.lower() == "right-up":
        return True

    if state == (17, 27) and action.lower() == "right":
        return True

    if state == (17, 27) and action.lower() == "right-down":
        return True

    if state == (17, 27) and action.lower() == "down":
        return True

    if state == (17, 27) and action.lower() == "left":
        return True

    if state == (17, 28) and action.lower() == "up":
        return True

    if state == (17, 28) and action.lower() == "right":
        return True

    if state == (17, 28) and action.lower() == "right-down":
        return True

    if state == (17, 28) and action.lower() == "down":
        return True

    if state == (17, 28) and action.lower() == "left-down":
        return True

    if state == (17, 28) and action.lower() == "left":
        return True

    if state == (17, 29) and action.lower() == "left-up":
        return True

    if state == (17, 29) and action.lower() == "right":
        return True

    if state == (17, 29) and action.lower() == "down":
        return True

    if state == (17, 29) and action.lower() == "left-down":
        return True

    if state == (17, 29) and action.lower() == "left":
        return True

    if state == (17, 30) and action.lower() == "right":
        return True

    if state == (17, 30) and action.lower() == "left-down":
        return True

    if state == (17, 30) and action.lower() == "left":
        return True

    if state == (17, 31) and action.lower() == "right-up":
        return True

    if state == (17, 31) and action.lower() == "right-down":
        return True

    if state == (17, 31) and action.lower() == "left":
        return True

    if state == (17, 34) and action.lower() == "up":
        return True

    if state == (17, 34) and action.lower() == "right-up":
        return True

    if state == (17, 34) and action.lower() == "down":
        return True

    if state == (17, 34) and action.lower() == "left-down":
        return True

    if state == (17, 37) and action.lower() == "left-up":
        return True

    if state == (17, 37) and action.lower() == "right-up":
        return True

    if state == (17, 37) and action.lower() == "right":
        return True

    if state == (17, 37) and action.lower() == "left-down":
        return True

    if state == (17, 38) and action.lower() == "up":
        return True

    if state == (17, 38) and action.lower() == "right-up":
        return True

    if state == (17, 38) and action.lower() == "right":
        return True

    if state == (17, 38) and action.lower() == "left":
        return True

    if state == (17, 39) and action.lower() == "left-up":
        return True

    if state == (17, 39) and action.lower() == "up":
        return True

    if state == (17, 39) and action.lower() == "right-up":
        return True

    if state == (17, 39) and action.lower() == "right-down":
        return True

    if state == (17, 39) and action.lower() == "left":
        return True

    if state == (17, 41) and action.lower() == "left-up":
        return True

    if state == (17, 41) and action.lower() == "up":
        return True

    if state == (17, 41) and action.lower() == "right-up":
        return True

    if state == (17, 41) and action.lower() == "right":
        return True

    if state == (17, 41) and action.lower() == "down":
        return True

    if state == (17, 41) and action.lower() == "left-down":
        return True

    if state == (17, 42) and action.lower() == "left-up":
        return True

    if state == (17, 42) and action.lower() == "up":
        return True

    if state == (17, 42) and action.lower() == "right":
        return True

    if state == (17, 42) and action.lower() == "right-down":
        return True

    if state == (17, 42) and action.lower() == "left-down":
        return True

    if state == (17, 42) and action.lower() == "left":
        return True

    if state == (17, 43) and action.lower() == "left-up":
        return True

    if state == (17, 43) and action.lower() == "right":
        return True

    if state == (17, 43) and action.lower() == "right-down":
        return True

    if state == (17, 43) and action.lower() == "down":
        return True

    if state == (17, 43) and action.lower() == "left":
        return True

    if state == (17, 44) and action.lower() == "right":
        return True

    if state == (17, 44) and action.lower() == "right-down":
        return True

    if state == (17, 44) and action.lower() == "down":
        return True

    if state == (17, 44) and action.lower() == "left-down":
        return True

    if state == (17, 44) and action.lower() == "left":
        return True

    if state == (17, 45) and action.lower() == "right-up":
        return True

    if state == (17, 45) and action.lower() == "right":
        return True

    if state == (17, 45) and action.lower() == "right-down":
        return True

    if state == (17, 45) and action.lower() == "down":
        return True

    if state == (17, 45) and action.lower() == "left-down":
        return True

    if state == (17, 45) and action.lower() == "left":
        return True

    if state == (17, 46) and action.lower() == "up":
        return True

    if state == (17, 46) and action.lower() == "right-up":
        return True

    if state == (17, 46) and action.lower() == "down":
        return True

    if state == (17, 46) and action.lower() == "left-down":
        return True

    if state == (17, 46) and action.lower() == "left":
        return True

    if state == (17, 49) and action.lower() == "left-up":
        return True

    if state == (17, 49) and action.lower() == "right-up":
        return True

    if state == (17, 49) and action.lower() == "right":
        return True

    if state == (17, 49) and action.lower() == "left-down":
        return True

    if state == (17, 50) and action.lower() == "up":
        return True

    if state == (17, 50) and action.lower() == "right":
        return True

    if state == (17, 50) and action.lower() == "right-down":
        return True

    if state == (17, 50) and action.lower() == "left":
        return True

    if state == (17, 51) and action.lower() == "left-up":
        return True

    if state == (17, 51) and action.lower() == "down":
        return True

    if state == (17, 51) and action.lower() == "left":
        return True

    if state == (18, 0) and action.lower() == "up":
        return True

    if state == (18, 0) and action.lower() == "right-up":
        return True

    if state == (18, 0) and action.lower() == "right":
        return True

    if state == (18, 1) and action.lower() == "left-up":
        return True

    if state == (18, 1) and action.lower() == "up":
        return True

    if state == (18, 1) and action.lower() == "right-down":
        return True

    if state == (18, 1) and action.lower() == "left":
        return True

    if state == (18, 3) and action.lower() == "up":
        return True

    if state == (18, 3) and action.lower() == "right":
        return True

    if state == (18, 3) and action.lower() == "left-down":
        return True

    if state == (18, 4) and action.lower() == "left-up":
        return True

    if state == (18, 4) and action.lower() == "right-down":
        return True

    if state == (18, 4) and action.lower() == "left":
        return True

    if state == (18, 6) and action.lower() == "right-up":
        return True

    if state == (18, 6) and action.lower() == "right-down":
        return True

    if state == (18, 6) and action.lower() == "down":
        return True

    if state == (18, 6) and action.lower() == "left-down":
        return True

    if state == (18, 11) and action.lower() == "up":
        return True

    if state == (18, 11) and action.lower() == "right-up":
        return True

    if state == (18, 11) and action.lower() == "left-down":
        return True

    if state == (18, 15) and action.lower() == "right-down":
        return True

    if state == (18, 15) and action.lower() == "down":
        return True

    if state == (18, 17) and action.lower() == "right-up":
        return True

    if state == (18, 17) and action.lower() == "right":
        return True

    if state == (18, 17) and action.lower() == "right-down":
        return True

    if state == (18, 17) and action.lower() == "down":
        return True

    if state == (18, 17) and action.lower() == "left-down":
        return True

    if state == (18, 18) and action.lower() == "up":
        return True

    if state == (18, 18) and action.lower() == "right-up":
        return True

    if state == (18, 18) and action.lower() == "down":
        return True

    if state == (18, 18) and action.lower() == "left-down":
        return True

    if state == (18, 18) and action.lower() == "left":
        return True

    if state == (18, 20) and action.lower() == "left-up":
        return True

    if state == (18, 20) and action.lower() == "up":
        return True

    if state == (18, 23) and action.lower() == "left-up":
        return True

    if state == (18, 23) and action.lower() == "right":
        return True

    if state == (18, 23) and action.lower() == "left-down":
        return True

    if state == (18, 24) and action.lower() == "right":
        return True

    if state == (18, 24) and action.lower() == "right-down":
        return True

    if state == (18, 24) and action.lower() == "left":
        return True

    if state == (18, 25) and action.lower() == "right-up":
        return True

    if state == (18, 25) and action.lower() == "down":
        return True

    if state == (18, 25) and action.lower() == "left":
        return True

    if state == (18, 27) and action.lower() == "left-up":
        return True

    if state == (18, 27) and action.lower() == "up":
        return True

    if state == (18, 27) and action.lower() == "right-up":
        return True

    if state == (18, 27) and action.lower() == "right":
        return True

    if state == (18, 27) and action.lower() == "down":
        return True

    if state == (18, 28) and action.lower() == "left-up":
        return True

    if state == (18, 28) and action.lower() == "up":
        return True

    if state == (18, 28) and action.lower() == "right-up":
        return True

    if state == (18, 28) and action.lower() == "right":
        return True

    if state == (18, 28) and action.lower() == "left-down":
        return True

    if state == (18, 28) and action.lower() == "left":
        return True

    if state == (18, 29) and action.lower() == "left-up":
        return True

    if state == (18, 29) and action.lower() == "up":
        return True

    if state == (18, 29) and action.lower() == "right-up":
        return True

    if state == (18, 29) and action.lower() == "left":
        return True

    if state == (18, 32) and action.lower() == "left-up":
        return True

    if state == (18, 32) and action.lower() == "right":
        return True

    if state == (18, 32) and action.lower() == "right-down":
        return True

    if state == (18, 33) and action.lower() == "right-up":
        return True

    if state == (18, 33) and action.lower() == "right":
        return True

    if state == (18, 33) and action.lower() == "right-down":
        return True

    if state == (18, 33) and action.lower() == "down":
        return True

    if state == (18, 33) and action.lower() == "left":
        return True

    if state == (18, 34) and action.lower() == "up":
        return True

    if state == (18, 34) and action.lower() == "down":
        return True

    if state == (18, 34) and action.lower() == "left-down":
        return True

    if state == (18, 34) and action.lower() == "left":
        return True

    if state == (18, 36) and action.lower() == "right-up":
        return True

    if state == (18, 36) and action.lower() == "right-down":
        return True

    if state == (18, 40) and action.lower() == "left-up":
        return True

    if state == (18, 40) and action.lower() == "right-up":
        return True

    if state == (18, 40) and action.lower() == "right":
        return True

    if state == (18, 40) and action.lower() == "right-down":
        return True

    if state == (18, 41) and action.lower() == "up":
        return True

    if state == (18, 41) and action.lower() == "right-up":
        return True

    if state == (18, 41) and action.lower() == "down":
        return True

    if state == (18, 41) and action.lower() == "left":
        return True

    if state == (18, 43) and action.lower() == "left-up":
        return True

    if state == (18, 43) and action.lower() == "up":
        return True

    if state == (18, 43) and action.lower() == "right-up":
        return True

    if state == (18, 43) and action.lower() == "right":
        return True

    if state == (18, 43) and action.lower() == "right-down":
        return True

    if state == (18, 43) and action.lower() == "down":
        return True

    if state == (18, 44) and action.lower() == "left-up":
        return True

    if state == (18, 44) and action.lower() == "up":
        return True

    if state == (18, 44) and action.lower() == "right-up":
        return True

    if state == (18, 44) and action.lower() == "right":
        return True

    if state == (18, 44) and action.lower() == "down":
        return True

    if state == (18, 44) and action.lower() == "left-down":
        return True

    if state == (18, 44) and action.lower() == "left":
        return True

    if state == (18, 45) and action.lower() == "left-up":
        return True

    if state == (18, 45) and action.lower() == "up":
        return True

    if state == (18, 45) and action.lower() == "right-up":
        return True

    if state == (18, 45) and action.lower() == "right":
        return True

    if state == (18, 45) and action.lower() == "left-down":
        return True

    if state == (18, 45) and action.lower() == "left":
        return True

    if state == (18, 46) and action.lower() == "left-up":
        return True

    if state == (18, 46) and action.lower() == "up":
        return True

    if state == (18, 46) and action.lower() == "left":
        return True

    if state == (18, 48) and action.lower() == "right-up":
        return True

    if state == (18, 51) and action.lower() == "left-up":
        return True

    if state == (18, 51) and action.lower() == "up":
        return True

    if state == (18, 51) and action.lower() == "down":
        return True

    if state == (18, 51) and action.lower() == "left-down":
        return True

    if state == (19, 2) and action.lower() == "left-up":
        return True

    if state == (19, 2) and action.lower() == "right-up":
        return True

    if state == (19, 2) and action.lower() == "left-down":
        return True

    if state == (19, 5) and action.lower() == "left-up":
        return True

    if state == (19, 5) and action.lower() == "right-up":
        return True

    if state == (19, 5) and action.lower() == "right":
        return True

    if state == (19, 6) and action.lower() == "up":
        return True

    if state == (19, 6) and action.lower() == "right":
        return True

    if state == (19, 6) and action.lower() == "left":
        return True

    if state == (19, 7) and action.lower() == "left-up":
        return True

    if state == (19, 7) and action.lower() == "right-down":
        return True

    if state == (19, 7) and action.lower() == "left":
        return True

    if state == (19, 9) and action.lower() == "right":
        return True

    if state == (19, 9) and action.lower() == "right-down":
        return True

    if state == (19, 9) and action.lower() == "down":
        return True

    if state == (19, 9) and action.lower() == "left-down":
        return True

    if state == (19, 10) and action.lower() == "right-up":
        return True

    if state == (19, 10) and action.lower() == "right-down":
        return True

    if state == (19, 10) and action.lower() == "down":
        return True

    if state == (19, 10) and action.lower() == "left-down":
        return True

    if state == (19, 10) and action.lower() == "left":
        return True

    if state == (19, 15) and action.lower() == "up":
        return True

    if state == (19, 15) and action.lower() == "right":
        return True

    if state == (19, 15) and action.lower() == "right-down":
        return True

    if state == (19, 15) and action.lower() == "down":
        return True

    if state == (19, 15) and action.lower() == "left-down":
        return True

    if state == (19, 16) and action.lower() == "left-up":
        return True

    if state == (19, 16) and action.lower() == "right-up":
        return True

    if state == (19, 16) and action.lower() == "right":
        return True

    if state == (19, 16) and action.lower() == "down":
        return True

    if state == (19, 16) and action.lower() == "left-down":
        return True

    if state == (19, 16) and action.lower() == "left":
        return True

    if state == (19, 17) and action.lower() == "up":
        return True

    if state == (19, 17) and action.lower() == "right-up":
        return True

    if state == (19, 17) and action.lower() == "right":
        return True

    if state == (19, 17) and action.lower() == "left-down":
        return True

    if state == (19, 17) and action.lower() == "left":
        return True

    if state == (19, 18) and action.lower() == "left-up":
        return True

    if state == (19, 18) and action.lower() == "up":
        return True

    if state == (19, 18) and action.lower() == "right-down":
        return True

    if state == (19, 18) and action.lower() == "left":
        return True

    if state == (19, 22) and action.lower() == "right-up":
        return True

    if state == (19, 22) and action.lower() == "right-down":
        return True

    if state == (19, 22) and action.lower() == "down":
        return True

    if state == (19, 25) and action.lower() == "left-up":
        return True

    if state == (19, 25) and action.lower() == "up":
        return True

    if state == (19, 25) and action.lower() == "right-down":
        return True

    if state == (19, 25) and action.lower() == "down":
        return True

    if state == (19, 25) and action.lower() == "left-down":
        return True

    if state == (19, 27) and action.lower() == "up":
        return True

    if state == (19, 27) and action.lower() == "right-up":
        return True

    if state == (19, 27) and action.lower() == "right-down":
        return True

    if state == (19, 27) and action.lower() == "left-down":
        return True

    if state == (19, 33) and action.lower() == "left-up":
        return True

    if state == (19, 33) and action.lower() == "up":
        return True

    if state == (19, 33) and action.lower() == "right-up":
        return True

    if state == (19, 33) and action.lower() == "right":
        return True

    if state == (19, 33) and action.lower() == "down":
        return True

    if state == (19, 33) and action.lower() == "left-down":
        return True

    if state == (19, 34) and action.lower() == "left-up":
        return True

    if state == (19, 34) and action.lower() == "up":
        return True

    if state == (19, 34) and action.lower() == "right-down":
        return True

    if state == (19, 34) and action.lower() == "left-down":
        return True

    if state == (19, 34) and action.lower() == "left":
        return True

    if state == (19, 37) and action.lower() == "left-up":
        return True

    if state == (19, 41) and action.lower() == "left-up":
        return True

    if state == (19, 41) and action.lower() == "up":
        return True

    if state == (19, 41) and action.lower() == "right-down":
        return True

    if state == (19, 43) and action.lower() == "up":
        return True

    if state == (19, 43) and action.lower() == "right-up":
        return True

    if state == (19, 43) and action.lower() == "right":
        return True

    if state == (19, 43) and action.lower() == "right-down":
        return True

    if state == (19, 43) and action.lower() == "left-down":
        return True

    if state == (19, 44) and action.lower() == "left-up":
        return True

    if state == (19, 44) and action.lower() == "up":
        return True

    if state == (19, 44) and action.lower() == "right-up":
        return True

    if state == (19, 44) and action.lower() == "down":
        return True

    if state == (19, 44) and action.lower() == "left":
        return True

    if state == (19, 50) and action.lower() == "right-up":
        return True

    if state == (19, 50) and action.lower() == "right":
        return True

    if state == (19, 50) and action.lower() == "right-down":
        return True

    if state == (19, 51) and action.lower() == "up":
        return True

    if state == (19, 51) and action.lower() == "down":
        return True

    if state == (19, 51) and action.lower() == "left":
        return True

    if state == (20, 0) and action.lower() == "right":
        return True

    if state == (20, 0) and action.lower() == "down":
        return True

    if state == (20, 1) and action.lower() == "right-up":
        return True

    if state == (20, 1) and action.lower() == "left-down":
        return True

    if state == (20, 1) and action.lower() == "left":
        return True

    if state == (20, 8) and action.lower() == "left-up":
        return True

    if state == (20, 8) and action.lower() == "right-up":
        return True

    if state == (20, 8) and action.lower() == "right":
        return True

    if state == (20, 8) and action.lower() == "right-down":
        return True

    if state == (20, 9) and action.lower() == "up":
        return True

    if state == (20, 9) and action.lower() == "right-up":
        return True

    if state == (20, 9) and action.lower() == "right":
        return True

    if state == (20, 9) and action.lower() == "down":
        return True

    if state == (20, 9) and action.lower() == "left":
        return True

    if state == (20, 10) and action.lower() == "left-up":
        return True

    if state == (20, 10) and action.lower() == "up":
        return True

    if state == (20, 10) and action.lower() == "right":
        return True

    if state == (20, 10) and action.lower() == "left-down":
        return True

    if state == (20, 10) and action.lower() == "left":
        return True

    if state == (20, 11) and action.lower() == "left-up":
        return True

    if state == (20, 11) and action.lower() == "right-down":
        return True

    if state == (20, 11) and action.lower() == "left":
        return True

    if state == (20, 13) and action.lower() == "right":
        return True

    if state == (20, 13) and action.lower() == "down":
        return True

    if state == (20, 13) and action.lower() == "left-down":
        return True

    if state == (20, 14) and action.lower() == "right-up":
        return True

    if state == (20, 14) and action.lower() == "right":
        return True

    if state == (20, 14) and action.lower() == "right-down":
        return True

    if state == (20, 14) and action.lower() == "left-down":
        return True

    if state == (20, 14) and action.lower() == "left":
        return True

    if state == (20, 15) and action.lower() == "up":
        return True

    if state == (20, 15) and action.lower() == "right-up":
        return True

    if state == (20, 15) and action.lower() == "right":
        return True

    if state == (20, 15) and action.lower() == "right-down":
        return True

    if state == (20, 15) and action.lower() == "down":
        return True

    if state == (20, 15) and action.lower() == "left":
        return True

    if state == (20, 16) and action.lower() == "left-up":
        return True

    if state == (20, 16) and action.lower() == "up":
        return True

    if state == (20, 16) and action.lower() == "right-up":
        return True

    if state == (20, 16) and action.lower() == "right-down":
        return True

    if state == (20, 16) and action.lower() == "down":
        return True

    if state == (20, 16) and action.lower() == "left-down":
        return True

    if state == (20, 16) and action.lower() == "left":
        return True

    if state == (20, 19) and action.lower() == "left-up":
        return True

    if state == (20, 19) and action.lower() == "down":
        return True

    if state == (20, 19) and action.lower() == "left-down":
        return True

    if state == (20, 22) and action.lower() == "up":
        return True

    if state == (20, 22) and action.lower() == "right":
        return True

    if state == (20, 22) and action.lower() == "right-down":
        return True

    if state == (20, 22) and action.lower() == "down":
        return True

    if state == (20, 22) and action.lower() == "left-down":
        return True

    if state == (20, 23) and action.lower() == "left-up":
        return True

    if state == (20, 23) and action.lower() == "right":
        return True

    if state == (20, 23) and action.lower() == "down":
        return True

    if state == (20, 23) and action.lower() == "left-down":
        return True

    if state == (20, 23) and action.lower() == "left":
        return True

    if state == (20, 24) and action.lower() == "right-up":
        return True

    if state == (20, 24) and action.lower() == "right":
        return True

    if state == (20, 24) and action.lower() == "left-down":
        return True

    if state == (20, 24) and action.lower() == "left":
        return True

    if state == (20, 25) and action.lower() == "up":
        return True

    if state == (20, 25) and action.lower() == "right":
        return True

    if state == (20, 25) and action.lower() == "left":
        return True

    if state == (20, 26) and action.lower() == "left-up":
        return True

    if state == (20, 26) and action.lower() == "right-up":
        return True

    if state == (20, 26) and action.lower() == "left":
        return True

    if state == (20, 28) and action.lower() == "left-up":
        return True

    if state == (20, 28) and action.lower() == "right":
        return True

    if state == (20, 28) and action.lower() == "down":
        return True

    if state == (20, 29) and action.lower() == "right":
        return True

    if state == (20, 29) and action.lower() == "left-down":
        return True

    if state == (20, 29) and action.lower() == "left":
        return True

    if state == (20, 30) and action.lower() == "left":
        return True

    if state == (20, 32) and action.lower() == "right-up":
        return True

    if state == (20, 32) and action.lower() == "right":
        return True

    if state == (20, 32) and action.lower() == "right-down":
        return True

    if state == (20, 33) and action.lower() == "up":
        return True

    if state == (20, 33) and action.lower() == "right-up":
        return True

    if state == (20, 33) and action.lower() == "down":
        return True

    if state == (20, 33) and action.lower() == "left":
        return True

    if state == (20, 35) and action.lower() == "left-up":
        return True

    if state == (20, 39) and action.lower() == "down":
        return True

    if state == (20, 42) and action.lower() == "left-up":
        return True

    if state == (20, 42) and action.lower() == "right-up":
        return True

    if state == (20, 42) and action.lower() == "right-down":
        return True

    if state == (20, 44) and action.lower() == "left-up":
        return True

    if state == (20, 44) and action.lower() == "up":
        return True

    if state == (20, 44) and action.lower() == "left-down":
        return True

    if state == (20, 51) and action.lower() == "left-up":
        return True

    if state == (20, 51) and action.lower() == "up":
        return True

    if state == (21, 0) and action.lower() == "up":
        return True

    if state == (21, 0) and action.lower() == "right-up":
        return True

    if state == (21, 0) and action.lower() == "right-down":
        return True

    if state == (21, 3) and action.lower() == "down":
        return True

    if state == (21, 5) and action.lower() == "right":
        return True

    if state == (21, 5) and action.lower() == "down":
        return True

    if state == (21, 6) and action.lower() == "left-down":
        return True

    if state == (21, 6) and action.lower() == "left":
        return True

    if state == (21, 9) and action.lower() == "left-up":
        return True

    if state == (21, 9) and action.lower() == "up":
        return True

    if state == (21, 9) and action.lower() == "right-up":
        return True

    if state == (21, 12) and action.lower() == "left-up":
        return True

    if state == (21, 12) and action.lower() == "right-up":
        return True

    if state == (21, 12) and action.lower() == "right":
        return True

    if state == (21, 12) and action.lower() == "right-down":
        return True

    if state == (21, 12) and action.lower() == "left-down":
        return True

    if state == (21, 13) and action.lower() == "up":
        return True

    if state == (21, 13) and action.lower() == "right-up":
        return True

    if state == (21, 13) and action.lower() == "right-down":
        return True

    if state == (21, 13) and action.lower() == "down":
        return True

    if state == (21, 13) and action.lower() == "left":
        return True

    if state == (21, 15) and action.lower() == "left-up":
        return True

    if state == (21, 15) and action.lower() == "up":
        return True

    if state == (21, 15) and action.lower() == "right-up":
        return True

    if state == (21, 15) and action.lower() == "right":
        return True

    if state == (21, 15) and action.lower() == "left-down":
        return True

    if state == (21, 16) and action.lower() == "left-up":
        return True

    if state == (21, 16) and action.lower() == "up":
        return True

    if state == (21, 16) and action.lower() == "right":
        return True

    if state == (21, 16) and action.lower() == "right-down":
        return True

    if state == (21, 16) and action.lower() == "left":
        return True

    if state == (21, 17) and action.lower() == "left-up":
        return True

    if state == (21, 17) and action.lower() == "right":
        return True

    if state == (21, 17) and action.lower() == "down":
        return True

    if state == (21, 17) and action.lower() == "left":
        return True

    if state == (21, 18) and action.lower() == "right-up":
        return True

    if state == (21, 18) and action.lower() == "right":
        return True

    if state == (21, 18) and action.lower() == "left-down":
        return True

    if state == (21, 18) and action.lower() == "left":
        return True

    if state == (21, 19) and action.lower() == "up":
        return True

    if state == (21, 19) and action.lower() == "right-down":
        return True

    if state == (21, 19) and action.lower() == "left":
        return True

    if state == (21, 21) and action.lower() == "right-up":
        return True

    if state == (21, 21) and action.lower() == "right":
        return True

    if state == (21, 21) and action.lower() == "down":
        return True

    if state == (21, 21) and action.lower() == "left-down":
        return True

    if state == (21, 22) and action.lower() == "up":
        return True

    if state == (21, 22) and action.lower() == "right-up":
        return True

    if state == (21, 22) and action.lower() == "right":
        return True

    if state == (21, 22) and action.lower() == "left-down":
        return True

    if state == (21, 22) and action.lower() == "left":
        return True

    if state == (21, 23) and action.lower() == "left-up":
        return True

    if state == (21, 23) and action.lower() == "up":
        return True

    if state == (21, 23) and action.lower() == "right-up":
        return True

    if state == (21, 23) and action.lower() == "right-down":
        return True

    if state == (21, 23) and action.lower() == "left":
        return True

    if state == (21, 28) and action.lower() == "up":
        return True

    if state == (21, 28) and action.lower() == "right-up":
        return True

    if state == (21, 33) and action.lower() == "left-up":
        return True

    if state == (21, 33) and action.lower() == "up":
        return True

    if state == (21, 37) and action.lower() == "down":
        return True

    if state == (21, 39) and action.lower() == "up":
        return True

    if state == (21, 39) and action.lower() == "right-down":
        return True

    if state == (21, 43) and action.lower() == "left-up":
        return True

    if state == (21, 43) and action.lower() == "right-up":
        return True

    if state == (21, 43) and action.lower() == "down":
        return True

    if state == (21, 46) and action.lower() == "right":
        return True

    if state == (21, 46) and action.lower() == "down":
        return True

    if state == (21, 47) and action.lower() == "left-down":
        return True

    if state == (21, 47) and action.lower() == "left":
        return True

    if state == (21, 49) and action.lower() == "right-down":
        return True

    if state == (22, 1) and action.lower() == "left-up":
        return True

    if state == (22, 3) and action.lower() == "up":
        return True

    if state == (22, 3) and action.lower() == "right-down":
        return True

    if state == (22, 3) and action.lower() == "down":
        return True

    if state == (22, 5) and action.lower() == "up":
        return True

    if state == (22, 5) and action.lower() == "right-up":
        return True

    if state == (22, 5) and action.lower() == "down":
        return True

    if state == (22, 5) and action.lower() == "left-down":
        return True

    if state == (22, 11) and action.lower() == "right-up":
        return True

    if state == (22, 11) and action.lower() == "left-down":
        return True

    if state == (22, 13) and action.lower() == "left-up":
        return True

    if state == (22, 13) and action.lower() == "up":
        return True

    if state == (22, 13) and action.lower() == "right":
        return True

    if state == (22, 13) and action.lower() == "right-down":
        return True

    if state == (22, 13) and action.lower() == "down":
        return True

    if state == (22, 14) and action.lower() == "left-up":
        return True

    if state == (22, 14) and action.lower() == "right-up":
        return True

    if state == (22, 14) and action.lower() == "right-down":
        return True

    if state == (22, 14) and action.lower() == "down":
        return True

    if state == (22, 14) and action.lower() == "left-down":
        return True

    if state == (22, 14) and action.lower() == "left":
        return True

    if state == (22, 17) and action.lower() == "left-up":
        return True

    if state == (22, 17) and action.lower() == "up":
        return True

    if state == (22, 17) and action.lower() == "right-up":
        return True

    if state == (22, 17) and action.lower() == "down":
        return True

    if state == (22, 17) and action.lower() == "left-down":
        return True

    if state == (22, 20) and action.lower() == "left-up":
        return True

    if state == (22, 20) and action.lower() == "right-up":
        return True

    if state == (22, 20) and action.lower() == "right":
        return True

    if state == (22, 20) and action.lower() == "right-down":
        return True

    if state == (22, 20) and action.lower() == "left-down":
        return True

    if state == (22, 21) and action.lower() == "up":
        return True

    if state == (22, 21) and action.lower() == "right-up":
        return True

    if state == (22, 21) and action.lower() == "right-down":
        return True

    if state == (22, 21) and action.lower() == "down":
        return True

    if state == (22, 21) and action.lower() == "left":
        return True

    if state == (22, 24) and action.lower() == "left-up":
        return True

    if state == (22, 24) and action.lower() == "down":
        return True

    if state == (22, 35) and action.lower() == "down":
        return True

    if state == (22, 37) and action.lower() == "up":
        return True

    if state == (22, 40) and action.lower() == "left-up":
        return True

    if state == (22, 40) and action.lower() == "right-down":
        return True

    if state == (22, 40) and action.lower() == "down":
        return True

    if state == (22, 40) and action.lower() == "left-down":
        return True

    if state == (22, 43) and action.lower() == "up":
        return True

    if state == (22, 43) and action.lower() == "right-down":
        return True

    if state == (22, 46) and action.lower() == "up":
        return True

    if state == (22, 46) and action.lower() == "right-up":
        return True

    if state == (22, 46) and action.lower() == "down":
        return True

    if state == (22, 50) and action.lower() == "left-up":
        return True

    if state == (22, 50) and action.lower() == "right":
        return True

    if state == (22, 50) and action.lower() == "right-down":
        return True

    if state == (22, 50) and action.lower() == "down":
        return True

    if state == (22, 50) and action.lower() == "left-down":
        return True

    if state == (22, 51) and action.lower() == "down":
        return True

    if state == (22, 51) and action.lower() == "left-down":
        return True

    if state == (22, 51) and action.lower() == "left":
        return True

    if state == (23, 3) and action.lower() == "up":
        return True

    if state == (23, 3) and action.lower() == "right":
        return True

    if state == (23, 3) and action.lower() == "right-down":
        return True

    if state == (23, 3) and action.lower() == "down":
        return True

    if state == (23, 3) and action.lower() == "left-down":
        return True

    if state == (23, 4) and action.lower() == "left-up":
        return True

    if state == (23, 4) and action.lower() == "right-up":
        return True

    if state == (23, 4) and action.lower() == "right":
        return True

    if state == (23, 4) and action.lower() == "right-down":
        return True

    if state == (23, 4) and action.lower() == "down":
        return True

    if state == (23, 4) and action.lower() == "left-down":
        return True

    if state == (23, 4) and action.lower() == "left":
        return True

    if state == (23, 5) and action.lower() == "up":
        return True

    if state == (23, 5) and action.lower() == "right-down":
        return True

    if state == (23, 5) and action.lower() == "down":
        return True

    if state == (23, 5) and action.lower() == "left-down":
        return True

    if state == (23, 5) and action.lower() == "left":
        return True

    if state == (23, 9) and action.lower() == "right":
        return True

    if state == (23, 10) and action.lower() == "right-up":
        return True

    if state == (23, 10) and action.lower() == "left":
        return True

    if state == (23, 13) and action.lower() == "up":
        return True

    if state == (23, 13) and action.lower() == "right-up":
        return True

    if state == (23, 13) and action.lower() == "right":
        return True

    if state == (23, 13) and action.lower() == "down":
        return True

    if state == (23, 14) and action.lower() == "left-up":
        return True

    if state == (23, 14) and action.lower() == "up":
        return True

    if state == (23, 14) and action.lower() == "right":
        return True

    if state == (23, 14) and action.lower() == "right-down":
        return True

    if state == (23, 14) and action.lower() == "left-down":
        return True

    if state == (23, 14) and action.lower() == "left":
        return True

    if state == (23, 15) and action.lower() == "left-up":
        return True

    if state == (23, 15) and action.lower() == "right":
        return True

    if state == (23, 15) and action.lower() == "right-down":
        return True

    if state == (23, 15) and action.lower() == "down":
        return True

    if state == (23, 15) and action.lower() == "left":
        return True

    if state == (23, 16) and action.lower() == "right-up":
        return True

    if state == (23, 16) and action.lower() == "right":
        return True

    if state == (23, 16) and action.lower() == "down":
        return True

    if state == (23, 16) and action.lower() == "left-down":
        return True

    if state == (23, 16) and action.lower() == "left":
        return True

    if state == (23, 17) and action.lower() == "up":
        return True

    if state == (23, 17) and action.lower() == "left-down":
        return True

    if state == (23, 17) and action.lower() == "left":
        return True

    if state == (23, 19) and action.lower() == "right-up":
        return True

    if state == (23, 19) and action.lower() == "right-down":
        return True

    if state == (23, 19) and action.lower() == "down":
        return True

    if state == (23, 21) and action.lower() == "left-up":
        return True

    if state == (23, 21) and action.lower() == "up":
        return True

    if state == (23, 21) and action.lower() == "right":
        return True

    if state == (23, 21) and action.lower() == "right-down":
        return True

    if state == (23, 21) and action.lower() == "left-down":
        return True

    if state == (23, 22) and action.lower() == "left-up":
        return True

    if state == (23, 22) and action.lower() == "right-down":
        return True

    if state == (23, 22) and action.lower() == "down":
        return True

    if state == (23, 22) and action.lower() == "left":
        return True

    if state == (23, 24) and action.lower() == "up":
        return True

    if state == (23, 24) and action.lower() == "down":
        return True

    if state == (23, 24) and action.lower() == "left-down":
        return True

    if state == (23, 33) and action.lower() == "right-down":
        return True

    if state == (23, 33) and action.lower() == "down":
        return True

    if state == (23, 35) and action.lower() == "up":
        return True

    if state == (23, 35) and action.lower() == "right-down":
        return True

    if state == (23, 35) and action.lower() == "left-down":
        return True

    if state == (23, 39) and action.lower() == "right-up":
        return True

    if state == (23, 39) and action.lower() == "right":
        return True

    if state == (23, 39) and action.lower() == "right-down":
        return True

    if state == (23, 39) and action.lower() == "left-down":
        return True

    if state == (23, 40) and action.lower() == "up":
        return True

    if state == (23, 40) and action.lower() == "right":
        return True

    if state == (23, 40) and action.lower() == "right-down":
        return True

    if state == (23, 40) and action.lower() == "down":
        return True

    if state == (23, 40) and action.lower() == "left":
        return True

    if state == (23, 41) and action.lower() == "left-up":
        return True

    if state == (23, 41) and action.lower() == "down":
        return True

    if state == (23, 41) and action.lower() == "left-down":
        return True

    if state == (23, 41) and action.lower() == "left":
        return True

    if state == (23, 44) and action.lower() == "left-up":
        return True

    if state == (23, 46) and action.lower() == "up":
        return True

    if state == (23, 46) and action.lower() == "down":
        return True

    if state == (23, 49) and action.lower() == "right-up":
        return True

    if state == (23, 49) and action.lower() == "right":
        return True

    if state == (23, 49) and action.lower() == "left-down":
        return True

    if state == (23, 50) and action.lower() == "up":
        return True

    if state == (23, 50) and action.lower() == "right-up":
        return True

    if state == (23, 50) and action.lower() == "right":
        return True

    if state == (23, 50) and action.lower() == "right-down":
        return True

    if state == (23, 50) and action.lower() == "left":
        return True

    if state == (23, 51) and action.lower() == "left-up":
        return True

    if state == (23, 51) and action.lower() == "up":
        return True

    if state == (23, 51) and action.lower() == "down":
        return True

    if state == (23, 51) and action.lower() == "left":
        return True

    if state == (24, 1) and action.lower() == "right":
        return True

    if state == (24, 1) and action.lower() == "left-down":
        return True

    if state == (24, 2) and action.lower() == "right-up":
        return True

    if state == (24, 2) and action.lower() == "right":
        return True

    if state == (24, 2) and action.lower() == "left":
        return True

    if state == (24, 3) and action.lower() == "up":
        return True

    if state == (24, 3) and action.lower() == "right-up":
        return True

    if state == (24, 3) and action.lower() == "right":
        return True

    if state == (24, 3) and action.lower() == "left":
        return True

    if state == (24, 4) and action.lower() == "left-up":
        return True

    if state == (24, 4) and action.lower() == "up":
        return True

    if state == (24, 4) and action.lower() == "right-up":
        return True

    if state == (24, 4) and action.lower() == "right":
        return True

    if state == (24, 4) and action.lower() == "left":
        return True

    if state == (24, 5) and action.lower() == "left-up":
        return True

    if state == (24, 5) and action.lower() == "up":
        return True

    if state == (24, 5) and action.lower() == "right":
        return True

    if state == (24, 5) and action.lower() == "left":
        return True

    if state == (24, 6) and action.lower() == "left-up":
        return True

    if state == (24, 6) and action.lower() == "right":
        return True

    if state == (24, 6) and action.lower() == "right-down":
        return True

    if state == (24, 6) and action.lower() == "left":
        return True

    if state == (24, 7) and action.lower() == "down":
        return True

    if state == (24, 7) and action.lower() == "left":
        return True

    if state == (24, 13) and action.lower() == "up":
        return True

    if state == (24, 13) and action.lower() == "right-up":
        return True

    if state == (24, 13) and action.lower() == "right-down":
        return True

    if state == (24, 13) and action.lower() == "left-down":
        return True

    if state == (24, 15) and action.lower() == "left-up":
        return True

    if state == (24, 15) and action.lower() == "up":
        return True

    if state == (24, 15) and action.lower() == "right-up":
        return True

    if state == (24, 15) and action.lower() == "right":
        return True

    if state == (24, 15) and action.lower() == "left-down":
        return True

    if state == (24, 16) and action.lower() == "left-up":
        return True

    if state == (24, 16) and action.lower() == "up":
        return True

    if state == (24, 16) and action.lower() == "right-up":
        return True

    if state == (24, 16) and action.lower() == "left":
        return True

    if state == (24, 19) and action.lower() == "up":
        return True

    if state == (24, 19) and action.lower() == "right":
        return True

    if state == (24, 19) and action.lower() == "down":
        return True

    if state == (24, 19) and action.lower() == "left-down":
        return True

    if state == (24, 20) and action.lower() == "left-up":
        return True

    if state == (24, 20) and action.lower() == "right-up":
        return True

    if state == (24, 20) and action.lower() == "right-down":
        return True

    if state == (24, 20) and action.lower() == "left-down":
        return True

    if state == (24, 20) and action.lower() == "left":
        return True

    if state == (24, 22) and action.lower() == "left-up":
        return True

    if state == (24, 22) and action.lower() == "up":
        return True

    if state == (24, 22) and action.lower() == "right":
        return True

    if state == (24, 22) and action.lower() == "right-down":
        return True

    if state == (24, 22) and action.lower() == "left-down":
        return True

    if state == (24, 23) and action.lower() == "left-up":
        return True

    if state == (24, 23) and action.lower() == "right-up":
        return True

    if state == (24, 23) and action.lower() == "right":
        return True

    if state == (24, 23) and action.lower() == "right-down":
        return True

    if state == (24, 23) and action.lower() == "down":
        return True

    if state == (24, 23) and action.lower() == "left":
        return True

    if state == (24, 24) and action.lower() == "up":
        return True

    if state == (24, 24) and action.lower() == "down":
        return True

    if state == (24, 24) and action.lower() == "left-down":
        return True

    if state == (24, 24) and action.lower() == "left":
        return True

    if state == (24, 26) and action.lower() == "down":
        return True

    if state == (24, 31) and action.lower() == "right-down":
        return True

    if state == (24, 33) and action.lower() == "up":
        return True

    if state == (24, 33) and action.lower() == "right":
        return True

    if state == (24, 33) and action.lower() == "right-down":
        return True

    if state == (24, 33) and action.lower() == "down":
        return True

    if state == (24, 33) and action.lower() == "left-down":
        return True

    if state == (24, 34) and action.lower() == "left-up":
        return True

    if state == (24, 34) and action.lower() == "right-up":
        return True

    if state == (24, 34) and action.lower() == "right-down":
        return True

    if state == (24, 34) and action.lower() == "down":
        return True

    if state == (24, 34) and action.lower() == "left-down":
        return True

    if state == (24, 34) and action.lower() == "left":
        return True

    if state == (24, 36) and action.lower() == "left-up":
        return True

    if state == (24, 36) and action.lower() == "right":
        return True

    if state == (24, 36) and action.lower() == "down":
        return True

    if state == (24, 36) and action.lower() == "left-down":
        return True

    if state == (24, 37) and action.lower() == "right":
        return True

    if state == (24, 37) and action.lower() == "right-down":
        return True

    if state == (24, 37) and action.lower() == "left-down":
        return True

    if state == (24, 37) and action.lower() == "left":
        return True

    if state == (24, 38) and action.lower() == "right-up":
        return True

    if state == (24, 38) and action.lower() == "right-down":
        return True

    if state == (24, 38) and action.lower() == "down":
        return True

    if state == (24, 38) and action.lower() == "left":
        return True

    if state == (24, 40) and action.lower() == "left-up":
        return True

    if state == (24, 40) and action.lower() == "up":
        return True

    if state == (24, 40) and action.lower() == "right-up":
        return True

    if state == (24, 40) and action.lower() == "right":
        return True

    if state == (24, 40) and action.lower() == "right-down":
        return True

    if state == (24, 40) and action.lower() == "down":
        return True

    if state == (24, 40) and action.lower() == "left-down":
        return True

    if state == (24, 41) and action.lower() == "left-up":
        return True

    if state == (24, 41) and action.lower() == "up":
        return True

    if state == (24, 41) and action.lower() == "down":
        return True

    if state == (24, 41) and action.lower() == "left-down":
        return True

    if state == (24, 41) and action.lower() == "left":
        return True

    if state == (24, 46) and action.lower() == "up":
        return True

    if state == (24, 46) and action.lower() == "left-down":
        return True

    if state == (24, 48) and action.lower() == "right-up":
        return True

    if state == (24, 48) and action.lower() == "right-down":
        return True

    if state == (24, 51) and action.lower() == "left-up":
        return True

    if state == (24, 51) and action.lower() == "up":
        return True

    if state == (24, 51) and action.lower() == "down":
        return True

    if state == (25, 0) and action.lower() == "right-up":
        return True

    if state == (25, 0) and action.lower() == "down":
        return True

    if state == (25, 7) and action.lower() == "left-up":
        return True

    if state == (25, 7) and action.lower() == "up":
        return True

    if state == (25, 7) and action.lower() == "left-down":
        return True

    if state == (25, 12) and action.lower() == "right-up":
        return True

    if state == (25, 12) and action.lower() == "right-down":
        return True

    if state == (25, 12) and action.lower() == "left-down":
        return True

    if state == (25, 14) and action.lower() == "left-up":
        return True

    if state == (25, 14) and action.lower() == "right-up":
        return True

    if state == (25, 14) and action.lower() == "down":
        return True

    if state == (25, 14) and action.lower() == "left-down":
        return True

    if state == (25, 18) and action.lower() == "right-up":
        return True

    if state == (25, 18) and action.lower() == "right":
        return True

    if state == (25, 18) and action.lower() == "right-down":
        return True

    if state == (25, 18) and action.lower() == "left-down":
        return True

    if state == (25, 19) and action.lower() == "up":
        return True

    if state == (25, 19) and action.lower() == "right-up":
        return True

    if state == (25, 19) and action.lower() == "right-down":
        return True

    if state == (25, 19) and action.lower() == "down":
        return True

    if state == (25, 19) and action.lower() == "left":
        return True

    if state == (25, 21) and action.lower() == "left-up":
        return True

    if state == (25, 21) and action.lower() == "right-up":
        return True

    if state == (25, 21) and action.lower() == "left-down":
        return True

    if state == (25, 23) and action.lower() == "left-up":
        return True

    if state == (25, 23) and action.lower() == "up":
        return True

    if state == (25, 23) and action.lower() == "right-up":
        return True

    if state == (25, 23) and action.lower() == "right":
        return True

    if state == (25, 23) and action.lower() == "right-down":
        return True

    if state == (25, 24) and action.lower() == "left-up":
        return True

    if state == (25, 24) and action.lower() == "up":
        return True

    if state == (25, 24) and action.lower() == "down":
        return True

    if state == (25, 24) and action.lower() == "left":
        return True

    if state == (25, 26) and action.lower() == "up":
        return True

    if state == (25, 26) and action.lower() == "right-down":
        return True

    if state == (25, 26) and action.lower() == "down":
        return True

    if state == (25, 32) and action.lower() == "left-up":
        return True

    if state == (25, 32) and action.lower() == "right-up":
        return True

    if state == (25, 32) and action.lower() == "right":
        return True

    if state == (25, 32) and action.lower() == "left-down":
        return True

    if state == (25, 33) and action.lower() == "up":
        return True

    if state == (25, 33) and action.lower() == "right-up":
        return True

    if state == (25, 33) and action.lower() == "right":
        return True

    if state == (25, 33) and action.lower() == "right-down":
        return True

    if state == (25, 33) and action.lower() == "left":
        return True

    if state == (25, 34) and action.lower() == "left-up":
        return True

    if state == (25, 34) and action.lower() == "up":
        return True

    if state == (25, 34) and action.lower() == "right":
        return True

    if state == (25, 34) and action.lower() == "down":
        return True

    if state == (25, 34) and action.lower() == "left":
        return True

    if state == (25, 35) and action.lower() == "left-up":
        return True

    if state == (25, 35) and action.lower() == "right-up":
        return True

    if state == (25, 35) and action.lower() == "right":
        return True

    if state == (25, 35) and action.lower() == "right-down":
        return True

    if state == (25, 35) and action.lower() == "left-down":
        return True

    if state == (25, 35) and action.lower() == "left":
        return True

    if state == (25, 36) and action.lower() == "up":
        return True

    if state == (25, 36) and action.lower() == "right-up":
        return True

    if state == (25, 36) and action.lower() == "right-down":
        return True

    if state == (25, 36) and action.lower() == "down":
        return True

    if state == (25, 36) and action.lower() == "left":
        return True

    if state == (25, 38) and action.lower() == "left-up":
        return True

    if state == (25, 38) and action.lower() == "up":
        return True

    if state == (25, 38) and action.lower() == "right":
        return True

    if state == (25, 38) and action.lower() == "right-down":
        return True

    if state == (25, 38) and action.lower() == "left-down":
        return True

    if state == (25, 39) and action.lower() == "left-up":
        return True

    if state == (25, 39) and action.lower() == "right-up":
        return True

    if state == (25, 39) and action.lower() == "right":
        return True

    if state == (25, 39) and action.lower() == "right-down":
        return True

    if state == (25, 39) and action.lower() == "down":
        return True

    if state == (25, 39) and action.lower() == "left":
        return True

    if state == (25, 40) and action.lower() == "up":
        return True

    if state == (25, 40) and action.lower() == "right-up":
        return True

    if state == (25, 40) and action.lower() == "right":
        return True

    if state == (25, 40) and action.lower() == "right-down":
        return True

    if state == (25, 40) and action.lower() == "down":
        return True

    if state == (25, 40) and action.lower() == "left-down":
        return True

    if state == (25, 40) and action.lower() == "left":
        return True

    if state == (25, 41) and action.lower() == "left-up":
        return True

    if state == (25, 41) and action.lower() == "up":
        return True

    if state == (25, 41) and action.lower() == "down":
        return True

    if state == (25, 41) and action.lower() == "left-down":
        return True

    if state == (25, 41) and action.lower() == "left":
        return True

    if state == (25, 43) and action.lower() == "right":
        return True

    if state == (25, 43) and action.lower() == "down":
        return True

    if state == (25, 44) and action.lower() == "right":
        return True

    if state == (25, 44) and action.lower() == "left-down":
        return True

    if state == (25, 44) and action.lower() == "left":
        return True

    if state == (25, 45) and action.lower() == "right-up":
        return True

    if state == (25, 45) and action.lower() == "right-down":
        return True

    if state == (25, 45) and action.lower() == "left":
        return True

    if state == (25, 49) and action.lower() == "left-up":
        return True

    if state == (25, 49) and action.lower() == "left-down":
        return True

    if state == (25, 51) and action.lower() == "up":
        return True

    if state == (25, 51) and action.lower() == "down":
        return True

    if state == (26, 0) and action.lower() == "up":
        return True

    if state == (26, 0) and action.lower() == "right-down":
        return True

    if state == (26, 2) and action.lower() == "right":
        return True

    if state == (26, 2) and action.lower() == "down":
        return True

    if state == (26, 2) and action.lower() == "left-down":
        return True

    if state == (26, 3) and action.lower() == "left-down":
        return True

    if state == (26, 3) and action.lower() == "left":
        return True

    if state == (26, 6) and action.lower() == "right-up":
        return True

    if state == (26, 6) and action.lower() == "down":
        return True

    if state == (26, 9) and action.lower() == "down":
        return True

    if state == (26, 9) and action.lower() == "left-down":
        return True

    if state == (26, 11) and action.lower() == "right-up":
        return True

    if state == (26, 11) and action.lower() == "down":
        return True

    if state == (26, 13) and action.lower() == "left-up":
        return True

    if state == (26, 13) and action.lower() == "right-up":
        return True

    if state == (26, 13) and action.lower() == "right":
        return True

    if state == (26, 14) and action.lower() == "up":
        return True

    if state == (26, 14) and action.lower() == "right-down":
        return True

    if state == (26, 14) and action.lower() == "left":
        return True

    if state == (26, 16) and action.lower() == "right":
        return True

    if state == (26, 16) and action.lower() == "down":
        return True

    if state == (26, 16) and action.lower() == "left-down":
        return True

    if state == (26, 17) and action.lower() == "right-up":
        return True

    if state == (26, 17) and action.lower() == "right-down":
        return True

    if state == (26, 17) and action.lower() == "left-down":
        return True

    if state == (26, 17) and action.lower() == "left":
        return True

    if state == (26, 19) and action.lower() == "left-up":
        return True

    if state == (26, 19) and action.lower() == "up":
        return True

    if state == (26, 19) and action.lower() == "right":
        return True

    if state == (26, 19) and action.lower() == "right-down":
        return True

    if state == (26, 19) and action.lower() == "down":
        return True

    if state == (26, 19) and action.lower() == "left-down":
        return True

    if state == (26, 20) and action.lower() == "left-up":
        return True

    if state == (26, 20) and action.lower() == "right-up":
        return True

    if state == (26, 20) and action.lower() == "down":
        return True

    if state == (26, 20) and action.lower() == "left-down":
        return True

    if state == (26, 20) and action.lower() == "left":
        return True

    if state == (26, 24) and action.lower() == "left-up":
        return True

    if state == (26, 24) and action.lower() == "up":
        return True

    if state == (26, 26) and action.lower() == "up":
        return True

    if state == (26, 26) and action.lower() == "right":
        return True

    if state == (26, 26) and action.lower() == "right-down":
        return True

    if state == (26, 26) and action.lower() == "down":
        return True

    if state == (26, 27) and action.lower() == "left-up":
        return True

    if state == (26, 27) and action.lower() == "right":
        return True

    if state == (26, 27) and action.lower() == "down":
        return True

    if state == (26, 27) and action.lower() == "left-down":
        return True

    if state == (26, 27) and action.lower() == "left":
        return True

    if state == (26, 28) and action.lower() == "left-down":
        return True

    if state == (26, 28) and action.lower() == "left":
        return True

    if state == (26, 31) and action.lower() == "right-up":
        return True

    if state == (26, 31) and action.lower() == "right-down":
        return True

    if state == (26, 31) and action.lower() == "down":
        return True

    if state == (26, 31) and action.lower() == "left-down":
        return True

    if state == (26, 34) and action.lower() == "left-up":
        return True

    if state == (26, 34) and action.lower() == "up":
        return True

    if state == (26, 34) and action.lower() == "right-up":
        return True

    if state == (26, 34) and action.lower() == "right-down":
        return True

    if state == (26, 34) and action.lower() == "down":
        return True

    if state == (26, 36) and action.lower() == "left-up":
        return True

    if state == (26, 36) and action.lower() == "up":
        return True

    if state == (26, 36) and action.lower() == "right":
        return True

    if state == (26, 36) and action.lower() == "right-down":
        return True

    if state == (26, 36) and action.lower() == "left-down":
        return True

    if state == (26, 37) and action.lower() == "left-up":
        return True

    if state == (26, 37) and action.lower() == "right-up":
        return True

    if state == (26, 37) and action.lower() == "down":
        return True

    if state == (26, 37) and action.lower() == "left":
        return True

    if state == (26, 39) and action.lower() == "left-up":
        return True

    if state == (26, 39) and action.lower() == "up":
        return True

    if state == (26, 39) and action.lower() == "right-up":
        return True

    if state == (26, 39) and action.lower() == "right":
        return True

    if state == (26, 39) and action.lower() == "down":
        return True

    if state == (26, 40) and action.lower() == "left-up":
        return True

    if state == (26, 40) and action.lower() == "up":
        return True

    if state == (26, 40) and action.lower() == "right-up":
        return True

    if state == (26, 40) and action.lower() == "right":
        return True

    if state == (26, 40) and action.lower() == "right-down":
        return True

    if state == (26, 40) and action.lower() == "left-down":
        return True

    if state == (26, 40) and action.lower() == "left":
        return True

    if state == (26, 41) and action.lower() == "left-up":
        return True

    if state == (26, 41) and action.lower() == "up":
        return True

    if state == (26, 41) and action.lower() == "right-down":
        return True

    if state == (26, 41) and action.lower() == "down":
        return True

    if state == (26, 41) and action.lower() == "left":
        return True

    if state == (26, 43) and action.lower() == "up":
        return True

    if state == (26, 43) and action.lower() == "right-up":
        return True

    if state == (26, 43) and action.lower() == "down":
        return True

    if state == (26, 43) and action.lower() == "left-down":
        return True

    if state == (26, 46) and action.lower() == "left-up":
        return True

    if state == (26, 46) and action.lower() == "right":
        return True

    if state == (26, 47) and action.lower() == "right":
        return True

    if state == (26, 47) and action.lower() == "right-down":
        return True

    if state == (26, 47) and action.lower() == "left":
        return True

    if state == (26, 48) and action.lower() == "right-up":
        return True

    if state == (26, 48) and action.lower() == "down":
        return True

    if state == (26, 48) and action.lower() == "left":
        return True

    if state == (26, 51) and action.lower() == "up":
        return True

    if state == (26, 51) and action.lower() == "left-down":
        return True

    if state == (27, 1) and action.lower() == "left-up":
        return True

    if state == (27, 1) and action.lower() == "right-up":
        return True

    if state == (27, 1) and action.lower() == "right":
        return True

    if state == (27, 1) and action.lower() == "right-down":
        return True

    if state == (27, 1) and action.lower() == "down":
        return True

    if state == (27, 1) and action.lower() == "left-down":
        return True

    if state == (27, 2) and action.lower() == "up":
        return True

    if state == (27, 2) and action.lower() == "right-up":
        return True

    if state == (27, 2) and action.lower() == "down":
        return True

    if state == (27, 2) and action.lower() == "left-down":
        return True

    if state == (27, 2) and action.lower() == "left":
        return True

    if state == (27, 6) and action.lower() == "up":
        return True

    if state == (27, 6) and action.lower() == "right-down":
        return True

    if state == (27, 6) and action.lower() == "left-down":
        return True

    if state == (27, 8) and action.lower() == "right-up":
        return True

    if state == (27, 8) and action.lower() == "right":
        return True

    if state == (27, 8) and action.lower() == "left-down":
        return True

    if state == (27, 9) and action.lower() == "up":
        return True

    if state == (27, 9) and action.lower() == "left":
        return True

    if state == (27, 11) and action.lower() == "up":
        return True

    if state == (27, 15) and action.lower() == "left-up":
        return True

    if state == (27, 15) and action.lower() == "right-up":
        return True

    if state == (27, 15) and action.lower() == "right":
        return True

    if state == (27, 16) and action.lower() == "up":
        return True

    if state == (27, 16) and action.lower() == "right-up":
        return True

    if state == (27, 16) and action.lower() == "right-down":
        return True

    if state == (27, 16) and action.lower() == "left":
        return True

    if state == (27, 18) and action.lower() == "left-up":
        return True

    if state == (27, 18) and action.lower() == "right-up":
        return True

    if state == (27, 18) and action.lower() == "right":
        return True

    if state == (27, 18) and action.lower() == "left-down":
        return True

    if state == (27, 19) and action.lower() == "up":
        return True

    if state == (27, 19) and action.lower() == "right-up":
        return True

    if state == (27, 19) and action.lower() == "right":
        return True

    if state == (27, 19) and action.lower() == "right-down":
        return True

    if state == (27, 19) and action.lower() == "left":
        return True

    if state == (27, 20) and action.lower() == "left-up":
        return True

    if state == (27, 20) and action.lower() == "up":
        return True

    if state == (27, 20) and action.lower() == "down":
        return True

    if state == (27, 20) and action.lower() == "left":
        return True

    if state == (27, 22) and action.lower() == "down":
        return True

    if state == (27, 26) and action.lower() == "up":
        return True

    if state == (27, 26) and action.lower() == "right-up":
        return True

    if state == (27, 26) and action.lower() == "right":
        return True

    if state == (27, 26) and action.lower() == "down":
        return True

    if state == (27, 27) and action.lower() == "left-up":
        return True

    if state == (27, 27) and action.lower() == "up":
        return True

    if state == (27, 27) and action.lower() == "right-up":
        return True

    if state == (27, 27) and action.lower() == "left-down":
        return True

    if state == (27, 27) and action.lower() == "left":
        return True

    if state == (27, 30) and action.lower() == "right-up":
        return True

    if state == (27, 30) and action.lower() == "right":
        return True

    if state == (27, 30) and action.lower() == "left-down":
        return True

    if state == (27, 31) and action.lower() == "up":
        return True

    if state == (27, 31) and action.lower() == "right":
        return True

    if state == (27, 31) and action.lower() == "left":
        return True

    if state == (27, 32) and action.lower() == "left-up":
        return True

    if state == (27, 32) and action.lower() == "right-down":
        return True

    if state == (27, 32) and action.lower() == "left":
        return True

    if state == (27, 34) and action.lower() == "up":
        return True

    if state == (27, 34) and action.lower() == "right":
        return True

    if state == (27, 34) and action.lower() == "right-down":
        return True

    if state == (27, 34) and action.lower() == "down":
        return True

    if state == (27, 34) and action.lower() == "left-down":
        return True

    if state == (27, 35) and action.lower() == "left-up":
        return True

    if state == (27, 35) and action.lower() == "right-up":
        return True

    if state == (27, 35) and action.lower() == "down":
        return True

    if state == (27, 35) and action.lower() == "left-down":
        return True

    if state == (27, 35) and action.lower() == "left":
        return True

    if state == (27, 37) and action.lower() == "left-up":
        return True

    if state == (27, 37) and action.lower() == "up":
        return True

    if state == (27, 37) and action.lower() == "down":
        return True

    if state == (27, 39) and action.lower() == "up":
        return True

    if state == (27, 39) and action.lower() == "right-up":
        return True

    if state == (27, 41) and action.lower() == "left-up":
        return True

    if state == (27, 41) and action.lower() == "up":
        return True

    if state == (27, 41) and action.lower() == "right":
        return True

    if state == (27, 41) and action.lower() == "right-down":
        return True

    if state == (27, 42) and action.lower() == "left-up":
        return True

    if state == (27, 42) and action.lower() == "right-up":
        return True

    if state == (27, 42) and action.lower() == "right":
        return True

    if state == (27, 42) and action.lower() == "right-down":
        return True

    if state == (27, 42) and action.lower() == "down":
        return True

    if state == (27, 42) and action.lower() == "left":
        return True

    if state == (27, 43) and action.lower() == "up":
        return True

    if state == (27, 43) and action.lower() == "down":
        return True

    if state == (27, 43) and action.lower() == "left-down":
        return True

    if state == (27, 43) and action.lower() == "left":
        return True

    if state == (27, 48) and action.lower() == "left-up":
        return True

    if state == (27, 48) and action.lower() == "up":
        return True

    if state == (27, 48) and action.lower() == "right-down":
        return True

    if state == (27, 48) and action.lower() == "down":
        return True

    if state == (27, 50) and action.lower() == "right-up":
        return True

    if state == (27, 50) and action.lower() == "left-down":
        return True

    if state == (28, 0) and action.lower() == "right-up":
        return True

    if state == (28, 0) and action.lower() == "right":
        return True

    if state == (28, 1) and action.lower() == "up":
        return True

    if state == (28, 1) and action.lower() == "right-up":
        return True

    if state == (28, 1) and action.lower() == "right":
        return True

    if state == (28, 1) and action.lower() == "right-down":
        return True

    if state == (28, 1) and action.lower() == "left":
        return True

    if state == (28, 2) and action.lower() == "left-up":
        return True

    if state == (28, 2) and action.lower() == "up":
        return True

    if state == (28, 2) and action.lower() == "down":
        return True

    if state == (28, 2) and action.lower() == "left":
        return True

    if state == (28, 5) and action.lower() == "right-up":
        return True

    if state == (28, 5) and action.lower() == "left-down":
        return True

    if state == (28, 7) and action.lower() == "left-up":
        return True

    if state == (28, 7) and action.lower() == "right-up":
        return True

    if state == (28, 7) and action.lower() == "right-down":
        return True

    if state == (28, 7) and action.lower() == "down":
        return True

    if state == (28, 13) and action.lower() == "right-down":
        return True

    if state == (28, 17) and action.lower() == "left-up":
        return True

    if state == (28, 17) and action.lower() == "right-up":
        return True

    if state == (28, 17) and action.lower() == "right-down":
        return True

    if state == (28, 17) and action.lower() == "down":
        return True

    if state == (28, 17) and action.lower() == "left-down":
        return True

    if state == (28, 20) and action.lower() == "left-up":
        return True

    if state == (28, 20) and action.lower() == "up":
        return True

    if state == (28, 20) and action.lower() == "right-down":
        return True

    if state == (28, 20) and action.lower() == "down":
        return True

    if state == (28, 22) and action.lower() == "up":
        return True

    if state == (28, 22) and action.lower() == "right-down":
        return True

    if state == (28, 22) and action.lower() == "down":
        return True

    if state == (28, 22) and action.lower() == "left-down":
        return True

    if state == (28, 24) and action.lower() == "right-down":
        return True

    if state == (28, 24) and action.lower() == "left-down":
        return True

    if state == (28, 26) and action.lower() == "up":
        return True

    if state == (28, 26) and action.lower() == "right-up":
        return True

    if state == (28, 26) and action.lower() == "left-down":
        return True

    if state == (28, 29) and action.lower() == "right-up":
        return True

    if state == (28, 29) and action.lower() == "right-down":
        return True

    if state == (28, 29) and action.lower() == "down":
        return True

    if state == (28, 33) and action.lower() == "left-up":
        return True

    if state == (28, 33) and action.lower() == "right-up":
        return True

    if state == (28, 33) and action.lower() == "right":
        return True

    if state == (28, 33) and action.lower() == "down":
        return True

    if state == (28, 34) and action.lower() == "up":
        return True

    if state == (28, 34) and action.lower() == "right-up":
        return True

    if state == (28, 34) and action.lower() == "right":
        return True

    if state == (28, 34) and action.lower() == "left-down":
        return True

    if state == (28, 34) and action.lower() == "left":
        return True

    if state == (28, 35) and action.lower() == "left-up":
        return True

    if state == (28, 35) and action.lower() == "up":
        return True

    if state == (28, 35) and action.lower() == "right-down":
        return True

    if state == (28, 35) and action.lower() == "left":
        return True

    if state == (28, 37) and action.lower() == "up":
        return True

    if state == (28, 37) and action.lower() == "right-down":
        return True

    if state == (28, 37) and action.lower() == "left-down":
        return True

    if state == (28, 42) and action.lower() == "left-up":
        return True

    if state == (28, 42) and action.lower() == "up":
        return True

    if state == (28, 42) and action.lower() == "right-up":
        return True

    if state == (28, 42) and action.lower() == "right":
        return True

    if state == (28, 42) and action.lower() == "right-down":
        return True

    if state == (28, 42) and action.lower() == "down":
        return True

    if state == (28, 43) and action.lower() == "left-up":
        return True

    if state == (28, 43) and action.lower() == "up":
        return True

    if state == (28, 43) and action.lower() == "right-down":
        return True

    if state == (28, 43) and action.lower() == "down":
        return True

    if state == (28, 43) and action.lower() == "left-down":
        return True

    if state == (28, 43) and action.lower() == "left":
        return True

    if state == (28, 45) and action.lower() == "down":
        return True

    if state == (28, 45) and action.lower() == "left-down":
        return True

    if state == (28, 48) and action.lower() == "up":
        return True

    if state == (28, 48) and action.lower() == "right":
        return True

    if state == (28, 48) and action.lower() == "right-down":
        return True

    if state == (28, 48) and action.lower() == "down":
        return True

    if state == (28, 48) and action.lower() == "left-down":
        return True

    if state == (28, 49) and action.lower() == "left-up":
        return True

    if state == (28, 49) and action.lower() == "right-up":
        return True

    if state == (28, 49) and action.lower() == "down":
        return True

    if state == (28, 49) and action.lower() == "left-down":
        return True

    if state == (28, 49) and action.lower() == "left":
        return True

    if state == (29, 2) and action.lower() == "left-up":
        return True

    if state == (29, 2) and action.lower() == "up":
        return True

    if state == (29, 4) and action.lower() == "right-up":
        return True

    if state == (29, 4) and action.lower() == "right-down":
        return True

    if state == (29, 4) and action.lower() == "down":
        return True

    if state == (29, 7) and action.lower() == "up":
        return True

    if state == (29, 7) and action.lower() == "right":
        return True

    if state == (29, 7) and action.lower() == "right-down":
        return True

    if state == (29, 7) and action.lower() == "left-down":
        return True

    if state == (29, 8) and action.lower() == "left-up":
        return True

    if state == (29, 8) and action.lower() == "right":
        return True

    if state == (29, 8) and action.lower() == "down":
        return True

    if state == (29, 8) and action.lower() == "left":
        return True

    if state == (29, 9) and action.lower() == "right":
        return True

    if state == (29, 9) and action.lower() == "left-down":
        return True

    if state == (29, 9) and action.lower() == "left":
        return True

    if state == (29, 10) and action.lower() == "right-down":
        return True

    if state == (29, 10) and action.lower() == "left":
        return True

    if state == (29, 14) and action.lower() == "left-up":
        return True

    if state == (29, 14) and action.lower() == "down":
        return True

    if state == (29, 16) and action.lower() == "right-up":
        return True

    if state == (29, 16) and action.lower() == "right":
        return True

    if state == (29, 16) and action.lower() == "right-down":
        return True

    if state == (29, 16) and action.lower() == "down":
        return True

    if state == (29, 17) and action.lower() == "up":
        return True

    if state == (29, 17) and action.lower() == "right":
        return True

    if state == (29, 17) and action.lower() == "right-down":
        return True

    if state == (29, 17) and action.lower() == "down":
        return True

    if state == (29, 17) and action.lower() == "left-down":
        return True

    if state == (29, 17) and action.lower() == "left":
        return True

    if state == (29, 18) and action.lower() == "left-up":
        return True

    if state == (29, 18) and action.lower() == "down":
        return True

    if state == (29, 18) and action.lower() == "left-down":
        return True

    if state == (29, 18) and action.lower() == "left":
        return True

    if state == (29, 20) and action.lower() == "up":
        return True

    if state == (29, 20) and action.lower() == "right":
        return True

    if state == (29, 20) and action.lower() == "right-down":
        return True

    if state == (29, 20) and action.lower() == "down":
        return True

    if state == (29, 21) and action.lower() == "left-up":
        return True

    if state == (29, 21) and action.lower() == "right-up":
        return True

    if state == (29, 21) and action.lower() == "right":
        return True

    if state == (29, 21) and action.lower() == "down":
        return True

    if state == (29, 21) and action.lower() == "left-down":
        return True

    if state == (29, 21) and action.lower() == "left":
        return True

    if state == (29, 22) and action.lower() == "up":
        return True

    if state == (29, 22) and action.lower() == "right":
        return True

    if state == (29, 22) and action.lower() == "right-down":
        return True

    if state == (29, 22) and action.lower() == "left-down":
        return True

    if state == (29, 22) and action.lower() == "left":
        return True

    if state == (29, 23) and action.lower() == "left-up":
        return True

    if state == (29, 23) and action.lower() == "right-up":
        return True

    if state == (29, 23) and action.lower() == "right-down":
        return True

    if state == (29, 23) and action.lower() == "down":
        return True

    if state == (29, 23) and action.lower() == "left":
        return True

    if state == (29, 25) and action.lower() == "left-up":
        return True

    if state == (29, 25) and action.lower() == "right-up":
        return True

    if state == (29, 25) and action.lower() == "right-down":
        return True

    if state == (29, 25) and action.lower() == "down":
        return True

    if state == (29, 25) and action.lower() == "left-down":
        return True

    if state == (29, 29) and action.lower() == "up":
        return True

    if state == (29, 29) and action.lower() == "right":
        return True

    if state == (29, 29) and action.lower() == "right-down":
        return True

    if state == (29, 29) and action.lower() == "down":
        return True

    if state == (29, 30) and action.lower() == "left-up":
        return True

    if state == (29, 30) and action.lower() == "right":
        return True

    if state == (29, 30) and action.lower() == "right-down":
        return True

    if state == (29, 30) and action.lower() == "down":
        return True

    if state == (29, 30) and action.lower() == "left-down":
        return True

    if state == (29, 30) and action.lower() == "left":
        return True

    if state == (29, 31) and action.lower() == "right-down":
        return True

    if state == (29, 31) and action.lower() == "down":
        return True

    if state == (29, 31) and action.lower() == "left-down":
        return True

    if state == (29, 31) and action.lower() == "left":
        return True

    if state == (29, 33) and action.lower() == "up":
        return True

    if state == (29, 33) and action.lower() == "right-up":
        return True

    if state == (29, 33) and action.lower() == "down":
        return True

    if state == (29, 33) and action.lower() == "left-down":
        return True

    if state == (29, 36) and action.lower() == "left-up":
        return True

    if state == (29, 36) and action.lower() == "right-up":
        return True

    if state == (29, 36) and action.lower() == "right-down":
        return True

    if state == (29, 38) and action.lower() == "left-up":
        return True

    if state == (29, 38) and action.lower() == "right":
        return True

    if state == (29, 38) and action.lower() == "left-down":
        return True

    if state == (29, 39) and action.lower() == "right-down":
        return True

    if state == (29, 39) and action.lower() == "left":
        return True

    if state == (29, 42) and action.lower() == "up":
        return True

    if state == (29, 42) and action.lower() == "right-up":
        return True

    if state == (29, 42) and action.lower() == "right":
        return True

    if state == (29, 42) and action.lower() == "right-down":
        return True

    if state == (29, 43) and action.lower() == "left-up":
        return True

    if state == (29, 43) and action.lower() == "up":
        return True

    if state == (29, 43) and action.lower() == "right":
        return True

    if state == (29, 43) and action.lower() == "right-down":
        return True

    if state == (29, 43) and action.lower() == "down":
        return True

    if state == (29, 43) and action.lower() == "left":
        return True

    if state == (29, 44) and action.lower() == "left-up":
        return True

    if state == (29, 44) and action.lower() == "right-up":
        return True

    if state == (29, 44) and action.lower() == "right":
        return True

    if state == (29, 44) and action.lower() == "right-down":
        return True

    if state == (29, 44) and action.lower() == "down":
        return True

    if state == (29, 44) and action.lower() == "left-down":
        return True

    if state == (29, 44) and action.lower() == "left":
        return True

    if state == (29, 45) and action.lower() == "up":
        return True

    if state == (29, 45) and action.lower() == "right-down":
        return True

    if state == (29, 45) and action.lower() == "down":
        return True

    if state == (29, 45) and action.lower() == "left-down":
        return True

    if state == (29, 45) and action.lower() == "left":
        return True

    if state == (29, 47) and action.lower() == "right-up":
        return True

    if state == (29, 47) and action.lower() == "right":
        return True

    if state == (29, 47) and action.lower() == "down":
        return True

    if state == (29, 47) and action.lower() == "left-down":
        return True

    if state == (29, 48) and action.lower() == "up":
        return True

    if state == (29, 48) and action.lower() == "right-up":
        return True

    if state == (29, 48) and action.lower() == "right":
        return True

    if state == (29, 48) and action.lower() == "right-down":
        return True

    if state == (29, 48) and action.lower() == "left-down":
        return True

    if state == (29, 48) and action.lower() == "left":
        return True

    if state == (29, 49) and action.lower() == "left-up":
        return True

    if state == (29, 49) and action.lower() == "up":
        return True

    if state == (29, 49) and action.lower() == "right-down":
        return True

    if state == (29, 49) and action.lower() == "down":
        return True

    if state == (29, 49) and action.lower() == "left":
        return True

    if state == (30, 0) and action.lower() == "right-down":
        return True

    if state == (30, 0) and action.lower() == "down":
        return True

    if state == (30, 4) and action.lower() == "up":
        return True

    if state == (30, 4) and action.lower() == "right":
        return True

    if state == (30, 5) and action.lower() == "left-up":
        return True

    if state == (30, 5) and action.lower() == "right":
        return True

    if state == (30, 5) and action.lower() == "right-down":
        return True

    if state == (30, 5) and action.lower() == "left":
        return True

    if state == (30, 6) and action.lower() == "right-up":
        return True

    if state == (30, 6) and action.lower() == "right-down":
        return True

    if state == (30, 6) and action.lower() == "down":
        return True

    if state == (30, 6) and action.lower() == "left":
        return True

    if state == (30, 8) and action.lower() == "left-up":
        return True

    if state == (30, 8) and action.lower() == "up":
        return True

    if state == (30, 8) and action.lower() == "right-up":
        return True

    if state == (30, 8) and action.lower() == "left-down":
        return True

    if state == (30, 11) and action.lower() == "left-up":
        return True

    if state == (30, 11) and action.lower() == "right-down":
        return True

    if state == (30, 14) and action.lower() == "up":
        return True

    if state == (30, 14) and action.lower() == "down":
        return True

    if state == (30, 16) and action.lower() == "up":
        return True

    if state == (30, 16) and action.lower() == "right-up":
        return True

    if state == (30, 16) and action.lower() == "right":
        return True

    if state == (30, 16) and action.lower() == "right-down":
        return True

    if state == (30, 17) and action.lower() == "left-up":
        return True

    if state == (30, 17) and action.lower() == "up":
        return True

    if state == (30, 17) and action.lower() == "right-up":
        return True

    if state == (30, 17) and action.lower() == "right":
        return True

    if state == (30, 17) and action.lower() == "right-down":
        return True

    if state == (30, 17) and action.lower() == "down":
        return True

    if state == (30, 17) and action.lower() == "left":
        return True

    if state == (30, 18) and action.lower() == "left-up":
        return True

    if state == (30, 18) and action.lower() == "up":
        return True

    if state == (30, 18) and action.lower() == "down":
        return True

    if state == (30, 18) and action.lower() == "left-down":
        return True

    if state == (30, 18) and action.lower() == "left":
        return True

    if state == (30, 20) and action.lower() == "up":
        return True

    if state == (30, 20) and action.lower() == "right-up":
        return True

    if state == (30, 20) and action.lower() == "right":
        return True

    if state == (30, 21) and action.lower() == "left-up":
        return True

    if state == (30, 21) and action.lower() == "up":
        return True

    if state == (30, 21) and action.lower() == "right-up":
        return True

    if state == (30, 21) and action.lower() == "right-down":
        return True

    if state == (30, 21) and action.lower() == "left":
        return True

    if state == (30, 23) and action.lower() == "left-up":
        return True

    if state == (30, 23) and action.lower() == "up":
        return True

    if state == (30, 23) and action.lower() == "right":
        return True

    if state == (30, 23) and action.lower() == "left-down":
        return True

    if state == (30, 24) and action.lower() == "left-up":
        return True

    if state == (30, 24) and action.lower() == "right-up":
        return True

    if state == (30, 24) and action.lower() == "right":
        return True

    if state == (30, 24) and action.lower() == "right-down":
        return True

    if state == (30, 24) and action.lower() == "left":
        return True

    if state == (30, 25) and action.lower() == "up":
        return True

    if state == (30, 25) and action.lower() == "right":
        return True

    if state == (30, 25) and action.lower() == "right-down":
        return True

    if state == (30, 25) and action.lower() == "down":
        return True

    if state == (30, 25) and action.lower() == "left":
        return True

    if state == (30, 26) and action.lower() == "left-up":
        return True

    if state == (30, 26) and action.lower() == "right-down":
        return True

    if state == (30, 26) and action.lower() == "down":
        return True

    if state == (30, 26) and action.lower() == "left-down":
        return True

    if state == (30, 26) and action.lower() == "left":
        return True

    if state == (30, 29) and action.lower() == "up":
        return True

    if state == (30, 29) and action.lower() == "right-up":
        return True

    if state == (30, 29) and action.lower() == "right":
        return True

    if state == (30, 29) and action.lower() == "right-down":
        return True

    if state == (30, 29) and action.lower() == "left-down":
        return True

    if state == (30, 30) and action.lower() == "left-up":
        return True

    if state == (30, 30) and action.lower() == "up":
        return True

    if state == (30, 30) and action.lower() == "right-up":
        return True

    if state == (30, 30) and action.lower() == "right":
        return True

    if state == (30, 30) and action.lower() == "down":
        return True

    if state == (30, 30) and action.lower() == "left":
        return True

    if state == (30, 31) and action.lower() == "left-up":
        return True

    if state == (30, 31) and action.lower() == "up":
        return True

    if state == (30, 31) and action.lower() == "right":
        return True

    if state == (30, 31) and action.lower() == "left-down":
        return True

    if state == (30, 31) and action.lower() == "left":
        return True

    if state == (30, 32) and action.lower() == "left-up":
        return True

    if state == (30, 32) and action.lower() == "right-up":
        return True

    if state == (30, 32) and action.lower() == "right":
        return True

    if state == (30, 32) and action.lower() == "right-down":
        return True

    if state == (30, 32) and action.lower() == "left":
        return True

    if state == (30, 33) and action.lower() == "up":
        return True

    if state == (30, 33) and action.lower() == "right-down":
        return True

    if state == (30, 33) and action.lower() == "down":
        return True

    if state == (30, 33) and action.lower() == "left":
        return True

    if state == (30, 37) and action.lower() == "left-up":
        return True

    if state == (30, 37) and action.lower() == "right-up":
        return True

    if state == (30, 37) and action.lower() == "down":
        return True

    if state == (30, 37) and action.lower() == "left-down":
        return True

    if state == (30, 40) and action.lower() == "left-up":
        return True

    if state == (30, 40) and action.lower() == "right-down":
        return True

    if state == (30, 40) and action.lower() == "down":
        return True

    if state == (30, 43) and action.lower() == "left-up":
        return True

    if state == (30, 43) and action.lower() == "up":
        return True

    if state == (30, 43) and action.lower() == "right-up":
        return True

    if state == (30, 43) and action.lower() == "right":
        return True

    if state == (30, 43) and action.lower() == "left-down":
        return True

    if state == (30, 44) and action.lower() == "left-up":
        return True

    if state == (30, 44) and action.lower() == "up":
        return True

    if state == (30, 44) and action.lower() == "right-up":
        return True

    if state == (30, 44) and action.lower() == "right":
        return True

    if state == (30, 44) and action.lower() == "right-down":
        return True

    if state == (30, 44) and action.lower() == "left":
        return True

    if state == (30, 45) and action.lower() == "left-up":
        return True

    if state == (30, 45) and action.lower() == "up":
        return True

    if state == (30, 45) and action.lower() == "right":
        return True

    if state == (30, 45) and action.lower() == "down":
        return True

    if state == (30, 45) and action.lower() == "left":
        return True

    if state == (30, 46) and action.lower() == "left-up":
        return True

    if state == (30, 46) and action.lower() == "right-up":
        return True

    if state == (30, 46) and action.lower() == "right":
        return True

    if state == (30, 46) and action.lower() == "right-down":
        return True

    if state == (30, 46) and action.lower() == "left-down":
        return True

    if state == (30, 46) and action.lower() == "left":
        return True

    if state == (30, 47) and action.lower() == "up":
        return True

    if state == (30, 47) and action.lower() == "right-up":
        return True

    if state == (30, 47) and action.lower() == "down":
        return True

    if state == (30, 47) and action.lower() == "left":
        return True

    if state == (30, 49) and action.lower() == "left-up":
        return True

    if state == (30, 49) and action.lower() == "up":
        return True

    if state == (30, 49) and action.lower() == "right":
        return True

    if state == (30, 50) and action.lower() == "left-up":
        return True

    if state == (30, 50) and action.lower() == "right":
        return True

    if state == (30, 50) and action.lower() == "right-down":
        return True

    if state == (30, 50) and action.lower() == "left":
        return True

    if state == (30, 51) and action.lower() == "down":
        return True

    if state == (30, 51) and action.lower() == "left":
        return True

    if state == (31, 0) and action.lower() == "up":
        return True

    if state == (31, 0) and action.lower() == "right":
        return True

    if state == (31, 0) and action.lower() == "right-down":
        return True

    if state == (31, 0) and action.lower() == "down":
        return True

    if state == (31, 1) and action.lower() == "left-up":
        return True

    if state == (31, 1) and action.lower() == "right":
        return True

    if state == (31, 1) and action.lower() == "down":
        return True

    if state == (31, 1) and action.lower() == "left-down":
        return True

    if state == (31, 1) and action.lower() == "left":
        return True

    if state == (31, 2) and action.lower() == "right-down":
        return True

    if state == (31, 2) and action.lower() == "left-down":
        return True

    if state == (31, 2) and action.lower() == "left":
        return True

    if state == (31, 6) and action.lower() == "left-up":
        return True

    if state == (31, 6) and action.lower() == "up":
        return True

    if state == (31, 6) and action.lower() == "right":
        return True

    if state == (31, 6) and action.lower() == "right-down":
        return True

    if state == (31, 6) and action.lower() == "left-down":
        return True

    if state == (31, 7) and action.lower() == "left-up":
        return True

    if state == (31, 7) and action.lower() == "right-up":
        return True

    if state == (31, 7) and action.lower() == "down":
        return True

    if state == (31, 7) and action.lower() == "left":
        return True

    if state == (31, 12) and action.lower() == "left-up":
        return True

    if state == (31, 14) and action.lower() == "up":
        return True

    if state == (31, 14) and action.lower() == "right-down":
        return True

    if state == (31, 14) and action.lower() == "down":
        return True

    if state == (31, 17) and action.lower() == "left-up":
        return True

    if state == (31, 17) and action.lower() == "up":
        return True

    if state == (31, 17) and action.lower() == "right-up":
        return True

    if state == (31, 17) and action.lower() == "right":
        return True

    if state == (31, 17) and action.lower() == "right-down":
        return True

    if state == (31, 17) and action.lower() == "down":
        return True

    if state == (31, 17) and action.lower() == "left-down":
        return True

    if state == (31, 18) and action.lower() == "left-up":
        return True

    if state == (31, 18) and action.lower() == "up":
        return True

    if state == (31, 18) and action.lower() == "right-down":
        return True

    if state == (31, 18) and action.lower() == "down":
        return True

    if state == (31, 18) and action.lower() == "left-down":
        return True

    if state == (31, 18) and action.lower() == "left":
        return True

    if state == (31, 22) and action.lower() == "left-up":
        return True

    if state == (31, 22) and action.lower() == "right-up":
        return True

    if state == (31, 22) and action.lower() == "right-down":
        return True

    if state == (31, 22) and action.lower() == "left-down":
        return True

    if state == (31, 25) and action.lower() == "left-up":
        return True

    if state == (31, 25) and action.lower() == "up":
        return True

    if state == (31, 25) and action.lower() == "right-up":
        return True

    if state == (31, 25) and action.lower() == "right":
        return True

    if state == (31, 25) and action.lower() == "right-down":
        return True

    if state == (31, 25) and action.lower() == "left-down":
        return True

    if state == (31, 26) and action.lower() == "left-up":
        return True

    if state == (31, 26) and action.lower() == "up":
        return True

    if state == (31, 26) and action.lower() == "right":
        return True

    if state == (31, 26) and action.lower() == "down":
        return True

    if state == (31, 26) and action.lower() == "left":
        return True

    if state == (31, 27) and action.lower() == "left-up":
        return True

    if state == (31, 27) and action.lower() == "right":
        return True

    if state == (31, 27) and action.lower() == "left-down":
        return True

    if state == (31, 27) and action.lower() == "left":
        return True

    if state == (31, 28) and action.lower() == "right-up":
        return True

    if state == (31, 28) and action.lower() == "left":
        return True

    if state == (31, 30) and action.lower() == "left-up":
        return True

    if state == (31, 30) and action.lower() == "up":
        return True

    if state == (31, 30) and action.lower() == "right-up":
        return True

    if state == (31, 30) and action.lower() == "right-down":
        return True

    if state == (31, 33) and action.lower() == "left-up":
        return True

    if state == (31, 33) and action.lower() == "up":
        return True

    if state == (31, 33) and action.lower() == "right":
        return True

    if state == (31, 33) and action.lower() == "right-down":
        return True

    if state == (31, 33) and action.lower() == "left-down":
        return True

    if state == (31, 34) and action.lower() == "left-up":
        return True

    if state == (31, 34) and action.lower() == "right-down":
        return True

    if state == (31, 34) and action.lower() == "down":
        return True

    if state == (31, 34) and action.lower() == "left":
        return True

    if state == (31, 36) and action.lower() == "right-up":
        return True

    if state == (31, 36) and action.lower() == "right":
        return True

    if state == (31, 36) and action.lower() == "down":
        return True

    if state == (31, 36) and action.lower() == "left-down":
        return True

    if state == (31, 37) and action.lower() == "up":
        return True

    if state == (31, 37) and action.lower() == "right-down":
        return True

    if state == (31, 37) and action.lower() == "left-down":
        return True

    if state == (31, 37) and action.lower() == "left":
        return True

    if state == (31, 40) and action.lower() == "up":
        return True

    if state == (31, 40) and action.lower() == "right":
        return True

    if state == (31, 41) and action.lower() == "left-up":
        return True

    if state == (31, 41) and action.lower() == "right":
        return True

    if state == (31, 41) and action.lower() == "left":
        return True

    if state == (31, 42) and action.lower() == "right-up":
        return True

    if state == (31, 42) and action.lower() == "right-down":
        return True

    if state == (31, 42) and action.lower() == "left":
        return True

    if state == (31, 45) and action.lower() == "left-up":
        return True

    if state == (31, 45) and action.lower() == "up":
        return True

    if state == (31, 45) and action.lower() == "right-up":
        return True

    if state == (31, 45) and action.lower() == "right-down":
        return True

    if state == (31, 45) and action.lower() == "down":
        return True

    if state == (31, 45) and action.lower() == "left-down":
        return True

    if state == (31, 47) and action.lower() == "left-up":
        return True

    if state == (31, 47) and action.lower() == "up":
        return True

    if state == (31, 47) and action.lower() == "right-down":
        return True

    if state == (31, 47) and action.lower() == "down":
        return True

    if state == (31, 47) and action.lower() == "left-down":
        return True

    if state == (31, 51) and action.lower() == "left-up":
        return True

    if state == (31, 51) and action.lower() == "up":
        return True

    if state == (31, 51) and action.lower() == "down":
        return True

    if state == (31, 51) and action.lower() == "left-down":
        return True

    if state == (32, 0) and action.lower() == "up":
        return True

    if state == (32, 0) and action.lower() == "right-up":
        return True

    if state == (32, 0) and action.lower() == "right":
        return True

    if state == (32, 0) and action.lower() == "right-down":
        return True

    if state == (32, 1) and action.lower() == "left-up":
        return True

    if state == (32, 1) and action.lower() == "up":
        return True

    if state == (32, 1) and action.lower() == "right-up":
        return True

    if state == (32, 1) and action.lower() == "down":
        return True

    if state == (32, 1) and action.lower() == "left":
        return True

    if state == (32, 3) and action.lower() == "left-up":
        return True

    if state == (32, 3) and action.lower() == "down":
        return True

    if state == (32, 5) and action.lower() == "right-up":
        return True

    if state == (32, 7) and action.lower() == "left-up":
        return True

    if state == (32, 7) and action.lower() == "up":
        return True

    if state == (32, 7) and action.lower() == "down":
        return True

    if state == (32, 14) and action.lower() == "up":
        return True

    if state == (32, 14) and action.lower() == "right":
        return True

    if state == (32, 14) and action.lower() == "right-down":
        return True

    if state == (32, 14) and action.lower() == "left-down":
        return True

    if state == (32, 15) and action.lower() == "left-up":
        return True

    if state == (32, 15) and action.lower() == "right":
        return True

    if state == (32, 15) and action.lower() == "down":
        return True

    if state == (32, 15) and action.lower() == "left":
        return True

    if state == (32, 16) and action.lower() == "right-up":
        return True

    if state == (32, 16) and action.lower() == "right":
        return True

    if state == (32, 16) and action.lower() == "right-down":
        return True

    if state == (32, 16) and action.lower() == "left-down":
        return True

    if state == (32, 16) and action.lower() == "left":
        return True

    if state == (32, 17) and action.lower() == "up":
        return True

    if state == (32, 17) and action.lower() == "right-up":
        return True

    if state == (32, 17) and action.lower() == "right":
        return True

    if state == (32, 17) and action.lower() == "down":
        return True

    if state == (32, 17) and action.lower() == "left":
        return True

    if state == (32, 18) and action.lower() == "left-up":
        return True

    if state == (32, 18) and action.lower() == "up":
        return True

    if state == (32, 18) and action.lower() == "right":
        return True

    if state == (32, 18) and action.lower() == "left-down":
        return True

    if state == (32, 18) and action.lower() == "left":
        return True

    if state == (32, 19) and action.lower() == "left-up":
        return True

    if state == (32, 19) and action.lower() == "right":
        return True

    if state == (32, 19) and action.lower() == "right-down":
        return True

    if state == (32, 19) and action.lower() == "left":
        return True

    if state == (32, 20) and action.lower() == "right":
        return True

    if state == (32, 20) and action.lower() == "right-down":
        return True

    if state == (32, 20) and action.lower() == "down":
        return True

    if state == (32, 20) and action.lower() == "left":
        return True

    if state == (32, 21) and action.lower() == "right-up":
        return True

    if state == (32, 21) and action.lower() == "down":
        return True

    if state == (32, 21) and action.lower() == "left-down":
        return True

    if state == (32, 21) and action.lower() == "left":
        return True

    if state == (32, 23) and action.lower() == "left-up":
        return True

    if state == (32, 23) and action.lower() == "right":
        return True

    if state == (32, 23) and action.lower() == "right-down":
        return True

    if state == (32, 23) and action.lower() == "down":
        return True

    if state == (32, 24) and action.lower() == "right-up":
        return True

    if state == (32, 24) and action.lower() == "right-down":
        return True

    if state == (32, 24) and action.lower() == "down":
        return True

    if state == (32, 24) and action.lower() == "left-down":
        return True

    if state == (32, 24) and action.lower() == "left":
        return True

    if state == (32, 26) and action.lower() == "left-up":
        return True

    if state == (32, 26) and action.lower() == "up":
        return True

    if state == (32, 26) and action.lower() == "right-up":
        return True

    if state == (32, 26) and action.lower() == "right-down":
        return True

    if state == (32, 26) and action.lower() == "down":
        return True

    if state == (32, 26) and action.lower() == "left-down":
        return True

    if state == (32, 31) and action.lower() == "left-up":
        return True

    if state == (32, 31) and action.lower() == "right":
        return True

    if state == (32, 32) and action.lower() == "right-up":
        return True

    if state == (32, 32) and action.lower() == "right-down":
        return True

    if state == (32, 32) and action.lower() == "left":
        return True

    if state == (32, 34) and action.lower() == "left-up":
        return True

    if state == (32, 34) and action.lower() == "up":
        return True

    if state == (32, 34) and action.lower() == "right":
        return True

    if state == (32, 34) and action.lower() == "right-down":
        return True

    if state == (32, 34) and action.lower() == "left-down":
        return True

    if state == (32, 35) and action.lower() == "left-up":
        return True

    if state == (32, 35) and action.lower() == "right-up":
        return True

    if state == (32, 35) and action.lower() == "right":
        return True

    if state == (32, 35) and action.lower() == "right-down":
        return True

    if state == (32, 35) and action.lower() == "down":
        return True

    if state == (32, 35) and action.lower() == "left":
        return True

    if state == (32, 36) and action.lower() == "up":
        return True

    if state == (32, 36) and action.lower() == "right-up":
        return True

    if state == (32, 36) and action.lower() == "down":
        return True

    if state == (32, 36) and action.lower() == "left-down":
        return True

    if state == (32, 36) and action.lower() == "left":
        return True

    if state == (32, 38) and action.lower() == "left-up":
        return True

    if state == (32, 38) and action.lower() == "down":
        return True

    if state == (32, 43) and action.lower() == "left-up":
        return True

    if state == (32, 43) and action.lower() == "right":
        return True

    if state == (32, 43) and action.lower() == "right-down":
        return True

    if state == (32, 43) and action.lower() == "down":
        return True

    if state == (32, 44) and action.lower() == "right-up":
        return True

    if state == (32, 44) and action.lower() == "right":
        return True

    if state == (32, 44) and action.lower() == "right-down":
        return True

    if state == (32, 44) and action.lower() == "down":
        return True

    if state == (32, 44) and action.lower() == "left-down":
        return True

    if state == (32, 44) and action.lower() == "left":
        return True

    if state == (32, 45) and action.lower() == "up":
        return True

    if state == (32, 45) and action.lower() == "right":
        return True

    if state == (32, 45) and action.lower() == "down":
        return True

    if state == (32, 45) and action.lower() == "left-down":
        return True

    if state == (32, 45) and action.lower() == "left":
        return True

    if state == (32, 46) and action.lower() == "left-up":
        return True

    if state == (32, 46) and action.lower() == "right-up":
        return True

    if state == (32, 46) and action.lower() == "right":
        return True

    if state == (32, 46) and action.lower() == "right-down":
        return True

    if state == (32, 46) and action.lower() == "left-down":
        return True

    if state == (32, 46) and action.lower() == "left":
        return True

    if state == (32, 47) and action.lower() == "up":
        return True

    if state == (32, 47) and action.lower() == "right":
        return True

    if state == (32, 47) and action.lower() == "right-down":
        return True

    if state == (32, 47) and action.lower() == "down":
        return True

    if state == (32, 47) and action.lower() == "left":
        return True

    if state == (32, 48) and action.lower() == "left-up":
        return True

    if state == (32, 48) and action.lower() == "right":
        return True

    if state == (32, 48) and action.lower() == "right-down":
        return True

    if state == (32, 48) and action.lower() == "down":
        return True

    if state == (32, 48) and action.lower() == "left-down":
        return True

    if state == (32, 48) and action.lower() == "left":
        return True

    if state == (32, 49) and action.lower() == "right":
        return True

    if state == (32, 49) and action.lower() == "down":
        return True

    if state == (32, 49) and action.lower() == "left-down":
        return True

    if state == (32, 49) and action.lower() == "left":
        return True

    if state == (32, 50) and action.lower() == "right-up":
        return True

    if state == (32, 50) and action.lower() == "right":
        return True

    if state == (32, 50) and action.lower() == "left-down":
        return True

    if state == (32, 50) and action.lower() == "left":
        return True

    if state == (32, 51) and action.lower() == "up":
        return True

    if state == (32, 51) and action.lower() == "left":
        return True

    if state == (33, 1) and action.lower() == "left-up":
        return True

    if state == (33, 1) and action.lower() == "up":
        return True

    if state == (33, 1) and action.lower() == "right-down":
        return True

    if state == (33, 3) and action.lower() == "up":
        return True

    if state == (33, 3) and action.lower() == "right-down":
        return True

    if state == (33, 3) and action.lower() == "down":
        return True

    if state == (33, 3) and action.lower() == "left-down":
        return True

    if state == (33, 7) and action.lower() == "up":
        return True

    if state == (33, 7) and action.lower() == "down":
        return True

    if state == (33, 13) and action.lower() == "right-up":
        return True

    if state == (33, 15) and action.lower() == "left-up":
        return True

    if state == (33, 15) and action.lower() == "up":
        return True

    if state == (33, 15) and action.lower() == "right-up":
        return True

    if state == (33, 15) and action.lower() == "right-down":
        return True

    if state == (33, 15) and action.lower() == "down":
        return True

    if state == (33, 17) and action.lower() == "left-up":
        return True

    if state == (33, 17) and action.lower() == "up":
        return True

    if state == (33, 17) and action.lower() == "right-up":
        return True

    if state == (33, 17) and action.lower() == "left-down":
        return True

    if state == (33, 20) and action.lower() == "left-up":
        return True

    if state == (33, 20) and action.lower() == "up":
        return True

    if state == (33, 20) and action.lower() == "right-up":
        return True

    if state == (33, 20) and action.lower() == "right":
        return True

    if state == (33, 21) and action.lower() == "left-up":
        return True

    if state == (33, 21) and action.lower() == "up":
        return True

    if state == (33, 21) and action.lower() == "right-down":
        return True

    if state == (33, 21) and action.lower() == "left":
        return True

    if state == (33, 23) and action.lower() == "up":
        return True

    if state == (33, 23) and action.lower() == "right-up":
        return True

    if state == (33, 23) and action.lower() == "right":
        return True

    if state == (33, 23) and action.lower() == "right-down":
        return True

    if state == (33, 23) and action.lower() == "left-down":
        return True

    if state == (33, 24) and action.lower() == "left-up":
        return True

    if state == (33, 24) and action.lower() == "up":
        return True

    if state == (33, 24) and action.lower() == "right":
        return True

    if state == (33, 24) and action.lower() == "down":
        return True

    if state == (33, 24) and action.lower() == "left":
        return True

    if state == (33, 25) and action.lower() == "left-up":
        return True

    if state == (33, 25) and action.lower() == "right-up":
        return True

    if state == (33, 25) and action.lower() == "right":
        return True

    if state == (33, 25) and action.lower() == "left-down":
        return True

    if state == (33, 25) and action.lower() == "left":
        return True

    if state == (33, 26) and action.lower() == "up":
        return True

    if state == (33, 26) and action.lower() == "right":
        return True

    if state == (33, 26) and action.lower() == "right-down":
        return True

    if state == (33, 26) and action.lower() == "left":
        return True

    if state == (33, 27) and action.lower() == "left-up":
        return True

    if state == (33, 27) and action.lower() == "right-down":
        return True

    if state == (33, 27) and action.lower() == "down":
        return True

    if state == (33, 27) and action.lower() == "left":
        return True

    if state == (33, 33) and action.lower() == "left-up":
        return True

    if state == (33, 33) and action.lower() == "right-up":
        return True

    if state == (33, 33) and action.lower() == "right-down":
        return True

    if state == (33, 35) and action.lower() == "left-up":
        return True

    if state == (33, 35) and action.lower() == "up":
        return True

    if state == (33, 35) and action.lower() == "right-up":
        return True

    if state == (33, 35) and action.lower() == "right":
        return True

    if state == (33, 35) and action.lower() == "right-down":
        return True

    if state == (33, 35) and action.lower() == "left-down":
        return True

    if state == (33, 36) and action.lower() == "left-up":
        return True

    if state == (33, 36) and action.lower() == "up":
        return True

    if state == (33, 36) and action.lower() == "right-down":
        return True

    if state == (33, 36) and action.lower() == "down":
        return True

    if state == (33, 36) and action.lower() == "left":
        return True

    if state == (33, 38) and action.lower() == "up":
        return True

    if state == (33, 38) and action.lower() == "right-down":
        return True

    if state == (33, 38) and action.lower() == "left-down":
        return True

    if state == (33, 40) and action.lower() == "right":
        return True

    if state == (33, 40) and action.lower() == "down":
        return True

    if state == (33, 40) and action.lower() == "left-down":
        return True

    if state == (33, 41) and action.lower() == "left-down":
        return True

    if state == (33, 41) and action.lower() == "left":
        return True

    if state == (33, 43) and action.lower() == "up":
        return True

    if state == (33, 43) and action.lower() == "right-up":
        return True

    if state == (33, 43) and action.lower() == "right":
        return True

    if state == (33, 43) and action.lower() == "right-down":
        return True

    if state == (33, 43) and action.lower() == "down":
        return True

    if state == (33, 44) and action.lower() == "left-up":
        return True

    if state == (33, 44) and action.lower() == "up":
        return True

    if state == (33, 44) and action.lower() == "right-up":
        return True

    if state == (33, 44) and action.lower() == "right":
        return True

    if state == (33, 44) and action.lower() == "down":
        return True

    if state == (33, 44) and action.lower() == "left-down":
        return True

    if state == (33, 44) and action.lower() == "left":
        return True

    if state == (33, 45) and action.lower() == "left-up":
        return True

    if state == (33, 45) and action.lower() == "up":
        return True

    if state == (33, 45) and action.lower() == "right-up":
        return True

    if state == (33, 45) and action.lower() == "left-down":
        return True

    if state == (33, 45) and action.lower() == "left":
        return True

    if state == (33, 47) and action.lower() == "left-up":
        return True

    if state == (33, 47) and action.lower() == "up":
        return True

    if state == (33, 47) and action.lower() == "right-up":
        return True

    if state == (33, 47) and action.lower() == "right":
        return True

    if state == (33, 47) and action.lower() == "right-down":
        return True

    if state == (33, 47) and action.lower() == "down":
        return True

    if state == (33, 48) and action.lower() == "left-up":
        return True

    if state == (33, 48) and action.lower() == "up":
        return True

    if state == (33, 48) and action.lower() == "right-up":
        return True

    if state == (33, 48) and action.lower() == "right":
        return True

    if state == (33, 48) and action.lower() == "down":
        return True

    if state == (33, 48) and action.lower() == "left-down":
        return True

    if state == (33, 48) and action.lower() == "left":
        return True

    if state == (33, 49) and action.lower() == "left-up":
        return True

    if state == (33, 49) and action.lower() == "up":
        return True

    if state == (33, 49) and action.lower() == "right-up":
        return True

    if state == (33, 49) and action.lower() == "right-down":
        return True

    if state == (33, 49) and action.lower() == "left-down":
        return True

    if state == (33, 49) and action.lower() == "left":
        return True

    if state == (34, 2) and action.lower() == "left-up":
        return True

    if state == (34, 2) and action.lower() == "right-up":
        return True

    if state == (34, 2) and action.lower() == "right":
        return True

    if state == (34, 2) and action.lower() == "down":
        return True

    if state == (34, 2) and action.lower() == "left-down":
        return True

    if state == (34, 3) and action.lower() == "up":
        return True

    if state == (34, 3) and action.lower() == "right":
        return True

    if state == (34, 3) and action.lower() == "left-down":
        return True

    if state == (34, 3) and action.lower() == "left":
        return True

    if state == (34, 4) and action.lower() == "left-up":
        return True

    if state == (34, 4) and action.lower() == "right":
        return True

    if state == (34, 4) and action.lower() == "left":
        return True

    if state == (34, 5) and action.lower() == "right-down":
        return True

    if state == (34, 5) and action.lower() == "left":
        return True

    if state == (34, 7) and action.lower() == "up":
        return True

    if state == (34, 7) and action.lower() == "right-down":
        return True

    if state == (34, 7) and action.lower() == "left-down":
        return True

    if state == (34, 10) and action.lower() == "right-down":
        return True

    if state == (34, 10) and action.lower() == "down":
        return True

    if state == (34, 15) and action.lower() == "up":
        return True

    if state == (34, 15) and action.lower() == "right":
        return True

    if state == (34, 15) and action.lower() == "right-down":
        return True

    if state == (34, 16) and action.lower() == "left-up":
        return True

    if state == (34, 16) and action.lower() == "right-up":
        return True

    if state == (34, 16) and action.lower() == "right-down":
        return True

    if state == (34, 16) and action.lower() == "down":
        return True

    if state == (34, 16) and action.lower() == "left":
        return True

    if state == (34, 22) and action.lower() == "left-up":
        return True

    if state == (34, 22) and action.lower() == "right-up":
        return True

    if state == (34, 22) and action.lower() == "down":
        return True

    if state == (34, 22) and action.lower() == "left-down":
        return True

    if state == (34, 24) and action.lower() == "left-up":
        return True

    if state == (34, 24) and action.lower() == "up":
        return True

    if state == (34, 24) and action.lower() == "right-up":
        return True

    if state == (34, 24) and action.lower() == "right-down":
        return True

    if state == (34, 27) and action.lower() == "left-up":
        return True

    if state == (34, 27) and action.lower() == "up":
        return True

    if state == (34, 27) and action.lower() == "right":
        return True

    if state == (34, 27) and action.lower() == "right-down":
        return True

    if state == (34, 27) and action.lower() == "down":
        return True

    if state == (34, 28) and action.lower() == "left-up":
        return True

    if state == (34, 28) and action.lower() == "right-down":
        return True

    if state == (34, 28) and action.lower() == "down":
        return True

    if state == (34, 28) and action.lower() == "left-down":
        return True

    if state == (34, 28) and action.lower() == "left":
        return True

    if state == (34, 34) and action.lower() == "left-up":
        return True

    if state == (34, 34) and action.lower() == "right-up":
        return True

    if state == (34, 34) and action.lower() == "left-down":
        return True

    if state == (34, 36) and action.lower() == "left-up":
        return True

    if state == (34, 36) and action.lower() == "up":
        return True

    if state == (34, 36) and action.lower() == "right":
        return True

    if state == (34, 36) and action.lower() == "down":
        return True

    if state == (34, 37) and action.lower() == "left-up":
        return True

    if state == (34, 37) and action.lower() == "right-up":
        return True

    if state == (34, 37) and action.lower() == "right-down":
        return True

    if state == (34, 37) and action.lower() == "left-down":
        return True

    if state == (34, 37) and action.lower() == "left":
        return True

    if state == (34, 39) and action.lower() == "left-up":
        return True

    if state == (34, 39) and action.lower() == "right-up":
        return True

    if state == (34, 39) and action.lower() == "right":
        return True

    if state == (34, 39) and action.lower() == "right-down":
        return True

    if state == (34, 39) and action.lower() == "down":
        return True

    if state == (34, 39) and action.lower() == "left-down":
        return True

    if state == (34, 40) and action.lower() == "up":
        return True

    if state == (34, 40) and action.lower() == "right-up":
        return True

    if state == (34, 40) and action.lower() == "down":
        return True

    if state == (34, 40) and action.lower() == "left-down":
        return True

    if state == (34, 40) and action.lower() == "left":
        return True

    if state == (34, 43) and action.lower() == "up":
        return True

    if state == (34, 43) and action.lower() == "right-up":
        return True

    if state == (34, 43) and action.lower() == "right":
        return True

    if state == (34, 43) and action.lower() == "down":
        return True

    if state == (34, 43) and action.lower() == "left-down":
        return True

    if state == (34, 44) and action.lower() == "left-up":
        return True

    if state == (34, 44) and action.lower() == "up":
        return True

    if state == (34, 44) and action.lower() == "right-up":
        return True

    if state == (34, 44) and action.lower() == "right-down":
        return True

    if state == (34, 44) and action.lower() == "left-down":
        return True

    if state == (34, 44) and action.lower() == "left":
        return True

    if state == (34, 47) and action.lower() == "up":
        return True

    if state == (34, 47) and action.lower() == "right-up":
        return True

    if state == (34, 47) and action.lower() == "right":
        return True

    if state == (34, 47) and action.lower() == "left-down":
        return True

    if state == (34, 48) and action.lower() == "left-up":
        return True

    if state == (34, 48) and action.lower() == "up":
        return True

    if state == (34, 48) and action.lower() == "right-up":
        return True

    if state == (34, 48) and action.lower() == "left":
        return True

    if state == (34, 50) and action.lower() == "left-up":
        return True

    if state == (34, 50) and action.lower() == "right-down":
        return True

    if state == (35, 1) and action.lower() == "right-up":
        return True

    if state == (35, 1) and action.lower() == "right":
        return True

    if state == (35, 1) and action.lower() == "right-down":
        return True

    if state == (35, 2) and action.lower() == "up":
        return True

    if state == (35, 2) and action.lower() == "right-up":
        return True

    if state == (35, 2) and action.lower() == "right-down":
        return True

    if state == (35, 2) and action.lower() == "down":
        return True

    if state == (35, 2) and action.lower() == "left":
        return True

    if state == (35, 6) and action.lower() == "left-up":
        return True

    if state == (35, 6) and action.lower() == "right-up":
        return True

    if state == (35, 6) and action.lower() == "down":
        return True

    if state == (35, 6) and action.lower() == "left-down":
        return True

    if state == (35, 8) and action.lower() == "left-up":
        return True

    if state == (35, 8) and action.lower() == "right-down":
        return True

    if state == (35, 10) and action.lower() == "up":
        return True

    if state == (35, 10) and action.lower() == "right":
        return True

    if state == (35, 10) and action.lower() == "left-down":
        return True

    if state == (35, 11) and action.lower() == "left-up":
        return True

    if state == (35, 11) and action.lower() == "right":
        return True

    if state == (35, 11) and action.lower() == "right-down":
        return True

    if state == (35, 11) and action.lower() == "left":
        return True

    if state == (35, 12) and action.lower() == "right":
        return True

    if state == (35, 12) and action.lower() == "down":
        return True

    if state == (35, 12) and action.lower() == "left":
        return True

    if state == (35, 13) and action.lower() == "right-down":
        return True

    if state == (35, 13) and action.lower() == "left-down":
        return True

    if state == (35, 13) and action.lower() == "left":
        return True

    if state == (35, 16) and action.lower() == "left-up":
        return True

    if state == (35, 16) and action.lower() == "up":
        return True

    if state == (35, 16) and action.lower() == "right":
        return True

    if state == (35, 16) and action.lower() == "down":
        return True

    if state == (35, 16) and action.lower() == "left-down":
        return True

    if state == (35, 17) and action.lower() == "left-up":
        return True

    if state == (35, 17) and action.lower() == "left-down":
        return True

    if state == (35, 17) and action.lower() == "left":
        return True

    if state == (35, 21) and action.lower() == "right-up":
        return True

    if state == (35, 21) and action.lower() == "right":
        return True

    if state == (35, 21) and action.lower() == "right-down":
        return True

    if state == (35, 21) and action.lower() == "down":
        return True

    if state == (35, 21) and action.lower() == "left-down":
        return True

    if state == (35, 22) and action.lower() == "up":
        return True

    if state == (35, 22) and action.lower() == "right-down":
        return True

    if state == (35, 22) and action.lower() == "down":
        return True

    if state == (35, 22) and action.lower() == "left-down":
        return True

    if state == (35, 22) and action.lower() == "left":
        return True

    if state == (35, 25) and action.lower() == "left-up":
        return True

    if state == (35, 25) and action.lower() == "down":
        return True

    if state == (35, 27) and action.lower() == "up":
        return True

    if state == (35, 27) and action.lower() == "right-up":
        return True

    if state == (35, 27) and action.lower() == "right":
        return True

    if state == (35, 27) and action.lower() == "right-down":
        return True

    if state == (35, 27) and action.lower() == "down":
        return True

    if state == (35, 28) and action.lower() == "left-up":
        return True

    if state == (35, 28) and action.lower() == "up":
        return True

    if state == (35, 28) and action.lower() == "right":
        return True

    if state == (35, 28) and action.lower() == "down":
        return True

    if state == (35, 28) and action.lower() == "left-down":
        return True

    if state == (35, 28) and action.lower() == "left":
        return True

    if state == (35, 29) and action.lower() == "left-up":
        return True

    if state == (35, 29) and action.lower() == "right-down":
        return True

    if state == (35, 29) and action.lower() == "left-down":
        return True

    if state == (35, 29) and action.lower() == "left":
        return True

    if state == (35, 33) and action.lower() == "right-up":
        return True

    if state == (35, 36) and action.lower() == "up":
        return True

    if state == (35, 36) and action.lower() == "right-up":
        return True

    if state == (35, 36) and action.lower() == "down":
        return True

    if state == (35, 36) and action.lower() == "left-down":
        return True

    if state == (35, 38) and action.lower() == "left-up":
        return True

    if state == (35, 38) and action.lower() == "right-up":
        return True

    if state == (35, 38) and action.lower() == "right":
        return True

    if state == (35, 39) and action.lower() == "up":
        return True

    if state == (35, 39) and action.lower() == "right-up":
        return True

    if state == (35, 39) and action.lower() == "right":
        return True

    if state == (35, 39) and action.lower() == "left":
        return True

    if state == (35, 40) and action.lower() == "left-up":
        return True

    if state == (35, 40) and action.lower() == "up":
        return True

    if state == (35, 40) and action.lower() == "left":
        return True

    if state == (35, 42) and action.lower() == "right-up":
        return True

    if state == (35, 42) and action.lower() == "right":
        return True

    if state == (35, 42) and action.lower() == "right-down":
        return True

    if state == (35, 42) and action.lower() == "down":
        return True

    if state == (35, 43) and action.lower() == "up":
        return True

    if state == (35, 43) and action.lower() == "right-up":
        return True

    if state == (35, 43) and action.lower() == "right-down":
        return True

    if state == (35, 43) and action.lower() == "down":
        return True

    if state == (35, 43) and action.lower() == "left-down":
        return True

    if state == (35, 43) and action.lower() == "left":
        return True

    if state == (35, 45) and action.lower() == "left-up":
        return True

    if state == (35, 45) and action.lower() == "right":
        return True

    if state == (35, 45) and action.lower() == "right-down":
        return True

    if state == (35, 45) and action.lower() == "left-down":
        return True

    if state == (35, 46) and action.lower() == "right-up":
        return True

    if state == (35, 46) and action.lower() == "right-down":
        return True

    if state == (35, 46) and action.lower() == "down":
        return True

    if state == (35, 46) and action.lower() == "left":
        return True

    if state == (35, 51) and action.lower() == "left-up":
        return True

    if state == (35, 51) and action.lower() == "left-down":
        return True

    if state == (36, 2) and action.lower() == "left-up":
        return True

    if state == (36, 2) and action.lower() == "up":
        return True

    if state == (36, 2) and action.lower() == "right":
        return True

    if state == (36, 3) and action.lower() == "left-up":
        return True

    if state == (36, 3) and action.lower() == "left":
        return True

    if state == (36, 5) and action.lower() == "right-up":
        return True

    if state == (36, 5) and action.lower() == "right":
        return True

    if state == (36, 5) and action.lower() == "right-down":
        return True

    if state == (36, 6) and action.lower() == "up":
        return True

    if state == (36, 6) and action.lower() == "right-down":
        return True

    if state == (36, 6) and action.lower() == "down":
        return True

    if state == (36, 6) and action.lower() == "left":
        return True

    if state == (36, 9) and action.lower() == "left-up":
        return True

    if state == (36, 9) and action.lower() == "right-up":
        return True

    if state == (36, 12) and action.lower() == "left-up":
        return True

    if state == (36, 12) and action.lower() == "up":
        return True

    if state == (36, 12) and action.lower() == "right-up":
        return True

    if state == (36, 12) and action.lower() == "left-down":
        return True

    if state == (36, 14) and action.lower() == "left-up":
        return True

    if state == (36, 14) and action.lower() == "right":
        return True

    if state == (36, 14) and action.lower() == "right-down":
        return True

    if state == (36, 15) and action.lower() == "right-up":
        return True

    if state == (36, 15) and action.lower() == "right":
        return True

    if state == (36, 15) and action.lower() == "down":
        return True

    if state == (36, 15) and action.lower() == "left":
        return True

    if state == (36, 16) and action.lower() == "up":
        return True

    if state == (36, 16) and action.lower() == "right-up":
        return True

    if state == (36, 16) and action.lower() == "left-down":
        return True

    if state == (36, 16) and action.lower() == "left":
        return True

    if state == (36, 19) and action.lower() == "right":
        return True

    if state == (36, 19) and action.lower() == "down":
        return True

    if state == (36, 19) and action.lower() == "left-down":
        return True

    if state == (36, 20) and action.lower() == "right-up":
        return True

    if state == (36, 20) and action.lower() == "right":
        return True

    if state == (36, 20) and action.lower() == "right-down":
        return True

    if state == (36, 20) and action.lower() == "left-down":
        return True

    if state == (36, 20) and action.lower() == "left":
        return True

    if state == (36, 21) and action.lower() == "up":
        return True

    if state == (36, 21) and action.lower() == "right-up":
        return True

    if state == (36, 21) and action.lower() == "right":
        return True

    if state == (36, 21) and action.lower() == "right-down":
        return True

    if state == (36, 21) and action.lower() == "down":
        return True

    if state == (36, 21) and action.lower() == "left":
        return True

    if state == (36, 22) and action.lower() == "left-up":
        return True

    if state == (36, 22) and action.lower() == "up":
        return True

    if state == (36, 22) and action.lower() == "right":
        return True

    if state == (36, 22) and action.lower() == "down":
        return True

    if state == (36, 22) and action.lower() == "left-down":
        return True

    if state == (36, 22) and action.lower() == "left":
        return True

    if state == (36, 23) and action.lower() == "left-up":
        return True

    if state == (36, 23) and action.lower() == "left-down":
        return True

    if state == (36, 23) and action.lower() == "left":
        return True

    if state == (36, 25) and action.lower() == "up":
        return True

    if state == (36, 25) and action.lower() == "right-down":
        return True

    if state == (36, 25) and action.lower() == "down":
        return True

    if state == (36, 27) and action.lower() == "up":
        return True

    if state == (36, 27) and action.lower() == "right-up":
        return True

    if state == (36, 27) and action.lower() == "right":
        return True

    if state == (36, 27) and action.lower() == "right-down":
        return True

    if state == (36, 27) and action.lower() == "down":
        return True

    if state == (36, 27) and action.lower() == "left-down":
        return True

    if state == (36, 28) and action.lower() == "left-up":
        return True

    if state == (36, 28) and action.lower() == "up":
        return True

    if state == (36, 28) and action.lower() == "right-up":
        return True

    if state == (36, 28) and action.lower() == "right-down":
        return True

    if state == (36, 28) and action.lower() == "down":
        return True

    if state == (36, 28) and action.lower() == "left-down":
        return True

    if state == (36, 28) and action.lower() == "left":
        return True

    if state == (36, 30) and action.lower() == "left-up":
        return True

    if state == (36, 30) and action.lower() == "right":
        return True

    if state == (36, 30) and action.lower() == "down":
        return True

    if state == (36, 30) and action.lower() == "left-down":
        return True

    if state == (36, 31) and action.lower() == "left-down":
        return True

    if state == (36, 31) and action.lower() == "left":
        return True

    if state == (36, 35) and action.lower() == "right-up":
        return True

    if state == (36, 35) and action.lower() == "right":
        return True

    if state == (36, 35) and action.lower() == "left-down":
        return True

    if state == (36, 36) and action.lower() == "up":
        return True

    if state == (36, 36) and action.lower() == "right-down":
        return True

    if state == (36, 36) and action.lower() == "left":
        return True

    if state == (36, 42) and action.lower() == "up":
        return True

    if state == (36, 42) and action.lower() == "right-up":
        return True

    if state == (36, 42) and action.lower() == "right":
        return True

    if state == (36, 42) and action.lower() == "left-down":
        return True

    if state == (36, 43) and action.lower() == "left-up":
        return True

    if state == (36, 43) and action.lower() == "up":
        return True

    if state == (36, 43) and action.lower() == "right":
        return True

    if state == (36, 43) and action.lower() == "left":
        return True

    if state == (36, 44) and action.lower() == "left-up":
        return True

    if state == (36, 44) and action.lower() == "right-up":
        return True

    if state == (36, 44) and action.lower() == "right-down":
        return True

    if state == (36, 44) and action.lower() == "left":
        return True

    if state == (36, 46) and action.lower() == "left-up":
        return True

    if state == (36, 46) and action.lower() == "up":
        return True

    if state == (36, 46) and action.lower() == "right":
        return True

    if state == (36, 46) and action.lower() == "right-down":
        return True

    if state == (36, 46) and action.lower() == "left-down":
        return True

    if state == (36, 47) and action.lower() == "left-up":
        return True

    if state == (36, 47) and action.lower() == "right":
        return True

    if state == (36, 47) and action.lower() == "right-down":
        return True

    if state == (36, 47) and action.lower() == "down":
        return True

    if state == (36, 47) and action.lower() == "left":
        return True

    if state == (36, 48) and action.lower() == "right":
        return True

    if state == (36, 48) and action.lower() == "right-down":
        return True

    if state == (36, 48) and action.lower() == "down":
        return True

    if state == (36, 48) and action.lower() == "left-down":
        return True

    if state == (36, 48) and action.lower() == "left":
        return True

    if state == (36, 49) and action.lower() == "right":
        return True

    if state == (36, 49) and action.lower() == "right-down":
        return True

    if state == (36, 49) and action.lower() == "down":
        return True

    if state == (36, 49) and action.lower() == "left-down":
        return True

    if state == (36, 49) and action.lower() == "left":
        return True

    if state == (36, 50) and action.lower() == "right-up":
        return True

    if state == (36, 50) and action.lower() == "down":
        return True

    if state == (36, 50) and action.lower() == "left-down":
        return True

    if state == (36, 50) and action.lower() == "left":
        return True

    if state == (37, 6) and action.lower() == "left-up":
        return True

    if state == (37, 6) and action.lower() == "up":
        return True

    if state == (37, 6) and action.lower() == "right":
        return True

    if state == (37, 6) and action.lower() == "right-down":
        return True

    if state == (37, 7) and action.lower() == "left-up":
        return True

    if state == (37, 7) and action.lower() == "right-down":
        return True

    if state == (37, 7) and action.lower() == "down":
        return True

    if state == (37, 7) and action.lower() == "left":
        return True

    if state == (37, 11) and action.lower() == "right-up":
        return True

    if state == (37, 11) and action.lower() == "down":
        return True

    if state == (37, 11) and action.lower() == "left-down":
        return True

    if state == (37, 15) and action.lower() == "left-up":
        return True

    if state == (37, 15) and action.lower() == "up":
        return True

    if state == (37, 15) and action.lower() == "right-up":
        return True

    if state == (37, 18) and action.lower() == "right-up":
        return True

    if state == (37, 18) and action.lower() == "right":
        return True

    if state == (37, 18) and action.lower() == "right-down":
        return True

    if state == (37, 18) and action.lower() == "down":
        return True

    if state == (37, 19) and action.lower() == "up":
        return True

    if state == (37, 19) and action.lower() == "right-up":
        return True

    if state == (37, 19) and action.lower() == "right-down":
        return True

    if state == (37, 19) and action.lower() == "down":
        return True

    if state == (37, 19) and action.lower() == "left-down":
        return True

    if state == (37, 19) and action.lower() == "left":
        return True

    if state == (37, 21) and action.lower() == "left-up":
        return True

    if state == (37, 21) and action.lower() == "up":
        return True

    if state == (37, 21) and action.lower() == "right-up":
        return True

    if state == (37, 21) and action.lower() == "right":
        return True

    if state == (37, 21) and action.lower() == "right-down":
        return True

    if state == (37, 21) and action.lower() == "left-down":
        return True

    if state == (37, 22) and action.lower() == "left-up":
        return True

    if state == (37, 22) and action.lower() == "up":
        return True

    if state == (37, 22) and action.lower() == "right-up":
        return True

    if state == (37, 22) and action.lower() == "down":
        return True

    if state == (37, 22) and action.lower() == "left":
        return True

    if state == (37, 25) and action.lower() == "up":
        return True

    if state == (37, 25) and action.lower() == "right":
        return True

    if state == (37, 25) and action.lower() == "down":
        return True

    if state == (37, 25) and action.lower() == "left-down":
        return True

    if state == (37, 26) and action.lower() == "left-up":
        return True

    if state == (37, 26) and action.lower() == "right-up":
        return True

    if state == (37, 26) and action.lower() == "right":
        return True

    if state == (37, 26) and action.lower() == "left-down":
        return True

    if state == (37, 26) and action.lower() == "left":
        return True

    if state == (37, 27) and action.lower() == "up":
        return True

    if state == (37, 27) and action.lower() == "right-up":
        return True

    if state == (37, 27) and action.lower() == "right":
        return True

    if state == (37, 27) and action.lower() == "right-down":
        return True

    if state == (37, 27) and action.lower() == "left":
        return True

    if state == (37, 28) and action.lower() == "left-up":
        return True

    if state == (37, 28) and action.lower() == "up":
        return True

    if state == (37, 28) and action.lower() == "right":
        return True

    if state == (37, 28) and action.lower() == "right-down":
        return True

    if state == (37, 28) and action.lower() == "down":
        return True

    if state == (37, 28) and action.lower() == "left":
        return True

    if state == (37, 29) and action.lower() == "left-up":
        return True

    if state == (37, 29) and action.lower() == "right-up":
        return True

    if state == (37, 29) and action.lower() == "right":
        return True

    if state == (37, 29) and action.lower() == "right-down":
        return True

    if state == (37, 29) and action.lower() == "down":
        return True

    if state == (37, 29) and action.lower() == "left-down":
        return True

    if state == (37, 29) and action.lower() == "left":
        return True

    if state == (37, 30) and action.lower() == "up":
        return True

    if state == (37, 30) and action.lower() == "right-up":
        return True

    if state == (37, 30) and action.lower() == "right-down":
        return True

    if state == (37, 30) and action.lower() == "down":
        return True

    if state == (37, 30) and action.lower() == "left-down":
        return True

    if state == (37, 30) and action.lower() == "left":
        return True

    if state == (37, 33) and action.lower() == "right":
        return True

    if state == (37, 33) and action.lower() == "right-down":
        return True

    if state == (37, 34) and action.lower() == "right-up":
        return True

    if state == (37, 34) and action.lower() == "right-down":
        return True

    if state == (37, 34) and action.lower() == "down":
        return True

    if state == (37, 34) and action.lower() == "left":
        return True

    if state == (37, 37) and action.lower() == "left-up":
        return True

    if state == (37, 37) and action.lower() == "right-down":
        return True

    if state == (37, 37) and action.lower() == "left-down":
        return True

    if state == (37, 39) and action.lower() == "right":
        return True

    if state == (37, 39) and action.lower() == "right-down":
        return True

    if state == (37, 39) and action.lower() == "down":
        return True

    if state == (37, 39) and action.lower() == "left-down":
        return True

    if state == (37, 40) and action.lower() == "right":
        return True

    if state == (37, 40) and action.lower() == "right-down":
        return True

    if state == (37, 40) and action.lower() == "down":
        return True

    if state == (37, 40) and action.lower() == "left-down":
        return True

    if state == (37, 40) and action.lower() == "left":
        return True

    if state == (37, 41) and action.lower() == "right-up":
        return True

    if state == (37, 41) and action.lower() == "down":
        return True

    if state == (37, 41) and action.lower() == "left-down":
        return True

    if state == (37, 41) and action.lower() == "left":
        return True

    if state == (37, 45) and action.lower() == "left-up":
        return True

    if state == (37, 45) and action.lower() == "right-up":
        return True

    if state == (37, 45) and action.lower() == "right-down":
        return True

    if state == (37, 45) and action.lower() == "down":
        return True

    if state == (37, 47) and action.lower() == "left-up":
        return True

    if state == (37, 47) and action.lower() == "up":
        return True

    if state == (37, 47) and action.lower() == "right-up":
        return True

    if state == (37, 47) and action.lower() == "right":
        return True

    if state == (37, 47) and action.lower() == "right-down":
        return True

    if state == (37, 47) and action.lower() == "down":
        return True

    if state == (37, 47) and action.lower() == "left-down":
        return True

    if state == (37, 48) and action.lower() == "left-up":
        return True

    if state == (37, 48) and action.lower() == "up":
        return True

    if state == (37, 48) and action.lower() == "right-up":
        return True

    if state == (37, 48) and action.lower() == "right":
        return True

    if state == (37, 48) and action.lower() == "down":
        return True

    if state == (37, 48) and action.lower() == "left-down":
        return True

    if state == (37, 48) and action.lower() == "left":
        return True

    if state == (37, 49) and action.lower() == "left-up":
        return True

    if state == (37, 49) and action.lower() == "up":
        return True

    if state == (37, 49) and action.lower() == "right-up":
        return True

    if state == (37, 49) and action.lower() == "right":
        return True

    if state == (37, 49) and action.lower() == "left-down":
        return True

    if state == (37, 49) and action.lower() == "left":
        return True

    if state == (37, 50) and action.lower() == "left-up":
        return True

    if state == (37, 50) and action.lower() == "up":
        return True

    if state == (37, 50) and action.lower() == "right-down":
        return True

    if state == (37, 50) and action.lower() == "left":
        return True

    if state == (38, 0) and action.lower() == "right-down":
        return True

    if state == (38, 0) and action.lower() == "down":
        return True

    if state == (38, 7) and action.lower() == "left-up":
        return True

    if state == (38, 7) and action.lower() == "up":
        return True

    if state == (38, 7) and action.lower() == "right":
        return True

    if state == (38, 7) and action.lower() == "right-down":
        return True

    if state == (38, 7) and action.lower() == "down":
        return True

    if state == (38, 7) and action.lower() == "left-down":
        return True

    if state == (38, 8) and action.lower() == "left-up":
        return True

    if state == (38, 8) and action.lower() == "right-down":
        return True

    if state == (38, 8) and action.lower() == "down":
        return True

    if state == (38, 8) and action.lower() == "left-down":
        return True

    if state == (38, 8) and action.lower() == "left":
        return True

    if state == (38, 10) and action.lower() == "right-up":
        return True

    if state == (38, 10) and action.lower() == "right":
        return True

    if state == (38, 10) and action.lower() == "right-down":
        return True

    if state == (38, 10) and action.lower() == "down":
        return True

    if state == (38, 10) and action.lower() == "left-down":
        return True

    if state == (38, 11) and action.lower() == "up":
        return True

    if state == (38, 11) and action.lower() == "down":
        return True

    if state == (38, 11) and action.lower() == "left-down":
        return True

    if state == (38, 11) and action.lower() == "left":
        return True

    if state == (38, 18) and action.lower() == "up":
        return True

    if state == (38, 18) and action.lower() == "right-up":
        return True

    if state == (38, 18) and action.lower() == "right":
        return True

    if state == (38, 18) and action.lower() == "down":
        return True

    if state == (38, 18) and action.lower() == "left-down":
        return True

    if state == (38, 19) and action.lower() == "left-up":
        return True

    if state == (38, 19) and action.lower() == "up":
        return True

    if state == (38, 19) and action.lower() == "right":
        return True

    if state == (38, 19) and action.lower() == "right-down":
        return True

    if state == (38, 19) and action.lower() == "left-down":
        return True

    if state == (38, 19) and action.lower() == "left":
        return True

    if state == (38, 20) and action.lower() == "left-up":
        return True

    if state == (38, 20) and action.lower() == "right-up":
        return True

    if state == (38, 20) and action.lower() == "down":
        return True

    if state == (38, 20) and action.lower() == "left":
        return True

    if state == (38, 22) and action.lower() == "left-up":
        return True

    if state == (38, 22) and action.lower() == "up":
        return True

    if state == (38, 24) and action.lower() == "right-up":
        return True

    if state == (38, 24) and action.lower() == "right":
        return True

    if state == (38, 24) and action.lower() == "down":
        return True

    if state == (38, 25) and action.lower() == "up":
        return True

    if state == (38, 25) and action.lower() == "right-up":
        return True

    if state == (38, 25) and action.lower() == "left-down":
        return True

    if state == (38, 25) and action.lower() == "left":
        return True

    if state == (38, 28) and action.lower() == "left-up":
        return True

    if state == (38, 28) and action.lower() == "up":
        return True

    if state == (38, 28) and action.lower() == "right-up":
        return True

    if state == (38, 28) and action.lower() == "right":
        return True

    if state == (38, 28) and action.lower() == "right-down":
        return True

    if state == (38, 28) and action.lower() == "down":
        return True

    if state == (38, 29) and action.lower() == "left-up":
        return True

    if state == (38, 29) and action.lower() == "up":
        return True

    if state == (38, 29) and action.lower() == "right-up":
        return True

    if state == (38, 29) and action.lower() == "right":
        return True

    if state == (38, 29) and action.lower() == "down":
        return True

    if state == (38, 29) and action.lower() == "left-down":
        return True

    if state == (38, 29) and action.lower() == "left":
        return True

    if state == (38, 30) and action.lower() == "left-up":
        return True

    if state == (38, 30) and action.lower() == "up":
        return True

    if state == (38, 30) and action.lower() == "right":
        return True

    if state == (38, 30) and action.lower() == "left-down":
        return True

    if state == (38, 30) and action.lower() == "left":
        return True

    if state == (38, 31) and action.lower() == "left-up":
        return True

    if state == (38, 31) and action.lower() == "right-down":
        return True

    if state == (38, 31) and action.lower() == "left":
        return True

    if state == (38, 34) and action.lower() == "left-up":
        return True

    if state == (38, 34) and action.lower() == "up":
        return True

    if state == (38, 34) and action.lower() == "right":
        return True

    if state == (38, 34) and action.lower() == "left-down":
        return True

    if state == (38, 35) and action.lower() == "left-up":
        return True

    if state == (38, 35) and action.lower() == "right":
        return True

    if state == (38, 35) and action.lower() == "right-down":
        return True

    if state == (38, 35) and action.lower() == "left":
        return True

    if state == (38, 36) and action.lower() == "right-up":
        return True

    if state == (38, 36) and action.lower() == "right-down":
        return True

    if state == (38, 36) and action.lower() == "down":
        return True

    if state == (38, 36) and action.lower() == "left":
        return True

    if state == (38, 38) and action.lower() == "left-up":
        return True

    if state == (38, 38) and action.lower() == "right-up":
        return True

    if state == (38, 38) and action.lower() == "right":
        return True

    if state == (38, 38) and action.lower() == "down":
        return True

    if state == (38, 38) and action.lower() == "left-down":
        return True

    if state == (38, 39) and action.lower() == "up":
        return True

    if state == (38, 39) and action.lower() == "right-up":
        return True

    if state == (38, 39) and action.lower() == "right":
        return True

    if state == (38, 39) and action.lower() == "left-down":
        return True

    if state == (38, 39) and action.lower() == "left":
        return True

    if state == (38, 40) and action.lower() == "left-up":
        return True

    if state == (38, 40) and action.lower() == "up":
        return True

    if state == (38, 40) and action.lower() == "right-up":
        return True

    if state == (38, 40) and action.lower() == "right":
        return True

    if state == (38, 40) and action.lower() == "left":
        return True

    if state == (38, 41) and action.lower() == "left-up":
        return True

    if state == (38, 41) and action.lower() == "up":
        return True

    if state == (38, 41) and action.lower() == "left":
        return True

    if state == (38, 45) and action.lower() == "up":
        return True

    if state == (38, 45) and action.lower() == "right":
        return True

    if state == (38, 45) and action.lower() == "left-down":
        return True

    if state == (38, 46) and action.lower() == "left-up":
        return True

    if state == (38, 46) and action.lower() == "right-up":
        return True

    if state == (38, 46) and action.lower() == "right":
        return True

    if state == (38, 46) and action.lower() == "right-down":
        return True

    if state == (38, 46) and action.lower() == "left":
        return True

    if state == (38, 47) and action.lower() == "up":
        return True

    if state == (38, 47) and action.lower() == "right-up":
        return True

    if state == (38, 47) and action.lower() == "right":
        return True

    if state == (38, 47) and action.lower() == "down":
        return True

    if state == (38, 47) and action.lower() == "left":
        return True

    if state == (38, 48) and action.lower() == "left-up":
        return True

    if state == (38, 48) and action.lower() == "up":
        return True

    if state == (38, 48) and action.lower() == "right-up":
        return True

    if state == (38, 48) and action.lower() == "left-down":
        return True

    if state == (38, 48) and action.lower() == "left":
        return True

    if state == (38, 51) and action.lower() == "left-up":
        return True

    if state == (38, 51) and action.lower() == "down":
        return True

    if state == (38, 51) and action.lower() == "left-down":
        return True

    if state == (39, 0) and action.lower() == "up":
        return True

    if state == (39, 0) and action.lower() == "right":
        return True

    if state == (39, 0) and action.lower() == "right-down":
        return True

    if state == (39, 1) and action.lower() == "left-up":
        return True

    if state == (39, 1) and action.lower() == "down":
        return True

    if state == (39, 1) and action.lower() == "left":
        return True

    if state == (39, 5) and action.lower() == "right":
        return True

    if state == (39, 5) and action.lower() == "down":
        return True

    if state == (39, 6) and action.lower() == "right-up":
        return True

    if state == (39, 6) and action.lower() == "right":
        return True

    if state == (39, 6) and action.lower() == "left-down":
        return True

    if state == (39, 6) and action.lower() == "left":
        return True

    if state == (39, 7) and action.lower() == "up":
        return True

    if state == (39, 7) and action.lower() == "right-up":
        return True

    if state == (39, 7) and action.lower() == "right":
        return True

    if state == (39, 7) and action.lower() == "right-down":
        return True

    if state == (39, 7) and action.lower() == "left":
        return True

    if state == (39, 8) and action.lower() == "left-up":
        return True

    if state == (39, 8) and action.lower() == "up":
        return True

    if state == (39, 8) and action.lower() == "right":
        return True

    if state == (39, 8) and action.lower() == "right-down":
        return True

    if state == (39, 8) and action.lower() == "down":
        return True

    if state == (39, 8) and action.lower() == "left":
        return True

    if state == (39, 9) and action.lower() == "left-up":
        return True

    if state == (39, 9) and action.lower() == "right-up":
        return True

    if state == (39, 9) and action.lower() == "right":
        return True

    if state == (39, 9) and action.lower() == "down":
        return True

    if state == (39, 9) and action.lower() == "left-down":
        return True

    if state == (39, 9) and action.lower() == "left":
        return True

    if state == (39, 10) and action.lower() == "up":
        return True

    if state == (39, 10) and action.lower() == "right-up":
        return True

    if state == (39, 10) and action.lower() == "right":
        return True

    if state == (39, 10) and action.lower() == "right-down":
        return True

    if state == (39, 10) and action.lower() == "left-down":
        return True

    if state == (39, 10) and action.lower() == "left":
        return True

    if state == (39, 11) and action.lower() == "left-up":
        return True

    if state == (39, 11) and action.lower() == "up":
        return True

    if state == (39, 11) and action.lower() == "down":
        return True

    if state == (39, 11) and action.lower() == "left":
        return True

    if state == (39, 13) and action.lower() == "down":
        return True

    if state == (39, 15) and action.lower() == "right-down":
        return True

    if state == (39, 15) and action.lower() == "down":
        return True

    if state == (39, 17) and action.lower() == "right-up":
        return True

    if state == (39, 17) and action.lower() == "right":
        return True

    if state == (39, 17) and action.lower() == "left-down":
        return True

    if state == (39, 18) and action.lower() == "up":
        return True

    if state == (39, 18) and action.lower() == "right-up":
        return True

    if state == (39, 18) and action.lower() == "right-down":
        return True

    if state == (39, 18) and action.lower() == "left":
        return True

    if state == (39, 20) and action.lower() == "left-up":
        return True

    if state == (39, 20) and action.lower() == "up":
        return True

    if state == (39, 20) and action.lower() == "down":
        return True

    if state == (39, 20) and action.lower() == "left-down":
        return True

    if state == (39, 24) and action.lower() == "up":
        return True

    if state == (39, 24) and action.lower() == "right-up":
        return True

    if state == (39, 28) and action.lower() == "up":
        return True

    if state == (39, 28) and action.lower() == "right-up":
        return True

    if state == (39, 28) and action.lower() == "right":
        return True

    if state == (39, 28) and action.lower() == "left-down":
        return True

    if state == (39, 29) and action.lower() == "left-up":
        return True

    if state == (39, 29) and action.lower() == "up":
        return True

    if state == (39, 29) and action.lower() == "right-up":
        return True

    if state == (39, 29) and action.lower() == "right-down":
        return True

    if state == (39, 29) and action.lower() == "left":
        return True

    if state == (39, 32) and action.lower() == "left-up":
        return True

    if state == (39, 32) and action.lower() == "right":
        return True

    if state == (39, 32) and action.lower() == "right-down":
        return True

    if state == (39, 33) and action.lower() == "right-up":
        return True

    if state == (39, 33) and action.lower() == "right-down":
        return True

    if state == (39, 33) and action.lower() == "down":
        return True

    if state == (39, 33) and action.lower() == "left":
        return True

    if state == (39, 36) and action.lower() == "left-up":
        return True

    if state == (39, 36) and action.lower() == "up":
        return True

    if state == (39, 36) and action.lower() == "right":
        return True

    if state == (39, 36) and action.lower() == "right-down":
        return True

    if state == (39, 36) and action.lower() == "down":
        return True

    if state == (39, 36) and action.lower() == "left-down":
        return True

    if state == (39, 37) and action.lower() == "left-up":
        return True

    if state == (39, 37) and action.lower() == "right-up":
        return True

    if state == (39, 37) and action.lower() == "right":
        return True

    if state == (39, 37) and action.lower() == "down":
        return True

    if state == (39, 37) and action.lower() == "left-down":
        return True

    if state == (39, 37) and action.lower() == "left":
        return True

    if state == (39, 38) and action.lower() == "up":
        return True

    if state == (39, 38) and action.lower() == "right-up":
        return True

    if state == (39, 38) and action.lower() == "right-down":
        return True

    if state == (39, 38) and action.lower() == "left-down":
        return True

    if state == (39, 38) and action.lower() == "left":
        return True

    if state == (39, 44) and action.lower() == "right-up":
        return True

    if state == (39, 44) and action.lower() == "right-down":
        return True

    if state == (39, 44) and action.lower() == "down":
        return True

    if state == (39, 47) and action.lower() == "left-up":
        return True

    if state == (39, 47) and action.lower() == "up":
        return True

    if state == (39, 47) and action.lower() == "right-up":
        return True

    if state == (39, 47) and action.lower() == "down":
        return True

    if state == (39, 50) and action.lower() == "right-up":
        return True

    if state == (39, 50) and action.lower() == "right":
        return True

    if state == (39, 50) and action.lower() == "left-down":
        return True

    if state == (39, 51) and action.lower() == "up":
        return True

    if state == (39, 51) and action.lower() == "left":
        return True

    if state == (40, 1) and action.lower() == "left-up":
        return True

    if state == (40, 1) and action.lower() == "up":
        return True

    if state == (40, 1) and action.lower() == "right-down":
        return True

    if state == (40, 1) and action.lower() == "down":
        return True

    if state == (40, 1) and action.lower() == "left-down":
        return True

    if state == (40, 5) and action.lower() == "up":
        return True

    if state == (40, 5) and action.lower() == "right-up":
        return True

    if state == (40, 5) and action.lower() == "right-down":
        return True

    if state == (40, 5) and action.lower() == "down":
        return True

    if state == (40, 8) and action.lower() == "left-up":
        return True

    if state == (40, 8) and action.lower() == "up":
        return True

    if state == (40, 8) and action.lower() == "right-up":
        return True

    if state == (40, 8) and action.lower() == "right":
        return True

    if state == (40, 9) and action.lower() == "left-up":
        return True

    if state == (40, 9) and action.lower() == "up":
        return True

    if state == (40, 9) and action.lower() == "right-up":
        return True

    if state == (40, 9) and action.lower() == "right-down":
        return True

    if state == (40, 9) and action.lower() == "left":
        return True

    if state == (40, 11) and action.lower() == "left-up":
        return True

    if state == (40, 11) and action.lower() == "up":
        return True

    if state == (40, 11) and action.lower() == "left-down":
        return True

    if state == (40, 13) and action.lower() == "up":
        return True

    if state == (40, 13) and action.lower() == "right-down":
        return True

    if state == (40, 15) and action.lower() == "up":
        return True

    if state == (40, 15) and action.lower() == "right":
        return True

    if state == (40, 15) and action.lower() == "down":
        return True

    if state == (40, 15) and action.lower() == "left-down":
        return True

    if state == (40, 16) and action.lower() == "left-up":
        return True

    if state == (40, 16) and action.lower() == "right-up":
        return True

    if state == (40, 16) and action.lower() == "right-down":
        return True

    if state == (40, 16) and action.lower() == "left-down":
        return True

    if state == (40, 16) and action.lower() == "left":
        return True

    if state == (40, 19) and action.lower() == "left-up":
        return True

    if state == (40, 19) and action.lower() == "right-up":
        return True

    if state == (40, 19) and action.lower() == "right":
        return True

    if state == (40, 19) and action.lower() == "left-down":
        return True

    if state == (40, 20) and action.lower() == "up":
        return True

    if state == (40, 20) and action.lower() == "left":
        return True

    if state == (40, 22) and action.lower() == "down":
        return True

    if state == (40, 26) and action.lower() == "right":
        return True

    if state == (40, 26) and action.lower() == "down":
        return True

    if state == (40, 27) and action.lower() == "right-up":
        return True

    if state == (40, 27) and action.lower() == "left-down":
        return True

    if state == (40, 27) and action.lower() == "left":
        return True

    if state == (40, 30) and action.lower() == "left-up":
        return True

    if state == (40, 30) and action.lower() == "down":
        return True

    if state == (40, 30) and action.lower() == "left-down":
        return True

    if state == (40, 33) and action.lower() == "left-up":
        return True

    if state == (40, 33) and action.lower() == "up":
        return True

    if state == (40, 33) and action.lower() == "right":
        return True

    if state == (40, 33) and action.lower() == "down":
        return True

    if state == (40, 34) and action.lower() == "left-up":
        return True

    if state == (40, 34) and action.lower() == "right":
        return True

    if state == (40, 34) and action.lower() == "right-down":
        return True

    if state == (40, 34) and action.lower() == "left-down":
        return True

    if state == (40, 34) and action.lower() == "left":
        return True

    if state == (40, 35) and action.lower() == "right-up":
        return True

    if state == (40, 35) and action.lower() == "right":
        return True

    if state == (40, 35) and action.lower() == "right-down":
        return True

    if state == (40, 35) and action.lower() == "down":
        return True

    if state == (40, 35) and action.lower() == "left":
        return True

    if state == (40, 36) and action.lower() == "up":
        return True

    if state == (40, 36) and action.lower() == "right-up":
        return True

    if state == (40, 36) and action.lower() == "right":
        return True

    if state == (40, 36) and action.lower() == "down":
        return True

    if state == (40, 36) and action.lower() == "left-down":
        return True

    if state == (40, 36) and action.lower() == "left":
        return True

    if state == (40, 37) and action.lower() == "left-up":
        return True

    if state == (40, 37) and action.lower() == "up":
        return True

    if state == (40, 37) and action.lower() == "right-up":
        return True

    if state == (40, 37) and action.lower() == "right-down":
        return True

    if state == (40, 37) and action.lower() == "left-down":
        return True

    if state == (40, 37) and action.lower() == "left":
        return True

    if state == (40, 39) and action.lower() == "left-up":
        return True

    if state == (40, 39) and action.lower() == "right":
        return True

    if state == (40, 39) and action.lower() == "right-down":
        return True

    if state == (40, 39) and action.lower() == "down":
        return True

    if state == (40, 39) and action.lower() == "left-down":
        return True

    if state == (40, 40) and action.lower() == "right":
        return True

    if state == (40, 40) and action.lower() == "right-down":
        return True

    if state == (40, 40) and action.lower() == "down":
        return True

    if state == (40, 40) and action.lower() == "left-down":
        return True

    if state == (40, 40) and action.lower() == "left":
        return True

    if state == (40, 41) and action.lower() == "down":
        return True

    if state == (40, 41) and action.lower() == "left-down":
        return True

    if state == (40, 41) and action.lower() == "left":
        return True

    if state == (40, 44) and action.lower() == "up":
        return True

    if state == (40, 44) and action.lower() == "right":
        return True

    if state == (40, 44) and action.lower() == "left-down":
        return True

    if state == (40, 45) and action.lower() == "left-up":
        return True

    if state == (40, 45) and action.lower() == "left":
        return True

    if state == (40, 47) and action.lower() == "up":
        return True

    if state == (40, 47) and action.lower() == "right-down":
        return True

    if state == (40, 47) and action.lower() == "down":
        return True

    if state == (40, 49) and action.lower() == "right-up":
        return True

    if state == (40, 49) and action.lower() == "down":
        return True

    if state == (40, 49) and action.lower() == "left-down":
        return True

    if state == (41, 0) and action.lower() == "right-up":
        return True

    if state == (41, 0) and action.lower() == "right":
        return True

    if state == (41, 1) and action.lower() == "up":
        return True

    if state == (41, 1) and action.lower() == "right":
        return True

    if state == (41, 1) and action.lower() == "right-down":
        return True

    if state == (41, 1) and action.lower() == "left":
        return True

    if state == (41, 2) and action.lower() == "left-up":
        return True

    if state == (41, 2) and action.lower() == "right":
        return True

    if state == (41, 2) and action.lower() == "down":
        return True

    if state == (41, 2) and action.lower() == "left":
        return True

    if state == (41, 3) and action.lower() == "right-down":
        return True

    if state == (41, 3) and action.lower() == "left-down":
        return True

    if state == (41, 3) and action.lower() == "left":
        return True

    if state == (41, 5) and action.lower() == "up":
        return True

    if state == (41, 5) and action.lower() == "right":
        return True

    if state == (41, 5) and action.lower() == "right-down":
        return True

    if state == (41, 5) and action.lower() == "left-down":
        return True

    if state == (41, 6) and action.lower() == "left-up":
        return True

    if state == (41, 6) and action.lower() == "right-down":
        return True

    if state == (41, 6) and action.lower() == "down":
        return True

    if state == (41, 6) and action.lower() == "left":
        return True

    if state == (41, 10) and action.lower() == "left-up":
        return True

    if state == (41, 10) and action.lower() == "right-up":
        return True

    if state == (41, 10) and action.lower() == "right-down":
        return True

    if state == (41, 10) and action.lower() == "down":
        return True

    if state == (41, 14) and action.lower() == "left-up":
        return True

    if state == (41, 14) and action.lower() == "right-up":
        return True

    if state == (41, 14) and action.lower() == "right":
        return True

    if state == (41, 14) and action.lower() == "right-down":
        return True

    if state == (41, 15) and action.lower() == "up":
        return True

    if state == (41, 15) and action.lower() == "right-up":
        return True

    if state == (41, 15) and action.lower() == "down":
        return True

    if state == (41, 15) and action.lower() == "left":
        return True

    if state == (41, 17) and action.lower() == "left-up":
        return True

    if state == (41, 17) and action.lower() == "right":
        return True

    if state == (41, 17) and action.lower() == "down":
        return True

    if state == (41, 18) and action.lower() == "right-up":
        return True

    if state == (41, 18) and action.lower() == "right-down":
        return True

    if state == (41, 18) and action.lower() == "left-down":
        return True

    if state == (41, 18) and action.lower() == "left":
        return True

    if state == (41, 22) and action.lower() == "up":
        return True

    if state == (41, 22) and action.lower() == "down":
        return True

    if state == (41, 22) and action.lower() == "left-down":
        return True

    if state == (41, 26) and action.lower() == "up":
        return True

    if state == (41, 26) and action.lower() == "right-up":
        return True

    if state == (41, 26) and action.lower() == "down":
        return True

    if state == (41, 29) and action.lower() == "right-up":
        return True

    if state == (41, 29) and action.lower() == "right":
        return True

    if state == (41, 29) and action.lower() == "right-down":
        return True

    if state == (41, 29) and action.lower() == "left-down":
        return True

    if state == (41, 30) and action.lower() == "up":
        return True

    if state == (41, 30) and action.lower() == "down":
        return True

    if state == (41, 30) and action.lower() == "left":
        return True

    if state == (41, 33) and action.lower() == "up":
        return True

    if state == (41, 33) and action.lower() == "right-up":
        return True

    if state == (41, 33) and action.lower() == "left-down":
        return True

    if state == (41, 35) and action.lower() == "left-up":
        return True

    if state == (41, 35) and action.lower() == "up":
        return True

    if state == (41, 35) and action.lower() == "right-up":
        return True

    if state == (41, 35) and action.lower() == "right":
        return True

    if state == (41, 35) and action.lower() == "right-down":
        return True

    if state == (41, 35) and action.lower() == "down":
        return True

    if state == (41, 36) and action.lower() == "left-up":
        return True

    if state == (41, 36) and action.lower() == "up":
        return True

    if state == (41, 36) and action.lower() == "right-up":
        return True

    if state == (41, 36) and action.lower() == "right-down":
        return True

    if state == (41, 36) and action.lower() == "down":
        return True

    if state == (41, 36) and action.lower() == "left-down":
        return True

    if state == (41, 36) and action.lower() == "left":
        return True

    if state == (41, 38) and action.lower() == "left-up":
        return True

    if state == (41, 38) and action.lower() == "right-up":
        return True

    if state == (41, 38) and action.lower() == "right":
        return True

    if state == (41, 38) and action.lower() == "right-down":
        return True

    if state == (41, 38) and action.lower() == "left-down":
        return True

    if state == (41, 39) and action.lower() == "up":
        return True

    if state == (41, 39) and action.lower() == "right-up":
        return True

    if state == (41, 39) and action.lower() == "right":
        return True

    if state == (41, 39) and action.lower() == "right-down":
        return True

    if state == (41, 39) and action.lower() == "down":
        return True

    if state == (41, 39) and action.lower() == "left":
        return True

    if state == (41, 40) and action.lower() == "left-up":
        return True

    if state == (41, 40) and action.lower() == "up":
        return True

    if state == (41, 40) and action.lower() == "right-up":
        return True

    if state == (41, 40) and action.lower() == "right":
        return True

    if state == (41, 40) and action.lower() == "right-down":
        return True

    if state == (41, 40) and action.lower() == "down":
        return True

    if state == (41, 40) and action.lower() == "left-down":
        return True

    if state == (41, 40) and action.lower() == "left":
        return True

    if state == (41, 41) and action.lower() == "left-up":
        return True

    if state == (41, 41) and action.lower() == "up":
        return True

    if state == (41, 41) and action.lower() == "down":
        return True

    if state == (41, 41) and action.lower() == "left-down":
        return True

    if state == (41, 41) and action.lower() == "left":
        return True

    if state == (41, 43) and action.lower() == "right-up":
        return True

    if state == (41, 43) and action.lower() == "down":
        return True

    if state == (41, 47) and action.lower() == "up":
        return True

    if state == (41, 47) and action.lower() == "right":
        return True

    if state == (41, 47) and action.lower() == "right-down":
        return True

    if state == (41, 47) and action.lower() == "left-down":
        return True

    if state == (41, 48) and action.lower() == "left-up":
        return True

    if state == (41, 48) and action.lower() == "right-up":
        return True

    if state == (41, 48) and action.lower() == "right":
        return True

    if state == (41, 48) and action.lower() == "right-down":
        return True

    if state == (41, 48) and action.lower() == "down":
        return True

    if state == (41, 48) and action.lower() == "left":
        return True

    if state == (41, 49) and action.lower() == "up":
        return True

    if state == (41, 49) and action.lower() == "down":
        return True

    if state == (41, 49) and action.lower() == "left-down":
        return True

    if state == (41, 49) and action.lower() == "left":
        return True

    if state == (41, 51) and action.lower() == "down":
        return True

    if state == (42, 2) and action.lower() == "left-up":
        return True

    if state == (42, 2) and action.lower() == "up":
        return True

    if state == (42, 2) and action.lower() == "right-up":
        return True

    if state == (42, 2) and action.lower() == "right-down":
        return True

    if state == (42, 2) and action.lower() == "down":
        return True

    if state == (42, 4) and action.lower() == "left-up":
        return True

    if state == (42, 4) and action.lower() == "right-up":
        return True

    if state == (42, 4) and action.lower() == "right-down":
        return True

    if state == (42, 4) and action.lower() == "left-down":
        return True

    if state == (42, 6) and action.lower() == "left-up":
        return True

    if state == (42, 6) and action.lower() == "up":
        return True

    if state == (42, 6) and action.lower() == "right":
        return True

    if state == (42, 6) and action.lower() == "right-down":
        return True

    if state == (42, 6) and action.lower() == "down":
        return True

    if state == (42, 6) and action.lower() == "left-down":
        return True

    if state == (42, 7) and action.lower() == "left-up":
        return True

    if state == (42, 7) and action.lower() == "right":
        return True

    if state == (42, 7) and action.lower() == "right-down":
        return True

    if state == (42, 7) and action.lower() == "down":
        return True

    if state == (42, 7) and action.lower() == "left-down":
        return True

    if state == (42, 7) and action.lower() == "left":
        return True

    if state == (42, 8) and action.lower() == "down":
        return True

    if state == (42, 8) and action.lower() == "left-down":
        return True

    if state == (42, 8) and action.lower() == "left":
        return True

    if state == (42, 10) and action.lower() == "up":
        return True

    if state == (42, 10) and action.lower() == "right":
        return True

    if state == (42, 10) and action.lower() == "right-down":
        return True

    if state == (42, 10) and action.lower() == "down":
        return True

    if state == (42, 11) and action.lower() == "left-up":
        return True

    if state == (42, 11) and action.lower() == "down":
        return True

    if state == (42, 11) and action.lower() == "left-down":
        return True

    if state == (42, 11) and action.lower() == "left":
        return True

    if state == (42, 15) and action.lower() == "left-up":
        return True

    if state == (42, 15) and action.lower() == "up":
        return True

    if state == (42, 15) and action.lower() == "right-down":
        return True

    if state == (42, 15) and action.lower() == "left-down":
        return True

    if state == (42, 17) and action.lower() == "up":
        return True

    if state == (42, 17) and action.lower() == "right-up":
        return True

    if state == (42, 17) and action.lower() == "down":
        return True

    if state == (42, 17) and action.lower() == "left-down":
        return True

    if state == (42, 19) and action.lower() == "left-up":
        return True

    if state == (42, 19) and action.lower() == "right":
        return True

    if state == (42, 20) and action.lower() == "right":
        return True

    if state == (42, 20) and action.lower() == "right-down":
        return True

    if state == (42, 20) and action.lower() == "left":
        return True

    if state == (42, 21) and action.lower() == "right-up":
        return True

    if state == (42, 21) and action.lower() == "right":
        return True

    if state == (42, 21) and action.lower() == "right-down":
        return True

    if state == (42, 21) and action.lower() == "down":
        return True

    if state == (42, 21) and action.lower() == "left":
        return True

    if state == (42, 22) and action.lower() == "up":
        return True

    if state == (42, 22) and action.lower() == "right-down":
        return True

    if state == (42, 22) and action.lower() == "down":
        return True

    if state == (42, 22) and action.lower() == "left-down":
        return True

    if state == (42, 22) and action.lower() == "left":
        return True

    if state == (42, 26) and action.lower() == "up":
        return True

    if state == (42, 28) and action.lower() == "right-up":
        return True

    if state == (42, 28) and action.lower() == "right-down":
        return True

    if state == (42, 28) and action.lower() == "down":
        return True

    if state == (42, 30) and action.lower() == "left-up":
        return True

    if state == (42, 30) and action.lower() == "up":
        return True

    if state == (42, 30) and action.lower() == "left-down":
        return True

    if state == (42, 32) and action.lower() == "right-up":
        return True

    if state == (42, 35) and action.lower() == "up":
        return True

    if state == (42, 35) and action.lower() == "right-up":
        return True

    if state == (42, 35) and action.lower() == "right":
        return True

    if state == (42, 35) and action.lower() == "right-down":
        return True

    if state == (42, 36) and action.lower() == "left-up":
        return True

    if state == (42, 36) and action.lower() == "up":
        return True

    if state == (42, 36) and action.lower() == "right":
        return True

    if state == (42, 36) and action.lower() == "down":
        return True

    if state == (42, 36) and action.lower() == "left":
        return True

    if state == (42, 37) and action.lower() == "left-up":
        return True

    if state == (42, 37) and action.lower() == "right-up":
        return True

    if state == (42, 37) and action.lower() == "left-down":
        return True

    if state == (42, 37) and action.lower() == "left":
        return True

    if state == (42, 39) and action.lower() == "left-up":
        return True

    if state == (42, 39) and action.lower() == "up":
        return True

    if state == (42, 39) and action.lower() == "right-up":
        return True

    if state == (42, 39) and action.lower() == "right":
        return True

    if state == (42, 40) and action.lower() == "left-up":
        return True

    if state == (42, 40) and action.lower() == "up":
        return True

    if state == (42, 40) and action.lower() == "right-up":
        return True

    if state == (42, 40) and action.lower() == "right":
        return True

    if state == (42, 40) and action.lower() == "left":
        return True

    if state == (42, 41) and action.lower() == "left-up":
        return True

    if state == (42, 41) and action.lower() == "up":
        return True

    if state == (42, 41) and action.lower() == "left":
        return True

    if state == (42, 43) and action.lower() == "up":
        return True

    if state == (42, 46) and action.lower() == "right-up":
        return True

    if state == (42, 46) and action.lower() == "down":
        return True

    if state == (42, 46) and action.lower() == "left-down":
        return True

    if state == (42, 48) and action.lower() == "left-up":
        return True

    if state == (42, 48) and action.lower() == "up":
        return True

    if state == (42, 48) and action.lower() == "right-up":
        return True

    if state == (42, 48) and action.lower() == "right":
        return True

    if state == (42, 49) and action.lower() == "left-up":
        return True

    if state == (42, 49) and action.lower() == "up":
        return True

    if state == (42, 49) and action.lower() == "right-down":
        return True

    if state == (42, 49) and action.lower() == "left":
        return True

    if state == (42, 51) and action.lower() == "up":
        return True

    if state == (42, 51) and action.lower() == "left-down":
        return True

    if state == (43, 2) and action.lower() == "up":
        return True

    if state == (43, 2) and action.lower() == "right":
        return True

    if state == (43, 2) and action.lower() == "down":
        return True

    if state == (43, 3) and action.lower() == "left-up":
        return True

    if state == (43, 3) and action.lower() == "right-up":
        return True

    if state == (43, 3) and action.lower() == "left-down":
        return True

    if state == (43, 3) and action.lower() == "left":
        return True

    if state == (43, 5) and action.lower() == "left-up":
        return True

    if state == (43, 5) and action.lower() == "right-up":
        return True

    if state == (43, 5) and action.lower() == "right":
        return True

    if state == (43, 5) and action.lower() == "right-down":
        return True

    if state == (43, 6) and action.lower() == "up":
        return True

    if state == (43, 6) and action.lower() == "right-up":
        return True

    if state == (43, 6) and action.lower() == "right":
        return True

    if state == (43, 6) and action.lower() == "down":
        return True

    if state == (43, 6) and action.lower() == "left":
        return True

    if state == (43, 7) and action.lower() == "left-up":
        return True

    if state == (43, 7) and action.lower() == "up":
        return True

    if state == (43, 7) and action.lower() == "right-up":
        return True

    if state == (43, 7) and action.lower() == "right":
        return True

    if state == (43, 7) and action.lower() == "right-down":
        return True

    if state == (43, 7) and action.lower() == "left-down":
        return True

    if state == (43, 7) and action.lower() == "left":
        return True

    if state == (43, 8) and action.lower() == "left-up":
        return True

    if state == (43, 8) and action.lower() == "up":
        return True

    if state == (43, 8) and action.lower() == "right-down":
        return True

    if state == (43, 8) and action.lower() == "down":
        return True

    if state == (43, 8) and action.lower() == "left":
        return True

    if state == (43, 10) and action.lower() == "up":
        return True

    if state == (43, 10) and action.lower() == "right-up":
        return True

    if state == (43, 10) and action.lower() == "right":
        return True

    if state == (43, 10) and action.lower() == "left-down":
        return True

    if state == (43, 11) and action.lower() == "left-up":
        return True

    if state == (43, 11) and action.lower() == "up":
        return True

    if state == (43, 11) and action.lower() == "right-down":
        return True

    if state == (43, 11) and action.lower() == "left":
        return True

    if state == (43, 14) and action.lower() == "right-up":
        return True

    if state == (43, 14) and action.lower() == "left-down":
        return True

    if state == (43, 16) and action.lower() == "left-up":
        return True

    if state == (43, 16) and action.lower() == "right-up":
        return True

    if state == (43, 16) and action.lower() == "right":
        return True

    if state == (43, 17) and action.lower() == "up":
        return True

    if state == (43, 17) and action.lower() == "left":
        return True

    if state == (43, 21) and action.lower() == "left-up":
        return True

    if state == (43, 21) and action.lower() == "up":
        return True

    if state == (43, 21) and action.lower() == "right-up":
        return True

    if state == (43, 21) and action.lower() == "right":
        return True

    if state == (43, 21) and action.lower() == "right-down":
        return True

    if state == (43, 21) and action.lower() == "left-down":
        return True

    if state == (43, 22) and action.lower() == "left-up":
        return True

    if state == (43, 22) and action.lower() == "up":
        return True

    if state == (43, 22) and action.lower() == "right":
        return True

    if state == (43, 22) and action.lower() == "down":
        return True

    if state == (43, 22) and action.lower() == "left":
        return True

    if state == (43, 23) and action.lower() == "left-up":
        return True

    if state == (43, 23) and action.lower() == "left-down":
        return True

    if state == (43, 23) and action.lower() == "left":
        return True

    if state == (43, 28) and action.lower() == "up":
        return True

    if state == (43, 28) and action.lower() == "right":
        return True

    if state == (43, 28) and action.lower() == "down":
        return True

    if state == (43, 28) and action.lower() == "left-down":
        return True

    if state == (43, 29) and action.lower() == "left-up":
        return True

    if state == (43, 29) and action.lower() == "right-up":
        return True

    if state == (43, 29) and action.lower() == "left-down":
        return True

    if state == (43, 29) and action.lower() == "left":
        return True

    if state == (43, 36) and action.lower() == "left-up":
        return True

    if state == (43, 36) and action.lower() == "up":
        return True

    if state == (43, 36) and action.lower() == "right-up":
        return True

    if state == (43, 36) and action.lower() == "down":
        return True

    if state == (43, 36) and action.lower() == "left-down":
        return True

    if state == (43, 45) and action.lower() == "right-up":
        return True

    if state == (43, 45) and action.lower() == "right":
        return True

    if state == (43, 45) and action.lower() == "left-down":
        return True

    if state == (43, 46) and action.lower() == "up":
        return True

    if state == (43, 46) and action.lower() == "right-down":
        return True

    if state == (43, 46) and action.lower() == "left":
        return True

    if state == (43, 50) and action.lower() == "left-up":
        return True

    if state == (43, 50) and action.lower() == "right-up":
        return True

    if state == (44, 2) and action.lower() == "up":
        return True

    if state == (44, 2) and action.lower() == "right-up":
        return True

    if state == (44, 2) and action.lower() == "right-down":
        return True

    if state == (44, 6) and action.lower() == "left-up":
        return True

    if state == (44, 6) and action.lower() == "up":
        return True

    if state == (44, 6) and action.lower() == "right-up":
        return True

    if state == (44, 6) and action.lower() == "left-down":
        return True

    if state == (44, 8) and action.lower() == "left-up":
        return True

    if state == (44, 8) and action.lower() == "up":
        return True

    if state == (44, 8) and action.lower() == "right":
        return True

    if state == (44, 8) and action.lower() == "right-down":
        return True

    if state == (44, 8) and action.lower() == "down":
        return True

    if state == (44, 9) and action.lower() == "left-up":
        return True

    if state == (44, 9) and action.lower() == "right-up":
        return True

    if state == (44, 9) and action.lower() == "down":
        return True

    if state == (44, 9) and action.lower() == "left-down":
        return True

    if state == (44, 9) and action.lower() == "left":
        return True

    if state == (44, 12) and action.lower() == "left-up":
        return True

    if state == (44, 12) and action.lower() == "right":
        return True

    if state == (44, 12) and action.lower() == "right-down":
        return True

    if state == (44, 13) and action.lower() == "right-up":
        return True

    if state == (44, 13) and action.lower() == "down":
        return True

    if state == (44, 13) and action.lower() == "left":
        return True

    if state == (44, 20) and action.lower() == "right-up":
        return True

    if state == (44, 20) and action.lower() == "left-down":
        return True

    if state == (44, 22) and action.lower() == "left-up":
        return True

    if state == (44, 22) and action.lower() == "up":
        return True

    if state == (44, 22) and action.lower() == "right-up":
        return True

    if state == (44, 22) and action.lower() == "down":
        return True

    if state == (44, 25) and action.lower() == "right-down":
        return True

    if state == (44, 25) and action.lower() == "down":
        return True

    if state == (44, 25) and action.lower() == "left-down":
        return True

    if state == (44, 27) and action.lower() == "right-up":
        return True

    if state == (44, 27) and action.lower() == "right":
        return True

    if state == (44, 27) and action.lower() == "down":
        return True

    if state == (44, 27) and action.lower() == "left-down":
        return True

    if state == (44, 28) and action.lower() == "up":
        return True

    if state == (44, 28) and action.lower() == "right-up":
        return True

    if state == (44, 28) and action.lower() == "right-down":
        return True

    if state == (44, 28) and action.lower() == "left-down":
        return True

    if state == (44, 28) and action.lower() == "left":
        return True

    if state == (44, 31) and action.lower() == "down":
        return True

    if state == (44, 34) and action.lower() == "right":
        return True

    if state == (44, 34) and action.lower() == "right-down":
        return True

    if state == (44, 35) and action.lower() == "right-up":
        return True

    if state == (44, 35) and action.lower() == "right":
        return True

    if state == (44, 35) and action.lower() == "right-down":
        return True

    if state == (44, 35) and action.lower() == "down":
        return True

    if state == (44, 35) and action.lower() == "left":
        return True

    if state == (44, 36) and action.lower() == "up":
        return True

    if state == (44, 36) and action.lower() == "right-down":
        return True

    if state == (44, 36) and action.lower() == "down":
        return True

    if state == (44, 36) and action.lower() == "left-down":
        return True

    if state == (44, 36) and action.lower() == "left":
        return True

    if state == (44, 41) and action.lower() == "right":
        return True

    if state == (44, 41) and action.lower() == "right-down":
        return True

    if state == (44, 41) and action.lower() == "left-down":
        return True

    if state == (44, 42) and action.lower() == "right":
        return True

    if state == (44, 42) and action.lower() == "right-down":
        return True

    if state == (44, 42) and action.lower() == "down":
        return True

    if state == (44, 42) and action.lower() == "left":
        return True

    if state == (44, 43) and action.lower() == "right":
        return True

    if state == (44, 43) and action.lower() == "down":
        return True

    if state == (44, 43) and action.lower() == "left-down":
        return True

    if state == (44, 43) and action.lower() == "left":
        return True

    if state == (44, 44) and action.lower() == "right-up":
        return True

    if state == (44, 44) and action.lower() == "left-down":
        return True

    if state == (44, 44) and action.lower() == "left":
        return True

    if state == (44, 47) and action.lower() == "left-up":
        return True

    if state == (44, 47) and action.lower() == "right-down":
        return True

    if state == (45, 0) and action.lower() == "down":
        return True

    if state == (45, 3) and action.lower() == "left-up":
        return True

    if state == (45, 3) and action.lower() == "right-down":
        return True

    if state == (45, 5) and action.lower() == "right-up":
        return True

    if state == (45, 5) and action.lower() == "down":
        return True

    if state == (45, 5) and action.lower() == "left-down":
        return True

    if state == (45, 8) and action.lower() == "up":
        return True

    if state == (45, 8) and action.lower() == "right-up":
        return True

    if state == (45, 8) and action.lower() == "right":
        return True

    if state == (45, 8) and action.lower() == "down":
        return True

    if state == (45, 9) and action.lower() == "left-up":
        return True

    if state == (45, 9) and action.lower() == "up":
        return True

    if state == (45, 9) and action.lower() == "left-down":
        return True

    if state == (45, 9) and action.lower() == "left":
        return True

    if state == (45, 13) and action.lower() == "left-up":
        return True

    if state == (45, 13) and action.lower() == "up":
        return True

    if state == (45, 13) and action.lower() == "right-down":
        return True

    if state == (45, 13) and action.lower() == "down":
        return True

    if state == (45, 18) and action.lower() == "right":
        return True

    if state == (45, 18) and action.lower() == "right-down":
        return True

    if state == (45, 19) and action.lower() == "right-up":
        return True

    if state == (45, 19) and action.lower() == "right-down":
        return True

    if state == (45, 19) and action.lower() == "down":
        return True

    if state == (45, 19) and action.lower() == "left":
        return True

    if state == (45, 22) and action.lower() == "up":
        return True

    if state == (45, 22) and action.lower() == "down":
        return True

    if state == (45, 24) and action.lower() == "right-up":
        return True

    if state == (45, 24) and action.lower() == "right":
        return True

    if state == (45, 25) and action.lower() == "up":
        return True

    if state == (45, 25) and action.lower() == "right":
        return True

    if state == (45, 25) and action.lower() == "left":
        return True

    if state == (45, 26) and action.lower() == "left-up":
        return True

    if state == (45, 26) and action.lower() == "right-up":
        return True

    if state == (45, 26) and action.lower() == "right":
        return True

    if state == (45, 26) and action.lower() == "right-down":
        return True

    if state == (45, 26) and action.lower() == "left":
        return True

    if state == (45, 27) and action.lower() == "up":
        return True

    if state == (45, 27) and action.lower() == "right-up":
        return True

    if state == (45, 27) and action.lower() == "right-down":
        return True

    if state == (45, 27) and action.lower() == "down":
        return True

    if state == (45, 27) and action.lower() == "left":
        return True

    if state == (45, 29) and action.lower() == "left-up":
        return True

    if state == (45, 29) and action.lower() == "down":
        return True

    if state == (45, 29) and action.lower() == "left-down":
        return True

    if state == (45, 31) and action.lower() == "up":
        return True

    if state == (45, 35) and action.lower() == "left-up":
        return True

    if state == (45, 35) and action.lower() == "up":
        return True

    if state == (45, 35) and action.lower() == "right-up":
        return True

    if state == (45, 35) and action.lower() == "right":
        return True

    if state == (45, 36) and action.lower() == "left-up":
        return True

    if state == (45, 36) and action.lower() == "up":
        return True

    if state == (45, 36) and action.lower() == "right":
        return True

    if state == (45, 36) and action.lower() == "left":
        return True

    if state == (45, 37) and action.lower() == "left-up":
        return True

    if state == (45, 37) and action.lower() == "right-down":
        return True

    if state == (45, 37) and action.lower() == "left":
        return True

    if state == (45, 39) and action.lower() == "right":
        return True

    if state == (45, 39) and action.lower() == "right-down":
        return True

    if state == (45, 39) and action.lower() == "down":
        return True

    if state == (45, 39) and action.lower() == "left-down":
        return True

    if state == (45, 40) and action.lower() == "right-up":
        return True

    if state == (45, 40) and action.lower() == "right-down":
        return True

    if state == (45, 40) and action.lower() == "down":
        return True

    if state == (45, 40) and action.lower() == "left-down":
        return True

    if state == (45, 40) and action.lower() == "left":
        return True

    if state == (45, 42) and action.lower() == "left-up":
        return True

    if state == (45, 42) and action.lower() == "up":
        return True

    if state == (45, 42) and action.lower() == "right-up":
        return True

    if state == (45, 42) and action.lower() == "right":
        return True

    if state == (45, 42) and action.lower() == "left-down":
        return True

    if state == (45, 43) and action.lower() == "left-up":
        return True

    if state == (45, 43) and action.lower() == "up":
        return True

    if state == (45, 43) and action.lower() == "right-up":
        return True

    if state == (45, 43) and action.lower() == "right-down":
        return True

    if state == (45, 43) and action.lower() == "left":
        return True

    if state == (45, 48) and action.lower() == "left-up":
        return True

    if state == (45, 48) and action.lower() == "right":
        return True

    if state == (45, 48) and action.lower() == "right-down":
        return True

    if state == (45, 48) and action.lower() == "down":
        return True

    if state == (45, 49) and action.lower() == "right-down":
        return True

    if state == (45, 49) and action.lower() == "down":
        return True

    if state == (45, 49) and action.lower() == "left-down":
        return True

    if state == (45, 49) and action.lower() == "left":
        return True

    if state == (46, 0) and action.lower() == "up":
        return True

    if state == (46, 0) and action.lower() == "right-down":
        return True

    if state == (46, 0) and action.lower() == "down":
        return True

    if state == (46, 4) and action.lower() == "left-up":
        return True

    if state == (46, 4) and action.lower() == "right-up":
        return True

    if state == (46, 4) and action.lower() == "right":
        return True

    if state == (46, 4) and action.lower() == "right-down":
        return True

    if state == (46, 4) and action.lower() == "down":
        return True

    if state == (46, 4) and action.lower() == "left-down":
        return True

    if state == (46, 5) and action.lower() == "up":
        return True

    if state == (46, 5) and action.lower() == "down":
        return True

    if state == (46, 5) and action.lower() == "left-down":
        return True

    if state == (46, 5) and action.lower() == "left":
        return True

    if state == (46, 8) and action.lower() == "up":
        return True

    if state == (46, 8) and action.lower() == "right-up":
        return True

    if state == (46, 8) and action.lower() == "right-down":
        return True

    if state == (46, 8) and action.lower() == "left-down":
        return True

    if state == (46, 13) and action.lower() == "up":
        return True

    if state == (46, 13) and action.lower() == "right":
        return True

    if state == (46, 14) and action.lower() == "left-up":
        return True

    if state == (46, 14) and action.lower() == "left":
        return True

    if state == (46, 16) and action.lower() == "down":
        return True

    if state == (46, 19) and action.lower() == "left-up":
        return True

    if state == (46, 19) and action.lower() == "up":
        return True

    if state == (46, 19) and action.lower() == "right":
        return True

    if state == (46, 19) and action.lower() == "right-down":
        return True

    if state == (46, 19) and action.lower() == "down":
        return True

    if state == (46, 19) and action.lower() == "left-down":
        return True

    if state == (46, 20) and action.lower() == "left-up":
        return True

    if state == (46, 20) and action.lower() == "right-down":
        return True

    if state == (46, 20) and action.lower() == "down":
        return True

    if state == (46, 20) and action.lower() == "left-down":
        return True

    if state == (46, 20) and action.lower() == "left":
        return True

    if state == (46, 22) and action.lower() == "up":
        return True

    if state == (46, 22) and action.lower() == "down":
        return True

    if state == (46, 22) and action.lower() == "left-down":
        return True

    if state == (46, 27) and action.lower() == "left-up":
        return True

    if state == (46, 27) and action.lower() == "up":
        return True

    if state == (46, 27) and action.lower() == "right":
        return True

    if state == (46, 27) and action.lower() == "down":
        return True

    if state == (46, 28) and action.lower() == "left-up":
        return True

    if state == (46, 28) and action.lower() == "right-up":
        return True

    if state == (46, 28) and action.lower() == "right":
        return True

    if state == (46, 28) and action.lower() == "right-down":
        return True

    if state == (46, 28) and action.lower() == "left-down":
        return True

    if state == (46, 28) and action.lower() == "left":
        return True

    if state == (46, 29) and action.lower() == "up":
        return True

    if state == (46, 29) and action.lower() == "right-down":
        return True

    if state == (46, 29) and action.lower() == "down":
        return True

    if state == (46, 29) and action.lower() == "left":
        return True

    if state == (46, 33) and action.lower() == "down":
        return True

    if state == (46, 33) and action.lower() == "left-down":
        return True

    if state == (46, 38) and action.lower() == "left-up":
        return True

    if state == (46, 38) and action.lower() == "right-up":
        return True

    if state == (46, 38) and action.lower() == "right":
        return True

    if state == (46, 39) and action.lower() == "up":
        return True

    if state == (46, 39) and action.lower() == "right-up":
        return True

    if state == (46, 39) and action.lower() == "right":
        return True

    if state == (46, 39) and action.lower() == "right-down":
        return True

    if state == (46, 39) and action.lower() == "left":
        return True

    if state == (46, 40) and action.lower() == "left-up":
        return True

    if state == (46, 40) and action.lower() == "up":
        return True

    if state == (46, 40) and action.lower() == "right":
        return True

    if state == (46, 40) and action.lower() == "down":
        return True

    if state == (46, 40) and action.lower() == "left":
        return True

    if state == (46, 41) and action.lower() == "left-up":
        return True

    if state == (46, 41) and action.lower() == "right-up":
        return True

    if state == (46, 41) and action.lower() == "right-down":
        return True

    if state == (46, 41) and action.lower() == "left-down":
        return True

    if state == (46, 41) and action.lower() == "left":
        return True

    if state == (46, 44) and action.lower() == "left-up":
        return True

    if state == (46, 44) and action.lower() == "right":
        return True

    if state == (46, 44) and action.lower() == "right-down":
        return True

    if state == (46, 44) and action.lower() == "down":
        return True

    if state == (46, 44) and action.lower() == "left-down":
        return True

    if state == (46, 45) and action.lower() == "right-down":
        return True

    if state == (46, 45) and action.lower() == "down":
        return True

    if state == (46, 45) and action.lower() == "left-down":
        return True

    if state == (46, 45) and action.lower() == "left":
        return True

    if state == (46, 48) and action.lower() == "up":
        return True

    if state == (46, 48) and action.lower() == "right-up":
        return True

    if state == (46, 48) and action.lower() == "right":
        return True

    if state == (46, 48) and action.lower() == "right-down":
        return True

    if state == (46, 48) and action.lower() == "left-down":
        return True

    if state == (46, 49) and action.lower() == "left-up":
        return True

    if state == (46, 49) and action.lower() == "up":
        return True

    if state == (46, 49) and action.lower() == "right":
        return True

    if state == (46, 49) and action.lower() == "down":
        return True

    if state == (46, 49) and action.lower() == "left":
        return True

    if state == (46, 50) and action.lower() == "left-up":
        return True

    if state == (46, 50) and action.lower() == "right":
        return True

    if state == (46, 50) and action.lower() == "left-down":
        return True

    if state == (46, 50) and action.lower() == "left":
        return True

    if state == (46, 51) and action.lower() == "left":
        return True

    if state == (47, 0) and action.lower() == "up":
        return True

    if state == (47, 0) and action.lower() == "right":
        return True

    if state == (47, 0) and action.lower() == "right-down":
        return True

    if state == (47, 0) and action.lower() == "down":
        return True

    if state == (47, 1) and action.lower() == "left-up":
        return True

    if state == (47, 1) and action.lower() == "right":
        return True

    if state == (47, 1) and action.lower() == "right-down":
        return True

    if state == (47, 1) and action.lower() == "down":
        return True

    if state == (47, 1) and action.lower() == "left-down":
        return True

    if state == (47, 1) and action.lower() == "left":
        return True

    if state == (47, 2) and action.lower() == "right":
        return True

    if state == (47, 2) and action.lower() == "right-down":
        return True

    if state == (47, 2) and action.lower() == "down":
        return True

    if state == (47, 2) and action.lower() == "left-down":
        return True

    if state == (47, 2) and action.lower() == "left":
        return True

    if state == (47, 3) and action.lower() == "right-up":
        return True

    if state == (47, 3) and action.lower() == "right":
        return True

    if state == (47, 3) and action.lower() == "down":
        return True

    if state == (47, 3) and action.lower() == "left-down":
        return True

    if state == (47, 3) and action.lower() == "left":
        return True

    if state == (47, 4) and action.lower() == "up":
        return True

    if state == (47, 4) and action.lower() == "right-up":
        return True

    if state == (47, 4) and action.lower() == "right":
        return True

    if state == (47, 4) and action.lower() == "left-down":
        return True

    if state == (47, 4) and action.lower() == "left":
        return True

    if state == (47, 5) and action.lower() == "left-up":
        return True

    if state == (47, 5) and action.lower() == "up":
        return True

    if state == (47, 5) and action.lower() == "right-down":
        return True

    if state == (47, 5) and action.lower() == "left":
        return True

    if state == (47, 7) and action.lower() == "right-up":
        return True

    if state == (47, 7) and action.lower() == "left-down":
        return True

    if state == (47, 9) and action.lower() == "left-up":
        return True

    if state == (47, 9) and action.lower() == "down":
        return True

    if state == (47, 11) and action.lower() == "down":
        return True

    if state == (47, 16) and action.lower() == "up":
        return True

    if state == (47, 16) and action.lower() == "down":
        return True

    if state == (47, 16) and action.lower() == "left-down":
        return True

    if state == (47, 18) and action.lower() == "right-up":
        return True

    if state == (47, 18) and action.lower() == "right":
        return True

    if state == (47, 18) and action.lower() == "down":
        return True

    if state == (47, 19) and action.lower() == "up":
        return True

    if state == (47, 19) and action.lower() == "right-up":
        return True

    if state == (47, 19) and action.lower() == "right":
        return True

    if state == (47, 19) and action.lower() == "left-down":
        return True

    if state == (47, 19) and action.lower() == "left":
        return True

    if state == (47, 20) and action.lower() == "left-up":
        return True

    if state == (47, 20) and action.lower() == "up":
        return True

    if state == (47, 20) and action.lower() == "right":
        return True

    if state == (47, 20) and action.lower() == "right-down":
        return True

    if state == (47, 20) and action.lower() == "left":
        return True

    if state == (47, 21) and action.lower() == "left-up":
        return True

    if state == (47, 21) and action.lower() == "right-up":
        return True

    if state == (47, 21) and action.lower() == "right":
        return True

    if state == (47, 21) and action.lower() == "right-down":
        return True

    if state == (47, 21) and action.lower() == "down":
        return True

    if state == (47, 21) and action.lower() == "left":
        return True

    if state == (47, 22) and action.lower() == "up":
        return True

    if state == (47, 22) and action.lower() == "right-down":
        return True

    if state == (47, 22) and action.lower() == "down":
        return True

    if state == (47, 22) and action.lower() == "left-down":
        return True

    if state == (47, 22) and action.lower() == "left":
        return True

    if state == (47, 24) and action.lower() == "right":
        return True

    if state == (47, 24) and action.lower() == "right-down":
        return True

    if state == (47, 24) and action.lower() == "left-down":
        return True

    if state == (47, 25) and action.lower() == "down":
        return True

    if state == (47, 25) and action.lower() == "left":
        return True

    if state == (47, 27) and action.lower() == "up":
        return True

    if state == (47, 27) and action.lower() == "right-up":
        return True

    if state == (47, 27) and action.lower() == "down":
        return True

    if state == (47, 29) and action.lower() == "left-up":
        return True

    if state == (47, 29) and action.lower() == "up":
        return True

    if state == (47, 29) and action.lower() == "right":
        return True

    if state == (47, 29) and action.lower() == "down":
        return True

    if state == (47, 30) and action.lower() == "left-up":
        return True

    if state == (47, 30) and action.lower() == "left-down":
        return True

    if state == (47, 30) and action.lower() == "left":
        return True

    if state == (47, 32) and action.lower() == "right-up":
        return True

    if state == (47, 32) and action.lower() == "right":
        return True

    if state == (47, 33) and action.lower() == "up":
        return True

    if state == (47, 33) and action.lower() == "right-down":
        return True

    if state == (47, 33) and action.lower() == "left":
        return True

    if state == (47, 36) and action.lower() == "right-down":
        return True

    if state == (47, 36) and action.lower() == "down":
        return True

    if state == (47, 40) and action.lower() == "left-up":
        return True

    if state == (47, 40) and action.lower() == "up":
        return True

    if state == (47, 40) and action.lower() == "right-up":
        return True

    if state == (47, 40) and action.lower() == "right-down":
        return True

    if state == (47, 40) and action.lower() == "down":
        return True

    if state == (47, 40) and action.lower() == "left-down":
        return True

    if state == (47, 42) and action.lower() == "left-up":
        return True

    if state == (47, 42) and action.lower() == "right":
        return True

    if state == (47, 42) and action.lower() == "down":
        return True

    if state == (47, 42) and action.lower() == "left-down":
        return True

    if state == (47, 43) and action.lower() == "right-up":
        return True

    if state == (47, 43) and action.lower() == "right":
        return True

    if state == (47, 43) and action.lower() == "left-down":
        return True

    if state == (47, 43) and action.lower() == "left":
        return True

    if state == (47, 44) and action.lower() == "up":
        return True

    if state == (47, 44) and action.lower() == "right-up":
        return True

    if state == (47, 44) and action.lower() == "right":
        return True

    if state == (47, 44) and action.lower() == "right-down":
        return True

    if state == (47, 44) and action.lower() == "left":
        return True

    if state == (47, 45) and action.lower() == "left-up":
        return True

    if state == (47, 45) and action.lower() == "up":
        return True

    if state == (47, 45) and action.lower() == "right":
        return True

    if state == (47, 45) and action.lower() == "down":
        return True

    if state == (47, 45) and action.lower() == "left":
        return True

    if state == (47, 46) and action.lower() == "left-up":
        return True

    if state == (47, 46) and action.lower() == "right":
        return True

    if state == (47, 46) and action.lower() == "right-down":
        return True

    if state == (47, 46) and action.lower() == "left-down":
        return True

    if state == (47, 46) and action.lower() == "left":
        return True

    if state == (47, 47) and action.lower() == "right-up":
        return True

    if state == (47, 47) and action.lower() == "down":
        return True

    if state == (47, 47) and action.lower() == "left":
        return True

    if state == (47, 49) and action.lower() == "left-up":
        return True

    if state == (47, 49) and action.lower() == "up":
        return True

    if state == (47, 49) and action.lower() == "right-up":
        return True

    if state == (47, 49) and action.lower() == "right-down":
        return True

    if state == (47, 49) and action.lower() == "down":
        return True

    if state == (48, 0) and action.lower() == "up":
        return True

    if state == (48, 0) and action.lower() == "right-up":
        return True

    if state == (48, 0) and action.lower() == "right":
        return True

    if state == (48, 1) and action.lower() == "left-up":
        return True

    if state == (48, 1) and action.lower() == "up":
        return True

    if state == (48, 1) and action.lower() == "right-up":
        return True

    if state == (48, 1) and action.lower() == "right":
        return True

    if state == (48, 1) and action.lower() == "left":
        return True

    if state == (48, 2) and action.lower() == "left-up":
        return True

    if state == (48, 2) and action.lower() == "up":
        return True

    if state == (48, 2) and action.lower() == "right-up":
        return True

    if state == (48, 2) and action.lower() == "right":
        return True

    if state == (48, 2) and action.lower() == "left":
        return True

    if state == (48, 3) and action.lower() == "left-up":
        return True

    if state == (48, 3) and action.lower() == "up":
        return True

    if state == (48, 3) and action.lower() == "right-up":
        return True

    if state == (48, 3) and action.lower() == "left":
        return True

    if state == (48, 6) and action.lower() == "left-up":
        return True

    if state == (48, 6) and action.lower() == "right-up":
        return True

    if state == (48, 9) and action.lower() == "up":
        return True

    if state == (48, 11) and action.lower() == "up":
        return True

    if state == (48, 14) and action.lower() == "right":
        return True

    if state == (48, 15) and action.lower() == "right-up":
        return True

    if state == (48, 15) and action.lower() == "right":
        return True

    if state == (48, 15) and action.lower() == "left":
        return True

    if state == (48, 16) and action.lower() == "up":
        return True

    if state == (48, 16) and action.lower() == "left":
        return True

    if state == (48, 18) and action.lower() == "up":
        return True

    if state == (48, 18) and action.lower() == "right-up":
        return True

    if state == (48, 21) and action.lower() == "left-up":
        return True

    if state == (48, 21) and action.lower() == "up":
        return True

    if state == (48, 21) and action.lower() == "right-up":
        return True

    if state == (48, 21) and action.lower() == "right":
        return True

    if state == (48, 22) and action.lower() == "left-up":
        return True

    if state == (48, 22) and action.lower() == "up":
        return True

    if state == (48, 22) and action.lower() == "right":
        return True

    if state == (48, 22) and action.lower() == "left":
        return True

    if state == (48, 23) and action.lower() == "left-up":
        return True

    if state == (48, 23) and action.lower() == "right-up":
        return True

    if state == (48, 23) and action.lower() == "left":
        return True

    if state == (48, 25) and action.lower() == "left-up":
        return True

    if state == (48, 25) and action.lower() == "up":
        return True

    if state == (48, 27) and action.lower() == "up":
        return True

    if state == (48, 29) and action.lower() == "up":
        return True

    if state == (48, 29) and action.lower() == "right-up":
        return True

    if state == (48, 34) and action.lower() == "left-up":
        return True

    if state == (48, 36) and action.lower() == "up":
        return True

    if state == (48, 36) and action.lower() == "right":
        return True

    if state == (48, 37) and action.lower() == "left-up":
        return True

    if state == (48, 37) and action.lower() == "right":
        return True

    if state == (48, 37) and action.lower() == "left":
        return True

    if state == (48, 38) and action.lower() == "right":
        return True

    if state == (48, 38) and action.lower() == "left":
        return True

    if state == (48, 39) and action.lower() == "right-up":
        return True

    if state == (48, 39) and action.lower() == "right":
        return True

    if state == (48, 39) and action.lower() == "left":
        return True

    if state == (48, 40) and action.lower() == "up":
        return True

    if state == (48, 40) and action.lower() == "right":
        return True

    if state == (48, 40) and action.lower() == "left":
        return True

    if state == (48, 41) and action.lower() == "left-up":
        return True

    if state == (48, 41) and action.lower() == "right-up":
        return True

    if state == (48, 41) and action.lower() == "right":
        return True

    if state == (48, 41) and action.lower() == "left":
        return True

    if state == (48, 42) and action.lower() == "up":
        return True

    if state == (48, 42) and action.lower() == "right-up":
        return True

    if state == (48, 42) and action.lower() == "left":
        return True

    if state == (48, 45) and action.lower() == "left-up":
        return True

    if state == (48, 45) and action.lower() == "up":
        return True

    if state == (48, 45) and action.lower() == "right-up":
        return True

    if state == (48, 47) and action.lower() == "left-up":
        return True

    if state == (48, 47) and action.lower() == "up":
        return True

    if state == (48, 49) and action.lower() == "up":
        return True

    if state == (48, 49) and action.lower() == "right":
        return True

    if state == (48, 50) and action.lower() == "left-up":
        return True

    if state == (48, 50) and action.lower() == "left":
        return True

    return False




def K(state, action):

    if (state[0] < 0 or state[0] >= 49) or (state[1] < 0 or state[1] >= 52):
        raise Exception("The input state is not among the grid states.")

    if action.lower() not in ["up", "left-up", "right-up", "right", "right-down", "down", "left-down", "left"]:
        raise Exception("The input action is not among the actions that can be performed.")

    if state == (43, 50) and action.lower() == "left-up":
        return True

    if state == (15, 1) and action.lower() == "right-down":
        return True

    if state == (30, 24) and action.lower() == "right-down":
        return True

    if state == (16, 36) and action.lower() == "left":
        return True

    if state == (38, 22) and action.lower() == "up":
        return True

    if state == (24, 15) and action.lower() == "left-down":
        return True

    if state == (20, 9) and action.lower() == "right-up":
        return True

    if state == (47, 44) and action.lower() == "right-up":
        return True

    if state == (8, 50) and action.lower() == "left-up":
        return True

    if state == (2, 34) and action.lower() == "left-down":
        return True

    if state == (41, 29) and action.lower() == "right-up":
        return True

    if state == (48, 9) and action.lower() == "up":
        return True

    if state == (40, 15) and action.lower() == "right":
        return True

    if state == (11, 40) and action.lower() == "left":
        return True

    if state == (45, 3) and action.lower() == "right-down":
        return True

    if state == (14, 6) and action.lower() == "left":
        return True

    if state == (47, 0) and action.lower() == "right":
        return True

    if state == (21, 17) and action.lower() == "right":
        return True

    if state == (42, 4) and action.lower() == "right-up":
        return True

    if state == (19, 5) and action.lower() == "right-up":
        return True

    if state == (8, 28) and action.lower() == "left-down":
        return True

    if state == (14, 34) and action.lower() == "left-down":
        return True

    if state == (19, 50) and action.lower() == "right-up":
        return True

    if state == (37, 33) and action.lower() == "right-down":
        return True

    if state == (11, 49) and action.lower() == "left-down":
        return True

    if state == (19, 10) and action.lower() == "right-down":
        return True

    if state == (36, 36) and action.lower() == "right-down":
        return True

    if state == (12, 8) and action.lower() == "right-down":
        return True

    if state == (29, 10) and action.lower() == "left":
        return True

    if state == (43, 21) and action.lower() == "left-up":
        return True

    if state == (7, 34) and action.lower() == "left":
        return True

    if state == (0, 10) and action.lower() == "down":
        return True

    if state == (3, 21) and action.lower() == "left-down":
        return True

    if state == (6, 49) and action.lower() == "left-down":
        return True

    if state == (35, 1) and action.lower() == "right-up":
        return True

    if state == (24, 36) and action.lower() == "right":
        return True

    if state == (9, 3) and action.lower() == "left-up":
        return True

    if state == (4, 17) and action.lower() == "right-down":
        return True

    if state == (7, 5) and action.lower() == "left-down":
        return True

    if state == (46, 48) and action.lower() == "right-down":
        return True

    if state == (38, 31) and action.lower() == "right-down":
        return True

    if state == (24, 23) and action.lower() == "left":
        return True

    if state == (40, 27) and action.lower() == "right-up":
        return True

    if state == (14, 27) and action.lower() == "left-down":
        return True

    if state == (9, 29) and action.lower() == "left-down":
        return True

    if state == (33, 44) and action.lower() == "left-down":
        return True

    if state == (19, 41) and action.lower() == "left-up":
        return True

    if state == (47, 40) and action.lower() == "right-down":
        return True

    if state == (15, 33) and action.lower() == "left-down":
        return True

    if state == (29, 44) and action.lower() == "left-down":
        return True

    if state == (25, 43) and action.lower() == "down":
        return True

    if state == (45, 25) and action.lower() == "right":
        return True

    if state == (6, 10) and action.lower() == "left-up":
        return True

    if state == (27, 39) and action.lower() == "right-up":
        return True

    if state == (39, 32) and action.lower() == "right":
        return True

    if state == (48, 1) and action.lower() == "right":
        return True

    if state == (39, 11) and action.lower() == "up":
        return True

    if state == (6, 4) and action.lower() == "down":
        return True

    if state == (34, 15) and action.lower() == "right":
        return True

    if state == (0, 44) and action.lower() == "left-down":
        return True

    if state == (4, 25) and action.lower() == "down":
        return True

    if state == (12, 50) and action.lower() == "left-down":
        return True

    if state == (0, 47) and action.lower() == "left-down":
        return True

    if state == (23, 3) and action.lower() == "right-down":
        return True

    if state == (45, 24) and action.lower() == "right-up":
        return True

    if state == (5, 24) and action.lower() == "right-down":
        return True

    if state == (41, 36) and action.lower() == "left-down":
        return True

    if state == (11, 44) and action.lower() == "right-down":
        return True

    if state == (15, 24) and action.lower() == "left-down":
        return True

    if state == (6, 25) and action.lower() == "down":
        return True

    if state == (1, 39) and action.lower() == "down":
        return True

    if state == (16, 46) and action.lower() == "left-down":
        return True

    if state == (8, 48) and action.lower() == "left-down":
        return True

    if state == (27, 42) and action.lower() == "down":
        return True

    if state == (31, 0) and action.lower() == "right-down":
        return True

    if state == (33, 27) and action.lower() == "right-down":
        return True

    if state == (38, 28) and action.lower() == "right":
        return True

    if state == (25, 38) and action.lower() == "right":
        return True

    if state == (28, 37) and action.lower() == "right-down":
        return True

    if state == (20, 1) and action.lower() == "right-up":
        return True

    if state == (21, 23) and action.lower() == "left":
        return True

    if state == (12, 22) and action.lower() == "left-down":
        return True

    if state == (26, 3) and action.lower() == "left":
        return True

    if state == (40, 49) and action.lower() == "left-down":
        return True

    if state == (9, 33) and action.lower() == "right-down":
        return True

    if state == (16, 42) and action.lower() == "left":
        return True

    if state == (10, 16) and action.lower() == "right":
        return True

    if state == (4, 21) and action.lower() == "left-down":
        return True

    if state == (36, 47) and action.lower() == "down":
        return True

    if state == (24, 4) and action.lower() == "right-up":
        return True

    if state == (16, 14) and action.lower() == "right-up":
        return True

    if state == (33, 48) and action.lower() == "left-down":
        return True

    if state == (31, 1) and action.lower() == "right":
        return True

    if state == (44, 2) and action.lower() == "right-up":
        return True

    if state == (48, 38) and action.lower() == "right":
        return True

    if state == (17, 38) and action.lower() == "left":
        return True

    if state == (43, 5) and action.lower() == "right":
        return True

    if state == (15, 32) and action.lower() == "down":
        return True

    if state == (33, 7) and action.lower() == "down":
        return True

    if state == (21, 9) and action.lower() == "right-up":
        return True

    if state == (9, 40) and action.lower() == "left-down":
        return True

    if state == (3, 42) and action.lower() == "left":
        return True

    if state == (10, 50) and action.lower() == "left-down":
        return True

    if state == (39, 15) and action.lower() == "right-down":
        return True

    if state == (44, 20) and action.lower() == "right-up":
        return True

    if state == (18, 4) and action.lower() == "right-down":
        return True

    if state == (19, 33) and action.lower() == "left-up":
        return True

    if state == (37, 40) and action.lower() == "right":
        return True

    if state == (42, 49) and action.lower() == "left":
        return True

    if state == (40, 40) and action.lower() == "left":
        return True

    if state == (14, 48) and action.lower() == "left":
        return True

    if state == (23, 13) and action.lower() == "down":
        return True

    if state == (30, 20) and action.lower() == "right-up":
        return True

    if state == (36, 48) and action.lower() == "left-down":
        return True

    if state == (6, 28) and action.lower() == "left-down":
        return True

    if state == (13, 21) and action.lower() == "right-down":
        return True

    if state == (31, 26) and action.lower() == "down":
        return True

    if state == (10, 17) and action.lower() == "right-down":
        return True

    if state == (34, 28) and action.lower() == "right-down":
        return True

    if state == (19, 22) and action.lower() == "down":
        return True

    if state == (33, 49) and action.lower() == "right-down":
        return True

    if state == (2, 42) and action.lower() == "left-down":
        return True

    if state == (18, 46) and action.lower() == "left":
        return True

    if state == (5, 34) and action.lower() == "right-down":
        return True

    if state == (30, 21) and action.lower() == "right-up":
        return True

    if state == (45, 19) and action.lower() == "right-up":
        return True

    if state == (5, 23) and action.lower() == "left-down":
        return True

    if state == (4, 0) and action.lower() == "down":
        return True

    if state == (36, 50) and action.lower() == "left-down":
        return True

    if state == (1, 37) and action.lower() == "left-down":
        return True

    if state == (9, 2) and action.lower() == "left":
        return True

    if state == (16, 3) and action.lower() == "down":
        return True

    if state == (3, 8) and action.lower() == "down":
        return True

    if state == (1, 43) and action.lower() == "left-down":
        return True

    if state == (15, 38) and action.lower() == "left-up":
        return True

    if state == (5, 46) and action.lower() == "left":
        return True

    if state == (45, 8) and action.lower() == "right-up":
        return True

    if state == (23, 41) and action.lower() == "down":
        return True

    if state == (29, 16) and action.lower() == "right-down":
        return True

    if state == (5, 45) and action.lower() == "left-down":
        return True

    if state == (9, 37) and action.lower() == "left":
        return True

    if state == (18, 0) and action.lower() == "right-up":
        return True

    if state == (13, 43) and action.lower() == "left-down":
        return True

    if state == (10, 39) and action.lower() == "left-up":
        return True

    if state == (31, 47) and action.lower() == "left-down":
        return True

    if state == (16, 28) and action.lower() == "left-down":
        return True

    if state == (1, 33) and action.lower() == "right-down":
        return True

    if state == (14, 16) and action.lower() == "left-up":
        return True

    if state == (30, 33) and action.lower() == "right-down":
        return True

    if state == (29, 7) and action.lower() == "left-down":
        return True

    if state == (14, 19) and action.lower() == "left-down":
        return True

    if state == (35, 51) and action.lower() == "left-down":
        return True

    if state == (18, 6) and action.lower() == "right-down":
        return True

    if state == (22, 43) and action.lower() == "up":
        return True

    if state == (12, 19) and action.lower() == "right":
        return True

    if state == (24, 41) and action.lower() == "down":
        return True

    if state == (28, 17) and action.lower() == "right-up":
        return True

    if state == (30, 6) and action.lower() == "right-down":
        return True

    if state == (32, 18) and action.lower() == "right":
        return True

    if state == (16, 2) and action.lower() == "right-down":
        return True

    if state == (21, 5) and action.lower() == "down":
        return True

    if state == (43, 22) and action.lower() == "left":
        return True

    if state == (14, 47) and action.lower() == "left":
        return True

    if state == (42, 46) and action.lower() == "down":
        return True

    if state == (15, 41) and action.lower() == "left":
        return True

    if state == (31, 42) and action.lower() == "right-down":
        return True

    if state == (28, 13) and action.lower() == "right-down":
        return True

    if state == (30, 51) and action.lower() == "down":
        return True

    if state == (30, 44) and action.lower() == "right-down":
        return True

    if state == (31, 40) and action.lower() == "right":
        return True

    if state == (13, 28) and action.lower() == "left-down":
        return True

    if state == (30, 30) and action.lower() == "right-up":
        return True

    if state == (17, 7) and action.lower() == "left-down":
        return True

    if state == (18, 44) and action.lower() == "left":
        return True

    if state == (19, 6) and action.lower() == "right":
        return True

    if state == (38, 36) and action.lower() == "right-up":
        return True

    if state == (11, 15) and action.lower() == "right-up":
        return True

    if state == (23, 35) and action.lower() == "right-down":
        return True

    if state == (27, 8) and action.lower() == "left-down":
        return True

    if state == (24, 34) and action.lower() == "right-down":
        return True

    if state == (33, 47) and action.lower() == "down":
        return True

    if state == (9, 20) and action.lower() == "left-down":
        return True

    if state == (9, 18) and action.lower() == "right-down":
        return True

    if state == (47, 24) and action.lower() == "left-down":
        return True

    if state == (11, 45) and action.lower() == "down":
        return True

    if state == (42, 30) and action.lower() == "up":
        return True

    if state == (14, 11) and action.lower() == "up":
        return True

    if state == (30, 16) and action.lower() == "right":
        return True

    if state == (34, 3) and action.lower() == "right":
        return True

    if state == (35, 16) and action.lower() == "up":
        return True

    if state == (4, 40) and action.lower() == "left-down":
        return True

    if state == (37, 25) and action.lower() == "right":
        return True

    if state == (12, 51) and action.lower() == "left":
        return True

    if state == (1, 18) and action.lower() == "right":
        return True

    if state == (31, 27) and action.lower() == "left-down":
        return True

    if state == (9, 21) and action.lower() == "left":
        return True

    if state == (31, 18) and action.lower() == "right-down":
        return True

    if state == (24, 26) and action.lower() == "down":
        return True

    if state == (46, 29) and action.lower() == "up":
        return True

    if state == (39, 36) and action.lower() == "left-down":
        return True

    if state == (3, 33) and action.lower() == "down":
        return True

    if state == (41, 2) and action.lower() == "right":
        return True

    if state == (48, 3) and action.lower() == "right-up":
        return True

    if state == (20, 22) and action.lower() == "left-down":
        return True

    if state == (20, 19) and action.lower() == "down":
        return True

    if state == (30, 46) and action.lower() == "left-down":
        return True

    if state == (48, 40) and action.lower() == "right":
        return True

    if state == (39, 51) and action.lower() == "left":
        return True

    if state == (33, 15) and action.lower() == "right-up":
        return True

    if state == (20, 13) and action.lower() == "down":
        return True

    if state == (45, 29) and action.lower() == "left-up":
        return True

    if state == (29, 9) and action.lower() == "left-down":
        return True

    if state == (30, 37) and action.lower() == "right-up":
        return True

    if state == (35, 43) and action.lower() == "right-down":
        return True

    if state == (5, 20) and action.lower() == "down":
        return True

    if state == (35, 12) and action.lower() == "right":
        return True

    if state == (23, 5) and action.lower() == "right-down":
        return True

    if state == (34, 34) and action.lower() == "right-up":
        return True

    if state == (38, 51) and action.lower() == "left-down":
        return True

    if state == (30, 40) and action.lower() == "right-down":
        return True

    if state == (23, 33) and action.lower() == "right-down":
        return True

    if state == (42, 2) and action.lower() == "right-up":
        return True

    if state == (47, 36) and action.lower() == "right-down":
        return True

    if state == (18, 20) and action.lower() == "left-up":
        return True

    if state == (32, 50) and action.lower() == "left-down":
        return True

    if state == (45, 9) and action.lower() == "up":
        return True

    if state == (42, 22) and action.lower() == "left-down":
        return True

    if state == (13, 9) and action.lower() == "right-down":
        return True

    if state == (2, 21) and action.lower() == "left-down":
        return True

    if state == (34, 10) and action.lower() == "right-down":
        return True

    if state == (33, 40) and action.lower() == "left-down":
        return True

    if state == (42, 26) and action.lower() == "up":
        return True

    if state == (13, 15) and action.lower() == "left-up":
        return True

    if state == (42, 8) and action.lower() == "down":
        return True

    if state == (27, 11) and action.lower() == "up":
        return True

    if state == (7, 42) and action.lower() == "down":
        return True

    if state == (23, 46) and action.lower() == "down":
        return True

    if state == (7, 25) and action.lower() == "right-down":
        return True

    if state == (27, 15) and action.lower() == "right":
        return True

    if state == (37, 26) and action.lower() == "right-up":
        return True

    if state == (28, 29) and action.lower() == "right-down":
        return True

    if state == (3, 0) and action.lower() == "down":
        return True

    if state == (25, 45) and action.lower() == "left":
        return True

    if state == (10, 47) and action.lower() == "left-down":
        return True

    if state == (25, 41) and action.lower() == "down":
        return True

    if state == (29, 4) and action.lower() == "right-down":
        return True

    if state == (25, 35) and action.lower() == "right-down":
        return True

    if state == (47, 27) and action.lower() == "up":
        return True

    if state == (5, 0) and action.lower() == "right-down":
        return True

    if state == (35, 2) and action.lower() == "right-up":
        return True

    if state == (2, 14) and action.lower() == "right-down":
        return True

    if state == (39, 1) and action.lower() == "down":
        return True

    if state == (4, 42) and action.lower() == "left-up":
        return True

    if state == (29, 21) and action.lower() == "right-up":
        return True

    if state == (33, 25) and action.lower() == "right-up":
        return True

    if state == (41, 41) and action.lower() == "left":
        return True

    if state == (30, 14) and action.lower() == "down":
        return True

    if state == (46, 19) and action.lower() == "up":
        return True

    if state == (32, 34) and action.lower() == "right-down":
        return True

    if state == (35, 33) and action.lower() == "right-up":
        return True

    if state == (45, 22) and action.lower() == "up":
        return True

    if state == (42, 28) and action.lower() == "right-up":
        return True

    if state == (22, 35) and action.lower() == "down":
        return True

    if state == (23, 15) and action.lower() == "down":
        return True

    if state == (10, 19) and action.lower() == "right-down":
        return True

    if state == (17, 44) and action.lower() == "left-down":
        return True

    if state == (44, 35) and action.lower() == "right":
        return True

    if state == (4, 10) and action.lower() == "right":
        return True

    if state == (35, 13) and action.lower() == "right-down":
        return True

    if state == (5, 16) and action.lower() == "right-up":
        return True

    if state == (12, 7) and action.lower() == "right":
        return True

    if state == (11, 41) and action.lower() == "left":
        return True

    if state == (35, 28) and action.lower() == "right":
        return True

    if state == (13, 45) and action.lower() == "left":
        return True

    if state == (20, 39) and action.lower() == "down":
        return True

    if state == (32, 45) and action.lower() == "left-down":
        return True

    if state == (26, 36) and action.lower() == "right-down":
        return True

    if state == (7, 12) and action.lower() == "left":
        return True

    if state == (0, 16) and action.lower() == "left-down":
        return True

    if state == (2, 31) and action.lower() == "up":
        return True

    if state == (29, 43) and action.lower() == "down":
        return True

    if state == (7, 11) and action.lower() == "left-up":
        return True

    if state == (19, 37) and action.lower() == "left-up":
        return True

    if state == (25, 0) and action.lower() == "right-up":
        return True

    if state == (18, 48) and action.lower() == "right-up":
        return True

    if state == (48, 39) and action.lower() == "right-up":
        return True

    if state == (44, 47) and action.lower() == "right-down":
        return True

    if state == (14, 3) and action.lower() == "right-down":
        return True

    if state == (47, 21) and action.lower() == "left-up":
        return True

    if state == (25, 44) and action.lower() == "left-down":
        return True

    if state == (46, 4) and action.lower() == "right-up":
        return True

    if state == (8, 40) and action.lower() == "left-up":
        return True

    if state == (22, 50) and action.lower() == "left-down":
        return True

    if state == (21, 43) and action.lower() == "left-up":
        return True

    if state == (6, 0) and action.lower() == "right":
        return True

    if state == (14, 24) and action.lower() == "down":
        return True

    if state == (32, 44) and action.lower() == "left-down":
        return True

    if state == (36, 15) and action.lower() == "right-up":
        return True

    if state == (39, 44) and action.lower() == "right-up":
        return True

    if state == (0, 22) and action.lower() == "down":
        return True

    if state == (26, 0) and action.lower() == "up":
        return True

    if state == (37, 45) and action.lower() == "right-down":
        return True

    if state == (9, 38) and action.lower() == "left-down":
        return True

    if state == (8, 32) and action.lower() == "left-down":
        return True

    if state == (9, 0) and action.lower() == "down":
        return True

    if state == (20, 0) and action.lower() == "right":
        return True

    if state == (27, 50) and action.lower() == "left-down":
        return True

    if state == (3, 20) and action.lower() == "left-down":
        return True

    if state == (30, 26) and action.lower() == "left-down":
        return True

    if state == (5, 33) and action.lower() == "left-down":
        return True

    if state == (31, 41) and action.lower() == "right":
        return True

    if state == (32, 49) and action.lower() == "left-down":
        return True

    if state == (19, 25) and action.lower() == "left-down":
        return True

    if state == (44, 22) and action.lower() == "left-up":
        return True

    if state == (38, 11) and action.lower() == "up":
        return True

    if state == (19, 16) and action.lower() == "right-up":
        return True

    if state == (38, 20) and action.lower() == "right-up":
        return True

    if state == (10, 0) and action.lower() == "right-down":
        return True

    if state == (10, 34) and action.lower() == "down":
        return True

    if state == (40, 20) and action.lower() == "up":
        return True

    if state == (1, 35) and action.lower() == "left-down":
        return True

    if state == (1, 49) and action.lower() == "left-down":
        return True

    if state == (21, 16) and action.lower() == "right-down":
        return True

    if state == (9, 12) and action.lower() == "right":
        return True

    if state == (27, 35) and action.lower() == "down":
        return True

    if state == (31, 7) and action.lower() == "down":
        return True

    if state == (17, 39) and action.lower() == "left-up":
        return True

    if state == (41, 15) and action.lower() == "right-up":
        return True

    if state == (36, 12) and action.lower() == "right-up":
        return True

    if state == (27, 26) and action.lower() == "down":
        return True

    if state == (2, 22) and action.lower() == "left-down":
        return True

    if state == (32, 7) and action.lower() == "down":
        return True

    if state == (34, 24) and action.lower() == "right-down":
        return True

    if state == (46, 41) and action.lower() == "right-down":
        return True

    if state == (4, 9) and action.lower() == "right-up":
        return True

    if state == (48, 41) and action.lower() == "right":
        return True

    if state == (5, 8) and action.lower() == "left":
        return True

    if state == (21, 33) and action.lower() == "up":
        return True

    if state == (13, 39) and action.lower() == "right-down":
        return True

    if state == (2, 10) and action.lower() == "right":
        return True

    if state == (48, 42) and action.lower() == "right-up":
        return True

    if state == (42, 40) and action.lower() == "left":
        return True

    if state == (6, 17) and action.lower() == "right-up":
        return True

    if state == (7, 39) and action.lower() == "left-down":
        return True

    if state == (13, 3) and action.lower() == "right-down":
        return True

    if state == (29, 47) and action.lower() == "left-down":
        return True

    if state == (14, 43) and action.lower() == "left-down":
        return True

    if state == (21, 18) and action.lower() == "right":
        return True

    if state == (5, 28) and action.lower() == "left-down":
        return True

    if state == (17, 41) and action.lower() == "left-up":
        return True

    if state == (31, 6) and action.lower() == "right-down":
        return True

    if state == (42, 36) and action.lower() == "down":
        return True

    if state == (23, 4) and action.lower() == "right":
        return True

    if state == (2, 28) and action.lower() == "left-down":
        return True

    if state == (32, 5) and action.lower() == "right-up":
        return True

    if state == (9, 11) and action.lower() == "right":
        return True

    if state == (21, 28) and action.lower() == "up":
        return True

    if state == (10, 42) and action.lower() == "left":
        return True

    if state == (10, 24) and action.lower() == "up":
        return True

    if state == (21, 21) and action.lower() == "left-down":
        return True

    if state == (21, 46) and action.lower() == "down":
        return True

    if state == (32, 0) and action.lower() == "right-down":
        return True

    if state == (6, 16) and action.lower() == "right":
        return True

    if state == (25, 19) and action.lower() == "right-down":
        return True

    if state == (3, 27) and action.lower() == "right-down":
        return True

    if state == (38, 34) and action.lower() == "left-down":
        return True

    if state == (31, 12) and action.lower() == "left-up":
        return True

    if state == (4, 8) and action.lower() == "left-down":
        return True

    if state == (18, 15) and action.lower() == "right-down":
        return True

    if state == (14, 5) and action.lower() == "left-down":
        return True

    if state == (47, 22) and action.lower() == "up":
        return True

    if state == (17, 27) and action.lower() == "left":
        return True

    if state == (25, 21) and action.lower() == "left-down":
        return True

    if state == (14, 50) and action.lower() == "left-up":
        return True

    if state == (7, 14) and action.lower() == "right-up":
        return True

    if state == (6, 36) and action.lower() == "left-down":
        return True

    if state == (17, 43) and action.lower() == "left":
        return True

    if state == (11, 50) and action.lower() == "left-down":
        return True

    if state == (23, 50) and action.lower() == "right-down":
        return True

    if state == (8, 49) and action.lower() == "left":
        return True

    if state == (11, 20) and action.lower() == "right-down":
        return True

    if state == (42, 7) and action.lower() == "right-down":
        return True

    if state == (9, 42) and action.lower() == "left-down":
        return True

    if state == (35, 8) and action.lower() == "right-down":
        return True

    if state == (30, 32) and action.lower() == "right-down":
        return True

    if state == (32, 43) and action.lower() == "down":
        return True

    if state == (22, 14) and action.lower() == "left-down":
        return True

    if state == (48, 47) and action.lower() == "up":
        return True

    if state == (31, 17) and action.lower() == "right":
        return True

    if state == (23, 16) and action.lower() == "left-down":
        return True

    if state == (16, 23) and action.lower() == "left-down":
        return True

    if state == (28, 5) and action.lower() == "left-down":
        return True

    if state == (16, 17) and action.lower() == "right-down":
        return True

    if state == (0, 24) and action.lower() == "left-down":
        return True

    if state == (43, 36) and action.lower() == "down":
        return True

    if state == (27, 22) and action.lower() == "down":
        return True

    if state == (38, 35) and action.lower() == "right-down":
        return True

    if state == (47, 2) and action.lower() == "right":
        return True

    if state == (46, 50) and action.lower() == "left-down":
        return True

    if state == (26, 13) and action.lower() == "right":
        return True

    if state == (20, 26) and action.lower() == "left-up":
        return True

    if state == (40, 35) and action.lower() == "down":
        return True

    if state == (6, 38) and action.lower() == "left-down":
        return True

    if state == (12, 30) and action.lower() == "right-down":
        return True

    if state == (25, 40) and action.lower() == "right-down":
        return True

    if state == (29, 8) and action.lower() == "down":
        return True

    if state == (25, 14) and action.lower() == "down":
        return True

    if state == (38, 41) and action.lower() == "up":
        return True

    if state == (36, 44) and action.lower() == "right-down":
        return True

    if state == (4, 16) and action.lower() == "right":
        return True

    if state == (48, 45) and action.lower() == "right-up":
        return True

    if state == (18, 17) and action.lower() == "right-down":
        return True

    if state == (11, 39) and action.lower() == "left-down":
        return True

    if state == (8, 29) and action.lower() == "down":
        return True

    if state == (2, 37) and action.lower() == "left":
        return True

    if state == (41, 39) and action.lower() == "left":
        return True

    if state == (29, 22) and action.lower() == "right":
        return True

    if state == (6, 47) and action.lower() == "right-down":
        return True

    if state == (20, 16) and action.lower() == "right-down":
        return True

    if state == (44, 27) and action.lower() == "right-up":
        return True

    if state == (39, 50) and action.lower() == "left-down":
        return True

    if state == (22, 21) and action.lower() == "down":
        return True

    if state == (31, 25) and action.lower() == "right-down":
        return True

    if state == (36, 21) and action.lower() == "right-up":
        return True

    if state == (24, 38) and action.lower() == "right-down":
        return True

    if state == (23, 9) and action.lower() == "right":
        return True

    if state == (3, 23) and action.lower() == "right-down":
        return True

    if state == (17, 34) and action.lower() == "left-down":
        return True

    if state == (24, 24) and action.lower() == "left-down":
        return True

    if state == (24, 5) and action.lower() == "right":
        return True

    if state == (5, 49) and action.lower() == "down":
        return True

    if state == (25, 7) and action.lower() == "left-down":
        return True

    if state == (40, 45) and action.lower() == "left-up":
        return True

    if state == (22, 13) and action.lower() == "down":
        return True

    if state == (16, 48) and action.lower() == "left":
        return True

    if state == (23, 40) and action.lower() == "right-down":
        return True

    if state == (30, 47) and action.lower() == "down":
        return True

    if state == (26, 43) and action.lower() == "left-down":
        return True

    if state == (4, 24) and action.lower() == "left-down":
        return True

    if state == (42, 20) and action.lower() == "left":
        return True

    if state == (20, 24) and action.lower() == "left":
        return True

    if state == (0, 50) and action.lower() == "left-down":
        return True

    if state == (47, 43) and action.lower() == "right":
        return True

    if state == (37, 49) and action.lower() == "left-down":
        return True

    if state == (17, 1) and action.lower() == "right-up":
        return True

    if state == (29, 20) and action.lower() == "right":
        return True

    if state == (45, 48) and action.lower() == "right-down":
        return True

    if state == (26, 39) and action.lower() == "right":
        return True

    if state == (12, 49) and action.lower() == "down":
        return True

    if state == (3, 10) and action.lower() == "right-up":
        return True

    if state == (5, 18) and action.lower() == "right":
        return True

    if state == (39, 5) and action.lower() == "right":
        return True

    if state == (40, 37) and action.lower() == "left-down":
        return True

    if state == (10, 14) and action.lower() == "right-down":
        return True

    if state == (2, 46) and action.lower() == "left-down":
        return True

    if state == (14, 1) and action.lower() == "down":
        return True

    if state == (18, 28) and action.lower() == "left-down":
        return True

    if state == (19, 9) and action.lower() == "right":
        return True

    if state == (26, 34) and action.lower() == "right-down":
        return True

    if state == (2, 49) and action.lower() == "down":
        return True

    if state == (44, 28) and action.lower() == "right-up":
        return True

    if state == (28, 42) and action.lower() == "right-down":
        return True

    if state == (21, 0) and action.lower() == "right-up":
        return True

    if state == (38, 45) and action.lower() == "right":
        return True

    if state == (14, 37) and action.lower() == "left-down":
        return True

    if state == (7, 21) and action.lower() == "right-down":
        return True

    if state == (32, 46) and action.lower() == "left-down":
        return True

    if state == (43, 3) and action.lower() == "right-up":
        return True

    if state == (43, 7) and action.lower() == "right":
        return True

    if state == (28, 24) and action.lower() == "left-down":
        return True

    if state == (8, 2) and action.lower() == "left-down":
        return True

    if state == (46, 40) and action.lower() == "right":
        return True

    if state == (18, 1) and action.lower() == "right-down":
        return True

    if state == (17, 29) and action.lower() == "left-down":
        return True

    if state == (42, 32) and action.lower() == "right-up":
        return True

    if state == (24, 22) and action.lower() == "left-down":
        return True

    if state == (17, 0) and action.lower() == "right":
        return True

    if state == (33, 43) and action.lower() == "down":
        return True

    if state == (17, 12) and action.lower() == "left-down":
        return True

    if state == (30, 17) and action.lower() == "right-down":
        return True

    if state == (13, 50) and action.lower() == "left":
        return True

    if state == (11, 7) and action.lower() == "left-up":
        return True

    if state == (24, 37) and action.lower() == "right":
        return True

    if state == (36, 46) and action.lower() == "left-down":
        return True

    if state == (4, 50) and action.lower() == "left-down":
        return True

    if state == (5, 39) and action.lower() == "left-down":
        return True

    if state == (5, 17) and action.lower() == "right":
        return True

    if state == (39, 7) and action.lower() == "right-up":
        return True

    if state == (46, 5) and action.lower() == "up":
        return True

    if state == (48, 27) and action.lower() == "up":
        return True

    if state == (4, 5) and action.lower() == "right-down":
        return True

    if state == (3, 1) and action.lower() == "left-down":
        return True

    if state == (6, 29) and action.lower() == "left":
        return True

    if state == (6, 35) and action.lower() == "right-down":
        return True

    if state == (6, 20) and action.lower() == "right-down":
        return True

    if state == (37, 18) and action.lower() == "right":
        return True

    if state == (26, 11) and action.lower() == "right-up":
        return True

    if state == (3, 24) and action.lower() == "down":
        return True

    if state == (1, 20) and action.lower() == "down":
        return True

    if state == (36, 20) and action.lower() == "right-up":
        return True

    if state == (45, 13) and action.lower() == "up":
        return True

    if state == (12, 37) and action.lower() == "left-up":
        return True

    if state == (32, 23) and action.lower() == "right":
        return True

    if state == (20, 33) and action.lower() == "up":
        return True

    if state == (23, 44) and action.lower() == "left-up":
        return True

    if state == (47, 29) and action.lower() == "left-up":
        return True

    if state == (17, 28) and action.lower() == "left-down":
        return True

    if state == (40, 30) and action.lower() == "left-up":
        return True

    if state == (44, 34) and action.lower() == "right-down":
        return True

    if state == (1, 31) and action.lower() == "left-up":
        return True

    if state == (10, 11) and action.lower() == "right-up":
        return True

    if state == (31, 33) and action.lower() == "right-down":
        return True

    if state == (1, 36) and action.lower() == "down":
        return True

    if state == (5, 22) and action.lower() == "down":
        return True

    if state == (46, 27) and action.lower() == "up":
        return True

    if state == (1, 38) and action.lower() == "right-down":
        return True

    if state == (21, 13) and action.lower() == "down":
        return True

    if state == (23, 10) and action.lower() == "right-up":
        return True

    if state == (48, 50) and action.lower() == "left-up":
        return True

    if state == (20, 25) and action.lower() == "left":
        return True

    if state == (45, 0) and action.lower() == "down":
        return True

    if state == (36, 43) and action.lower() == "right":
        return True

    if state == (17, 50) and action.lower() == "left":
        return True

    if state == (43, 46) and action.lower() == "right-down":
        return True

    if state == (43, 8) and action.lower() == "right-down":
        return True

    if state == (9, 34) and action.lower() == "down":
        return True

    if state == (47, 5) and action.lower() == "right-down":
        return True

    if state == (47, 4) and action.lower() == "right":
        return True

    if state == (3, 9) and action.lower() == "right":
        return True

    if state == (35, 25) and action.lower() == "down":
        return True

    if state == (45, 42) and action.lower() == "right":
        return True

    if state == (39, 20) and action.lower() == "up":
        return True

    if state == (45, 36) and action.lower() == "right":
        return True

    if state == (14, 42) and action.lower() == "left-down":
        return True

    if state == (32, 16) and action.lower() == "right":
        return True

    if state == (36, 25) and action.lower() == "right-down":
        return True

    if state == (37, 41) and action.lower() == "right-up":
        return True

    if state == (0, 21) and action.lower() == "left-down":
        return True

    if state == (1, 10) and action.lower() == "right-down":
        return True

    if state == (15, 15) and action.lower() == "right-up":
        return True

    if state == (24, 33) and action.lower() == "right":
        return True

    if state == (20, 32) and action.lower() == "right-up":
        return True

    if state == (15, 12) and action.lower() == "left-up":
        return True

    if state == (36, 3) and action.lower() == "left-up":
        return True

    if state == (12, 5) and action.lower() == "left-down":
        return True

    if state == (32, 21) and action.lower() == "right-up":
        return True

    if state == (8, 31) and action.lower() == "down":
        return True

    if state == (17, 42) and action.lower() == "left-up":
        return True

    if state == (35, 45) and action.lower() == "left-down":
        return True

    if state == (48, 18) and action.lower() == "right-up":
        return True

    if state == (32, 1) and action.lower() == "down":
        return True

    if state == (38, 25) and action.lower() == "right-up":
        return True

    if state == (39, 37) and action.lower() == "right-up":
        return True

    if state == (41, 35) and action.lower() == "right-down":
        return True

    if state == (4, 33) and action.lower() == "left-down":
        return True

    if state == (38, 46) and action.lower() == "right-down":
        return True

    if state == (27, 48) and action.lower() == "down":
        return True

    if state == (11, 34) and action.lower() == "down":
        return True

    if state == (0, 20) and action.lower() == "down":
        return True

    if state == (12, 20) and action.lower() == "right-down":
        return True

    if state == (41, 0) and action.lower() == "right":
        return True

    if state == (20, 29) and action.lower() == "left":
        return True

    if state == (1, 50) and action.lower() == "left-down":
        return True

    if state == (7, 4) and action.lower() == "down":
        return True

    if state == (12, 38) and action.lower() == "left":
        return True

    if state == (8, 43) and action.lower() == "left-down":
        return True

    if state == (46, 8) and action.lower() == "right-up":
        return True

    if state == (37, 19) and action.lower() == "right-up":
        return True

    if state == (7, 48) and action.lower() == "down":
        return True

    if state == (1, 32) and action.lower() == "left":
        return True

    if state == (2, 11) and action.lower() == "right-down":
        return True

    if state == (32, 32) and action.lower() == "right-up":
        return True

    if state == (12, 45) and action.lower() == "left-down":
        return True

    if state == (36, 28) and action.lower() == "right-down":
        return True

    if state == (36, 35) and action.lower() == "right":
        return True

    if state == (4, 19) and action.lower() == "right-down":
        return True

    if state == (36, 5) and action.lower() == "right-up":
        return True

    if state == (30, 45) and action.lower() == "down":
        return True

    if state == (10, 28) and action.lower() == "down":
        return True

    if state == (34, 40) and action.lower() == "left":
        return True

    if state == (43, 2) and action.lower() == "right":
        return True

    if state == (26, 6) and action.lower() == "down":
        return True

    if state == (33, 21) and action.lower() == "right-down":
        return True

    if state == (8, 23) and action.lower() == "left":
        return True

    if state == (26, 24) and action.lower() == "left-up":
        return True

    if state == (39, 38) and action.lower() == "right-up":
        return True

    if state == (17, 49) and action.lower() == "left-up":
        return True

    if state == (42, 51) and action.lower() == "left-down":
        return True

    if state == (2, 39) and action.lower() == "down":
        return True

    if state == (40, 47) and action.lower() == "down":
        return True

    if state == (29, 45) and action.lower() == "left-down":
        return True

    if state == (36, 30) and action.lower() == "down":
        return True

    if state == (44, 6) and action.lower() == "right-up":
        return True

    if state == (1, 51) and action.lower() == "left-down":
        return True

    if state == (2, 13) and action.lower() == "right":
        return True

    if state == (47, 42) and action.lower() == "right":
        return True

    if state == (37, 50) and action.lower() == "right-down":
        return True

    if state == (5, 32) and action.lower() == "left":
        return True

    if state == (7, 35) and action.lower() == "right-down":
        return True

    if state == (48, 0) and action.lower() == "right-up":
        return True

    if state == (3, 29) and action.lower() == "left-down":
        return True

    if state == (47, 30) and action.lower() == "left-up":
        return True

    if state == (28, 49) and action.lower() == "left-down":
        return True

    if state == (18, 51) and action.lower() == "left-up":
        return True

    if state == (6, 6) and action.lower() == "left-down":
        return True

    if state == (10, 27) and action.lower() == "right-down":
        return True

    if state == (39, 28) and action.lower() == "right-up":
        return True

    if state == (28, 22) and action.lower() == "right-down":
        return True

    if state == (7, 24) and action.lower() == "left-down":
        return True

    if state == (38, 38) and action.lower() == "right-up":
        return True

    if state == (10, 43) and action.lower() == "left-up":
        return True

    if state == (4, 29) and action.lower() == "left-down":
        return True

    if state == (26, 2) and action.lower() == "left-down":
        return True

    if state == (18, 27) and action.lower() == "down":
        return True

    if state == (47, 19) and action.lower() == "up":
        return True

    if state == (17, 37) and action.lower() == "left-up":
        return True

    if state == (16, 32) and action.lower() == "left-down":
        return True

    if state == (5, 30) and action.lower() == "left":
        return True

    if state == (26, 47) and action.lower() == "right-down":
        return True

    if state == (42, 19) and action.lower() == "left-up":
        return True

    if state == (26, 26) and action.lower() == "down":
        return True

    if state == (37, 27) and action.lower() == "right":
        return True

    if state == (29, 38) and action.lower() == "right":
        return True

    if state == (47, 20) and action.lower() == "left-up":
        return True

    if state == (38, 0) and action.lower() == "right-down":
        return True

    if state == (43, 17) and action.lower() == "up":
        return True

    if state == (16, 26) and action.lower() == "down":
        return True

    if state == (28, 48) and action.lower() == "left-down":
        return True

    if state == (43, 29) and action.lower() == "right-up":
        return True

    if state == (17, 22) and action.lower() == "right-down":
        return True

    if state == (46, 13) and action.lower() == "up":
        return True

    if state == (8, 4) and action.lower() == "right-down":
        return True

    if state == (7, 40) and action.lower() == "left":
        return True

    if state == (25, 18) and action.lower() == "right-down":
        return True

    if state == (14, 22) and action.lower() == "left-down":
        return True

    if state == (34, 2) and action.lower() == "right-up":
        return True

    if state == (34, 48) and action.lower() == "left":
        return True

    if state == (4, 12) and action.lower() == "right":
        return True

    if state == (17, 20) and action.lower() == "left":
        return True

    if state == (43, 14) and action.lower() == "right-up":
        return True

    if state == (18, 3) and action.lower() == "right":
        return True

    if state == (24, 16) and action.lower() == "left":
        return True

    if state == (45, 40) and action.lower() == "right-down":
        return True

    if state == (36, 31) and action.lower() == "left-down":
        return True

    if state == (5, 3) and action.lower() == "right-down":
        return True

    if state == (18, 34) and action.lower() == "left-down":
        return True

    if state == (20, 11) and action.lower() == "right-down":
        return True

    if state == (33, 17) and action.lower() == "right-up":
        return True

    if state == (37, 47) and action.lower() == "left-down":
        return True

    if state == (28, 43) and action.lower() == "left-down":
        return True

    if state == (23, 49) and action.lower() == "left-down":
        return True

    if state == (12, 31) and action.lower() == "down":
        return True

    if state == (41, 17) and action.lower() == "left-up":
        return True

    if state == (33, 45) and action.lower() == "left-down":
        return True

    if state == (16, 34) and action.lower() == "left-up":
        return True

    if state == (26, 51) and action.lower() == "left-down":
        return True

    if state == (32, 17) and action.lower() == "right-up":
        return True

    if state == (19, 43) and action.lower() == "left-down":
        return True

    if state == (32, 26) and action.lower() == "right-down":
        return True

    if state == (3, 16) and action.lower() == "right-down":
        return True

    if state == (15, 26) and action.lower() == "down":
        return True

    if state == (20, 51) and action.lower() == "up":
        return True

    if state == (19, 15) and action.lower() == "right-down":
        return True

    if state == (25, 32) and action.lower() == "right":
        return True

    if state == (28, 20) and action.lower() == "right-down":
        return True

    if state == (6, 7) and action.lower() == "left":
        return True

    if state == (21, 39) and action.lower() == "right-down":
        return True

    if state == (39, 6) and action.lower() == "right":
        return True

    if state == (41, 6) and action.lower() == "right-down":
        return True

    if state == (35, 27) and action.lower() == "right-down":
        return True

    if state == (31, 28) and action.lower() == "left":
        return True

    if state == (9, 36) and action.lower() == "left-down":
        return True

    if state == (14, 33) and action.lower() == "left-down":
        return True

    if state == (37, 21) and action.lower() == "right-up":
        return True

    if state == (6, 22) and action.lower() == "left-down":
        return True

    if state == (46, 51) and action.lower() == "left":
        return True

    if state == (40, 9) and action.lower() == "right-up":
        return True

    if state == (46, 38) and action.lower() == "right":
        return True

    if state == (35, 21) and action.lower() == "right-up":
        return True

    if state == (15, 14) and action.lower() == "right":
        return True

    if state == (44, 44) and action.lower() == "right-up":
        return True

    if state == (41, 18) and action.lower() == "right-up":
        return True

    if state == (29, 14) and action.lower() == "down":
        return True

    if state == (25, 39) and action.lower() == "right-down":
        return True

    if state == (37, 29) and action.lower() == "right":
        return True

    if state == (15, 45) and action.lower() == "left":
        return True

    if state == (42, 21) and action.lower() == "left":
        return True

    if state == (30, 43) and action.lower() == "left-down":
        return True

    if state == (42, 35) and action.lower() == "right-down":
        return True

    if state == (9, 8) and action.lower() == "left-up":
        return True

    if state == (31, 14) and action.lower() == "right-down":
        return True

    if state == (19, 18) and action.lower() == "right-down":
        return True

    if state == (34, 47) and action.lower() == "left-down":
        return True

    if state == (26, 20) and action.lower() == "down":
        return True

    if state == (36, 6) and action.lower() == "right-down":
        return True

    if state == (28, 35) and action.lower() == "right-down":
        return True

    if state == (10, 44) and action.lower() == "right-down":
        return True

    if state == (40, 26) and action.lower() == "right":
        return True

    if state == (39, 8) and action.lower() == "right":
        return True

    if state == (4, 13) and action.lower() == "right-down":
        return True

    if state == (35, 22) and action.lower() == "up":
        return True

    if state == (24, 46) and action.lower() == "left-down":
        return True

    if state == (26, 48) and action.lower() == "down":
        return True

    if state == (32, 36) and action.lower() == "down":
        return True

    if state == (3, 15) and action.lower() == "right":
        return True

    if state == (11, 30) and action.lower() == "right-down":
        return True

    if state == (2, 38) and action.lower() == "right-down":
        return True

    if state == (42, 48) and action.lower() == "left-up":
        return True

    if state == (43, 10) and action.lower() == "right":
        return True

    if state == (48, 6) and action.lower() == "right-up":
        return True

    if state == (13, 49) and action.lower() == "left-down":
        return True

    if state == (47, 25) and action.lower() == "left":
        return True

    if state == (1, 42) and action.lower() == "left-down":
        return True

    if state == (30, 11) and action.lower() == "left-up":
        return True

    if state == (37, 11) and action.lower() == "right-up":
        return True

    if state == (5, 29) and action.lower() == "left-down":
        return True

    if state == (15, 4) and action.lower() == "left-down":
        return True

    if state == (38, 29) and action.lower() == "right-up":
        return True

    if state == (33, 13) and action.lower() == "right-up":
        return True

    if state == (4, 43) and action.lower() == "left":
        return True

    if state == (42, 39) and action.lower() == "left-up":
        return True

    if state == (4, 11) and action.lower() == "right-up":
        return True

    if state == (19, 27) and action.lower() == "left-down":
        return True

    if state == (10, 31) and action.lower() == "left-down":
        return True

    if state == (36, 49) and action.lower() == "left-down":
        return True

    if state == (42, 41) and action.lower() == "left-up":
        return True

    if state == (31, 51) and action.lower() == "left-down":
        return True

    if state == (4, 48) and action.lower() == "left":
        return True

    if state == (46, 20) and action.lower() == "left-up":
        return True

    if state == (27, 20) and action.lower() == "down":
        return True

    if state == (35, 11) and action.lower() == "right-down":
        return True

    if state == (0, 33) and action.lower() == "down":
        return True

    if state == (4, 46) and action.lower() == "left-down":
        return True

    if state == (28, 1) and action.lower() == "up":
        return True

    if state == (5, 7) and action.lower() == "left-down":
        return True

    if state == (7, 36) and action.lower() == "down":
        return True

    if state == (14, 26) and action.lower() == "left":
        return True

    if state == (1, 15) and action.lower() == "right-down":
        return True

    if state == (36, 23) and action.lower() == "left-up":
        return True

    if state == (23, 39) and action.lower() == "right-down":
        return True

    if state == (37, 6) and action.lower() == "right":
        return True

    if state == (21, 19) and action.lower() == "right-down":
        return True

    if state == (2, 36) and action.lower() == "left-down":
        return True

    if state == (5, 13) and action.lower() == "right":
        return True

    if state == (4, 28) and action.lower() == "down":
        return True

    if state == (5, 6) and action.lower() == "down":
        return True

    if state == (5, 9) and action.lower() == "right-up":
        return True

    if state == (39, 47) and action.lower() == "down":
        return True

    if state == (20, 30) and action.lower() == "left":
        return True

    if state == (0, 51) and action.lower() == "left-down":
        return True

    if state == (43, 45) and action.lower() == "right":
        return True

    if state == (18, 25) and action.lower() == "down":
        return True

    if state == (43, 23) and action.lower() == "left-down":
        return True

    if state == (8, 37) and action.lower() == "left-down":
        return True

    if state == (13, 11) and action.lower() == "right-up":
        return True

    if state == (2, 20) and action.lower() == "down":
        return True

    if state == (45, 39) and action.lower() == "right":
        return True

    if state == (33, 35) and action.lower() == "right-down":
        return True

    if state == (37, 7) and action.lower() == "right-down":
        return True

    if state == (40, 13) and action.lower() == "right-down":
        return True

    if state == (26, 41) and action.lower() == "right-down":
        return True

    if state == (36, 9) and action.lower() == "right-up":
        return True

    if state == (22, 40) and action.lower() == "right-down":
        return True

    if state == (22, 17) and action.lower() == "right-up":
        return True

    if state == (26, 27) and action.lower() == "left-down":
        return True

    if state == (6, 51) and action.lower() == "left-down":
        return True

    if state == (28, 45) and action.lower() == "left-down":
        return True

    if state == (18, 40) and action.lower() == "left-up":
        return True

    if state == (37, 37) and action.lower() == "right-down":
        return True

    if state == (29, 42) and action.lower() == "right-down":
        return True

    if state == (14, 13) and action.lower() == "right-down":
        return True

    if state == (0, 30) and action.lower() == "left":
        return True

    if state == (31, 34) and action.lower() == "right-down":
        return True

    if state == (34, 43) and action.lower() == "down":
        return True

    if state == (33, 20) and action.lower() == "right":
        return True

    if state == (11, 1) and action.lower() == "right-down":
        return True

    if state == (1, 24) and action.lower() == "left-down":
        return True

    if state == (15, 5) and action.lower() == "left":
        return True

    if state == (41, 40) and action.lower() == "left-down":
        return True

    if state == (25, 24) and action.lower() == "left":
        return True

    if state == (41, 1) and action.lower() == "right-down":
        return True

    if state == (36, 22) and action.lower() == "up":
        return True

    if state == (31, 37) and action.lower() == "up":
        return True

    if state == (1, 46) and action.lower() == "left-up":
        return True

    if state == (5, 51) and action.lower() == "down":
        return True

    if state == (41, 43) and action.lower() == "right-up":
        return True

    if state == (24, 31) and action.lower() == "right-down":
        return True

    if state == (27, 16) and action.lower() == "right-up":
        return True

    if state == (31, 36) and action.lower() == "right-up":
        return True

    if state == (35, 39) and action.lower() == "left":
        return True

    if state == (1, 9) and action.lower() == "right":
        return True

    if state == (38, 48) and action.lower() == "left-down":
        return True

    if state == (38, 8) and action.lower() == "right-down":
        return True

    if state == (18, 41) and action.lower() == "left":
        return True

    if state == (20, 44) and action.lower() == "left-down":
        return True

    if state == (24, 19) and action.lower() == "down":
        return True

    if state == (20, 35) and action.lower() == "left-up":
        return True

    if state == (48, 22) and action.lower() == "left-up":
        return True

    if state == (7, 27) and action.lower() == "left-down":
        return True

    if state == (5, 25) and action.lower() == "down":
        return True

    if state == (40, 8) and action.lower() == "right-up":
        return True

    if state == (24, 48) and action.lower() == "right-down":
        return True

    if state == (11, 14) and action.lower() == "right":
        return True

    if state == (35, 46) and action.lower() == "down":
        return True

    if state == (44, 12) and action.lower() == "right":
        return True

    if state == (24, 7) and action.lower() == "down":
        return True

    if state == (1, 27) and action.lower() == "right-down":
        return True

    if state == (48, 25) and action.lower() == "left-up":
        return True

    if state == (10, 35) and action.lower() == "left-down":
        return True

    if state == (29, 23) and action.lower() == "right-down":
        return True

    if state == (8, 42) and action.lower() == "down":
        return True

    if state == (3, 41) and action.lower() == "left-down":
        return True

    if state == (33, 23) and action.lower() == "right-down":
        return True

    if state == (16, 40) and action.lower() == "left":
        return True

    if state == (25, 26) and action.lower() == "down":
        return True

    if state == (40, 5) and action.lower() == "right-up":
        return True

    if state == (20, 23) and action.lower() == "left-down":
        return True

    if state == (19, 2) and action.lower() == "right-up":
        return True

    if state == (41, 49) and action.lower() == "left-down":
        return True

    if state == (3, 12) and action.lower() == "right-down":
        return True

    if state == (29, 25) and action.lower() == "left-down":
        return True

    if state == (23, 51) and action.lower() == "down":
        return True

    if state == (30, 29) and action.lower() == "right":
        return True

    if state == (0, 29) and action.lower() == "left-down":
        return True

    if state == (21, 6) and action.lower() == "left-down":
        return True

    if state == (13, 32) and action.lower() == "left-down":
        return True

    if state == (32, 14) and action.lower() == "right-down":
        return True

    if state == (30, 25) and action.lower() == "right-down":
        return True

    if state == (39, 13) and action.lower() == "down":
        return True

    if state == (23, 24) and action.lower() == "left-down":
        return True

    if state == (14, 31) and action.lower() == "right-down":
        return True

    if state == (6, 32) and action.lower() == "down":
        return True

    if state == (16, 21) and action.lower() == "right-down":
        return True

    if state == (31, 2) and action.lower() == "right-down":
        return True

    if state == (31, 30) and action.lower() == "right-up":
        return True

    if state == (38, 39) and action.lower() == "right":
        return True

    if state == (33, 24) and action.lower() == "right":
        return True

    if state == (47, 18) and action.lower() == "right-up":
        return True

    if state == (19, 17) and action.lower() == "right":
        return True

    if state == (14, 46) and action.lower() == "left-down":
        return True

    if state == (38, 10) and action.lower() == "right-up":
        return True

    if state == (17, 18) and action.lower() == "down":
        return True

    if state == (1, 41) and action.lower() == "down":
        return True

    if state == (26, 17) and action.lower() == "right-down":
        return True

    if state == (11, 9) and action.lower() == "left-down":
        return True

    if state == (40, 39) and action.lower() == "left-down":
        return True

    if state == (12, 27) and action.lower() == "right-down":
        return True

    if state == (5, 37) and action.lower() == "left-down":
        return True

    if state == (9, 26) and action.lower() == "right-down":
        return True

    if state == (9, 13) and action.lower() == "right-down":
        return True

    if state == (9, 47) and action.lower() == "down":
        return True

    if state == (39, 24) and action.lower() == "right-up":
        return True

    if state == (10, 9) and action.lower() == "left-down":
        return True

    if state == (37, 28) and action.lower() == "right-down":
        return True

    if state == (39, 9) and action.lower() == "right-up":
        return True

    if state == (22, 5) and action.lower() == "down":
        return True

    if state == (26, 9) and action.lower() == "left-down":
        return True

    if state == (7, 44) and action.lower() == "left-down":
        return True

    if state == (15, 10) and action.lower() == "right-up":
        return True

    if state == (10, 37) and action.lower() == "left-down":
        return True

    if state == (11, 24) and action.lower() == "up":
        return True

    if state == (16, 9) and action.lower() == "right-up":
        return True

    if state == (48, 36) and action.lower() == "right":
        return True

    if state == (22, 1) and action.lower() == "left-up":
        return True

    if state == (29, 49) and action.lower() == "right-down":
        return True

    if state == (15, 40) and action.lower() == "left-down":
        return True

    if state == (17, 30) and action.lower() == "left":
        return True

    if state == (39, 0) and action.lower() == "right-down":
        return True

    if state == (25, 12) and action.lower() == "right-down":
        return True

    if state == (19, 34) and action.lower() == "left":
        return True

    if state == (30, 50) and action.lower() == "right-down":
        return True

    if state == (35, 42) and action.lower() == "right":
        return True

    if state == (10, 51) and action.lower() == "left-down":
        return True

    if state == (40, 19) and action.lower() == "right-up":
        return True

    if state == (22, 51) and action.lower() == "down":
        return True

    if state == (43, 11) and action.lower() == "right-down":
        return True

    if state == (7, 32) and action.lower() == "left-down":
        return True

    if state == (8, 36) and action.lower() == "down":
        return True

    if state == (27, 31) and action.lower() == "right":
        return True

    if state == (46, 44) and action.lower() == "right":
        return True

    if state == (24, 2) and action.lower() == "right-up":
        return True

    if state == (5, 2) and action.lower() == "right":
        return True

    if state == (18, 18) and action.lower() == "down":
        return True

    if state == (0, 45) and action.lower() == "left":
        return True

    if state == (27, 9) and action.lower() == "left":
        return True

    if state == (35, 36) and action.lower() == "down":
        return True

    if state == (9, 14) and action.lower() == "down":
        return True

    if state == (0, 43) and action.lower() == "left-down":
        return True

    if state == (45, 18) and action.lower() == "right":
        return True

    if state == (14, 2) and action.lower() == "left-down":
        return True

    if state == (16, 41) and action.lower() == "left-up":
        return True

    if state == (13, 31) and action.lower() == "down":
        return True

    if state == (9, 22) and action.lower() == "left":
        return True

    if state == (29, 2) and action.lower() == "left-up":
        return True

    if state == (25, 23) and action.lower() == "left-up":
        return True

    if state == (39, 33) and action.lower() == "right-down":
        return True

    if state == (1, 14) and action.lower() == "right":
        return True

    if state == (20, 28) and action.lower() == "left-up":
        return True

    if state == (7, 33) and action.lower() == "left-down":
        return True

    if state == (20, 42) and action.lower() == "left-up":
        return True

    if state == (33, 33) and action.lower() == "right-up":
        return True

    if state == (42, 15) and action.lower() == "up":
        return True

    if state == (11, 18) and action.lower() == "right-down":
        return True

    if state == (41, 10) and action.lower() == "right-down":
        return True

    if state == (30, 49) and action.lower() == "right":
        return True

    if state == (4, 20) and action.lower() == "left-down":
        return True

    if state == (26, 16) and action.lower() == "right":
        return True

    if state == (41, 51) and action.lower() == "down":
        return True

    if state == (8, 7) and action.lower() == "left-down":
        return True

    if state == (40, 16) and action.lower() == "right-up":
        return True

    if state == (6, 42) and action.lower() == "down":
        return True

    if state == (19, 51) and action.lower() == "up":
        return True

    if state == (3, 45) and action.lower() == "left":
        return True

    if state == (36, 42) and action.lower() == "right-up":
        return True

    if state == (24, 3) and action.lower() == "right":
        return True

    if state == (3, 44) and action.lower() == "left":
        return True

    if state == (41, 22) and action.lower() == "left-down":
        return True

    if state == (42, 43) and action.lower() == "up":
        return True

    if state == (3, 34) and action.lower() == "left-down":
        return True

    if state == (18, 33) and action.lower() == "left":
        return True

    if state == (23, 19) and action.lower() == "down":
        return True

    if state == (29, 17) and action.lower() == "right-down":
        return True

    if state == (35, 17) and action.lower() == "left-up":
        return True

    if state == (40, 1) and action.lower() == "right-down":
        return True

    if state == (32, 35) and action.lower() == "right-down":
        return True

    if state == (25, 51) and action.lower() == "down":
        return True

    if state == (5, 19) and action.lower() == "right-down":
        return True

    if state == (5, 43) and action.lower() == "left-up":
        return True

    if state == (30, 23) and action.lower() == "right":
        return True

    if state == (21, 3) and action.lower() == "down":
        return True

    if state == (7, 51) and action.lower() == "left-down":
        return True

    if state == (9, 5) and action.lower() == "down":
        return True

    if state == (12, 4) and action.lower() == "left-down":
        return True

    if state == (15, 25) and action.lower() == "left":
        return True

    if state == (19, 44) and action.lower() == "left-up":
        return True

    if state == (17, 11) and action.lower() == "down":
        return True

    if state == (18, 45) and action.lower() == "left-down":
        return True

    if state == (1, 23) and action.lower() == "left-down":
        return True

    if state == (4, 35) and action.lower() == "left-down":
        return True

    if state == (9, 27) and action.lower() == "right-down":
        return True

    if state == (23, 14) and action.lower() == "left-down":
        return True

    if state == (18, 11) and action.lower() == "left-down":
        return True

    if state == (21, 22) and action.lower() == "left-down":
        return True

    if state == (7, 50) and action.lower() == "left":
        return True

    if state == (2, 41) and action.lower() == "down":
        return True

    if state == (37, 48) and action.lower() == "left-down":
        return True

    if state == (21, 47) and action.lower() == "left-down":
        return True

    if state == (38, 7) and action.lower() == "right":
        return True

    if state == (29, 39) and action.lower() == "right-down":
        return True

    if state == (11, 8) and action.lower() == "down":
        return True

    if state == (34, 5) and action.lower() == "right-down":
        return True

    if state == (34, 37) and action.lower() == "left-down":
        return True

    if state == (26, 46) and action.lower() == "right":
        return True

    if state == (27, 6) and action.lower() == "right-down":
        return True

    if state == (12, 3) and action.lower() == "down":
        return True

    if state == (7, 49) and action.lower() == "left-down":
        return True

    if state == (48, 23) and action.lower() == "left-up":
        return True

    if state == (13, 44) and action.lower() == "left-down":
        return True

    if state == (37, 22) and action.lower() == "up":
        return True

    if state == (37, 39) and action.lower() == "right-down":
        return True

    if state == (15, 21) and action.lower() == "down":
        return True

    if state == (4, 51) and action.lower() == "left-down":
        return True

    if state == (26, 37) and action.lower() == "down":
        return True

    if state == (47, 1) and action.lower() == "right-down":
        return True

    if state == (41, 14) and action.lower() == "right":
        return True

    if state == (37, 34) and action.lower() == "down":
        return True

    if state == (27, 41) and action.lower() == "right-down":
        return True

    if state == (14, 35) and action.lower() == "left":
        return True

    if state == (48, 2) and action.lower() == "right-up":
        return True

    if state == (23, 22) and action.lower() == "down":
        return True

    if state == (32, 19) and action.lower() == "right":
        return True

    if state == (41, 38) and action.lower() == "left-down":
        return True

    if state == (38, 47) and action.lower() == "down":
        return True

    if state == (3, 49) and action.lower() == "left-down":
        return True

    if state == (2, 18) and action.lower() == "right-up":
        return True

    if state == (16, 5) and action.lower() == "left-up":
        return True

    if state == (27, 34) and action.lower() == "right-down":
        return True

    if state == (29, 48) and action.lower() == "left-down":
        return True

    if state == (5, 14) and action.lower() == "right-up":
        return True

    if state == (32, 48) and action.lower() == "left-down":
        return True

    if state == (3, 35) and action.lower() == "down":
        return True

    if state == (10, 5) and action.lower() == "left-down":
        return True

    if state == (11, 4) and action.lower() == "left-down":
        return True

    if state == (22, 11) and action.lower() == "right-up":
        return True

    if state == (26, 19) and action.lower() == "right-down":
        return True

    if state == (17, 46) and action.lower() == "left-down":
        return True

    if state == (17, 26) and action.lower() == "left-down":
        return True

    if state == (11, 12) and action.lower() == "right-up":
        return True

    if state == (15, 18) and action.lower() == "left-down":
        return True

    if state == (26, 28) and action.lower() == "left-down":
        return True

    if state == (27, 2) and action.lower() == "left":
        return True

    if state == (17, 3) and action.lower() == "right-down":
        return True

    if state == (29, 29) and action.lower() == "right-down":
        return True

    if state == (41, 5) and action.lower() == "right":
        return True

    if state == (27, 43) and action.lower() == "left-down":
        return True

    if state == (29, 30) and action.lower() == "right":
        return True

    if state == (4, 41) and action.lower() == "left":
        return True

    if state == (27, 1) and action.lower() == "left-up":
        return True

    if state == (34, 7) and action.lower() == "right-down":
        return True

    if state == (40, 41) and action.lower() == "left-down":
        return True

    if state == (20, 8) and action.lower() == "right":
        return True

    if state == (33, 26) and action.lower() == "right":
        return True

    if state == (44, 9) and action.lower() == "right-up":
        return True

    if state == (6, 27) and action.lower() == "down":
        return True

    if state == (46, 45) and action.lower() == "right-down":
        return True

    if state == (32, 15) and action.lower() == "right":
        return True

    if state == (13, 5) and action.lower() == "left-down":
        return True

    if state == (11, 0) and action.lower() == "right":
        return True

    if state == (33, 38) and action.lower() == "left-down":
        return True

    if state == (14, 40) and action.lower() == "down":
        return True

    if state == (45, 5) and action.lower() == "right-up":
        return True

    if state == (24, 51) and action.lower() == "down":
        return True

    if state == (32, 20) and action.lower() == "right-down":
        return True

    if state == (30, 18) and action.lower() == "down":
        return True

    if state == (36, 16) and action.lower() == "up":
        return True

    if state == (4, 49) and action.lower() == "down":
        return True

    if state == (27, 30) and action.lower() == "right-up":
        return True

    if state == (0, 35) and action.lower() == "down":
        return True

    if state == (16, 50) and action.lower() == "left-down":
        return True

    if state == (0, 19) and action.lower() == "right-down":
        return True

    if state == (42, 11) and action.lower() == "down":
        return True

    if state == (45, 26) and action.lower() == "right-up":
        return True

    if state == (43, 28) and action.lower() == "up":
        return True

    if state == (7, 9) and action.lower() == "right-up":
        return True

    if state == (18, 43) and action.lower() == "left-up":
        return True

    if state == (47, 45) and action.lower() == "right":
        return True

    if state == (13, 46) and action.lower() == "left-up":
        return True

    if state == (11, 36) and action.lower() == "left-up":
        return True

    if state == (31, 22) and action.lower() == "right-up":
        return True

    if state == (38, 19) and action.lower() == "up":
        return True

    if state == (45, 43) and action.lower() == "right-down":
        return True

    if state == (1, 19) and action.lower() == "right-down":
        return True

    if state == (12, 12) and action.lower() == "up":
        return True

    if state == (35, 6) and action.lower() == "right-up":
        return True

    if state == (18, 32) and action.lower() == "left-up":
        return True

    if state == (8, 26) and action.lower() == "right-down":
        return True

    if state == (46, 14) and action.lower() == "left-up":
        return True

    if state == (25, 49) and action.lower() == "left-down":
        return True

    if state == (15, 31) and action.lower() == "right-down":
        return True

    if state == (30, 5) and action.lower() == "right-down":
        return True

    if state == (47, 7) and action.lower() == "right-up":
        return True

    if state == (34, 27) and action.lower() == "right":
        return True

    if state == (41, 48) and action.lower() == "left":
        return True

    if state == (9, 6) and action.lower() == "left-down":
        return True

    if state == (14, 51) and action.lower() == "left":
        return True

    if state == (11, 51) and action.lower() == "left-down":
        return True

    if state == (2, 16) and action.lower() == "down":
        return True

    if state == (21, 49) and action.lower() == "right-down":
        return True

    if state == (16, 39) and action.lower() == "left-up":
        return True

    if state == (18, 23) and action.lower() == "left-down":
        return True

    if state == (36, 19) and action.lower() == "right":
        return True

    if state == (32, 38) and action.lower() == "down":
        return True

    if state == (45, 49) and action.lower() == "left-down":
        return True

    if state == (18, 24) and action.lower() == "left":
        return True

    if state == (37, 30) and action.lower() == "right-down":
        return True

    if state == (14, 25) and action.lower() == "left-down":
        return True

    if state == (24, 1) and action.lower() == "right":
        return True

    if state == (29, 18) and action.lower() == "down":
        return True

    if state == (41, 26) and action.lower() == "right-up":
        return True

    if state == (15, 44) and action.lower() == "left-up":
        return True

    if state == (3, 2) and action.lower() == "left":
        return True

    if state == (2, 51) and action.lower() == "left":
        return True

    if state == (16, 38) and action.lower() == "left-down":
        return True

    if state == (29, 36) and action.lower() == "right-up":
        return True

    if state == (18, 36) and action.lower() == "right-up":
        return True

    if state == (27, 37) and action.lower() == "down":
        return True

    if state == (20, 14) and action.lower() == "right":
        return True

    if state == (10, 41) and action.lower() == "left-down":
        return True

    if state == (36, 2) and action.lower() == "up":
        return True

    if state == (31, 45) and action.lower() == "left-down":
        return True

    if state == (40, 22) and action.lower() == "down":
        return True

    if state == (39, 29) and action.lower() == "right-up":
        return True

    if state == (34, 22) and action.lower() == "right-up":
        return True

    if state == (3, 28) and action.lower() == "down":
        return True

    if state == (14, 18) and action.lower() == "down":
        return True

    if state == (33, 41) and action.lower() == "left":
        return True

    if state == (39, 18) and action.lower() == "right-up":
        return True

    if state == (17, 51) and action.lower() == "left-up":
        return True

    if state == (12, 21) and action.lower() == "down":
        return True

    if state == (41, 30) and action.lower() == "up":
        return True

    if state == (7, 37) and action.lower() == "left-down":
        return True

    if state == (33, 36) and action.lower() == "down":
        return True

    if state == (28, 26) and action.lower() == "left-down":
        return True

    if state == (36, 27) and action.lower() == "right-down":
        return True

    if state == (27, 19) and action.lower() == "right-down":
        return True

    if state == (1, 40) and action.lower() == "left-down":
        return True

    if state == (20, 15) and action.lower() == "right-down":
        return True

    if state == (46, 22) and action.lower() == "up":
        return True

    if state == (46, 49) and action.lower() == "down":
        return True

    if state == (35, 10) and action.lower() == "right":
        return True

    if state == (14, 10) and action.lower() == "right-up":
        return True

    if state == (12, 2) and action.lower() == "right-down":
        return True

    if state == (17, 45) and action.lower() == "left":
        return True

    if state == (7, 18) and action.lower() == "left-up":
        return True

    if state == (9, 31) and action.lower() == "down":
        return True

    if state == (19, 7) and action.lower() == "right-down":
        return True

    if state == (35, 38) and action.lower() == "left-up":
        return True

    if state == (13, 4) and action.lower() == "left-down":
        return True

    if state == (9, 24) and action.lower() == "left-up":
        return True

    if state == (28, 2) and action.lower() == "left-up":
        return True

    if state == (40, 33) and action.lower() == "right":
        return True

    if state == (15, 9) and action.lower() == "right-up":
        return True

    if state == (0, 28) and action.lower() == "down":
        return True

    if state == (5, 50) and action.lower() == "left-down":
        return True

    if state == (45, 35) and action.lower() == "right-up":
        return True

    if state == (6, 2) and action.lower() == "right-up":
        return True

    if state == (3, 39) and action.lower() == "down":
        return True

    if state == (30, 8) and action.lower() == "left-down":
        return True

    if state == (10, 6) and action.lower() == "left":
        return True

    if state == (46, 0) and action.lower() == "right-down":
        return True

    if state == (15, 36) and action.lower() == "left-down":
        return True

    if state == (15, 11) and action.lower() == "up":
        return True

    if state == (28, 33) and action.lower() == "right-up":
        return True

    if state == (8, 46) and action.lower() == "right-down":
        return True

    if state == (9, 1) and action.lower() == "left-down":
        return True

    if state == (44, 25) and action.lower() == "right-down":
        return True

    if state == (44, 41) and action.lower() == "right":
        return True

    if state == (0, 17) and action.lower() == "right-down":
        return True

    if state == (6, 15) and action.lower() == "right-up":
        return True

    if state == (44, 42) and action.lower() == "right-down":
        return True

    if state == (11, 28) and action.lower() == "left-down":
        return True

    if state == (26, 14) and action.lower() == "right-down":
        return True

    if state == (40, 34) and action.lower() == "right-down":
        return True

    if state == (46, 39) and action.lower() == "right-down":
        return True

    if state == (42, 6) and action.lower() == "right":
        return True

    if state == (5, 21) and action.lower() == "left-down":
        return True

    if state == (40, 11) and action.lower() == "up":
        return True

    if state == (22, 24) and action.lower() == "down":
        return True

    if state == (1, 28) and action.lower() == "down":
        return True

    if state == (13, 35) and action.lower() == "left-down":
        return True

    if state == (28, 7) and action.lower() == "down":
        return True

    if state == (17, 31) and action.lower() == "left":
        return True

    if state == (48, 49) and action.lower() == "up":
        return True

    if state == (6, 1) and action.lower() == "right":
        return True

    if state == (34, 16) and action.lower() == "right-up":
        return True

    if state == (9, 17) and action.lower() == "right":
        return True

    if state == (30, 0) and action.lower() == "right-down":
        return True

    if state == (28, 0) and action.lower() == "right-up":
        return True

    if state == (45, 37) and action.lower() == "right-down":
        return True

    if state == (2, 17) and action.lower() == "left-down":
        return True

    if state == (7, 0) and action.lower() == "right-up":
        return True

    if state == (46, 28) and action.lower() == "left-up":
        return True

    if state == (24, 20) and action.lower() == "left-down":
        return True

    if state == (36, 14) and action.lower() == "right":
        return True

    if state == (45, 27) and action.lower() == "right-up":
        return True

    if state == (14, 4) and action.lower() == "down":
        return True

    if state == (32, 51) and action.lower() == "left":
        return True

    if state == (33, 3) and action.lower() == "right-down":
        return True

    if state == (21, 15) and action.lower() == "right":
        return True

    if state == (40, 36) and action.lower() == "left-down":
        return True

    if state == (38, 40) and action.lower() == "right-up":
        return True

    if state == (42, 17) and action.lower() == "right-up":
        return True

    if state == (27, 27) and action.lower() == "left-down":
        return True

    if state == (8, 38) and action.lower() == "left":
        return True

    if state == (12, 34) and action.lower() == "right-down":
        return True

    if state == (48, 37) and action.lower() == "right":
        return True

    if state == (18, 29) and action.lower() == "left":
        return True

    if state == (16, 1) and action.lower() == "right":
        return True

    if state == (32, 3) and action.lower() == "down":
        return True

    if state == (16, 47) and action.lower() == "left-down":
        return True

    if state == (47, 46) and action.lower() == "right":
        return True

    if state == (22, 20) and action.lower() == "left-down":
        return True

    if state == (0, 14) and action.lower() == "right-down":
        return True

    if state == (30, 31) and action.lower() == "right":
        return True

    if state == (34, 50) and action.lower() == "right-down":
        return True

    if state == (10, 38) and action.lower() == "left":
        return True

    if state == (23, 17) and action.lower() == "up":
        return True

    if state == (9, 44) and action.lower() == "left-down":
        return True

    if state == (4, 39) and action.lower() == "down":
        return True

    if state == (6, 44) and action.lower() == "down":
        return True

    if state == (44, 43) and action.lower() == "right":
        return True

    if state == (47, 9) and action.lower() == "left-up":
        return True

    if state == (24, 6) and action.lower() == "right-down":
        return True

    if state == (38, 24) and action.lower() == "right":
        return True

    if state == (26, 40) and action.lower() == "right-down":
        return True

    if state == (3, 43) and action.lower() == "left-down":
        return True

    if state == (40, 44) and action.lower() == "up":
        return True

    if state == (33, 1) and action.lower() == "right-down":
        return True

    if state == (27, 32) and action.lower() == "right-down":
        return True

    if state == (11, 46) and action.lower() == "left-down":
        return True

    if state == (35, 29) and action.lower() == "right-down":
        return True

    if state == (22, 46) and action.lower() == "down":
        return True

    if state == (32, 47) and action.lower() == "down":
        return True

    if state == (34, 36) and action.lower() == "down":
        return True

    if state == (38, 18) and action.lower() == "right-up":
        return True

    if state == (43, 16) and action.lower() == "right-up":
        return True

    if state == (34, 4) and action.lower() == "right":
        return True

    if state == (12, 48) and action.lower() == "right-down":
        return True

    if state == (25, 36) and action.lower() == "right-down":
        return True

    if state == (15, 42) and action.lower() == "left-down":
        return True

    if state == (47, 3) and action.lower() == "right-up":
        return True

    if state == (13, 51) and action.lower() == "left-down":
        return True

    if state == (29, 31) and action.lower() == "right-down":
        return True

    if state == (35, 40) and action.lower() == "left-up":
        return True

    if state == (34, 39) and action.lower() == "left-down":
        return True

    if state == (32, 24) and action.lower() == "right-up":
        return True

    if state == (41, 47) and action.lower() == "left-down":
        return True

    if state == (29, 33) and action.lower() == "right-up":
        return True

    if state == (4, 47) and action.lower() == "left":
        return True

    if state == (44, 13) and action.lower() == "right-up":
        return True

    if state == (17, 19) and action.lower() == "left-down":
        return True

    if state == (20, 10) and action.lower() == "right":
        return True

    if state == (24, 13) and action.lower() == "right-down":
        return True

    if state == (48, 29) and action.lower() == "up":
        return True

    if state == (2, 23) and action.lower() == "right-down":
        return True

    if state == (5, 12) and action.lower() == "right-up":
        return True

    if state == (42, 10) and action.lower() == "right-down":
        return True

    if state == (15, 0) and action.lower() == "right":
        return True

    if state == (39, 10) and action.lower() == "right-up":
        return True

    if state == (32, 31) and action.lower() == "right":
        return True

    if state == (1, 22) and action.lower() == "left-down":
        return True

    if state == (47, 47) and action.lower() == "right-up":
        return True

    if state == (25, 34) and action.lower() == "right":
        return True

    if state == (22, 3) and action.lower() == "right-down":
        return True

    if state == (2, 48) and action.lower() == "right-down":
        return True

    if state == (21, 12) and action.lower() == "right-down":
        return True

    if state == (5, 31) and action.lower() == "left":
        return True

    if state == (26, 31) and action.lower() == "right-down":
        return True

    if state == (4, 15) and action.lower() == "right-up":
        return True

    if state == (44, 8) and action.lower() == "right":
        return True

    if state == (11, 32) and action.lower() == "left-down":
        return True

    if state == (23, 21) and action.lower() == "left-down":
        return True

    if state == (12, 14) and action.lower() == "right-up":
        return True

    if state == (38, 30) and action.lower() == "right":
        return True

    if state == (2, 50) and action.lower() == "left-down":
        return True

    if state == (16, 35) and action.lower() == "left-down":
        return True

    if state == (24, 40) and action.lower() == "right-down":
        return True

    if state == (25, 33) and action.lower() == "right-down":
        return True

    if state == (37, 15) and action.lower() == "right-up":
        return True

    if state == (42, 37) and action.lower() == "left-down":
        return True

    if state == (10, 13) and action.lower() == "right":
        return True

    if state == (13, 16) and action.lower() == "left":
        return True

    if state == (12, 11) and action.lower() == "right-up":
        return True

    if state == (15, 6) and action.lower() == "left-down":
        return True

    if state == (9, 50) and action.lower() == "left-up":
        return True

    if state == (44, 36) and action.lower() == "right-down":
        return True

    if state == (2, 29) and action.lower() == "left-down":
        return True

    if state == (41, 33) and action.lower() == "right-up":
        return True

    if state == (39, 17) and action.lower() == "right-up":
        return True

    if state == (28, 34) and action.lower() == "right":
        return True

    if state == (8, 22) and action.lower() == "left-down":
        return True

    if state == (34, 44) and action.lower() == "left-down":
        return True

    if state == (41, 3) and action.lower() == "right-down":
        return True

    if state == (48, 21) and action.lower() == "left-up":
        return True

    if state == (30, 4) and action.lower() == "right":
        return True

    if state == (43, 6) and action.lower() == "right-up":
        return True

    if state == (0, 42) and action.lower() == "left-down":
        return True

    if state == (27, 18) and action.lower() == "right":
        return True

    return False



