def CheckAmplZeroCross(signalc):  
  myArray = TPT.FloatArrayX()
  maxim = TPT.IntX()
  maxim(t) := 0
  minim = TPT.IntX()
  minim(t) := 0
 
during TPT.regexp([t>@]):
  for element in range(0, len(signalc(t))):
        if signalc[element](t)>maxim(t):
          maxim(t) :=signalc[element](t)
          myArray(t) += [maxim](t)
          maxim(t) := 0
        if signalc[element](t)==0:
          maxim(t) := 0
        if signalc[element](t) < minim(t):
          minim(t) := signalc[element](t)
          myArray(t) += [minim](t)
          minim(t) := 0
        if signalc[element](t) == 0:
          #myBoolean=True
          minim(t) :=0
  return myArray     


during TPT.regexp([t>@]):
    Expected(t) := signal1[element] == signal2[element] ? signal1(t) : 0
    Diff = TPT.hose(Out, expected, 0, 0)

    for i in range(0, len(mySignal)):
        if (signal1[i] == (signal2[i])):
            Expected(t) := signal1
        else:
            Expected(t) := 0

