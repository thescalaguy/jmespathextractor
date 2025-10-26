import jmespath


class Extractor:
    """Extract values from a dictionary using JMESPath expressions

    >>> instance = {"user": {"name": "John Doe"}}
    >>> ex = Extractor({"user_name": "user.name"})
    >>> result = ex.extract(instance)
    >>> assert result["user_name"] == "John Doe"
    """

    def __init__(self, mapping: dict[str, str]):
        self.mapping = {k: jmespath.compile(v) for k, v in mapping.items()}

    def extract(self, instance: dict):
        return {k: expr.search(instance) for k, expr in self.mapping.items()}


if __name__ == "__main__":
    import doctest
    doctest.testmod()
