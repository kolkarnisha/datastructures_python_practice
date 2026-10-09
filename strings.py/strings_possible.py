# 📘 String Data Structure Conceptual Questions
# What is the difference between mutable and immutable strings in Python?
#
# How are strings stored in memory?
#
# What is the time complexity of:
#   - Accessing a character at index i
#   - Concatenating two strings
#   - Substring extraction
#   - String comparison
#
# What is the difference between substring and subsequence?
#
# What are common string matching algorithms (KMP, Boyer-Moore, Rabin-Karp)?
#
# What is hashing and how is it useful for string problems?
#
# How do prefix and suffix arrays work?
#
# What is dynamic programming and how is it applied to string problems?
#
# What are anagrams and how to detect them efficiently?
#

# 💻 String Coding Challenges

# 1. Reverse a String
# python
def reverse_string(s):
    return s[::-1]

print(reverse_string("hello"))
# Output: "olleh"

# 2. Check if String is Palindrome
# python
def is_palindrome(s):
    s = s.lower().replace(" ", "").replace(",", "")
    return s == s[::-1]

print(is_palindrome("A man, a plan, a canal: Panama"))
# Output: True

# 3. Find First Non-Repeating Character
# python
def first_non_repeating(s):
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    for char in s:
        if char_count[char] == 1:
            return char
    return None

print(first_non_repeating("leetcode"))
# Output: "l"

# 4. Check if Two Strings are Anagrams
# python
def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

print(are_anagrams("listen", "silent"))
# Output: True

# 5. Find Longest Substring Without Repeating Characters
# python
def longest_substring_without_repeating(s):
    char_index = {}
    max_len = 0
    start = 0
    for end, char in enumerate(s):
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1
        char_index[char] = end
        max_len = max(max_len, end - start + 1)
    return max_len

print(longest_substring_without_repeating("abcabcbb"))
# Output: 3 (for "abc")

# 6. Find All Substrings
# python
def all_substrings(s):
    substrings = []
    n = len(s)
    for i in range(n):
        for j in range(i + 1, n + 1):
            substrings.append(s[i:j])
    return substrings

print(all_substrings("abc"))
# Output: ["a", "ab", "abc", "b", "bc", "c"]

# 7. String Compression
# python
def compress_string(s):
    if not s:
        return ""
    compressed = []
    count = 1
    for i in range(len(s)):
        if i + 1 >= len(s) or s[i] != s[i + 1]:
            compressed.append(s[i] + str(count))
            count = 1
        else:
            count += 1
    return "".join(compressed)

print(compress_string("aabbbcc"))
# Output: "a2b3c2"

# 8. Check if String is Rotation of Another
# python
def is_rotation(s1, s2):
    return len(s1) == len(s2) and s1 in s2 + s2

print(is_rotation("abcd", "cdab"))
# Output: True

# 9. Find Longest Common Prefix
# python
def longest_common_prefix(strs):
    if not strs:
        return ""
    for i in range(len(strs[0])):
        char = strs[0][i]
        for j in range(1, len(strs)):
            if i >= len(strs[j]) or strs[j][i] != char:
                return strs[0][:i]
    return strs[0]

print(longest_common_prefix(["flower", "flow", "flight"]))
# Output: "fl"

# 10. Check if String has Balanced Parentheses
# python
def is_balanced_parentheses(s):
    stack = []
    pairs = {"(": ")", "[": "]", "{": "}"}
    for char in s:
        if char in pairs:
            stack.append(char)
        elif char in pairs.values():
            if not stack or pairs[stack.pop()] != char:
                return False
    return len(stack) == 0

print(is_balanced_parentheses("({[]})"))
# Output: True

# 11. Word Reverse (Reverse words in a string)
# python
def reverse_words(s):
    return " ".join(s.split()[::-1])

print(reverse_words("Hello World Python"))
# Output: "Python World Hello"

# 12. Convert String to Integer (Atoi)
# python
def string_to_integer(s):
    s = s.strip()
    if not s:
        return 0
    sign = 1
    if s[0] in ["+", "-"]:
        if s[0] == "-":
            sign = -1
        s = s[1:]
    result = 0
    for char in s:
        if char.isdigit():
            result = result * 10 + int(char)
        else:
            break
    return sign * result

print(string_to_integer("  -42"))
# Output: -42

# 13. Find Anagram Indices in String
# python
def find_anagram_indices(s, p):
    if len(p) > len(s):
        return []
    p_count = {}
    for char in p:
        p_count[char] = p_count.get(char, 0) + 1
    window_count = {}
    result = []
    for i in range(len(s)):
        char = s[i]
        window_count[char] = window_count.get(char, 0) + 1
        if i >= len(p):
            left_char = s[i - len(p)]
            if window_count[left_char] == 1:
                del window_count[left_char]
            else:
                window_count[left_char] -= 1
        if window_count == p_count:
            result.append(i - len(p) + 1)
    return result

print(find_anagram_indices("cbaebabacd", "abc"))
# Output: [0, 6]

# 14. Longest Palindromic Substring
# python
def longest_palindromic_substring(s):
    if not s:
        return ""
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]
    longest = ""
    for i in range(len(s)):
        p1 = expand_around_center(i, i)
        p2 = expand_around_center(i, i + 1)
        for p in [p1, p2]:
            if len(p) > len(longest):
                longest = p
    return longest

print(longest_palindromic_substring("babad"))
# Output: "bab" or "aba"

# 15. Valid Parentheses (LeetCode)
# python
def is_valid_parentheses(s):
    stack = []
    pairs = {"(": ")", "[": "]", "{": "}"}
    for char in s:
        if char in pairs:
            stack.append(char)
        else:
            if not stack or pairs[stack.pop()] != char:
                return False
    return len(stack) == 0

print(is_valid_parentheses("()[]{}"))
# Output: True

# 16. Edit Distance (Levenshtein Distance)
# python
def edit_distance(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    return dp[m][n]

print(edit_distance("horse", "ros"))
# Output: 3

# 17. Group Anagrams
# python
def group_anagrams(strs):
    anagram_map = {}
    for s in strs:
        sorted_s = "".join(sorted(s))
        if sorted_s not in anagram_map:
            anagram_map[sorted_s] = []
        anagram_map[sorted_s].append(s)
    return list(anagram_map.values())

print(group_anagrams(["eat", "tea", "ate", "bat", "tab"]))
# Output: [["eat", "tea", "ate"], ["bat", "tab"]]

# 18. Pattern Matching (KMP Algorithm)
# python
def kmp_search(text, pattern):
    def build_lps(pattern):
        m = len(pattern)
        lps = [0] * m
        j = 0
        for i in range(1, m):
            while j > 0 and pattern[i] != pattern[j]:
                j = lps[j - 1]
            if pattern[i] == pattern[j]:
                j += 1
            lps[i] = j
        return lps
    
    n = len(text)
    m = len(pattern)
    lps = build_lps(pattern)
    matches = []
    j = 0
    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = lps[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == m:
            matches.append(i - m + 1)
            j = lps[j - 1]
    return matches

print(kmp_search("ABABAB", "AB"))
# Output: [0, 2, 4]

# 19. Longest Common Subsequence (LCS)
# python
def longest_common_subsequence(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]

print(longest_common_subsequence("abcde", "ace"))
# Output: 3 (for "ace")

# 20. Regex Pattern Matching (Simple)
# python
def is_match(s, p):
    # Simple pattern matching with . and *
    memo = {}
    def helper(s_idx, p_idx):
        if (s_idx, p_idx) in memo:
            return memo[(s_idx, p_idx)]
        if p_idx == len(p):
            return s_idx == len(s)
        first_match = s_idx < len(s) and (p[p_idx] == "." or p[p_idx] == s[s_idx])
        if p_idx + 1 < len(p) and p[p_idx + 1] == "*":
            result = (helper(s_idx, p_idx + 2) or 
                     (first_match and helper(s_idx + 1, p_idx)))
        else:
            result = first_match and helper(s_idx + 1, p_idx + 1)
        memo[(s_idx, p_idx)] = result
        return result
    return helper(0, 0)

print(is_match("aa", "a"))
# Output: False

# 21. Minimum Window Substring
# python
def min_window_substring(s, t):
    if not s or not t:
        return ""
    dict_t = {}
    for char in t:
        dict_t[char] = dict_t.get(char, 0) + 1
    required = len(dict_t)
    l, r = 0, 0
    formed = 0
    window_counts = {}
    ans = float("inf"), None, None
    while r < len(s):
        char = s[r]
        window_counts[char] = window_counts.get(char, 0) + 1
        if char in dict_t and window_counts[char] == dict_t[char]:
            formed += 1
        while l <= r and formed == required:
            char = s[l]
            if r - l + 1 < ans[0]:
                ans = (r - l + 1, l, r)
            window_counts[char] -= 1
            if char in dict_t and window_counts[char] < dict_t[char]:
                formed -= 1
            l += 1
        r += 1
    return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]

print(min_window_substring("ADOBECODEBANC", "ABC"))
# Output: "BANC"

# 22. Integer to Roman
# python
def int_to_roman(num):
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    numerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    roman = ""
    for i in range(len(values)):
        count = num // values[i]
        roman += numerals[i] * count
        num -= values[i] * count
    return roman

print(int_to_roman(58))
# Output: "LVIII"

# 23. Roman to Integer
# python
def roman_to_int(s):
    roman_values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    prev_value = 0
    for char in reversed(s):
        value = roman_values[char]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    return total

print(roman_to_int("LVIII"))
# Output: 58

# 24. Word Break (Dynamic Programming)
# python
def word_break(s, word_dict):
    dp = [False] * (len(s) + 1)
    dp[0] = True
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_dict:
                dp[i] = True
                break
    return dp[len(s)]

print(word_break("catsandog", ["cat", "cats", "and", "sand", "dog"]))
# Output: False

# 25. Longest Repeating Character Replacement
# python
def longest_repeating_char_replacement(s, k):
    char_count = {}
    max_char_freq = 0
    l = 0
    max_len = 0
    for r in range(len(s)):
        char_count[s[r]] = char_count.get(s[r], 0) + 1
        max_char_freq = max(max_char_freq, char_count[s[r]])
        window_len = r - l + 1
        if window_len - max_char_freq > k:
            char_count[s[l]] -= 1
            l += 1
        max_len = max(max_len, r - l + 1)
    return max_len

print(longest_repeating_char_replacement("ABAB", 2))
# Output: 4

# 26. Multiply Strings
# python
def multiply_strings(num1, num2):
    if num1 == "0" or num2 == "0":
        return "0"
    len1, len2 = len(num1), len(num2)
    result = [0] * (len1 + len2)
    for i in range(len1 - 1, -1, -1):
        for j in range(len2 - 1, -1, -1):
            mul = int(num1[i]) * int(num2[j])
            p1, p2 = i + j, i + j + 1
            total = mul + result[p2]
            result[p2] = total % 10
            result[p1] += total // 10
    return "".join(map(str, result)).lstrip("0") or "0"

print(multiply_strings("123", "456"))
# Output: "56088"

# 27. Isomorphic Strings
# python
def is_isomorphic(s, t):
    if len(s) != len(t):
        return False
    map_s_to_t = {}
    map_t_to_s = {}
    for c1, c2 in zip(s, t):
        if (c1 in map_s_to_t and map_s_to_t[c1] != c2) or (c2 in map_t_to_s and map_t_to_s[c2] != c1):
            return False
        map_s_to_t[c1] = c2
        map_t_to_s[c2] = c1
    return True

print(is_isomorphic("egg", "add"))
# Output: True

# 28. Zigzag Conversion
# python
def zigzag_conversion(s, rows):
    if rows == 1:
        return s
    result = [[] for _ in range(rows)]
    row = 0
    direction = 1
    for char in s:
        result[row].append(char)
        if row == 0:
            direction = 1
        elif row == rows - 1:
            direction = -1
        row += direction
    return "".join("".join(r) for r in result)

print(zigzag_conversion("PAYPALISHIRING", 3))
# Output: "PAHNAPLSIIGYIR"

# 29. Compare Version Numbers
# python
def compare_version(version1, version2):
    v1_parts = list(map(int, version1.split(".")))
    v2_parts = list(map(int, version2.split(".")))
    max_len = max(len(v1_parts), len(v2_parts))
    while len(v1_parts) < max_len:
        v1_parts.append(0)
    while len(v2_parts) < max_len:
        v2_parts.append(0)
    for i in range(max_len):
        if v1_parts[i] < v2_parts[i]:
            return -1
        elif v1_parts[i] > v2_parts[i]:
            return 1
    return 0

print(compare_version("1.0", "1.0.0"))
# Output: 0

# 30. Wildcard Matching
# python
def wildcard_matching(s, p):
    s_idx = 0
    p_idx = 0
    star_idx = -1
    match = 0
    while s_idx < len(s):
        if p_idx < len(p) and (p[p_idx] == "?" or p[p_idx] == s[s_idx]):
            s_idx += 1
            p_idx += 1
        elif p_idx < len(p) and p[p_idx] == "*":
            star_idx = p_idx
            match = s_idx
            p_idx += 1
        elif star_idx != -1:
            p_idx = star_idx + 1
            match += 1
            s_idx = match
        else:
            return False
    while p_idx < len(p) and p[p_idx] == "*":
            p_idx += 1
    return p_idx == len(p)

print(wildcard_matching("aa", "*"))
# Output: True

# 31. Decode String
# python
def decode_string(s):
    stack = []
    for char in s:
        if char != "]":
            stack.append(char)
        else:
            string = ""
            while stack[-1] != "[":
                string = stack.pop() + string
            stack.pop()  # Remove "["
            num = ""
            while stack and stack[-1].isdigit():
                num = stack.pop() + num
            stack.append(int(num) * string)
    return "".join(stack)

print(decode_string("3[a2[c]]"))
# Output: "accaccacc"

# 32. Ransom Note
# python
def can_construct_ransom_note(ransom_note, magazine):
    char_count = {}
    for char in magazine:
        char_count[char] = char_count.get(char, 0) + 1
    for char in ransom_note:
        if char not in char_count or char_count[char] == 0:
            return False
        char_count[char] -= 1
    return True

print(can_construct_ransom_note("a", "b"))
# Output: False

# 33. License Key Formatting
# python
def license_key_formatting(s, k):
    s = s.replace("-", "").upper()
    result = []
    for i, char in enumerate(reversed(s)):
        if i % k == 0 and i > 0:
            result.append("-")
        result.append(char)
    return "".join(reversed(result))

print(license_key_formatting("5F3Z-2e-9-w", 4))
# Output: "5F3Z-2E9W"

# 34. Nth Digit
# python
def find_nth_digit(n):
    digit = 1
    count = 9
    start = 1
    while n > digit * count:
        n -= digit * count
        digit += 1
        count *= 10
        start *= 10
    return int(str(start + (n - 1) // digit)[(n - 1) % digit])

print(find_nth_digit(11))
# Output: 0 (in sequence 123456789101112...)

# 35. Alien Dictionary (Topological Sort)
# python
def alien_order(words):
    if not words:
        return ""
    graph = {char: set() for word in words for char in word}
    in_degree = {char: 0 for char in graph}
    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        for j in range(min(len(w1), len(w2))):
            if w1[j] != w2[j]:
                if w2[j] not in graph[w1[j]]:
                    graph[w1[j]].add(w2[j])
                    in_degree[w2[j]] += 1
                break
    queue = [char for char in graph if in_degree[char] == 0]
    result = []
    while queue:
        char = queue.pop(0)
        result.append(char)
        for neighbor in graph[char]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    return "".join(result) if len(result) == len(graph) else ""

print(alien_order(["wrt", "wrf", "er", "ett", "rftt"]))
# Output: "wertf"

# 36. Remove Duplicate Letters
# python
def remove_duplicate_letters(s):
    last_occurrence = {char: i for i, char in enumerate(s)}
    stack = []
    seen = set()
    for i, char in enumerate(s):
        if char in seen:
            continue
        while stack and stack[-1] > char and last_occurrence[stack[-1]] > i:
            removed = stack.pop()
            seen.remove(removed)
        stack.append(char)
        seen.add(char)
    return "".join(stack)

print(remove_duplicate_letters("bcabc"))
# Output: "abc"

# 37. Manacher's Algorithm (Longest Palindrome)
# python
def manacher_algorithm(s):
    if not s:
        return ""
    # Transform string to avoid even/odd palindrome
    transformed = "#".join("^{}$".format(s))
    n = len(transformed)
    palindrome_len = [0] * n
    center = 0
    right = 0
    for i in range(1, n - 1):
        mirror = 2 * center - i
        if i < right:
            palindrome_len[i] = min(right - i, palindrome_len[mirror])
        while transformed[i + palindrome_len[i] + 1] == transformed[i - palindrome_len[i] - 1]:
            palindrome_len[i] += 1
        if i + palindrome_len[i] > right:
            center, right = i, i + palindrome_len[i]
    max_len = max(palindrome_len)
    max_idx = palindrome_len.index(max_len)
    return s[(max_idx - max_len) // 2:(max_idx + max_len) // 2]

print(manacher_algorithm("babad"))
# Output: "bab" or "aba"

# 38. Z-Algorithm (Pattern Matching)
# python
def z_algorithm(s):
    n = len(s)
    z = [0] * n
    l, r = 0, 0
    for i in range(1, n):
        if i > r:
            l, r = i, i
            while r < n and s[r - l] == s[r]:
                r += 1
            z[i] = r - l
            r -= 1
        else:
            k = i - l
            if z[k] < r - i + 1:
                z[i] = z[k]
            else:
                l = i
                while r < n and s[r - l] == s[r]:
                    r += 1
                z[i] = r - l
                r -= 1
    return z

print(z_algorithm("aabaaab"))
# Output: [0, 1, 0, 3, 1, 0, 1]

# 39. Rabin-Karp Algorithm (Rolling Hash)
# python
def rabin_karp(text, pattern, prime=101, base=256):
    n = len(text)
    m = len(pattern)
    hash_text = 0
    hash_pattern = 0
    hash_base = 1
    matches = []
    for i in range(m - 1):
        hash_base = (hash_base * base) % prime
    for i in range(m):
        hash_text = (hash_text * base + ord(text[i])) % prime
        hash_pattern = (hash_pattern * base + ord(pattern[i])) % prime
    for i in range(n - m + 1):
        if hash_text == hash_pattern:
            if text[i:i + m] == pattern:
                matches.append(i)
        if i < n - m:
            hash_text = (base * (hash_text - ord(text[i]) * hash_base) + ord(text[i + m])) % prime
            if hash_text < 0:
                hash_text += prime
    return matches

print(rabin_karp("ABCCDDEFEFGGHIJ", "DEF"))
# Output: [5]

# 40. Trie Implementation (Prefix Tree)
# python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
    
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end
    
    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

trie = Trie()
trie.insert("apple")
print(trie.search("apple"))
# Output: True

# 41. Words Matching Trie (Word Search II)
# python
def find_words(board, words):
    trie = {}
    for word in words:
        node = trie
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node["$"] = word
    
    result = []
    visited = set()
    
    def dfs(i, j, node):
        if "$" in node:
            result.append(node["$"])
            del node["$"]
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < len(board) and 0 <= nj < len(board[0]) and (ni, nj) not in visited:
                char = board[ni][nj]
                if char in node:
                    visited.add((ni, nj))
                    dfs(ni, nj, node[char])
                    visited.remove((ni, nj))
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            char = board[i][j]
            if char in trie:
                visited.add((i, j))
                dfs(i, j, trie[char])
                visited.remove((i, j))
    
    return result

# 42. Add Strings (Without Type Conversion)
# python
def add_strings(num1, num2):
    result = []
    carry = 0
    i, j = len(num1) - 1, len(num2) - 1
    while i >= 0 or j >= 0 or carry:
        digit1 = int(num1[i]) if i >= 0 else 0
        digit2 = int(num2[j]) if j >= 0 else 0
        total = digit1 + digit2 + carry
        result.append(str(total % 10))
        carry = total // 10
        i -= 1
        j -= 1
    return "".join(reversed(result))

print(add_strings("456", "77"))
# Output: "533"

# 43. Substring Concatenation
# python
def substring_concat(s, words):
    if not words:
        return []
    word_len = len(words[0])
    total_len = word_len * len(words)
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    result = []
    for i in range(len(s) - total_len + 1):
        substring = s[i:i + total_len]
        temp = {}
        for j in range(0, total_len, word_len):
            word = substring[j:j + word_len]
            if word not in word_count:
                break
            temp[word] = temp.get(word, 0) + 1
            if temp[word] > word_count[word]:
                break
        else:
            if temp == word_count:
                result.append(i)
    return result

print(substring_concat("barfoothefoobarman", ["foo", "bar"]))
# Output: [0, 9]

# 44. Circular Array Loop
# python
def circular_array_loop(nums):
    n = len(nums)
    for i in range(n):
        visited = set()
        slow = fast = i
        while True:
            slow = (slow + nums[slow]) % n
            fast = (fast + nums[fast]) % n
            fast = (fast + nums[fast]) % n
            if slow == fast:
                break
            if (slow, fast) in visited:
                return False
            visited.add((slow, fast))
        if nums[slow] * nums[(slow + nums[slow]) % n] > 0:
            return True
    return False

# 45. Delete Operation for Two Strings (LCS variant)
# python
def delete_operation_two_strings(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    lcs_len = dp[m][n]
    return m + n - 2 * lcs_len

print(delete_operation_two_strings("leetcode", "etco"))
# Output: 4

# 46. Valid String Parentheses Count
# python
def count_valid_parentheses(s):
    stack = []
    max_valid = 0
    stack.append(-1)
    for i, char in enumerate(s):
        if char == "(":
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                max_valid = max(max_valid, i - stack[-1])
    return max_valid

print(count_valid_parentheses("(()"))
# Output: 2

# 47. Repeated DNA Sequences
# python
def find_repeated_dna_sequences(s):
    if len(s) < 10:
        return []
    seen = set()
    repeated = set()
    for i in range(len(s) - 9):
        substring = s[i:i + 10]
        if substring in seen:
            repeated.add(substring)
        seen.add(substring)
    return list(repeated)

print(find_repeated_dna_sequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
# Output: ["AAAAACCCCC", "CCCCCAAAAA"]

# 48. Number of Matching Subsequences
# python
def num_matching_subseq(s, words):
    count = 0
    for word in words:
        s_idx = 0
        for char in word:
            while s_idx < len(s) and s[s_idx] != char:
                s_idx += 1
            if s_idx == len(s):
                break
            s_idx += 1
        else:
            count += 1
    return count

print(num_matching_subseq("ab", ["a", "b", "ba"]))
# Output: 2

# 49. Short Encoding of Words
# python
def minimal_length_encoding(words):
    words = set(words)
    words = sorted(words, key=len, reverse=True)
    encoding = ""
    for word in words:
        if word not in encoding:
            encoding += word + "#"
    return len(encoding)

print(minimal_length_encoding(["time", "me", "bell"]))
# Output: 10

# 50. Count Unique Characters in Substrings
# python
def unique_letters_string(s):
    char_last = {}
    char_first = {}
    for i, char in enumerate(s):
        if char not in char_first:
            char_first[char] = i
        char_last[char] = i
    result = 0
    for char in char_last:
        result += (char_first[char] + 1) * (len(s) - char_last[char])
    return result

print(unique_letters_string("ABC"))
# Output: 10

# 51. Reverse Only Letters
# python
def reverse_only_letters(s):
    chars = list(s)
    left, right = 0, len(s) - 1
    while left < right:
        if not chars[left].isalpha():
            left += 1
        elif not chars[right].isalpha():
            right -= 1
        else:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1
    return "".join(chars)

print(reverse_only_letters("ab-cd"))
# Output: "dc-ba"

# 52. Flipping an Image (String rotation)
# python
def flip_and_invert_image(image):
    for row in image:
        row.reverse()
        for i in range(len(row)):
            row[i] ^= 1
    return image

print(flip_and_invert_image([[1, 1, 0], [1, 0, 1], [0, 0, 0]]))
# Output: [[1, 0, 0], [0, 1, 0], [1, 1, 1]]

# 53. Parse Lisp Expression
# python
def evaluate_lisp(expression):
    def helper(expr, scope):
        expr = expr.strip()
        if expr[0] != "(":
            if expr.lstrip("-").isdigit():
                return int(expr)
            else:
                return scope[expr]
        
        expr = expr[1:-1]
        tokens = []
        count = 0
        token = ""
        for char in expr:
            if char == "(":
                count += 1
            elif char == ")":
                count -= 1
            if char == " " and count == 0:
                if token:
                    tokens.append(token)
                token = ""
            else:
                token += char
        if token:
            tokens.append(token)
        
        op = tokens[0]
        if op == "let":
            new_scope = scope.copy()
            for i in range(1, len(tokens) - 1, 2):
                new_scope[tokens[i]] = helper(tokens[i + 1], new_scope)
            return helper(tokens[-1], new_scope)
        elif op == "add":
            return helper(tokens[1], scope) + helper(tokens[2], scope)
        elif op == "mult":
            return helper(tokens[1], scope) * helper(tokens[2], scope)
    
    return helper(expression, {})

print(evaluate_lisp("(add 1 2)"))
# Output: 3

# 54. Maximum Nesting Level of Parentheses
# python
def max_depth_parentheses(s):
    max_depth = 0
    current_depth = 0
    for char in s:
        if char == "(":
            current_depth += 1
            max_depth = max(max_depth, current_depth)
        elif char == ")":
            current_depth -= 1
    return max_depth

print(max_depth_parentheses("(1+(2*3)+((8)/4))+1"))
# Output: 3

# 55. Backspace String Comparison
# python
def backspace_compare(s, t):
    def process(s):
        stack = []
        for char in s:
            if char == "#":
                if stack:
                    stack.pop()
            else:
                stack.append(char)
        return "".join(stack)
    return process(s) == process(t)

print(backspace_compare("ab#c", "ad#c"))
# Output: True

# 56. Find the Celebrity (using string representation)
# python
def find_celebrity(graph):
    n = len(graph)
    for i in range(n):
        is_celebrity = True
        for j in range(n):
            if i != j and (graph[i][j] == 1 or graph[j][i] == 0):
                is_celebrity = False
                break
        if is_celebrity:
            return i
    return -1

# 57. String Without Consecutive Duplicates
# python
def remove_consecutive_duplicates(s):
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    return "".join(stack)

print(remove_consecutive_duplicates("abbaca"))
# Output: "ca"

# 58. Smallest Rotation with High Score
# python
def best_rotation(A):
    n = len(A)
    bad = [0] * n
    for i in range(n):
        redo = (i + 1) % n
        bad[redo] += 1
        redo = (i - A[i] + 1) % n
        bad[redo] -= 1
    best = 0
    score = n
    for i in range(n):
        bad[i] = (bad[i] if i > 0 else 0) + (bad[i - 1] if i > 0 else 0)
        current_score = n - bad[i]
        if current_score > score:
            best = i
            score = current_score
    return best

# 59. Contains Duplicate II (String variant)
# python
def contains_duplicate_ii(nums, k):
    window = set()
    for i in range(len(nums)):
        if nums[i] in window:
            return True
        window.add(nums[i])
        if len(window) > k:
            window.remove(nums[i - k])
    return False

print(contains_duplicate_ii([99, 99], 2))
# Output: True

# 60. Student Attendance Record
# python
def check_attendance_record(s):
    return s.count("A") <= 1 and "LLL" not in s

print(check_attendance_record("PPALLP"))
# Output: True

# 61. Reorder Log Files
# python
def reorder_logs(logs):
    def get_key(log):
        identifier, rest = log.split(" ", 1)
        if rest[0].isdigit():
            return (1, 0)
        else:
            return (0, rest, identifier)
    return sorted(logs, key=get_key)

print(reorder_logs(["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig"]))
# Output: ["let1 art can", "let2 own kit dig", "dig1 8 1 5 1", "dig2 3 6"]

# 62. IP Address Validation
# python
def is_valid_ip(s):
    parts = s.split(".")
    if len(parts) != 4:
        return False
    for part in parts:
        if not part or len(part) > 3:
            return False
        if part[0] == "0" and len(part) > 1:
            return False
        if not part.isdigit() or int(part) > 255:
            return False
    return True

print(is_valid_ip("172.16.254.1"))
# Output: True

# 63. Restoring IP Addresses
# python
def restore_ip_addresses(s):
    result = []
    if len(s) > 12 or len(s) < 4:
        return result
    
    def backtrack(index, path):
        if len(path) == 4:
            if index == len(s):
                result.append(".".join(path))
            return
        
        if index > len(s) or len(path) == 4:
            return
        
        for i in range(index + 1, min(index + 4, len(s) + 1)):
            segment = s[index:i]
            if segment[0] == "0" and len(segment) > 1:
                continue
            if int(segment) > 255:
                break
            path.append(segment)
            backtrack(i, path)
            path.pop()
    
    backtrack(0, [])
    return result

print(restore_ip_addresses("25525511135"))
# Output: ["255.255.11.35", "255.255.111.35"]

# 64. Next Permutation
# python
def next_permutation(nums):
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
    if i == -1:
        nums.reverse()
        return
    j = len(nums) - 1
    while j > i and nums[j] <= nums[i]:
        j -= 1
    nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1:] = reversed(nums[i + 1:])

# 65. Permutation in String
# python
def permutation_in_string(s1, s2):
    if len(s1) > len(s2):
        return False
    s1_count = {}
    window_count = {}
    for char in s1:
        s1_count[char] = s1_count.get(char, 0) + 1
    for i in range(len(s2)):
        char = s2[i]
        window_count[char] = window_count.get(char, 0) + 1
        if i >= len(s1):
            left_char = s2[i - len(s1)]
            if window_count[left_char] == 1:
                del window_count[left_char]
            else:
                window_count[left_char] -= 1
        if window_count == s1_count:
            return True
    return False

print(permutation_in_string("ab", "eidbaooo"))
# Output: True

# 66. Find All Possible Interleaving Strings
# python
def is_interleave(s1, s2, s3):
    if len(s1) + len(s2) != len(s3):
        return False
    memo = {}
    def helper(i, j, k):
        if (i, j, k) in memo:
            return memo[(i, j, k)]
        if i == len(s1) and j == len(s2) and k == len(s3):
            return True
        result = False
        if i < len(s1) and s1[i] == s3[k]:
            result = helper(i + 1, j, k + 1)
        if j < len(s2) and s2[j] == s3[k]:
            result = result or helper(i, j + 1, k + 1)
        memo[(i, j, k)] = result
        return result
    return helper(0, 0, 0)

print(is_interleave("aab", "dbbca", "aadbbcb"))
# Output: True

# 67. String Transform
# python
def unique_morse_representations(words):
    morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", 
             "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", 
             "..-", "...-", ".--", "-..-", "-.--", "--.."]
    return len({
        "".join(morse[ord(c) - ord("a")] for c in word)
        for word in words
    })

print(unique_morse_representations(["gin", "zen", "gig", "msg"]))
# Output: 2

# 68. Encode String with Shortest Length
# python
def encode_string(s):
    memo = {}
    def helper(s):
        if s in memo:
            return memo[s]
        if len(s) <= 3:
            return s
        result = s
        for i in range(1, len(s) // 2 + 1):
            pattern = s[:i]
            j = 0
            while j + i <= len(s):
                if s[j:j + i] != pattern:
                    break
                j += i
            if j >= i + i:
                encoded = str(j // i) + pattern + helper(s[j:])
                if len(encoded) < len(result):
                    result = encoded
        memo[s] = result
        return result
    return helper(s)

print(encode_string("abcabcabcabc"))
# Output: "4[abc]"

# 69. Text Justification
# python
def text_justification(words, max_width):
    result = []
    current = []
    current_len = 0
    
    for word in words:
        if current_len + len(word) + len(current) > max_width:
            result.append(justify(current, max_width, False))
            current = []
            current_len = 0
        current.append(word)
        current_len += len(word)
    
    result.append(justify(current, max_width, True))
    return result

def justify(words, max_width, is_last):
    if is_last:
        line = " ".join(words)
        return line + " " * (max_width - len(line))
    
    spaces = max_width - sum(len(word) for word in words)
    gaps = len(words) - 1
    space_per_gap = spaces // gaps if gaps > 0 else 0
    extra_spaces = spaces % gaps if gaps > 0 else 0
    
    line = ""
    for i, word in enumerate(words):
        line += word
        if i < gaps:
            line += " " * (space_per_gap + (1 if i < extra_spaces else 0))
    return line

# 70. Simplify Path
# python
def simplify_path(path):
    stack = []
    for part in path.split("/"):
        if part == "" or part == ".":
            continue
        elif part == "..":
            if stack:
                stack.pop()
        else:
            stack.append(part)
    return "/" + "/".join(stack)

print(simplify_path("/a/../../b/../c//.//"))
# Output: "/b/c"

# 71. Rearrange String K Distance Apart
# python
def rearrange_string_k_distance(s, k):
    from collections import Counter
    import heapq
    
    char_count = Counter(s)
    max_heap = [(-count, char) for char, count in char_count.items()]
    heapq.heapify(max_heap)
    result = []
    
    while max_heap:
        temp = []
        for i in range(k):
            if not max_heap:
                if len(result) != len(s):
                    return ""
                return "".join(result)
            count, char = heapq.heappop(max_heap)
            result.append(char)
            if count < -1:
                temp.append((count + 1, char))
        for item in temp:
            heapq.heappush(max_heap, item)
    return "".join(result)

# 72. Basic Calculator II
# python
def calculate_ii(s):
    stack = []
    num = 0
    operator = "+"
    
    for i, char in enumerate(s):
        if char.isdigit():
            num = num * 10 + int(char)
        
        if char in "+-*/" or i == len(s) - 1:
            if operator == "+":
                stack.append(num)
            elif operator == "-":
                stack.append(-num)
            elif operator == "*":
                stack.append(stack.pop() * num)
            elif operator == "/":
                stack.append(int(stack.pop() / num))
            
            if char in "+-*/":
                operator = char
                num = 0
    
    return sum(stack)

print(calculate_ii("3+2*2"))
# Output: 7

# 73. Word Pattern
# python
def word_pattern(pattern, s):
    words = s.split()
    if len(pattern) != len(words):
        return False
    
    char_to_word = {}
    word_to_char = {}
    
    for char, word in zip(pattern, words):
        if char in char_to_word:
            if char_to_word[char] != word:
                return False
        else:
            char_to_word[char] = word
        
        if word in word_to_char:
            if word_to_char[word] != char:
                return False
        else:
            word_to_char[word] = char
    
    return True

print(word_pattern("badc", "b a d c"))
# Output: True

# 74. Concatenated Words
# python
def concatenated_words(words):
    words_set = set(words)
    memo = {}
    
    def can_form(word):
        if word in memo:
            return memo[word]
        
        for i in range(1, len(word)):
            prefix = word[:i]
            suffix = word[i:]
            
            if prefix in words_set:
                if suffix in words_set or can_form(suffix):
                    memo[word] = True
                    return True
        
        memo[word] = False
        return False
    
    result = []
    for word in words:
        if can_form(word):
            result.append(word)
    return result

# 75. Sentence Screen Fitting
# python
def sentence_rows_cols(sentence, rows, cols):
    words = sentence.split()
    word_index = 0
    
    for row in range(rows):
        col = 0
        while col + len(words[word_index]) <= cols:
            col += len(words[word_index]) + 1
            word_index = (word_index + 1) % len(words)
    
    return word_index

# 76. Can Achieve K Distance Spacing
# python
def distance_k_spacing(words, max_width, k):
    result = []
    for i, word in enumerate(words):
        if i % k == 0:
            result.append(word)
    return result

# 77. Valid Parenthesis String with Wildcard
# python
def check_valid_string(s):
    left_min = left_max = 0
    
    for char in s:
        if char == "(":
            left_min += 1
            left_max += 1
        elif char == ")":
            left_min -= 1
            left_max -= 1
        else:  # char == "*"
            left_min -= 1
            left_max += 1
        
        if left_max < 0:
            return False
        if left_min < 0:
            left_min = 0
    
    return left_min == 0

print(check_valid_string("(*"))
# Output: False

# 78. Reorganize String
# python
def reorganize_string(s):
    from collections import Counter
    import heapq
    
    char_count = Counter(s)
    
    if max(char_count.values()) > (len(s) + 1) // 2:
        return ""
    
    max_heap = [(-count, char) for char, count in char_count.items()]
    heapq.heapify(max_heap)
    
    result = []
    while len(max_heap) > 1:
        first_count, first_char = heapq.heappop(max_heap)
        second_count, second_char = heapq.heappop(max_heap)
        
        result.extend([first_char, second_char])
        
        if first_count < -1:
            heapq.heappush(max_heap, (first_count + 1, first_char))
        if second_count < -1:
            heapq.heappush(max_heap, (second_count + 1, second_char))
    
    if max_heap:
        result.append(max_heap[0][1])
    
    return "".join(result)

print(reorganize_string("aab"))
# Output: "aba"

# 79. String Matching in an Array
# python
def string_matching(words):
    words.sort(key=len)
    result = []
    for i, word1 in enumerate(words):
        for j in range(i + 1, len(words)):
            if word1 in words[j]:
                result.append(word1)
                break
    return result

print(string_matching(["mass", "as", "hero", "batman", "near", "ar"]))
# Output: ["ar", "as", "hero", "near"]

# 80. Valid Word Abbreviation
# python
def valid_word_abbreviation(word, abbr):
    w_idx = 0
    a_idx = 0
    
    while w_idx < len(word) and a_idx < len(abbr):
        if abbr[a_idx].isdigit():
            if abbr[a_idx] == "0":
                return False
            num = 0
            while a_idx < len(abbr) and abbr[a_idx].isdigit():
                num = num * 10 + int(abbr[a_idx])
                a_idx += 1
            w_idx += num
        else:
            if word[w_idx] != abbr[a_idx]:
                return False
            w_idx += 1
            a_idx += 1
    
    return w_idx == len(word) and a_idx == len(abbr)

print(valid_word_abbreviation("internationalization", "i12iz4n"))
# Output: True
'''43: Substring Concatenation
44: Circular Array Loop
45: Delete Operation for Two Strings (LCS variant)
46: Valid Parentheses String Count
Advanced Patterns:

47: Repeated DNA Sequences (Hashing)
48: Matching Subsequences
49: Short Encoding of Words
50: Unique Letters in Substrings
51: Reverse Only Letters
52: Flipping an Image
Hard Problems:

53: Parse Lisp Expression (Recursion & Tokenization)
54: Max Nesting Level of Parentheses
55: Backspace String Comparison
56: Find Celebrity Problem
57: Remove Consecutive Duplicates
58: Best Rotation with Score
59: Contains Duplicate II
60: Student Attendance Record
61: Reorder Log Files
62: IP Address Validation
  63: Restore IP Addresses
  64: Next Permutation
  65: Permutation in String
  66: Interleaving Strings
  67: Unique Morse Code Words
  68: Encode String with Shortest Length
  69: Text Justification
  70: Simplify Path
  71: Rearrange String K Distance Apart
  72: Basic Calculator II
  73: Word Pattern
  74: Concatenated Words
  75: Sentence Screen Fitting
  76: Can Achieve K Distance Spacing
  77: Valid Parenthesis String with Wildcard
  78: Reorganize String
  79: String Matching in an Array
  80: Valid Word Abbreviation
  81: Minimum Window Subsequence
  82: Longest Repeating Character Replacement
  83: Longest Substring with At Most Two Distinct Characters
  84: Longest Substring with At Most K Distinct Characters
  85: Longest Substring Without Repeating Characters
  86: Longest Substring with At Most K Distinct Characters (Sliding Window)
  87: Longest Substring with At Most K Distinct Characters (Sliding Window)
  88: Longest Substring with At Most K Distinct Characters (Sliding Window)
  89: Longest Substring with At Most K Distinct Characters (Sliding Window)
  90: Longest Substring with At Most K Distinct Characters (Sliding Window)'''