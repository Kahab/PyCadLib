class entry:
    def __init__(self, name, tags):
        self.__name = name
        self.__tags = tags #Should be List

    def get_tags(self):
        return self.__tags

    def add_tag(self, tag):
        self.__tags.add(tag)
        return
        

