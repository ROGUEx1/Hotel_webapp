def database(obj):
    write = open("static/databases/database.txt", "a")
    write.write(obj.room)
    write.write("\n")
    write.write(obj.passkey)
    print("Sign up done!")
    write.write("\n")
    write.close()
    print("This it done hereafter!")
