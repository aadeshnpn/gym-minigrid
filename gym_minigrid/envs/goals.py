# from gym_minigrid.minigrid import Ball
from gym_minigrid.roomgrid import RoomGrid
from gym_minigrid.register import register
from gym_minigrid.minigrid import Lava, Goal


class Goals(RoomGrid):
    """
    Unlock a door
    """

    def __init__(self, seed=None):
        room_size = 8
        super().__init__(
            num_rows=1,
            num_cols=2,
            room_size=room_size,
            max_steps=8*room_size**2,
            seed=seed
        )

    def _gen_grid(self, width, height):
        super()._gen_grid(width, height)

        # Make sure the two rooms are directly connected by a locked door
        door, _ = self.add_door(0, 0, 0, locked=True, color='green')
        # Add a key to unlock the door
        self.add_object(0, 0, 'key', door.color)
        # self.add_object(1, 0, 'key', door.color)

        self.place_agent(0, 0)

        self.door = door

        # Add balls
        self.add_object(0, 0, 'ball', door.color)
        self.add_object(1, 0, 'ball', door.color)
        # self.add_object(0, 0, 'ball', 'red')
        # self.add_object(1, 0, 'ball', 'blue')
        # self.mission = "open the door"

        # Add boxes
        self.add_object(0, 0, 'box', door.color)
        self.add_object(1, 0, 'box', door.color)
        # self.add_object(0, 0, 'box', 'red')
        # self.add_object(1, 0, 'box', 'blue')

        # Add lava
        self.grid.vert_wall(4, 3, height - 6, Lava)
        self.grid.horz_wall(9, 2, height - 6, Lava)
        # self.grid.horz_wall(4, width - 3, 3, Lava)

        # Place a goal in the bottom-right corner
        self.put_obj(Goal(), width - 2, height - 2)

    def step(self, action):
        obs, reward, done, info = super().step(action)

        if action == self.actions.toggle:
            if self.door.is_open:
                reward = self._reward()
                done = True

        return obs, reward, done, info


register(
    id='MiniGrid-Goals-v0',
    entry_point='gym_minigrid.envs:Goals'
)
