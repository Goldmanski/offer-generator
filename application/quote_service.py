from domain.quote import Quote


class QuoteService:
    def create_quote(self) -> Quote:
        return Quote(id=1)