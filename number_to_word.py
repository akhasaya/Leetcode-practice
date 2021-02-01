class Solution(object):
    def words(self, num):
        if num == 0:
            return ""
        storage = {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine"
        }

        tens = {
            2: "Twenty",
            3: "Thirty",
            4: "Forty",
            5: "Fifty",
            6: "Sixty",
            7: "Seventy",
            8: "Eighty",
            9: "Ninety"
        }

        teens = {
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen"
        }
        w = ""
        if num > 99:
            first = num // 100
            w += storage[first] + " Hundred"

        num = num % 100

        if num > 9:
            first = num // 10
            if 1 < first <= 9:
                if len(w) > 0:
                    w += " "
                w += tens[first]

                num = num % 10
                if num > 0:
                    w += " " + storage[num]
            elif first == 1:
                if len(w) > 0:
                    w += " "
                w += teens[num]

        elif num > 0:
            if len(w) > 0:
                w += " "
            w += storage[num]
        return w

    def numberToWords(self, num):
        if num == 0:
            return "Zero"
        three_digits = []

        while num > 0:
            three_digits.append(num % 1000)
            num = num / 1000

        print(three_digits)
        for i in range(len(three_digits)):
            three_digits[i] = self.words(three_digits[i])

        print(three_digits)
        places = ["", "Thousand", "Million", "Billion"]

        for i in range(1, len(three_digits)):
            if len(three_digits[i]) > 0:
                three_digits[i] += " " + places[i] + " "

        answer = ""
        for i in range(len(three_digits) - 1, -1, -1):
            answer += three_digits[i]

        if answer[-1] == " ":
            answer = answer[:len(answer) - 1]
        return answer

        """
        :type num: int
        :rtype: str
        """
mysol = Solution()
print(mysol.numberToWords(1234675890))