def timeit(stmt, globals):
    import timeit as _timeit
    import numpy as np
    
    # Rough approximation of a single run
    trial = _timeit.timeit(stmt, globals=globals, number=1)
    
    # Maximum duration
    duration = 1.0
    
    # Number of repeat
    repeat = 3
    
    # Compute rounded number of trials
    number = max(1,int(10**np.floor(np.log(duration/trial/repeat)/np.log(10))))
    
    # Only report best run
    best = min(_timeit.repeat(stmt, globals=globals, number=number, repeat=repeat))

    units = {"usec": 1, "msec": 1e3, "sec": 1e6}
    precision = 3
    usec = best * 1e6 / number
    if usec < 1000:
        print("%d loops, best of %d: %.*g usec per loop" % (number, repeat,
                                                            precision, usec))
    else:
        msec = usec / 1000
        if msec < 1000:
            print("%d loops, best of %d: %.*g msec per loop" % (number, repeat,
                                                                precision, msec))
        else:
            sec = msec / 1000
            print("%d loops, best of %d: %.*g sec per loop" % (number, repeat,
                                                               precision, sec))
   