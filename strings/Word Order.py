# Enter your code here. Read input from STDIN. Print output to STDOUT
def count_word_occurences(n, words):
    word_count = {}
    order = []
    
    for word in words:
        if word not in word_count:
            word_count[word] = 0
            order.append(word)
        word_count[word] += 1
    
    distinct_count = len(order)
    
    occurrences = [str(word_count[word]) for word in order]
    
    return distinct_count , occurrences
    
if __name__ =="__main__":
    n = int(input().strip())
    words = [input().strip() for _ in range(n)]
    distinct_count , occurrences = count_word_occurences(n , words)
    
    print(distinct_count)
    print(" ".join(occurrences))
    
    
    
