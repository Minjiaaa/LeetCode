class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # 假设dict不为null，假设beginword和endword是非空的
        # 必须加入end。可以加入start
        
        word_set = set(wordList)
        queue = deque([beginWord])
        visited = set([beginWord])
        
        distance = 0 # 注意是0不是1
        while queue:
            # 到当前层的长度
            distance += 1
            
            # 当前层有size个元素
            size = len(queue)
            # 分层遍历
            for i in range(size):
                word = queue.popleft()
                # 如果下一层的词为尾词，直接返回当前层的长度
                # 一旦找到一个就直接返回了
                if word == endWord:
                    return distance
                
                # 得到下一步的单词
                for next_word in self.get_next_words(word, word_set):
                    if next_word in visited:
                        continue
                
                    queue.append(next_word)
                    visited.add(next_word)
        return 0
    def get_next_words(self, word, dic):
        next_words = []
        for i in range(len(word)):
            left, right = word[:i], word[i + 1:]
            for char in "abcdefghijklmnopqrstuvwxyz":
                if word[i] == char:
                    continue
                # 在s中，把为止index的字母替换成c，返回替换后的字符串
                new_word = left + char + right
                # 如果字母替换后的单词存在于dict。加入next_words
                if new_word in dic:
                    next_words.append(new_word)
        return next_words