class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0
        read = 1
        count = 1

        while read <= len(chars) - 1:
            if chars[read] == chars[read - 1]:
                count += 1
                read +=1
            else:
                chars[write] = chars[read-1]
                if count > 1:
                    
                    cnt = str(count)
                    for letter in cnt:
                        write += 1
                        chars[write] = letter
                write += 1
                read += 1
                count = 1
        chars[write] = chars[read - 1]
        write += 1

        if count > 1:
            for letter in str(count):
                chars[write] = letter
                write += 1

        return write
    
                
                
            
        
            
