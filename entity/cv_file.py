from posixpath import basename


class CVFile:
    def __init__(self, id: str, name: str, path: str):
        self.id = id
        self.name = name
        self.path = path
        
    def __init__(self, id: str, path: str):
        self.id = id
        self.name = basename(path)
        self.path = path