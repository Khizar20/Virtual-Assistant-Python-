import VirtualAssistant
import sys


print("*************** VIRTUAL ASSISTANT *************")
jarvis = VirtualAssistant

def mainMenu():

    jarvis.speak("Do you want to Give Command or Select Manually")
    ans = input("Do you want to :\n1. Give command\n2. Select manually\n3. Exit\n")


    if ans == "1":
        jarvis.takeCommand()

    elif ans == "3":
        jarvis.speak("Exiting.")
        print("Exiting...")
        sys.exit(0)


    elif ans == "2":
        while True:
            jarvis.speak("Please select any of the commands manually")
            an = input("\nPlease select any of the commands manually\n1. Take A Quiz\n2. Get Weather Update\n3. Get Random Facts\n4. Get Time\n5. Search Anything\n6. Hear A Joke\n7. Send Email\n8. Get Nearby Places\n9. Get Book Recommendations\n10. Translate Text\n11.Exit To Main Menu")
            if an == "1":
                jarvis.takeQuiz()
            if an == "2":
                jarvis.getWeather()
            if an == "3":
                jarvis.getFacts()
            if an == "4":
                jarvis.time()
            if an == "5":
                jarvis.wiki()
            if an == "6":
                jarvis.hearJoke()
            if an =="7":
                jarvis.sendEmail()
            if an =="8":
                jarvis.getNearbyPlaces()
            if an == "9":
                jarvis.search_books_by_genre()
            if an == "10":
                jarvis.translateText()
            if an == "11":
                mainMenu()

    else:
        print("Invalid Option. Try Again!")
        jarvis.speak("Invalid Option. Try Again")
        mainMenu()

mainMenu()