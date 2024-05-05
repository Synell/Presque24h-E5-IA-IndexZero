class ClassDict:
    def __getitem__(self, key: str) -> str:
        new_s = ''
        for c in key:
            if c.isupper():
                new_s += '_' + c.lower()
            else:
                new_s += c

        return self.__dict__[new_s[1:]]


    def __setitem__(self, key: str, value: object) -> None:
        s = key.replace('_', ' ').title().replace(' ', '_')
        self.__dict__[s] = value
