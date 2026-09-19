class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        output = []
        cur_line = []
        cur_len = 0  # Combined character length of words in cur_line (excluding spaces)

        for word in words:
            # Check if adding this word (plus at least 1 space per existing word) exceeds maxWidth
            if cur_len + len(word) + len(cur_line) > maxWidth:
                # Calculate spaces for current line
                total_spaces = maxWidth - cur_len
                gaps = len(cur_line) - 1

                if gaps == 0:  # Single-word line
                    line = cur_line[0] + ' ' * total_spaces
                else:
                    space_per_gap, extra_spaces = divmod(total_spaces, gaps)
                    line_parts = []
                    for i in range(gaps):
                        spaces = space_per_gap + (1 if i < extra_spaces else 0)
                        line_parts.append(cur_line[i] + ' ' * spaces)
                    line_parts.append(cur_line[-1])
                    line = "".join(line_parts)

                output.append(line)
                cur_line = []
                cur_len = 0

            cur_line.append(word)
            cur_len += len(word)

        # Handle the last line (left-justified per LeetCode rules)
        last_line_str = " ".join(cur_line)
        last_line_str += ' ' * (maxWidth - len(last_line_str))
        output.append(last_line_str)

        return output