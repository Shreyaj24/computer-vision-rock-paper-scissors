import time
def countdown():
    t = 0
    i = 0
    j : int = 5
    start_counter = time.time()
    while t <= 6:
        end_counter = time.time()
        t = int(end_counter -start_counter)
        if t in ( 1, 2, 3, 4, 5, 6) and i!=t: 
            #print ('t: ',t)
            print(j)
            j -= 1
        i = t
    print('Start')    

countdown()