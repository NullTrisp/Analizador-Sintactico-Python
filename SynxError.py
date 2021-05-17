class SynxError(Exception):
    def __init__(self, err, message="Synx Error: "):
        self.message = message + err
        super().__init__(self.message)
