class Solution:
    def reverseWords(self, s: str) -> str:

        return ' '.join(word[::-1] for word in s.split())
        '''
        s = s.split()
        lst = list()
        for i in s:
            #print('i', i)
            n = len(i)
            for j in range(n):
                #i[j], i[n-1-j] = i[n-1-j], i[j]
                lst.append(i[n-1-j])
            lst.append(" ")
        print(lst)
        a = lst.pop()
        print(lst)
        s = ''.join(lst)
        return s
        '''
