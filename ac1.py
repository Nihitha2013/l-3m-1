import re,random
from colorama import Fore,init

init(autoreset=True)

destination={
  "beaches":["Bali","Maldives","Phuket"],
  "mountains":["Switzerland","Japan","New Zealand"],
  "cities":["New York","Paris","London"]         
}

jokes=[
  "Why don't scientists trust atoms? Because they make up everything!",
  "What do you call fake spaghetti? An impasta.",
  "Why did the scarecrow win an award? Because he was outstanding in his field!"
]

def normalize_input(text):
  return re.sub(r"/s+", " ", text.strip().lower())

def recommend():
  print("TravelBot:Beaches mountains,or cities?")
  preference= input("You:")
  preference=normalize_input(preference)

  if preference in destination:
    suggestion=random.choice(destination[preference])
    print(f"TravelBot:HOw about {suggestion}?")
    print("TravelBot:Do you like it?{yes/no}")
    answer=input("You:").lower()
    
    if answer=="yes":
      print("TravelBot:I'm glad you like it!")
    elif answer =="no":
      print("TravelBot:Let's try another.")
    else:
      print("TravelBot:I'll suggest again.")

  else:
    print("TravelBot:I'm sorry, I don't have that type of destination.")
  show_help()

def packing_tips():
  print("TravelBot:Where to?:")
  location= normalize_input(input("You:"))
  print("TravelBot:For how many days?:")
  days= input("You:")
  print(f"TravelBot:Packing tips for {days} days in {location}:")

def tell_joke():
  print(f"TravelBot: {random.choice(jokes)}")

def show_help():
  print("\nI can:")
  print("-Suggest travel sports(say'recommendation')")
  print("-Offer packing tips(say 'packing')")
  print("-Tell a joke(say 'joke')")
  print("-Type'exit' to end")
def chat():
  print("Hello! I'm TravelBot.")
  name=input("What's your name?")
  print(f"Nice to meet you,{name}!")
  show_help()
  while True:
    user_input=input(f"\n{name}:")
    user_input=normalize_input(user_input)
    if "recommend" in user_input or"suggest" in user_input:
      recommend()
    elif "packing" in user_input or "tips" in user_input:
      packing_tips()
    elif "joke" in user_input:
      tell_joke()
    elif"help" in user_input:
      show_help()
    elif"exit" in user_input:
      print("TravelBot:Goodbye!")
      break
    else:
      print("TravelBot:Could you rephrase?")

if __name__=="__main__":
  chat()