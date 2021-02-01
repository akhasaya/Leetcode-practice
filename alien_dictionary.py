from collections import defaultdict

class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        if len(words) == 1:
            return words[0]
        letters = set()
        depends_on = defaultdict(list)
        dependees = defaultdict(list)
        for index in range(len(words) - 1):
            f = words[index]
            s = words[index + 1]
            fl = len(f)
            fl = min(fl, len(s))

            i = 0
            while i < fl and f[i] == s[i]:
                letters.add(f[i])
                letters.add(s[i])
                i += 1

            if i < fl:
                letters.add(f[i])
                letters.add(s[i])
                depends_on[s[i]].append(f[i])
                dependees[f[i]].append(s[i])
            elif len(f) > i:
                return ""

            j = i
            while i < len(f):
                letters.add(f[i])
                i += 1

            while j < len(s):
                letters.add(s[j])
                j += 1

        answer = []
        letters = list(letters)
        while len(letters) > 0:
            added = 0
            for l in letters:
                satisfied = True
                for j in depends_on[l]:
                    if j not in answer:
                        satisfied = False
                        break
                if satisfied == True:
                    answer.append(l)
                    letters.remove(l)
                    added += 1

            if added == 0:
                return ""

        answer = "".join(answer)
        return answer