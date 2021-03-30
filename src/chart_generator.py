from pychartjs import BaseChart, ChartType, Color                                     
import os 
import json

class MyBarGraph(BaseChart):

    type = ChartType.Bar
    
    class labels:
        grouped  = None
    
    class data:
        data = None
        backgroundColor = Color.Black
        
    class options: 

        responsive = True
        maintainAspectRatio = False
        legend = {
                'display': False, 
                'scales': {
                    'yAxes': [{"display": False}], 
                    'xAxes': [{
			                
			                "ticks": {
			                    "fontColor": Color.Hex("#332d2d"),
			                    "fontSize": 9,
			                    "stepSize": 1,
			                    "beginAtZero": True,
			                	},
                            "scaleLabel": {
						        "display": True,
						        "labelString": "Year",
						        "fontColor": Color.Hex("#ffffff")
						      }
                             }]
                   
                        }
                }
    
    def get_json(self,filename):
        with open(filename) as f:
            jsonfile = json.load(f)
        return jsonfile

    
    def write_js(self,chartId, json_filename):
        jsonfile = chart1.get_json(json_filename)
        self.data.data = jsonfile['data']
        self.labels.grouped = jsonfile['index'] 
        line1 = "var ctx = document.getElementById('"+chartId+"').getContext('2d');"
        line2 = "var myChart = new Chart(ctx,"+self.get()+");" 
        filename = os.path.join("charts",chartId+".js")
        file = open(filename, "w") 
        file.write(line1+line2) 
        file.close() 
        
if __name__=="__main__":
        chart1 = MyBarGraph()
        json_filename = os.path.join("charts","chart1.json")
        chart1.write_js("chart1",json_filename)

       
       
        