global new_transition_P
global new_transition_R
global new_transition_S
global new_transition_any

transition_P = [[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0.5, 0, 0, 0.5, 0, 0, 0], [0, 0, 0, 0, 0, 0.5, 0, 0, 0.5, 0, 0],
                [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

transition_R = [[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

transition_S = [[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

transition_any = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

reward_function = [[0, 2, 0, -1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0],
                   [0, 0, 0, 0, 2, -1, 0, 2, 0, 0, 0], [0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0],
                   [0, 0, 0, 0, 0, 0, 2, 0, -1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

discount_rate = 0.99
new_transition_P = transition_P
new_transition_R = transition_R
new_transition_S = transition_S
new_transition_any = transition_any


def calculate_initial_value(i):
    value_p = 0
    value_r = 0
    value_s = 0
    value_any = 0
    for j in range(len(transition_P[i])):
        value_p = value_p + transition_P[i][j] * reward_function[i][j]
        value_r = value_r + transition_R[i][j] * reward_function[i][j]
        value_s = value_s + transition_S[i][j] * reward_function[i][j]
        value_any = value_any + transition_any[i][j] * reward_function[i][j]
        value = max(value_p, value_r, value_s, value_any)
        if transition_P[i][j] != 0:
            new_transition_P[i][j] = value
        if transition_R[i][j] != 0:
            new_transition_R[i][j] = value
        if transition_S[i][j] != 0:
            new_transition_S[i][j] = value
        if transition_any[i][j] != 0:
            new_transition_any[i][j] = value
    return value


def calculate_values_until_convergence(i):
    value_p = 0
    value_r = 0
    value_s = 0
    value_any = 0
    new_value_list_for_p = []
    new_value_list_for_r = []
    new_value_list_for_s = []
    new_value_list_for_any = []

    # calculate value function
    for j in range(len(transition_P[i])):
        value_p = value_p + transition_P[i][j] * (reward_function[i][j] + (discount_rate * new_transition_P[i][j]))
        value_r = value_r + transition_R[i][j] * (reward_function[i][j] + (discount_rate * new_transition_R[i][j]))
        value_s = value_s + transition_S[i][j] * (reward_function[i][j] + (discount_rate * new_transition_S[i][j]))
        value_any = value_any + transition_any[i][j] * (
                reward_function[i][j] + (discount_rate * new_transition_any[i][j]))
        value = max(value_p, value_r, value_s, value_any)

        # update with the new transitional probabilities
        if transition_P[i][j] != 0:
            new_transition_P[i][j] = value
            new_value_list_for_p.append(value)
        if transition_R[i][j] != 0:
            new_transition_R[i][j] = value
            new_value_list_for_r.append(value)
        if transition_S[i][j] != 0:
            new_transition_S[i][j] = value
            new_value_list_for_s.append(value)
        if transition_any[i][j] != 0:
            new_transition_any[i][j] = value
            new_value_list_for_any.append(value)

    # check for estimated value in each state
    if new_value_list_for_p:
        print("Estimated value for p", max(new_value_list_for_p))
    if new_value_list_for_r:
        print("Estimated value for r", max(new_value_list_for_r))
    if new_value_list_for_s:
        print("Estimated value for s", max(new_value_list_for_s))
    if new_value_list_for_any:
        print("Estimated value for any", max(new_value_list_for_any))
    return value


def find_value_function_for_all_states():
    i = 0
    while i <= 10:

        # value in previous state
        previous_value = calculate_initial_value(i)
        print("Previous value for state ", i, "is", previous_value)

        # new value in previous state
        new_value = calculate_values_until_convergence(i)
        print("New value for state ", i, "is", new_value)
        if new_value in new_transition_P:
            print("Action chosen: P")
        elif new_value in new_transition_R:
            print("Action chosen: R")
        elif new_value in new_transition_S:
            print("Action chosen: S")
        else:
            print("Action chosen: any \n")

        # check for difference in values
        if new_value - previous_value <= 0.001:
            break
        i = i + 1


find_value_function_for_all_states()
