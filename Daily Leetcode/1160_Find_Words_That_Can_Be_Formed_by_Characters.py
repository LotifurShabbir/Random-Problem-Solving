class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_count = Counter(chars)
        # print(chars_count)
        total_length = 0

        for word in words:
            word_count = Counter(word)
            can_form = True

            for key, value in word_count.items():
                if key not in chars_count or chars_count[key] < value: #caaat > cat
                    can_form = False
                    break

            if can_form == True:
                total_length += len(word)

        return total_length