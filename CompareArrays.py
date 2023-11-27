def CheckAmplZeroCross(signalc):  

  myArray = []
  maxim=0
  minim=0

  for element in range(0, len(signalc)):
        if signalc[element]>maxim:
          maxim=signalc[element]
          myArray +=[maxim]
          maxim = 0
        if signalc[element]==0:
          maxim=0
        if signalc[element] < minim:
          minim=signalc[element]
          myArray += [minim]
          minim = 0
        if signalc[element] == 0:
          minim=0
  return myArray     

mySignal = [1, 2, 3, 2, 1, 0, -1, -2, -3, -2, -1, 0, 1, 2, 3, 2, 1, 0, -1, -2, -3, -2, -1, 0, 1, 2]
print(CheckAmplZeroCross(mySignal))

mysecondsignal = [1, 2, 3, 2, 1, 0, -1, -2, -3, -2, -1, 0, 1, 2, 3, 2, 1, 0, -1, -2, -3, -2, -1, 0, 1, 2]
print(CheckAmplZeroCross(mysecondsignal))

for l1,l2 in zip(mySignal,mysecondsignal):
    if l1 < l2:
        print("l1 < l2")
    elif l1 > l2:
        print("l2 > l1")
    elif l1 == l2:
        print("l1 == l2")

for i in range(0, len(mySignal)):
    if (mySignal[i] == (mysecondsignal[i])):
        print("Samples equal")
    else:
        print("Different samples")