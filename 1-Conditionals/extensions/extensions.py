NAME = input("file name?")
if NAME.endswith((".jpg",".jpeg")) :
    print("photo/jpg")
elif NAME.endswith(".gif") :
    print("image/gif")
elif NAME.endswith(".png") :
    print("image/png")
elif NAME.endswith(".pdf") :
    print("application/pdf")
elif NAME.endswith(".txt") :
    print("text/plain")
elif NAME.endswith(".zip") :
    print("application/zip")
else:
    print("application/octet-stream")