#Lab 2 - Original reflex classroom agent from the lab manual.



class ClassroomAgent:
    def act(self, temp, occupied):
        if not occupied:
            return "ECO"
        if temp > 26:
            return "COOL"
        if temp < 20:
            return "WARM"
        return "IDLE"


if __name__ == "__main__":
    agent = ClassroomAgent()
    percepts = [(29, True), (24, True), (29, False)]

    print("Reflex agent: percept -> target mode")
    for percept in percepts:
        print(percept, "->", agent.act(*percept))
