class Course:
    name: str
    number: int
    prerequistes: list[str]

    def is_valid(self, prereq: str) -> bool:
        if self.number >= 400:
            if prereq in self.prerequistes:
                return True
        return False


