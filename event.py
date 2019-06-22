class Event():
    def __init__(self, correspondingEvents: dict(), objects: list(), characters: list(), name:str(), description:str(), event_id:int(), map_next:list(), map_prev:list() ):
        self.correspondingEvents = correspondingEvents
        self.objects = objects
        self.characters = characters
        self.name= name
        self.description= description
        self.event_id = event_id
        self.map_next = map_next
        self.map_prev = map_prev

            
  