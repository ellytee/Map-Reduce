from mrjob.job import MRJob
from collections import defaultdict

class ChiSquareMR(MRJob):

    def mapper(self, _, line):
        category, term = line.strip().split('\t')
        yield (category, term), 1

    def reducer_init(self):
        self.category_counts = defaultdict(int)
        self.term_counts = defaultdict(lambda: defaultdict(int))

    def reducer(self, key, values):
        category, term = key
        count = sum(values)
        self.category_counts[category] += count
        self.term_counts[category][term] += count

    def reducer_final(self):
        total_count = sum(self.category_counts.values())
        chi_square_values = defaultdict(lambda: defaultdict(float))
        for category, term_counts in self.term_counts.items():
            category_count = self.category_counts[category]
            for term, term_count in term_counts.items():
                a = term_count  # Observed count
                b = category_count - a  # Observed count of other terms in category
                c = total_count - category_count  # Observed count of term in other categories
                d = total_count - a - b - c  # Observed count of other terms in other categories
                
                # Error handling to avoid division by zero
                denominator = (a + c) * (b + d) * (a + b) * (c + d)
                if denominator == 0:
                    chi_square = 0
                else:
                    chi_square = (total_count * ((a * d - b * c) ** 2)) / denominator
                    
                chi_square_values[category][term] = chi_square

        top_terms = {}
        for category, term_chi_square in chi_square_values.items():
            sorted_terms = sorted(term_chi_square.items(), key=lambda x: x[1], reverse=True)[:75]
            top_terms[category] = [(term, chi_square) for term, chi_square in sorted_terms]

        yield None, top_terms

if __name__ == '__main__':
    ChiSquareMR.run()

