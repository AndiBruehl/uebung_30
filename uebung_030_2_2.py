file = open("env" , "w")
env_vars = "USER=otto\nPASS=otto\nHOST=192.168.0.34"
file.write(env_vars)
file.close()