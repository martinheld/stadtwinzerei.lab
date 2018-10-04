// chart colors
var colors = ["#007bff", "#28a745", "#333333", "#c3e6cb", "#dc3545", "#6c757d"];

function updatePlots() {
  $.get("measurements", function(data, status) {
    label = data.map(val => {
      return val.created_at;
    });

    temperature = data.map((val, idx, arr) => {
      return val.temperature;
    });

    humidity = data.map((val, idx, arr) => {
      return val.humidity;
    });

    co2ppm = data.map((val, idx, arr) => {
      return val.co2ppm;
    });

    pressure = data.map((val, idx, arr) => {
      return val.pressure;
    });
    lastElem = label.length - 1
    $("#last").text(label[lastElem]);
    $("#curr_temp").text("Temperatur: "+Math.round(temperature[lastElem]*100)/100+" °C");
    $("#curr_co2").text("CO2: "+Math.round(co2ppm[lastElem]*100)/100+" ppm");
    $("#curr_hum").text("rel. Feuchtigkeit: "+Math.round(humidity[lastElem]*100)/100+" %");
    $("#curr_press").text(pressure[lastElem]);

    drawChart("temperature", label, temperature, 1);
    drawChart("humidity", label, humidity, 4);
    drawChart("ppm", label, co2ppm, 0);
    setTimeout(updatePlots, 30000);
  });
}

updatePlots();

function drawChart(id, labels, data, lineColor) {

  var number = document.getElementById('foo');
 
  var chLine = document.getElementById(id);
  var chartData = {
    labels: labels,
    datasets: [
      {
        data: data,
        backgroundColor: "transparent",
        borderColor: colors[lineColor],
        borderWidth: 2,
        pointBackgroundColor: colors[lineColor]
      }
    ]
  };

  if (chLine) {
    new Chart(chLine, {
      type: "line",
      data: chartData,
      options: {
        animation: false,
        scales: {
          yAxes: [
            {
              ticks: {
                beginAtZero: false
              }
            }
          ]
        },
        legend: {
          display: false
        }
      }
    });
  }
}
