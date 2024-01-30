from RacingTurtle import RacingTurtle


class Race:
    def __init__(self, racingColors, startingX, startingY, distanceBetween, finishingLine):
        self.turtles = []
        self.finishingLine = finishingLine
        for color in racingColors:
            turtle_y_starting = startingY + (len(self.turtles) * distanceBetween)
            racingTurtle = RacingTurtle(color, (startingX, turtle_y_starting))
            self.turtles.append(racingTurtle)

    def startRace(self):
        race_on = True

        winner = ""
        while race_on:
            for turtle in self.turtles:
                if turtle.xcor() >= self.finishingLine - 20:
                    race_on = False
                    winner = turtle.pencolor()
                turtle.forward_random_amount(0, 10)

        return winner