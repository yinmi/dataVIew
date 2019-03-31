from die import Die
import pygal

die=Die()

list1=[]
for roll_num in range(1000):
    result=die.roll()
    list1.append(result)
#统计筛子点数
resultCont=[]
for value in range(1,7):
    frequency=list1.count(value)
    resultCont.append(frequency)
#直方图绘制
hist=pygal.Bar()
hist.title="result out rolling one to 1000 times"
hist.x_labels=['1','2','3','4','5','6']
hist.x_title="result"
hist.y_title="frequency of result"

hist.add('D6',resultCont)
hist.render_to_file('fsk.svg')