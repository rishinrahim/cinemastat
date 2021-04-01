var ctx = document.getElementById('chart4').getContext('2d');
var width = window.innerWidth || document.body.clientWidth;
var gradientStroke = ctx.createLinearGradient(0, 0, width, 0);
gradientStroke.addColorStop(0, "#FDC830");
gradientStroke.addColorStop(1, "#F37335");
			   // Bar chart
var myChart = new Chart(ctx, {
            type: 'horizontalBar',
            data: {
                labels: ['Sasikumar', 'IV Sasi', 'Joshiy', 'M Krishnan Nair', 'PG Vishwambharan', 'Sathyan Anthikkad', 'KS Sethumadhavan',
                 'P Chandrakumar', 'Hariharan', 'AB Raj', 'Sibi Malayil'],
                datasets:[{ backgroundColor : gradientStroke,        
                            data: [125, 100, 74, 67, 58, 56, 55, 51, 49, 47, 46]
                                        }]},
        
                options: {responsive: true,
                        maintainAspectRatio: false,
                        plugins: {
                            legend: false,
                            tooltip: true,
                            layout: {
                                padding: 24
                            }      
                    }
                        
                    
                }
            
				    

				    
				});