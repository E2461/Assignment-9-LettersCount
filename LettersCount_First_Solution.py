str1 = "hippo runs to us!"
  
kume = {} 
  
for i in str1: 
    if i in kume: 
        kume[i] += 1
    else: 
        kume[i] = 1
  
  
print ("Count of all characters in Str1 is :\n" +
                                          str(kume)) 
