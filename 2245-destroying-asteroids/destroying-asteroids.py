class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        # brute force
        asteroids.sort()
        for asteroid in asteroids:
            if (asteroid > mass): # check if bigger, return false if yes
                return False
            mass += asteroid
            # add mass
        return True
        