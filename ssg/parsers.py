from typing import List
from pathlib import Path
import shutil

class Parser:
    extensions = [] # type: List[str]

    def valid_extension(self, extension):
        return self.extensions.__contains__(extension)
    
    def parse(path, source, dest):
        raise NotImplementedError
    
    def read(path):
        with path.open('r') as file:
            return file.read()
        
    def write(self, path, dest, content, ext = ".html"):
        full_path = self.dest / path.with_suffix(ext).name
        with full_path.open('w') as file:
            file.write(content)

    def copy(path, source, dest):
        shutil.copy2(path, dest / path.relative_to(source))

    class ResourceParser(Parser):
        extensions = [ ".jpg", ".png", ".gif", ".css", ".html" ]

        def parse(path, source, dest):
            super().copy(path, source, dest)
