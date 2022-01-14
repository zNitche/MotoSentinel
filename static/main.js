function initSensorUpdate(sensorName)
{
    setInterval(updateSensorData, 1000, sensorName);
}

function updateSensorContainer(sensorData, sensorName)
{
    var elem;

    for (data in sensorData)
    {
        elem = getElementInsideContainerById(sensorName, data);

        elem.textContent = data + " : " + sensorData[data];
    }
}

function getElementInsideContainerById(containerId, elemId) {
    var elem = {};
    var containerElems = document.getElementById(containerId).getElementsByTagName("*");

    for (var i = 0; i < containerElems.length; i++)
    {
        if (containerElems[i].id === elemId)
        {
            elem = containerElems[i];
            break;
        }
    }
    return elem;
}

function updateSensorData(sensorName)
{
   fetch("api/sensors/" + sensorName)
  .then(response => response.json())
  .then(data => {
    updateSensorContainer(data, sensorName);
  }).catch(error => {
        console.error(error);
  });
}
