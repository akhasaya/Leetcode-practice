# hard problem solved it on my own - but took a lot of time - more than two hours


from collections import Counter
class Solution(object):
    def cornerReplace(self, str1, str2, ch3, ch2):
        for i in range(len(str1)):
            if str1[i] == ch3 and str2[i] != ch2:
                return False

            return True

    def checkConvert(self, str1, str2, i):
        print("replace {} with {}?".format(str1[i], str2[i]))
        ch1 = str1[i]
        ch2 = str2[i]
        needs_change = False
        for index in range(len(str1)):
            # if all occurances of str1[i] in str1 maps to same char
            if str1[index] == ch1 and str2[index] != ch2:
                print("not possible")
                return "0"
            # if str2[i] does not occur in str1, if it does, it does not change again..
            if str1[index] == ch2 and str2[index] != ch2:
                needs_change = True

        if needs_change == False:
            return ch2

        c = len(Counter(str1))
        d = len(Counter(str2))

        if c < 26:
            return "1"
        elif d < 26:
            # some other letter change to ch2 as well
            for i in range(len(str2)):
                if str2[i] == ch2 and str1[i] != ch1:
                    # if all str1[i] wants to change to ch2, possible
                    if self.cornerReplace(str1, str2, str1[i], ch2):
                        return ["3", str1[i]]

        return "2"

    def replace(self, str1, ch1, ch2):
        str2 = ""
        for i in range(len(str1)):
            if str1[i] == ch1:
                str2 += ch2
            else:
                str2 += str1[i]
        return str2

    def canConvert(self, str1, str2):
        l = len(str1)
        print("length = ", l)
        changes = True
        while changes == True:
            changes = False

            for i in range(l):
                if str1[i] != str2[i]:
                    result = self.checkConvert(str1, str2, i)
                    if result == "0":
                        return False
                    elif result == str2[i]:
                        str1 = self.replace(str1, str1[i], str2[i])
                        if str1 == str2:
                            return True
                        changes = True
                    elif result == "1":
                        other_letter = Counter("abcdefghijklmnopqrstuvwxyz") - Counter(str1)
                        if len(other_letter.keys()) > 0:
                            other_letter = list(other_letter.keys())[0]
                            str1 = self.replace(str1, str1[i], other_letter)
                            changes = True
                    elif result == "2":
                        pass
                    elif len(result) == 2 and result[0] == "3":
                        str1 = self.replace(str1, str1[i], result[1])
                        changes = True

        return str1 == str2