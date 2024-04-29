from mrjob.job import MRJob
from mrjob.protocol import RawValueProtocol
import json

class MergeTopTerms(MRJob):

    OUTPUT_PROTOCOL = RawValueProtocol

    #def mapper(self, _, line):
    #    # Split the line into category and JSON object
    #    _, terms_json = line.split('\t', 1) 
    #    # Parse the JSON object
    #    terms_dict = json.loads(terms_json)
    #    # Initialize a list to store all terms
    #    all_terms = []
    #    # Iterate through each category-term pair
    #    for term_list in terms_dict.values():
    #        # Iterate through the terms in the current category
    #        for term, _ in term_list:
    #            # Append the term to the list
    #            all_terms.append(term)
    #    # Emit each term
    #    for term in all_terms:
    #        yield term, None

    #def reducer(self, term, _):
    #    # Emit each term
    #    yield None, term

    #def reducer_final(self):
    #    # Sort and join all terms alphabetically
    #    all_terms_sorted = sorted(set(self.values()))
    #    merged_terms = ' '.join(all_terms_sorted)
    #    # Emit the merged terms
    #    yield None, merged_terms

    def mapper(self, _, line):
        # Split the line into category and JSON object
        _, terms_json = line.split('\t', 1) 
        # Parse the JSON object
        terms_dict = json.loads(terms_json)
        # Initialize a dictionary to store the counts of terms
        term_counts = {}
        # Iterate through each category-term pair
        for term_list in terms_dict.values():
            # Iterate through the terms in the current category
            for term, _ in term_list:
                # Increment the count of the term
                term_counts[term] = term_counts.get(term, 0) + 1
        # Emit each term and its count
        for term, count in term_counts.items():
            yield term, count

    def reducer(self, term, counts):
        result_string = "".join(term)
        # Sum the counts for each term
        total_count = sum(count for count in counts)
        # Emit the term and its total count
            
        yield None, result_string

if __name__ == '__main__':
    MergeTopTerms.run()

