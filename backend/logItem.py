class LogItem:
    def __init__(self, file_name, path):
        self.name = file_name
        self.lines = []
        self._parse_file(path)

    def _parse_file(self,path):
        path = path.replace('file://', '')
        with open(path, "r") as f:
            self.lines = f.readlines()
