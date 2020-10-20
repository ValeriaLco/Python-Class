# apples_and_oranges.py
# Valeria Lucio Rangel
# A01411381

s_t_hhu = (list(map(int, input().split())))
s = s_t_hhu[0] 
t = s_t_hhu[1]
hhu = s_t_hhu[2]
a_b= (list(map(int, input().split())))
a = a_b[0]
b = a_b[1]
m_n = (list(map(int, input().split())))
m = m_n[0]
n = m_n[1]
scndapp = (list(map(int, input().split())))
scndoran = (list(map(int, input().split())))

def count_apples_and_oranges(s, t, hhu, a, b, app, oran,m,n):
    first_addition = [] 
    scnd_addition= [] 
    for i in range(len(app)):
        op = a + app[i]
        first_addition.append(op)
    for i in range(len(oran)):
        op=  b + oran[i]
        scnd_addition.append(op)
    app = 0
    oran = 0
    for i in first_addition:
        if i <= hhu + s:
            app += 2
    for i in scnd_addition:
        if i <= hhu + t:
            oran += 1
    print(app)
    print(oran)

count_apples_and_oranges(s, t, hhu, a, b, scndoran, scndapp, m, n)