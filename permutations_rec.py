'''
suppose, we are given a string--> abc, bc,c
output--> abc acb bac bca cab cba
bc cb
c
INTUITION::
IMAGINE THREE SHAPES, LIKE CIRCLE, TRIANGLE, AND A RECTANGLE AND WE HAVE TO ARRANGE THEM IN ALL POSSIBLE WAYS. SUPPOSE,
WE HAVE THREE SPOTS FOR ALL OF THEM AND WE HAVE TO PUT ALL OF THEM AT EVERY POSSIBLE PLACE.
AS WE ARE USING RECURSION, WE WILL TRY TO DO THE LEAST WORK AND THUS, HANDLE THE FIRST PLACE AND ASK RECURSION TO HANDLE THE FIRST+1 TILL THE LAST PLACE.

--> SO, WE HAVE TO SWAP EACH ELEMENT SO THEY COULD APPEAR ON THE FIRST PLACE.
--> WE ALSO HAVE TO SWAP THEM AGAIN AFTER PERFORMING RECURSION (BACKTREKKING) DO REVERSE THE CHANGES THAT WE HAVE DONE FOR THE EASE OF WORK.
'''
def swap(i,j,s):
        arr=list(s) # as strings are immutable in python, so we are converting them into list...
        arr[i],arr[j]=arr[j],arr[i]
        # converting to string again
        s=""
        for i in arr:
            s+=i
        return s
        
    def helper(pos,str,ans,n): #make sure to don't change the order of the arguments passed...
        if pos>=len(str):
            ans.append(str[:])
            return    
        for i in range(pos,len(str)):
            str=swap(pos,i,str)
            # asking recursion to do the next task
            helper(pos+1,str,ans,n)
            # swap again by backtrekking as we have to handle the mess
            str=swap(pos,i,str)
    ans=[]
    n=len(str)
    helper(0,str,ans,n)
    return sorted(ans) # only if we has to return the ans in sorted form...
