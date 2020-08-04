# Bruteforce substring search
# Time complexity 
# Worst case Theta(N * M)


def str_search(pattern, text):
    """
    if pattern exists in text, return index where pattern starts. 
    :param pattern: string pattern
    :param text: string text 
    :returns: index of where pattern starts
    """
    N, M = len(text), len(pattern)
    i = 0 
    while i <= N-M:
        j = 0 
        while j < M:
            if text[i + j] != pattern[j]:
                break 
            j += 1
        if j == M: return i 
        i += 1
    return N


def str_search_two(pattern, text):
    """
    if pattern exists in text, return index where pattern starts. 
    :param pattern: string pattern
    :param text: string text 
    :returns: index of where pattern starts
    """
    N, M = len(text), len(pattern)
    i, j = 0, 0 
    while i < N and j < M:
        if text[i] == pattern[j]:
            j += 1
        else:
            i -= j
            j = 0 
        i += 1
    if j == M: return i - M 
    else: return N  
       

def main():
    print(str_search('ADACR', 'ABACADABRAC'))
    print(str_search('IN', 'VINCENT'))
    print(str_search_two('ADACR', 'ABACADABRAC'))
    print(str_search_two('IN', 'VINCENT'))

if __name__ == '__main__':
    main()
