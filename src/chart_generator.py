from pychartjs import BaseChart, ChartType, Color                                     

class MyBarGraph(BaseChart):

    type = ChartType.Bar

    class data:
        label = "Numbers"
        data = [12, 19, 3, 17, 10]
        backgroundColor = Color.Green
    
    def write_js(self,chartId):
        line1 = "var ctx = document.getElementById('"+chartId+"').getContext('2d');"
        line2 = "var myChart = new Chart(ctx,"+self.get()+");" 
        file = open("chart2.js", "w") 
        file.write(line1+line2) 
        file.close() 
        
if __name__=="__main__":
        NewChart = MyBarGraph()
        NewChart.data.label = "My Favourite Numbers" 
        NewChart.write_js("chart1")
