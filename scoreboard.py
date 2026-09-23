from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = self.get_highscore()
        self.color("white")
        self.penup()
        self.goto(0,250)
        self.hideturtle()
        self.update_scoreboard()
   
    def get_highscore(self):
        try:
            with open("highscore.txt", "r") as file:
                return int(file.read().strip() or 0)
        except (FileNotFoundError, ValueError):
            return 0
            

    
    def save_highscore(self):
       with open("highscore.txt","w") as file:
           file.write(str(self.highscore))
    
    def update_scoreboard(self):
        self.write(f"score : {self.score}  Highscore : {self.highscore}",align="center",font=("arial",24,"normal"))
    
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
    
    def game_over(self):
        self.screen.bgcolor("red")
        self.goto(0,0)
        if self.score > self.highscore:
            self.highscore = self.score
            self.save_highscore()
        self.write(f" ------------ Game over! ------------\n\n Score--> {self.score}\n\n highscore--> {self.highscore}",align="center",font=("arial",24,"normal"))

