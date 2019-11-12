import heapq


class Comparator(object):
    def __init__(self, val):
        self.val = val

    def __lt__(self, other):
        if self.val[0] == other.val[0]:
            return self.val[1] > other.val[1]
        else:
            return self.val[0] < other.val[0]

    def __repr__(self):
       return str(self.val)


class Solution:

    def topNCompetitor(self, numCompetitors, topNcompetitors, competitors, numReviews, reviews):

        if not numCompetitors or not competitors:
            return []
        if not numReviews or not reviews:
            return []

        assert numCompetitors == len(competitors), "numCompetitors is wrong"
        assert numReviews == len(reviews), "numReviews is wrong"

        hashmap = {c.lower(): 0 for c in competitors}

        for review in reviews:
            for word in review.split(' '):
                word_lower = word.lower()
                if word_lower in hashmap:
                    hashmap[word_lower] += 1

        print(hashmap)

        heap = []
        count = 0
        for word, fre in hashmap.items():
            heapq.heappush(heap, Comparator((fre, word)))
            count += 1
            if count > topNcompetitors:
                heapq.heappop(heap)

        return list(map(lambda x: x.val[1], heapq.nlargest(topNcompetitors, heap)))
        #[heapq.heappop(heap).val[1] for _ in range(0, topNcompetitors)][::-1]


###########################################
a = Solution()
numCompetitors = 7
topNcompetitors = 2
competitors = ['newshop', 'shopnow', 'afshion', 'bfshion', 'fashionbeats', 'mymarket', 'tcellular']
numReviews = 6
reviews = ["nEwshop is afshion providing good services in the city; everyone should use newshop", 
"best services by newshop", "fashionbeats has great services in the city",
"i am proud to have fashionbeats", "mymarket has awesome services", "Thanks Newshop for the quick delivery afshion"]

print(a.topNCompetitor(numCompetitors, topNcompetitors, competitors, numReviews, reviews))