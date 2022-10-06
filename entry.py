class entry:
    def __init__(self, name, tags, catID, fileID):
        self.__name = name
        self.__tags = tags #Should be List
        self.__catID = catID
        self.__fileID = fileID

    def get_tags(self):
        return self.__tags

    def add_tag(self, tag):
        self.__tags.add(tag)
        return

    def get_name(self):
        return self.__name

    def get_catID(self):
        return self.__catID

    def get_fileID(self):
        return self.__fileID
        

if __name__ == '__main__':
    print("I shouldnt be a main executable")

