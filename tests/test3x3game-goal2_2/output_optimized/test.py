

import synthesis as syn



def game_test():
    
    print("\n\n\n***** TEST CONTROLLER INTERROGATION *****\n")

    grid = [[0, 1, 1], [1, 0, 'I'], [1, 1, 'G']]

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print("{0}  ".format(grid[i][j]), end = '')
        print()

    print("\n\n")


    
    
    print("Legal(({0}, {1}), {2}) = {3}".format(1, 2, "down", syn.Legal((1, 2), "down")))
    print("K(({0}, {1}), {2}) = {3}".format(1, 2, "down", syn.K((1, 2), "down")))
    
    print("\n")

    print("Legal(({0}, {1}), {2}) = {3}".format(1, 2, "left", syn.Legal((1, 2), "left")))
    print("K(({0}, {1}), {2}) = {3}".format(1, 2, "left", syn.K((1, 2), "left")))

    print("\n")

    print("Legal(({0}, {1}), {2}) = {3}".format(1, 1, "left-up", syn.Legal((1, 1), "left-up")))
    print("K(({0}, {1}), {2}) = {3}".format(1, 1, "left-up", syn.K((1, 1), "left-up")))

 
    print("\n")

    print("Legal(({0}, {1}), {2}) = {3}".format(1, 1, "right", syn.Legal((1, 1), "right")))
    print("K(({0}, {1}), {2}) = {3}".format(1, 1, "right", syn.K((1, 1), "right")))

    print("\n")

    print("Legal(({0}, {1}), {2}) = {3}".format(1, 1, "right-down", syn.Legal((1, 1), "right-down")))
    print("K(({0}, {1}), {2}) = {3}".format(1, 1, "right-down", syn.K((1, 1), "right-down")))

   

if __name__ == "__main__":
    game_test()
