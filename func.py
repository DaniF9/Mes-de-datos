#Vamos a crear una función de longitud variable que pueda calcular cuántos 
#minutos quedan hasta el inicio, dado el tiempo que va a tardar cada paso:

def sequence_time(*args):
    total_minutes = sum(args)
    if total_minutes < 60:
        return f"Total time to launch is {total_minutes} minutes"
    else:
        return f"Total time to launch is {total_minutes/60} hours"

