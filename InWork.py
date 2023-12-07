#local minimum and maximum function - in progress

def MinMax (signalc):
    myDerivative = []
    minMax = []
    #j = 0
    for i in range(1, len(signalc)):
        delta = signalc[i] - signalc[i-1]
        myDerivative.append(delta)
        #myDerivative[j] = delta
        #j++
    for i in range(1, len(myDerivative)):
        
    return 

mySignal = [1, 2, 5, 2, 1, 0, -1, -2, -5, -2, -1, 0, 1, 2, 3, 2, 1, 0, -1, -2, -3, -2, -1, 0, 1, 2]

mysecondsignal = [1, 2, 5, 2, 1, 0, -1, -2, -5, -2, -1, 0, 1, 2, 3, 2, 1, 0, -1, -2, -3, -2, -1, 0, 1, 2]
