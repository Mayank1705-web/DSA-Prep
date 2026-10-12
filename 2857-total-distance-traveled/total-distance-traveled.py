class Solution:
    def distanceTraveled(self, a: int, b: int) -> int:
        return (a + min((a - 1) // 4, b)) * 10