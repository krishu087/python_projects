import os 
import pyttsx3

if __name__ == '__main__':
    print("Welcome to robo speaker !")

    while True:
        x=input("enter what you want me to speak :")
        if x=='q':
            break
        Command=x
        os.system(Command)