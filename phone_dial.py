class Solution(object):
    # def __init__(self):

    def changearray(self, array, digit):
        digit = int(digit)
        alpha = defaultdict(list)
        alpha[2] = ['a', 'b', 'c']
        alpha[3] = ['d', 'e', 'f']
        alpha[4] = ['g', 'h', 'i']
        alpha[5] = ['j', 'k', 'l']
        alpha[6] = ['m', 'n', 'o']
        alpha[7] = ['p', 'q', 'r', 's']
        alpha[8] = ['t', 'u', 'v']
        alpha[9] = ['w', 'x', 'y', 'z']

        if len(array) == 0:
            return alpha[digit]

        new_array = []
        for word in array:
            for letter in alpha[digit]:
                new_array.append(word + letter)

        return new_array

    def letterCombinations(self, digits):
        l = len(digits)
        if l == 0:
            return ""

        array = []
        for i in digits:
            array = self.changearray(array, i)

        return array
        """
        :type digits: str
        :rtype: List[str]
        """
