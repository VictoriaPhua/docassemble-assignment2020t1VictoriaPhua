import re
from docassemble.base.util import *

def check_nric(IC):
  flag = 0
  if not re.match(r'[STFGstfg][0-9]{7}[A-Za-z]', IC):
    validation_error('Invalid NRIC format.')
    flag = 1
  
  if flag != 1: 
    # storing the value of d0
    if IC[0]=='S' or IC[0]=='s' or IC[0]=='F' or IC[0]=='f' :
        d0 = 0
    elif IC[0]=='T' or IC[0]=='t' or IC[0]=='G' or IC[0]=='g' :
        d0 = 4
    try:   
      a = (d0 + int(IC[1])*2+int(IC[2])*7+int(IC[3])*6+int(IC[4])*5+int(IC[5])*4+int(IC[6])*3+int(IC[7])*2) % 11

      # storing the check digit in b
      if IC[0] == 'S' or IC[0] == 's' or IC[0] == 'T' or IC[0]=='t' :
          if IC[-1] == "J" or IC[-1] == "j":
                b = 0
          elif IC[-1] == "Z" or IC[-1] == "z":
                b = 1
          elif IC[-1] == "I" or IC[-1] == "i":
                b = 2
          elif IC[-1] == "H" or IC[-1] == "h":
                b = 3
          elif IC[-1] == "G" or IC[-1] == "g":
                b = 4
          elif IC[-1] == "F" or IC[-1] == "f":
                b = 5
          elif IC[-1] == "E" or IC[-1] == "e":
                b = 6
          elif IC[-1] == "D" or IC[-1] == "d":
                b = 7
          elif IC[-1] == "C" or IC[-1] == "c":
                b = 8
          elif IC[-1] == "B" or IC[-1] == "b":
                b = 9
          elif IC[-1] == "A" or IC[-1] == "a":
                b = 10
      elif IC[0] == 'F' or IC[0] == 'f' or IC[0] == 'G' or IC[0]=='g' :
        if IC[-1] == "K" or IC[-1] == "k":
                b = 10
        elif IC[-1] == "L" or IC[-1] == "l":
                b = 9
        elif IC[-1] == "M" or IC[-1] == "m":
                b = 8
        elif IC[-1] == "N" or IC[-1] == "n":
                b = 7
        elif IC[-1] == "P" or IC[-1] == "p":
                b = 6
        elif IC[-1] == "Q" or IC[-1] == "q":
                b = 5
        elif IC[-1] == "R" or IC[-1] == "r":
                b = 4
        elif IC[-1] == "T" or IC[-1] == "t":
                b = 3
        elif IC[-1] == "U" or IC[-1] == "u":
                b = 2
        elif IC[-1] == "W" or IC[-1] == "w":
                b = 1
        elif IC[-1] == "X" or IC[-1] == "x":
                b = 0
      try: 
        if not(a == b): validation_error('InValid NRIC format.')
      except: validation_error('Invalid NRIC format.')
    except: validation_error('Invalid NRIC format.')
    
  return True