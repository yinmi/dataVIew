from die import Die
import pygal

die_1=Die()
die_2=Die(10)

results=[]
for roll_num in range(50000):
    result=die_1.roll()+die_2.roll()
    results.append(result)

resultCount=list()
for value in range(2,17):
    ls=results.count(value)
    resultCount.append(ls)

hist=pygal.Bar()
hist.title="Result of rolling a D6 and a D10 50000 times"
hist.add('D6+D10',resultCount)   
hist.render_to_file('lk.svg')
