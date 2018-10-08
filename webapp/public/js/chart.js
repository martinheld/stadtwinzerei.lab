// chart colors
var colors = ["#5E8292", "#E7D792", "#D78898", "#c3e6cb", "#dc3545", "#6c757d"];

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

    drawChart("temperature", 'Temperatur', label, temperature, 0);
    drawChart("humidity", 'Feuchtigkeit', label, humidity, 1);
    drawChart("ppm", 'CO2 Ausstoß',label, co2ppm, 2);
    setTimeout(updatePlots, 30000);
  });
}

updatePlots();

function drawChart(id, title, labels, data, lineColor) {

  var chLine = document.getElementById(id);
  var chartData = {
    labels: labels,
    datasets: [
      {
        data: data,
        backgroundColor: colors[lineColor],
        borderColor: colors[lineColor],
        borderWidth: 1,
        pointRadius: 0,
        fill: 'start',
        pointBackgroundColor: colors[lineColor]
      }
    ]
  };

  if (chLine) {
    new Chart(chLine, {
      type: "line",
      data: chartData,
      options: {
        title: {
          display: true,
          text: title
        },
        animation: false,
        scales: {
          yAxes: [
            {
              scaleLabel: {
                display: true,
                labelString: id
              },
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
