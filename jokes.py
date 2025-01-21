import random
name=input("What is your name? ")
jokes=["Are you this charming with all your friends, or do I just get special treatment?", # type: ignore
      "I was gonna get some work done, but I could not stop thinking about you. So I figured I could call and blame you instead."
      "Tell me something—how am I supposed to behave when I keep remembering how good it feels to have you close?",
      "Is your name Google? Because you have everything I am searching for... especially in the naughty department",
      "Do you like raisins? How do you feel about a date? I promise it will be a little naughty and a lot of fun."]
selected_joke=random.choice(jokes) # type: ignore
print(f"{name},Here is a pick up joke for your friendzone whom you love\n {selected_joke}")