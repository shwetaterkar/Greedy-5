class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        sp=pp=0
        sstar=pstar=-1
        slen=len(s)
        plen=len(p)
        if(s==p):
            return True
        else:
            while (sp < slen):
                #print(" s[sp] is "+str(s[sp])+" ppp is "+str(p[pp]))
                if(pp < plen and (str(s[sp])== str(p[pp]) or p[pp] == '?')):
                    sp+=1
                    pp+=1
                    print("pp is "+str(pp))
                elif(pp < plen and p[pp] == '*'):
                    sstar = sp
                    pstar = pp
                    pp+=1
                elif(pstar == -1):
                    print("here "+str(pp))
                    return False
                else: #come back and match char to * till s[sp] = p[pp]
                    sstar+=1
                    sp=sstar
                    pp=pstar+1
                    
            while(pp<plen):
                if(p[pp]!='*'):
                    return False
                pp+=1
            return True
                
                
