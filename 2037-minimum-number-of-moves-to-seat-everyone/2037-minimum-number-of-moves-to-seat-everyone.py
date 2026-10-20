class Solution:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        seats.sort()
        students.sort()
        counter=0
        for i in range(len(seats)):
            counter+=(abs(seats[i]-students[i]))
        return counter

        