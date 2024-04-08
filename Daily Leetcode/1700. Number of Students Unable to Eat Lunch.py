class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        stu = deque(students)
        sand = deque(sandwiches)

        target = 0

        while stu:
            if stu[0] == sand[0]:
                stu.popleft()
                sand.popleft()
                target = 0
            else:
                stu.append(stu.popleft())
                target += 1

                if target == len(stu):
                    break

        return len(stu)
