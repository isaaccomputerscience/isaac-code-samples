
difficulty = "Hard"
score = 55
game_over = False

if not game_over:
    if difficulty == "Hard" and score > 60:
        print("Wow, you are doing great!")
    elif (difficulty == "Normal" or difficulty == "Easy") and score > 40:
        print("Good stuff, keep it up!")
    else:
        print("Keep going!")
        
