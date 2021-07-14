# This was the hardest bit of code yet:


# very impressed with myself


def format_duration(seconds):
    
    years = int(seconds/(365*24*60*60))
    days = int((seconds-(years*365*24*60*60))/(24*60*60))
    hours = int((seconds-(years*365*24*60*60)-(days*24*60*60)) / (60*60))
    mins = int((seconds-(years*365*24*60*60)-(days*24*60*60) - hours*60*60)/60)
    sec = (seconds -(years*365*24*60*60)-(days*24*60*60)- hours*60*60 - mins*60)
    
    total = [years, days, hours, mins, sec]
    
    x = ""
    
    if years == 1:
        x += "1 year, "
    elif years > 1:
        x += str(years) + " years, "
        
    if days == 1:
        x += "1 day, "
    elif days >1:
        x += str(days) + " days, "
    
    if hours == 1:
        x += "1 hour, "
    elif hours >1:
        x += str(hours) + " hours, "
    
    if sec == 0 and mins > 0:
        x = x[:-2]
        x += " and "
   
    if mins == 1:
        x += "1 minute, "
    elif mins >1:
        x += str(mins) + " minutes, "
    
       
    if sec == 1:
        x = x[:-2]
        x += " and 1 second"
    elif sec > 1:
        x = x[:-2]
        x += " and " + str(sec) + " seconds"
    
    
    if seconds == 0:
        x = "now"
    
    if x[0] == ",":
        x = x[1:]
    
    if x[0] == " ":
        x = x[1:]
    
    if x[-1] == " ":
        x = x[:-1]
        
    if x[-1] == ",":
        x = x[:-1]
    
    if x[0] == "a":
        x = x[4:]    
    return x
            
print(format_duration(100000))