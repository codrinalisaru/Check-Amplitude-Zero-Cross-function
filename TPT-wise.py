def CheckAmplZeroCross(signalc):  
  myArray = TPT.FloatArrayX()
  myBoolean = TPT.BooleanX()
  myBoolean(t) := True
  maxim = TPT.IntX()
  maxim(t) := 0
  minim = TPT.IntX()
  minim(t) := 0
 
  for element in range(0, len(signalc(t))):
    if (myBoolean == True):
        if signalc[element](t)>maxim(t):
          maxim(t) :=signalc[element](t)          
        if signalc[element](t)==0:
          myBoolean(t) := False
          myArray(t) += [maxim](t)
          maxim(t) := 0
    else:
        if signalc[element](t) < minim(t):
          minim(t) := signalc[element](t)
        if signalc[element](t) == 0:
          myBoolean=True
          myArray(t) += [minim](t)
          minim(t) :=0
  return myArray     



signal1 = CheckAmplZeroCross(input)
signal2 = CheckAmplZeroCross(output)

during TPT.regexp([t>@]):
    for i in range(0, 240):
        if (abs(signal1[i](t)) >= abs(signal2[i](t))):
            Expected(t) := signal1
        else:
            Expected(t) := 0
          

