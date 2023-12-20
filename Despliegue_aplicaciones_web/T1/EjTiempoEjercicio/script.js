async function fetchDatosJSON() {
    const latitud = parseFloat(document.getElementById('latitud').value);
    const longitud = parseFloat(document.getElementById('longitud').value);
    const url = `https://api.open-meteo.com/v1/forecast?latitude=${latitud}&longitude=${longitud}&current_weather=true&hourly=temperature_2m,weathercode,precipitation_probability,rain`;
  
    try {
      const respuesta = await fetch(url);
  
      if (respuesta.ok) {
        const datosJSON = await respuesta.json();
        const codigoWeather = datosJSON.current_weather.weathercode;
  
        // Show current weather icon
        const iconoTiempo = document.getElementById('iconoTiempo');
        iconoTiempo.src = getWeatherIcon(codigoWeather, new Date().getHours);
  
        // Display current temperature
        document.getElementById('temperatura').textContent = datosJSON.current_weather.temperature;
  
        // Display max and min temperature for today
        const tempMax = Math.max(...datosJSON.hourly.temperature_2m);
        const tempMin = Math.min(...datosJSON.hourly.temperature_2m);
        document.getElementById('tempMax').textContent = `${tempMax}`;
        document.getElementById('tempMin').textContent = `${tempMin}`;
  
        const pronosticoHoras = datosJSON.hourly;
        const listaPronostico = document.getElementById('pronostico');
        listaPronostico.innerHTML = '';
        
        // Next 7 days
        for (let i = 0; i < pronosticoHoras.time.length; i += 3 ) {
            const hora = pronosticoHoras.time[i];
            const date = new Date(hora);
            const horaMostrar = date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
            const dia = date.toLocaleDateString([], { month: 'short', weekday: 'short', day: '2-digit' });
            const horaInt = parseInt(horaMostrar);
            const currentDateObject = new Date();
            const temp = pronosticoHoras.temperature_2m[i];
            const rainPro = pronosticoHoras.precipitation_probability[i]
            
            const card = document.createElement('tr');
            
            // Check if the date is today or tomorrow
            let dayLabel = dia;
            if (date.toDateString() === currentDateObject.toDateString()) {
              dayLabel = 'Today';
            } else {
              const tomorrow = new Date();
              tomorrow.setDate(currentDateObject.getDate() + 1);
              if (date.toDateString() === tomorrow.toDateString()) {
                dayLabel = 'Tomorrow';
              }
            }
            
            card.innerHTML = `
              <td>${dayLabel}</td>
              <td>${horaMostrar}</td>
              <td><img src="${getWeatherIcon(codigoWeather, horaInt)}" alt="Weather Icon">
              ${rainPro} %</td>
              <td>${temp}</td>`;
            listaPronostico.appendChild(card);
          }
          
      } else {
        console.error('Fallo al procesar el archivo JSON:', respuesta.statusText);
      }
    } catch (error) {
      console.error('Error en la conexión o en el mostrado de datos JSON:', error);
    }
  }
  
// Show Icons
function getWeatherIcon(weatherCode, hour) {
    let icon;

    if (hour == 23 || hour >=0 && hour < 7) {
        if (weatherCode >= 0 && weatherCode <= 10) {
            icon = 'sun-night';
        } else if (weatherCode >= 11 && weatherCode <= 30) {
            icon = 'cloud-night';
        } else if (weatherCode >= 30 && weatherCode <= 50) {
            icon = 'cloud-rain';
        } else if (weatherCode >= 50 && weatherCode <= 71) {
            icon = 'snow-night';
        } else if (weatherCode >= 71 && weatherCode <= 90) {
        } else {
            icon = 'sun-night';
        }
    } else {
        if (weatherCode >= 0 && weatherCode <= 10) {
            icon = 'sun';
        } else if (weatherCode >= 11 && weatherCode <= 30) {
            icon = 'cloud';
        } else if (weatherCode >= 30 && weatherCode <= 50) {
            icon = 'cloud-rain';
        } else if (weatherCode >= 50 && weatherCode <= 71) {
            icon = 'snow';
        } else if (weatherCode >= 71 && weatherCode <= 90) {
            icon = 'cloud-rain';
        } else {
            icon = 'sun';
        }
    }

    return `./assests/${icon}.png`;
}


