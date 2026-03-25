class Fibonacci:
    def __init__(self):
        self.sequence = [0, 1]

    def get_nth_term(self, n):
        for _ in range(len(self.sequence), n + 1):
            next_number = self.sequence[-1] + self.sequence[-2]
            self.sequence.append(next_number)
        return self.sequence[n]

    def get_divisible_less_than_nth(self, n, m):
        self.get_nth_term(n)
        results = []
        for number in self.sequence[:n]:
            if number % m == 0 and number not in results:
                results.append(number)
        return results


fibbie = Fibonacci()


print(f'term 100 in Fibbie: {fibbie.get_nth_term(100)}')
print(fibbie.get_divisible_less_than_nth(100, 7))