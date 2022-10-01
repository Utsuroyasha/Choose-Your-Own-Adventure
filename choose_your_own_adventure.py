name = input('Type your name: ')
print('Welcome', name, "to this adventure!")

while True:
    answer = input("""\nAfter a long hard day at your boring office job you arrive at home. Before you walk into your house you see a letter in your mailbox, an unusual occurrence as bill day is Thursday not Monday.\nYou go up to the mailbox and see that there is a little red letter—quite suspicious.\nDo you want to open the mail or go inside?\nType open mail or type go inside: """).lower()

    if answer == 'open mail':
        answer = input("""\nYou are too curious not to answer your mail. So you grab it out of your mailbox and open it and find seven words\n‘Meet me on the docks at twelve’\nYou are not that sure whether to go or not because it seems like a stereotypical set up for a camp fire story.\nDrive up to the dock to find out who sent you the letter.\nType drive: """).lower()
        
        if answer == "drive":
            answer = input("""\nYou decide to go down to the docks to confront the person who wrote the red letter.\n11:59 pm and there is no one there. Where is he? You think to yourself, "Did he forget? Is it a prank?"\nThen you hear a car rumble in the distance. A pair of bright yellow headlights pop into existence and they are heading towards you and the noise is getting louder. Do you want to stand your ground or run away as fast as you can?\nType stand or type run: """).lower()
            
            if answer == "stand":
                    answer = input("""\nYou decide to stand your ground. The car is getting dangerously close to you. Five seconds feels like it has been an hour.\nThe car is getting nearer and you are regretting your decision. You can now see the red hood of the car coming towards you.\nJust as you get ready for the numbing pain of the car hitting you it screeches to a stop. A suited man comes out of the car and he is holding a hand gun. “Where is the money?” the man shouts at you. You run away.\nType run away: """).lower()
                    
            if answer == "run away" or answer == "run":                            
                print("""\nYou decide to run away. In the distance you hear a car. Its headlights are getting closer. You take a left turn into a dark alleyway and end up behind a small boat house. You see the car speed past you and you decide to flank it.\nYou run onto the main road and lose it. It only took you ten minutes to find the police station nearest to you.\nOnce you arrive you quickly tell your story. Thirty minutes later the police sergeant returns looking happy with himself. He tells you that you were the bait in a drug bust and now you are a key person in the crime of the year.\nTHE END\nYou completed the story!""")
            break
        

    elif answer == 'go inside':
        answer = input("""\nYou decide that it is too suspicious and you choose to go inside.\nHalf way up the driveway you slip and fall head first on a rock.\nNo one knows what happened to your body. Did the writer of the letter take it?\nGo back to the start to find out.\nType start: """).lower()
        
        if answer == "start": 
            continue
            
    else:
        print('Not a valid option, you lose.')
        restart= input("To play again, type restart: ").lower()
            
        if restart == "restart":
            continue
            
        else:
            exit()