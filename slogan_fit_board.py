# https://leetcode.com/problems/sentence-screen-fitting/
class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        # cols is multiple of whole sent
        # cols+1 is multiple of whole sent

        word_len = []
        for words in sentence:
            word_len.append(len(words))

        length = len(sentence)
        s = sum(word_len) + length
        # print("s : ", s )

        if cols % s == 0:
            return rows * (cols / s)
        elif (cols + 1) % s == 0:
            return rows * (cols + 1) / s

        remaining = [cols for i in range(rows)]
        # print("init remaining", remaining)
        fit = []
        fitted = 0
        index = 0
        for r in range(rows):
            # print("row: ", str(r))
            if r > 0 and index == 0:
                # print(fit)
                return (rows / r) * fit[r - 1] + (fit[(rows % r) - 1] if rows % r > 0 else 0)

            while index > 0 and word_len[index] <= remaining[r]:
                remaining[r] -= word_len[index] + 1
                index = (index + 1) % length
                if index == 0:
                    fitted += 1
                    # print("fitted one, remaining space: ",remaining[r])

            if remaining[r] >= s - 1:
                bunch_fit = max(remaining[r] / s, (remaining[r] + 1) / s)
                remaining[r] -= bunch_fit * s
                fitted += bunch_fit
                # print("row: ", r)
                # print("bunch_filled: ",bunch_fit)

            while index < length and word_len[index] <= remaining[r]:
                remaining[r] -= word_len[index] + 1
                index = (index + 1) % length
                if index == 0:
                    fitted += 1
                    # print("fitted one, remaining space: ",remaining[r])

            fit.append(fitted)

        return fitted
