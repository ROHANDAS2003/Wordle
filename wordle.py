class Wordle:

    MAX_ATTEMPTS = 6

    def __init__(self, secret: str):
        self.secret: str = secret
        self.attempts  = []
        pass

    def attempt(self, word: str):
        self.attempts.append(word)
        
    @property
    def is_solved(self):
        return len(self.attempts) > 0 and self.attempts[-1] == self.secret

    @property
    def remining_attempts(self) -> int:
        return self.MAX_ATTEMPTS - len(self.attempts)

    @property
    def can_attempt(self):
        return self.remining_attempts > 0 and not self.is_solved