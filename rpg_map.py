# Global error for requesting non-existent maps
RPG_ERROR = {'narration': 'Map name does not match save file',
             'inspection': 'Map name does not match save file',
             'encounter': 0}


class RPGMap:
    """A map object that allows for the construction of a map to be referenced by clients, using the rpg service key,
    to request map tile information."""
    def __init__(self, name):
        """Initialize the map object. with a name, tile information (including default tile for out of bounds requests)
        , and a layout."""
        self.name = name
        self.tiles = {'out_of_bounds': {
            'narration': 'You only see vast sea where you are trying to go.',
            'biome': 'None',
            'inspection': 'You smell salt.'}}
        self.layout = []

    def add_tile(self, name, tile):
        """Add a tile to the dictionary of tile information. Returns early if tile not valid format.

        Args: name (string): The key to be referenced for the tile info.
            tile (dict): The tile information object.
        """
        for key in tile:
            if key not in ('narration', 'inspection', 'encounter', 'biome'):
                print('Invalid tile information')
                return
        self.tiles[name] = tile

    def add_layout(self, layer):
        """Add a layer to the map layout, ensuring that all tiles in the layer correlate to a tile in self.tiles.

        Args: layer (list): A list of tile keys that will form a layer of the map.
        """
        if any(name not in self.tiles for name in layer):
            print('Map layer contains invalid tile(s)')
            return
        self.layout.append(layer)

    def get_tile(self, x, y):
        """Return the tile information of a given coordinate.

        Args: x (int): The x coordinate of the requested position.
            y (int): The y coordinate of the requested position.

        Returns (dict): The tile information of the requested position.
        """
        if 0 <= y < len(self.layout) and 0 <= x < len(self.layout[y]):
            tile_name = self.layout[x][y]
            return {'status': 'success', 'data': self.tiles[tile_name]}
        else:
            return {'status': 'out_of_bounds', 'data': self.tiles['out_of_bounds']}


# Construction of test map
test_map = RPGMap('test_map')
test_map.add_tile('fields', {
    'narration': "You stand in a vast field. The ground beneath you is as green as emerald.",
    'inspection': "You only notice the beauty of your surroundings.",
    'biome': 'fields',
    'encounter': 15})
test_map.add_tile('desert', {
    'narration': "You find yourself in a dry desert. It would take a hearty person to survive these lands.",
    'inspection': "You kick the sand around to find only more sand.",
    'biome': 'desert',
    'encounter': 10})
test_map.add_tile('scorched', {
    'narration': "The land that surrounds you is scorched. No life could ever live here.",
    'inspection': "you feel as though you are being watched.",
    'biome': 'scorched',
    'encounter': 5})
test_map_layout = [
    ['scorched', 'scorched', 'scorched', 'scorched', 'scorched', 'scorched', 'scorched', 'scorched'],
    ['scorched', 'desert', 'fields', 'fields', 'fields', 'fields', 'desert', 'scorched'],
    ['scorched', 'desert', 'fields', 'fields', 'fields', 'fields', 'desert', 'scorched'],
    ['scorched', 'desert', 'fields', 'fields', 'fields', 'fields', 'desert', 'scorched'],
    ['scorched', 'desert', 'fields', 'fields', 'fields', 'fields', 'desert', 'scorched'],
    ['scorched', 'desert', 'fields', 'fields', 'fields', 'fields', 'desert', 'scorched'],
    ['scorched', 'desert', 'fields', 'fields', 'fields', 'fields', 'desert', 'scorched'],
    ['scorched', 'desert', 'fields', 'fields', 'fields', 'fields', 'desert', 'scorched'],
    ['scorched', 'desert', 'fields', 'fields', 'fields', 'fields', 'desert', 'scorched'],
    ['scorched', 'scorched', 'scorched', 'scorched', 'scorched', 'scorched', 'scorched', 'scorched']]
for line in test_map_layout:
    test_map.add_layout(line)

# Dict to be referenced by server in case multiple maps are added
rpg_maps = {'test_map': test_map}
