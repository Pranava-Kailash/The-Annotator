class Checkpoint:
    def __init__(self, index):
        self.index = index
    
    def checkpoint_save(index):
        with open("checkpoint.txt", "w") as f:
            f.write(str(index))

    def checkpoint_load():
        try:
            with open("checkpoint.txt", "r") as f:
                return int(f.read())
        except FileNotFoundError:
            return 0