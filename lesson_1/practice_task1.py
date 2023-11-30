class BasePokemon:
    def __init__(self, name, poketype):
        self.name = name
        self.poketype = poketype

    def __str__(self):
        return f"{self.name}/{self.poketype}"


class EmojiMixin:
    def __str__(self):
        types = {"grass": "🌿", "fire": "🔥", "water": "🌊", "electric": "⚡"}
        return f"{self.name}/{types[self.poketype]}"


class Pokemon(EmojiMixin, BasePokemon):
    pass


if __name__ == "__main__":
    bulbasaur = BasePokemon(name="Bulbasaur", poketype="grass")
    pikachy = Pokemon(name="Pikachu", poketype="electric")

    print(bulbasaur)
    print(pikachy)
