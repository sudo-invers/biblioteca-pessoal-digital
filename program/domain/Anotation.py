from datetime import date


class Anotation:
    """
    Represents a anotaion made in a publication
    """

    def __init__(self, text: str, page: int | None = None, createdAt: date | None = None):
        self._text = text
        self._page = page
        self._createdAt = createdAt if createdAt else date.now() #if the user created a Date, use they date, else, date.now()

    @property
    def text(self):
        return self._text

    @property
    def page(self):
        return self._page

    @property
    def createdAt(self):
        return self._createdAt

    def __str__(self):
        """ if the page have a anotation, return it, else, return just the creation date
            (the user is don't have to make a Passage)
        """
        if self._page:
            return f"[Page: {self._page}] \nPassage{self._text} \nDate({self._createdAt:%d/%m/%Y %H:%M})"
        return f"{self._text} ({self._createdAt:%d/%m/%Y %H:%M})"