class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr2_set = set(arr2)
        count = defaultdict(int)
        end = []
        res = []

        for n in arr1:
            if n not in arr2_set:
                end.append(n)
            else:
                count[n] += 1
        end.sort()

        for n in arr2:
            for _ in range(count[n]):
                res.append(n)
        
        return res + end