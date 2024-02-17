from typing import List
from typing import Optional
import time
import math
import numpy
from collections import Counter
class Solution:
    def printMatrix(self, matrix):
        max_width = len(str(max(max(row) for row in matrix)))

        for row in matrix:
            for num in row:
                print(f"{num:>{max_width}}", end=" ")
            print()
        return 
    
    def binary_search_insert_index(self, lst, element, weights):
        left, right = 0, len(lst)
        while left < right:
            mid = (left + right) // 2
            # Compare weights instead of elements directly
            if weights[lst[mid]] < weights[element]:
                left = mid + 1
            else:
                right = mid
        return left

    def insert_element_sorted_by_weight(self, lst, element, weights):
        index = self.binary_search_insert_index(lst, element, weights)
        lst.insert(index, element)

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        dic = {}
        if (endWord not in wordList):
            return []
        
        if beginWord in wordList:    
            wordList.remove(beginWord)
       # wordList.sort()
        wordList = [beginWord] + wordList
        m = [[] for _ in wordList]
        for i in range(len(wordList)):
            keys = set()
            for c in range(len(wordList[i])):
                key = wordList[i][:c]+"0"+wordList[i][c+1:]
                if key in keys:
                    continue
                keys.add(key)
                if (key not in dic):
                    dic[key] = []
                else:
                    for j in dic[key]:
                        m[i].append(j)
                        m[j].append(i)
                dic[key].append(i)
        visited = set() 
        queue = [0]
        weight = [0 for _ in wordList]
        parent = [[] for _ in wordList]
        endindex = wordList.index(endWord)
        parent[0] = [-1]
  #      print(m)
        while queue:
            v = queue[0]
            queue.remove(v)
            if v in visited:
                continue
            visited.add(v)
            
            for next in m[v]:
                if next not in visited:
                    queue.append(next)
                    if weight[next] == 0 or weight[next] > weight[v] + 1:
                        weight[next] = weight[v] + 1
                        parent[next] = [v]
                    elif weight[next] == weight[v] + 1:
                        parent[next] += [v]
                    #if next == endindex:
                    #    queue.clear()
                    #    break
 #       print(weight)
        #print(parent) 
        #self.printMatrix(m)
        level = weight[endindex] + 1 if weight[endindex] > 0 else 0
        #print(level)
        if (level == 0):
            return []
        result = []
        self.find_paths(result, [], parent, endindex, wordList)
        return result

    def find_paths(self, paths: List[List[str]], path: List[str],
               parent: List[List[int]], u: int, wordList: List[str]) -> None:
        if (u == -1):
            paths.append(list(reversed(path.copy())))
            return
 
        for par in parent[u]:
            path.append(wordList[u])
            self.find_paths(paths, path, parent, par, wordList)
            path.pop()
    
    def findLadders2(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        dic = {}
        if (endWord not in wordList):
            return []
        
        if beginWord in wordList:    
            wordList.remove(beginWord)
        wordList.sort()
        wordList = [beginWord] + wordList
        m = [[] for _ in wordList]
        for i in range(len(wordList)):
            keys = set()
            for c in range(len(wordList[i])):
                key = wordList[i][:c]+"0"+wordList[i][c+1:]
                if key in keys:
                    continue
                keys.add(key)
                if (key not in dic):
                    dic[key] = []
                else:
                    for j in dic[key]:
                        m[i].append(j)
                        m[j].append(i)
                dic[key].append(i)
        visited = set() 
        queue = [wordList.index(endWord)]
        weight = [0 for _ in wordList]
        while queue:
            v = queue[0]
            visited.add(v)
            queue.remove(v)
            for next in m[v]:
                if next not in visited:
                    self.insert_element_sorted_by_weight(queue, next, weight)
                    weight[next] = weight[v] + 1
                    if next == 0:
                        queue.clear()
                        break
        
        #print(weight)
        #self.printMatrix(m)
        level = weight[0] + 1 if weight[0] > 0 else 0
        print(level)
        if (level == 0):
            return []
        visit = [0 for _ in wordList]
        visit[0] = 1        
        return self.findLadderRec(m, visit, level, 0, wordList.index(endWord), wordList, weight)
    
    def findLadderRec(self, matrix, visited, level, startindex, endindex, wordList, weight) -> List[List[str]]:
        if (level == 1):
            return [[wordList[endindex]]] if startindex == endindex else [] 
        if (level < weight[startindex]):
            return [] 
        result = []
        for next in matrix[startindex]:
            if not(visited[next]) and weight[next] < level:
                visited[next] = 1
                prev = self.findLadderRec(matrix, visited, level-1, next, endindex, wordList, weight)
                if (prev):
                    result += [[wordList[startindex]] + subpath 
                            for subpath in 
                            prev] 
                visited[next] = 0
        return result
                    
start_time = time.time()
app = Solution()

#root = app.findLadders("hit", "cog", ["hot","dot","dog","lot","log","cog"])
root = app.findLadders("aaaaa", "ggggg", ["aaaaa","caaaa","cbaaa","daaaa","dbaaa","eaaaa","ebaaa","faaaa","fbaaa","gaaaa","gbaaa","haaaa","hbaaa","iaaaa","ibaaa","jaaaa","jbaaa","kaaaa","kbaaa","laaaa","lbaaa","maaaa","mbaaa","naaaa","nbaaa","oaaaa","obaaa","paaaa","pbaaa","bbaaa","bbcaa","bbcba","bbdaa","bbdba","bbeaa","bbeba","bbfaa","bbfba","bbgaa","bbgba","bbhaa","bbhba","bbiaa","bbiba","bbjaa","bbjba","bbkaa","bbkba","bblaa","bblba","bbmaa","bbmba","bbnaa","bbnba","bboaa","bboba","bbpaa","bbpba","bbbba","abbba","acbba","dbbba","dcbba","ebbba","ecbba","fbbba","fcbba","gbbba","gcbba","hbbba","hcbba","ibbba","icbba","jbbba","jcbba","kbbba","kcbba","lbbba","lcbba","mbbba","mcbba","nbbba","ncbba","obbba","ocbba","pbbba","pcbba","ccbba","ccaba","ccaca","ccdba","ccdca","cceba","cceca","ccfba","ccfca","ccgba","ccgca","cchba","cchca","cciba","ccica","ccjba","ccjca","cckba","cckca","cclba","cclca","ccmba","ccmca","ccnba","ccnca","ccoba","ccoca","ccpba","ccpca","cccca","accca","adcca","bccca","bdcca","eccca","edcca","fccca","fdcca","gccca","gdcca","hccca","hdcca","iccca","idcca","jccca","jdcca","kccca","kdcca","lccca","ldcca","mccca","mdcca","nccca","ndcca","occca","odcca","pccca","pdcca","ddcca","ddaca","ddada","ddbca","ddbda","ddeca","ddeda","ddfca","ddfda","ddgca","ddgda","ddhca","ddhda","ddica","ddida","ddjca","ddjda","ddkca","ddkda","ddlca","ddlda","ddmca","ddmda","ddnca","ddnda","ddoca","ddoda","ddpca","ddpda","dddda","addda","aedda","bddda","bedda","cddda","cedda","fddda","fedda","gddda","gedda","hddda","hedda","iddda","iedda","jddda","jedda","kddda","kedda","lddda","ledda","mddda","medda","nddda","nedda","oddda","oedda","pddda","pedda","eedda","eeada","eeaea","eebda","eebea","eecda","eecea","eefda","eefea","eegda","eegea","eehda","eehea","eeida","eeiea","eejda","eejea","eekda","eekea","eelda","eelea","eemda","eemea","eenda","eenea","eeoda","eeoea","eepda","eepea","eeeea","ggggg","agggg","ahggg","bgggg","bhggg","cgggg","chggg","dgggg","dhggg","egggg","ehggg","fgggg","fhggg","igggg","ihggg","jgggg","jhggg","kgggg","khggg","lgggg","lhggg","mgggg","mhggg","ngggg","nhggg","ogggg","ohggg","pgggg","phggg","hhggg","hhagg","hhahg","hhbgg","hhbhg","hhcgg","hhchg","hhdgg","hhdhg","hhegg","hhehg","hhfgg","hhfhg","hhigg","hhihg","hhjgg","hhjhg","hhkgg","hhkhg","hhlgg","hhlhg","hhmgg","hhmhg","hhngg","hhnhg","hhogg","hhohg","hhpgg","hhphg","hhhhg","ahhhg","aihhg","bhhhg","bihhg","chhhg","cihhg","dhhhg","dihhg","ehhhg","eihhg","fhhhg","fihhg","ghhhg","gihhg","jhhhg","jihhg","khhhg","kihhg","lhhhg","lihhg","mhhhg","mihhg","nhhhg","nihhg","ohhhg","oihhg","phhhg","pihhg","iihhg","iiahg","iiaig","iibhg","iibig","iichg","iicig","iidhg","iidig","iiehg","iieig","iifhg","iifig","iighg","iigig","iijhg","iijig","iikhg","iikig","iilhg","iilig","iimhg","iimig","iinhg","iinig","iiohg","iioig","iiphg","iipig","iiiig","aiiig","ajiig","biiig","bjiig","ciiig","cjiig","diiig","djiig","eiiig","ejiig","fiiig","fjiig","giiig","gjiig","hiiig","hjiig","kiiig","kjiig","liiig","ljiig","miiig","mjiig","niiig","njiig","oiiig","ojiig","piiig","pjiig","jjiig","jjaig","jjajg","jjbig","jjbjg","jjcig","jjcjg","jjdig","jjdjg","jjeig","jjejg","jjfig","jjfjg","jjgig","jjgjg","jjhig","jjhjg","jjkig","jjkjg","jjlig","jjljg","jjmig","jjmjg","jjnig","jjnjg","jjoig","jjojg","jjpig","jjpjg","jjjjg","ajjjg","akjjg","bjjjg","bkjjg","cjjjg","ckjjg","djjjg","dkjjg","ejjjg","ekjjg","fjjjg","fkjjg","gjjjg","gkjjg","hjjjg","hkjjg","ijjjg","ikjjg","ljjjg","lkjjg","mjjjg","mkjjg","njjjg","nkjjg","ojjjg","okjjg","pjjjg","pkjjg","kkjjg","kkajg","kkakg","kkbjg","kkbkg","kkcjg","kkckg","kkdjg","kkdkg","kkejg","kkekg","kkfjg","kkfkg","kkgjg","kkgkg","kkhjg","kkhkg","kkijg","kkikg","kkljg","kklkg","kkmjg","kkmkg","kknjg","kknkg","kkojg","kkokg","kkpjg","kkpkg","kkkkg","ggggx","gggxx","ggxxx","gxxxx","xxxxx","xxxxy","xxxyy","xxyyy","xyyyy","yyyyy","yyyyw","yyyww","yywww","ywwww","wwwww","wwvww","wvvww","vvvww","vvvwz","avvwz","aavwz","aaawz","aaaaz"])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
