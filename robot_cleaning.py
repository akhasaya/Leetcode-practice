# https://leetcode.com/problems/robot-room-cleaner/

# my solution is the first one - TLE

# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
# class Robot(object):
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution(object):
    def count(self, seen):
        c = 0
        if [0, 1] in seen:
            c += 1
        if [0, -1] in seen:
            c += 1
        if [1, 0] in seen:
            c += 1
        if [-1, 0] in seen:
            c += 1

        return c

    def cleanRoom(self, robot):
        moves = []
        robot.clean()
        direction = 0
        seen = []
        seen.append([0, 0])
        current = [0, 0]
        while direction < 4:
            if [current[0] - 1, current[1]] not in seen:
                seen.append([current[0] - 1, current[1]])
                if robot.move():
                    current = [current[0] - 1, current[1]]
                    moves.append("U")
                    robot.clean()
                    continue

            if [current[0], current[1] - 1] not in seen:
                robot.turnLeft()
                seen.append([current[0], current[1] - 1])
                if robot.move():
                    current = [current[0], current[1] - 1]
                    moves.append("L")
                    robot.clean()
                    continue
                robot.turnRight()

            if [current[0] + 1, current[1]] not in seen:
                robot.turnLeft()
                robot.turnLeft()
                seen.append([current[0] + 1, current[1]])
                if robot.move():
                    current = [current[0] + 1, current[1]]
                    moves.append("D")
                    robot.clean()
                    continue
                robot.turnLeft()
                robot.turnLeft()

            if [current[0], current[1] + 1] not in seen:
                robot.turnRight()
                seen.append([current[0], current[1] + 1])
                if robot.move():
                    current = [current[0], current[1] + 1]
                    moves.append("R")
                    robot.clean()
                    continue
                robot.turnLeft()

            # if all 4 directions are cleaned, backtrack

            last_move = moves.pop()
            if last_move == "R":
                current = [current[0], current[1] - 1]
            elif last_move == "L":
                current = [current[0], current[1] + 1]
            elif last_move == "U":
                current = [current[0] + 1, current[1]]
            elif last_move == "D":
                current = [current[0] - 1, current[1]]

            direction = self.count(seen)

        """
        :type robot: Robot
        :rtype: None
        """


# solution provided in leetcode

class Solution(object):
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """

        def go_back():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()

        def backtrack(cell=(0, 0), d=0):
            visited.add(cell)
            robot.clean()
            # going clockwise : 0: 'up', 1: 'right', 2: 'down', 3: 'left'
            for i in range(4):
                new_d = (d + i) % 4
                new_cell = (cell[0] + directions[new_d][0], \
                            cell[1] + directions[new_d][1])

                if not new_cell in visited and robot.move():
                    backtrack(new_cell, new_d)
                    go_back()
                # turn the robot following chosen direction : clockwise
                robot.turnRight()

        # going clockwise : 0: 'up', 1: 'right', 2: 'down', 3: 'left'
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visited = set()
        backtrack()