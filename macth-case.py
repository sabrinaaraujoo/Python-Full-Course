# Match Case (switch) =  An alternative way to use 'elif'
#                       If the valeu mathes if the case return a output
#                       Benefits: It's clean and readable

def isWeekend(day):
    match day:
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case "Saturday" | "Sunday":
            return True
        case _:
            return False

print(isWeekend("day"))