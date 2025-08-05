class Config:
    def __init__(self):
        self.version = None
        self.snippetStacking = None
        self.viewportSize = None
    
    def set_version(self, version: str):
        self.version = version
        return self
    
    def set_snippet_stacking(self, snippetStacking: str):
        self.snippetStacking = snippetStacking
        return self
    
    def set_viewport_size(self, viewportSize: int):
        self.viewportSize = viewportSize
        return self 