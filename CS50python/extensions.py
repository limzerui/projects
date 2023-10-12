# Get user input
filename=input("File name: ")
filename = filename.lower()
# If gif or png or jpg or jpeg, print "image/type"
if '.gif' in filename:
    print("image/gif")
elif '.png' in filename:
    print("image/png")
elif '.jgp' in filename:
    print("image/jpg")
elif '.jpeg' in filename:
    print("image/jpeg")
# If pdf or zip, print "application/type"
elif '.pdf' in filename:
    print("application/pdf")
elif '.zip' in filename:
    print("application/zip")
# If txt, print "text/plain"
elif '.txt' in filename:
    print("text/plain")
# Otherwise, print "application/octet-stream"
else:
    print("application/octet-stream")
# Otherwise, print "application/octet-stream"