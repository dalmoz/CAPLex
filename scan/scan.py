def integers ( chlng ):
    units = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen" ]
    
    tens = [
        "twenty", "thirty", "forty", "fifty", "sixty", "seventy",
        "eighty", "ninety" ]
    magnitude = ["hundred", "thousand", "million", "billion", "trillion"]
    
    cUnits = [s[:1].upper() + s[1:] for s in units]
    cTens = [s[:1].upper() + s[1:] for s in tens]
    cMagnitude = [s[:1].upper() + s[1:] for s in magnitude]
    
    integers = [ "0","1","2","3","4","5","6","7","8","9"]
    
       
    #python magic right here
    
    keywords = units + tens + cUnits + cTens + magnitude + cMagnitude + integers
    
    spot = False
    
    for i in keywords:
        if i in chlng:
            spot = True
            break
    
    return spot
        
def names ( chlng ):
    sNames = ["name", "Name"] 
    #python magic right here
    
    keywords = sNames
    
    spot = False
    
    for i in keywords:
        if i in chlng:
            spot = True
            break
    
    return spot
    
def color ( chlng ):
    sColor = ["Colour", "colour", "Color", "color"] 
    #python magic right here
    
    keywords = sColor
    
    spot = False
    
    for i in keywords:
        if i in chlng:
            spot = True
            break
    
    return spot
      
def position ( chlng ):
    sPos = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh"
            "eighth", "ninth"]
    nPos = ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th"]
    cSPos = [s[:1].upper() + s[1:] for s in sPos]
    cNPos = [s[:1].upper() + s[1:] for s in nPos]
    
    #python magic right here
    
    keywords = sPos + nPos + cSPos + cNPos
    
    spot = False
    
    for i in keywords:
        if i in chlng:
            spot = True
            break
    
    return spot

def math ( chlng ):
    signs = [ "+", "-", "=", "/" ]
    sSigns = ["add", "plus", "minus", "equal", "divide", "factor", "multiply",
              "reduce", "result", "number", "and"]
    
    #python magic right here
    
    keywords = signs + sSigns
    
    spot = False
    
    for i in keywords:
        if i in chlng:
            spot = True
            break
    
    return spot
    
def counting ( chlng ):
    scount = [ "count", "how many" , "the number of" ]
    cscount = [s[:1].upper() + s[1:] for s in scount]
    #python magic right here
    
    keywords = scount + cscount
    
    spot = False
    
    for i in keywords:
        if i in chlng:
            spot = True
            break
    
    return spot

def compare ( chlng ):
    sCompare = [ "biggest", "smallest", "largest", "lowest", "highest",
                "maximum", "maximal", "minimum", "minimal"]
    cCompare = [s[:1].upper() + s[1:] for s in sCompare]

    #python magic right here
    
    keywords = sCompare
    
    spot = False
    
    for i in keywords:
        if i in chlng:
            spot = True
            break
    
    return spot

def bodyPart ( chlng ):
    units = [ "body", "part" ]   
    #python magic right here
    
    keywords = units
    
    spot = False
    
    for i in keywords:
        if i in chlng:
            spot = True
            break
    
    return spot

def listSelect ( chlng ):
    units = [ "list", "List", "series", ": the" ]   
    #python magic right here
    
    keywords = units
    
    spot = False
    
    for i in keywords:
        if i in chlng:
            spot = True
            break
    
    return spot
  
def dayRef ( chlng ):
    units = [ "today", "yesterday", "tomorrow",
             "Today", "Yesterday", "Tomorrow", " day" ]   
    #python magic right here
    
    keywords = units
    
    spot = False
    
    for i in keywords:
        if i in chlng:
            spot = True
            break
    
    return spot

def digits ( chlng ):
    units = [ "digit", "as a" ]   
    #python magic right here
    
    keywords = units
    
    spot = False
    
    for i in keywords:
        if i in chlng:
            spot = True
            break
    
    return spot