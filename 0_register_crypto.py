st = "AMKNYLWAYRYJMEILCCKYGJ"
for i in range(1,26):
    ans=""
    for j in st.lower():
        ans = ans + chr(ord(j)+i)

    print (st+"\n"+ans+"\n\n")
