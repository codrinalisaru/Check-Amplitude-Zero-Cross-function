def CheckAmplZeroCross(signalc):  
 
  myBoolean = true
  Vector = [] 
  maxim = TPT.FloatX()
  minim = TPT.FloatX()
  maxim=0
  minim=0
  
#  inputsignalc_deriv_previos2 = TPT.Double()      
#  inputsignalc_deriv2         = TPT.Double()
  if signalc(@)>=0:
    myBoolean=true
  else:
    myBoolean=false
#  during TPT.regexp([t>@]):
  if myBoolean==true:
      if signalc>maxim:
        maxim=signalc
      if signalc==0:
        myBoolean=false
        Vector.append(maxim)
        maxim=0
  else:
      if signalc(t) < minim:
        minim=signalc(t)
      if signalc == 0:
        myBoolean=true
        Vector.append(minim)
        minim=0
  return Vector     
