import base64
import os

filelist = os.listdir("./Adobe/")


for file in filelist:
    with open(f"./Adobe/{file}", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
        with open("data.txt", "a") as f:
            f.write(
                f'"{file[:2].capitalize()}":"url(\'data:image/jpeg;base64,{encoded_string.decode()}\')",\n'
            )
