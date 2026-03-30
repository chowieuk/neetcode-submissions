class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for i, op in enumerate(operations):
            match op:
                case "+":
                    result = record[-1] + record[-2]
                    record.append(result)
                case "D":
                    result = record[-1] * 2
                    record.append(result)
                case "C":
                    record.pop()
                case _:
                    record.append(int(op))

        return sum(record)