import random
name = input("Whats your name? ")
roasts = ['Yeah of course humans make mistakes {}. Thats how you were born.',
          'Oh {}, You are the sun in my life… now get 93 million miles away from me.',
          "If anyone ever wants to kill themselves, just jump from {}'s ego to his IQ",
          'I wasnt insulting you {}, I was just describing you',
          'The last time I saw {}, he was behind metal bars with some chimpanzees around him',
          'Hi {}, we accidentally sent you your IQ results not your covid test. But neverthless, glad it was negative',
          'The only thing I laugh at is you {}',
          'You can’t imagine how much happiness you can bring {}… by leaving the room.',
          '{} may be weird, but atleast he isnt smart enough to know that',
          "I am sure people like you {}, and also that they dont know you"]

roast = random.choice(roasts)
print(roast)
print(roast.format(name))
