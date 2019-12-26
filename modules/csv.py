


def csv(file,values):
    humidity, temperature = values
    with open(file,"a") as f:
        f.write(time.strftime("%d.%m.%Y - %H:%M:%S")+","+str(temperature)+","+str(humidity)+"\n")
