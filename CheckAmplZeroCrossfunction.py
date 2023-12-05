#Original code from Bogdan:
# def CheckAmplZeroCross(signalc):  
 
#   myBoolean = true
#   Vector = [] 
#   maxim = TPT.FloatX()
#   minim = TPT.FloatX()
#   maxim=0
#   minim=0
  
# #  inputsignalc_deriv_previos2 = TPT.Double()      
# #  inputsignalc_deriv2         = TPT.Double()
#   if signalc(@)>=0:
#     myBoolean=true
#   else:
#     myBoolean=false
# #  during TPT.regexp([t>@]):
#   if myBoolean==true:
#       if signalc>maxim:
#         maxim=signalc
#       if signalc==0:
#         myBoolean=false
#         Vector.append(maxim)
#         maxim=0
#   else:
#       if signalc(t) < minim:
#         minim=signalc(t)
#       if signalc == 0:
#         myBoolean=true
#         Vector.append(minim)
#         minim=0
#   return Vector     


def CheckAmplZeroCross(signalc):  
  #myBoolean = True
  myArray = []
  maxim=0
  minim=0
  
  # if signalc(@)>=0:
  #   myBoolean=True
  # else:
  #   myBoolean=False
#  during TPT.regexp([t>@]):
  for element in range(0, len(signalc)):
    #if myBoolean==True:
        if signalc[element]>maxim:
          maxim=signalc[element]
          myArray.append(maxim)
          maxim = 0
        if signalc[element]==0:
          #myBoolean=False
          #Vector.append(maxim)
          maxim=0
    #elif myBoolean==False:
        if signalc[element] < minim:
          minim=signalc[element]
          myArray.append(minim)
          minim = 0
        if signalc[element] == 0:
          #myBoolean=True
          minim=0
  return myArray     

mySignal = [1, 2, 3, 2, 1, 0, -1, -2, -3, -2, -1, 0, 1, 2, 3, 2, 1, 0, -1, -2, -3, -2, -1, 0, 1, 2]
print(CheckAmplZeroCross(mySignal))


# for i in range(0, len(mySignal)):
#     print(mySignal[i])


#Best version

def CheckAmplZeroCross(signalc):  

  myArray = []
  maxim=0
  minim=0
  myBoolean = True

  for element in range(0, len(signalc)):
      if myBoolean == True:
            if signalc[element]>maxim:
              maxim=signalc[element]
    
            if signalc==0:
              myBoolean = False
              myArray +=[maxim]
              maxim=0
      else:
            if signalc < minim:
                minim=signalc[element]

            if signalc == 0:
                myBoolean = True
                myArray += [minim]
                minim=0

  return myArray     

mySignal = [1, 2, 5, 2, 1, 0, -1, -2, -5, -2, -1, 0, 1, 2, 3, 2, 1, 0, -1, -2, -3, -2, -1, 0, 1, 2]
print(CheckAmplZeroCross(mySignal))

mysecondsignal = [1, 2, 5, 2, 1, 0, -1, -2, -5, -2, -1, 0, 1, 2, 3, 2, 1, 0, -1, -2, -3, -2, -1, 0, 1, 2]
print(CheckAmplZeroCross(mysecondsignal))
for i in range(0, len(mySignal)):
    if (mySignal[i] == (mysecondsignal[i])):
        print("Samples equal")
    else:
        print("Different samples")

