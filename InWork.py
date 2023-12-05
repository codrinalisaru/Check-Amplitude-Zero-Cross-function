def CheckAmplZeroCross(signalc):  

  myArray = []
  maxim=0
  minim=0
  isPositiveCycle = True

  for i in range(0, len(signalc)):
      if isPositiveCycle == True:
            if signalc[i]>maxim:
              maxim=signalc[i]
    
            if signalc[i]==0:
              isPositiveCycle = False
              myArray +=[maxim]
              maxim=0
      else:
            if signalc[i] < minim:
                minim=signalc[i]

            if signalc[i] == 0:
                isPositiveCycle = True
                myArray += [minim]
                minim=0

  return myArray     

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
print(CheckAmplZeroCross(mySignal))

mysecondsignal = [1, 2, 5, 2, 1, 0, -1, -2, -5, -2, -1, 0, 1, 2, 3, 2, 1, 0, -1, -2, -3, -2, -1, 0, 1, 2]
print(CheckAmplZeroCross(mysecondsignal))
for i in range(0, len(mySignal)):
    if (mySignal[i] == (mysecondsignal[i])):
        print("Samples equal")
    else:
        print("Different samples")
