class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        sub_word = word
        sub_abbr = abbr
        while len(sub_abbr) > 0 and len(sub_word) > 0:
            head = self.get_next_head(sub_abbr)
            sub_abbr = sub_abbr[len(head):]
            print(head, ':', sub_word, ':', sub_abbr)
            if head[0] == '0':
                return False

            if not self.is_match(head, sub_word):
                return False

            if head.isalpha():
                sub_word = sub_word[1:]
            else:
                sub_word = sub_word[int(head):]

        if not (len(sub_abbr) == 0 and len(sub_word) == 0):
            return False
        return True

    def get_next_head(self, sub_abbr):
        head = sub_abbr[0]
        if head.isalpha():
            return head
        idx = 1
        while idx < len(sub_abbr):
            if sub_abbr[idx].isalpha():
                break
            else:
                head += sub_abbr[idx]
                idx += 1
        return head

    def is_match(self, head, sub_word):
        if head.isalpha():
            return sub_word[0] == head
        return len(sub_word) >= int(head)


word = "apple"
abbr = "a2e"
ob = Solution()
ob.validWordAbbreviation(word, abbr)
