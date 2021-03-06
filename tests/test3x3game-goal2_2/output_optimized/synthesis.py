def Legal(state, action):

    if (state[0] < 0 or state[0] >= 3) or (state[1] < 0 or state[1] >= 3):
        raise Exception("The input state is not among the grid states.")

    if action.lower() not in ["up", "left-up", "right-up", "right", "right-down", "down", "left-down", "left"]:
        raise Exception("The input action is not among the actions that can be performed.")

    if state == (0, 0) and action.lower() == "right-down":
        return True

    if state == (1, 1) and action.lower() == "left-up":
        return True

    if state == (1, 1) and action.lower() == "right":
        return True

    if state == (1, 1) and action.lower() == "right-down":
        return True

    if state == (1, 2) and action.lower() == "down":
        return True

    if state == (1, 2) and action.lower() == "left":
        return True

    if state == (2, 2) and action.lower() == "left-up":
        return True

    if state == (2, 2) and action.lower() == "up":
        return True

    return False



def K(state, action):

    if (state[0] < 0 or state[0] >= 3) or (state[1] < 0 or state[1] >= 3):
        raise Exception("The input state is not among the grid states.")

    if action.lower() not in ["up", "left-up", "right-up", "right", "right-down", "down", "left-down", "left"]:
        raise Exception("The input action is not among the actions that can be performed.")

    if state == (1, 1) and action.lower() == "right-down":
        return True

    if state == (1, 2) and action.lower() == "down":
        return True

    if state == (0, 0) and action.lower() == "right-down":
        return True

    return False



