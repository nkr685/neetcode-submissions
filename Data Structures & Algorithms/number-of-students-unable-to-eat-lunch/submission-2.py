class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        while len(students):
            if students[0] == sandwiches[0]:
                st = students.pop(0)
                sandwiches.pop(0)
            elif sandwiches[0] not in students:
                break
            else:
                st = students.pop(0)
                students.append(st)
        return len(students)