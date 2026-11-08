"""Lab 2 - Stateful classroom agent that suppresses duplicate commands.

The policy keeps the lab manual's original thresholds and occupancy priority:
- Empty room: ECO
- Occupied and temperature > 26 C: COOL
- Occupied and temperature < 20 C: WARM
- Otherwise: IDLE


"""


class ClassroomAgent:
    def __init__(self):
        self.previous_mode = None

    def act(self, temp, occupied):
        """Return (target_mode, should_send_command) for the current percept."""
        if not isinstance(temp, (int, float)) or isinstance(temp, bool):
            raise TypeError("temp must be a number representing degrees Celsius")
        if not isinstance(occupied, bool):
            raise TypeError("occupied must be a Boolean")

        # Occupancy has priority over temperature, exactly as in the manual.
        if not occupied:
            target_mode = "ECO"
        elif temp > 26:
            target_mode = "COOL"
        elif temp < 20:
            target_mode = "WARM"
        else:
            target_mode = "IDLE"

        should_send_command = target_mode != self.previous_mode
        self.previous_mode = target_mode
        return target_mode, should_send_command


def run_required_trace():
    """Run repeated, boundary, transition, and empty-room cases."""
    percepts = [
        (29, True),   
        (29, True),   
        (20, True),   
        (26, True),   
        (19, True),   
        (29, False),  
        (29, False),  
        (24, True),   
        (24, True),   
    ]

    agent = ClassroomAgent()
    print("Step | Previous mode | Percept (temp, occupied) | Target | Command")
    print("-----|---------------|--------------------------|--------|--------")
    for step, percept in enumerate(percepts, start=1):
        previous_mode = agent.previous_mode
        target_mode, should_send = agent.act(*percept)
        command = "SEND" if should_send else "NO SEND"
        previous_label = previous_mode if previous_mode is not None else "NONE"
        print(
            f"{step:>4} | {previous_label:<13} | {str(percept):<24} | "
            f"{target_mode:<6} | {command}"
        )


def run_threshold_noise_trace():
    """Show why duplicate suppression alone is not temperature hysteresis."""
    percepts = [(25.9, True), (26.1, True), (25.9, True), (26.1, True)]
    agent = ClassroomAgent()
    print("Step | Previous mode | Percept (temp, occupied) | Target | Command")
    print("-----|---------------|--------------------------|--------|--------")
    for step, percept in enumerate(percepts, start=1):
        previous_mode = agent.previous_mode
        target_mode, should_send = agent.act(*percept)
        command = "SEND" if should_send else "NO SEND"
        previous_label = previous_mode if previous_mode is not None else "NONE"
        print(
            f"{step:>4} | {previous_label:<13} | {str(percept):<24} | "
            f"{target_mode:<6} | {command}"
        )


if __name__ == "__main__":
    print("REQUIRED LAB TASK TRACE")
    run_required_trace()
    print("\nTHRESHOLD-NOISE EDGE-CASE TRACE")
    run_threshold_noise_trace()
