from room import Room
from player import Player
from world import World
from collections import deque

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
# create a dictionary with room id's as the keys and the values
# are a dictionary of directions and the room connected in that direction
rooms = {player.current_room.id: {direction: '?' for direction in player.current_room.get_exits()}}
# first do a depth first traversal to go as far as possible down one path
def dft():
    curr = player.current_room
    while '?' in rooms[curr.id].values():       
        if 'w' in rooms[curr.id] and rooms[curr.id]['w'] == '?':
            # set the next room to that room's id in the dict
            rooms[curr.id]['w'] = curr.get_room_in_direction('w').id
            # go into that room
            player.travel('w')
            # replace curr
            curr = player.current_room
            # create that room in the dict
            if curr.id not in rooms:
                rooms[curr.id] = {direction: '?' for direction in curr.get_exits()}
            # set the previous room's id as the oppsite direction
            rooms[curr.id]['e'] = curr.get_room_in_direction('e').id
            # add to the traversal_path
            traversal_path.append('w')
        elif 's' in rooms[curr.id] and rooms[curr.id]['s'] == '?':
            rooms[curr.id]['s'] = curr.get_room_in_direction('s').id
            player.travel('s')
            curr = player.current_room
            if curr.id not in rooms:
                rooms[curr.id] = {direction: '?' for direction in curr.get_exits()}
            rooms[curr.id]['n'] = curr.get_room_in_direction('n').id
            traversal_path.append('s')    
        elif 'n' in rooms[curr.id] and rooms[curr.id]['n'] == '?':           
            rooms[curr.id]['n'] = curr.get_room_in_direction('n').id            
            player.travel('n')           
            curr = player.current_room           
            if curr.id not in rooms:
                rooms[curr.id] = {direction: '?' for direction in curr.get_exits()}           
            rooms[curr.id]['s'] = curr.get_room_in_direction('s').id           
            traversal_path.append('n') 
        elif 'e' in rooms[curr.id] and rooms[curr.id]['e'] == '?':
                    rooms[curr.id]['e'] = curr.get_room_in_direction('e').id
                    player.travel('e')
                    curr = player.current_room
                    if curr.id not in rooms:
                        rooms[curr.id] = {direction: '?' for direction in curr.get_exits()}
                    rooms[curr.id]['w'] = curr.get_room_in_direction('w').id
                    traversal_path.append('e')
        
        
        

def bfs():
    '''
    Search room starting from our current room looking for unexplored rooms
    Keeps track of the path to each room
    returns the path to the closest room with an unexplored connecting room
    If all rooms have been explored, return None
    '''
    curr_path = (player.current_room, [])
    # keep track of rooms that have been visited
    visited = {curr_path[0].id}
    q = deque()
    q.append(curr_path)
    while len(q)>0:
        curr_path = q.popleft()
        # return the path to that room if there is an unexplored connection
        if '?' in rooms[curr_path[0].id].values():
            return curr_path[1]
        # traverses in each direction keeping track of the path to that room
        for direction in curr_path[0].get_exits():
            next_room = curr_path[0].get_room_in_direction(direction)
            if next_room.id not in visited:
                visited.add(next_room.id)
                q.append((next_room, curr_path[1] + [direction]))
        
    return None

def room_traversal():
    '''
    Traverses each room in a connected map of rooms
    '''
    # dft to go as far as we can
    dft()
    # back track to find unexplored paths
    return_to_closest_unexplored_room = bfs()
    # contiune this process until there are no unexplored paths
    while return_to_closest_unexplored_room:
        for direction in return_to_closest_unexplored_room:
            traversal_path.append(direction)
            player.travel(direction)
        dft()
        return_to_closest_unexplored_room = bfs()
room_traversal()
        

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")





#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
