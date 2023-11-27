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


# for i in range(0, len(mySignal)):
#     print(mySignal[i])


