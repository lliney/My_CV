class PositiveList (list):
    def append(self, x):
        if x > 0:
            super().append(x)

        else:
            raise NonPositiveError("NonPositiveError")
class NonPositiveError(Exception):
    pass
