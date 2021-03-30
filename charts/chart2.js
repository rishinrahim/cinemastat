var ctx = document.getElementById("chart2").getContext("2d");
          
var myChart = new Chart(ctx, {
    type: "bar",
    data: {

    "labels":[1928, 1933, 1938, 1940, 1941, 1948, 1949, 1950, 1951, 1952],

    "datasets":[{"backgroundColor": "#0d062b",
    			"data":[6, 8, 12, 7, 8, 7, 5, 7, 4, 4],
            	"lineTension":0.1}]

            },

    options:{ 	responsive: true,
			 	maintainAspectRatio: true,
    			legend: {display: false},
			  	scales: {

			  		yAxes: [{display: false}],
			  		xAxes: [{
			                
			                ticks: {
			                    fontColor: "#332d2d",
			                    fontSize: 9,
			                    stepSize: 1,
			                    beginAtZero: true,
			                	},

			                scaleLabel: {
						        display: true,
						        labelString: "Year",
						        fontColor: "#ffffff"
						      }
			           		}]
			        	}	
			   }
			 
			 
});
