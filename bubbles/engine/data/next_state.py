class NextState:
    def __init__(self, running=True, add_circles_count=0, mode_changed=False, mode_index=0):
        self.running = running
        self.add_circles = add_circles_count
        self.mode_changed = mode_changed
        self.mode_index = mode_index
