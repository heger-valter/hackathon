SWARM_DESCRIPTION = {
  "includedFields": [
    {
      "fieldName": "timestamp", 
      "fieldType": "datetime"
    }, 
    {
      "fieldName": "consumption", 
      "fieldType": "float"
    }
  ], 
  "streamDef": {
    "info": "test", 
    "version": 1, 
    "streams": [
      {
        "info": "hotGym.csv", 
        "source": "file://rec-center_hourly.csv", 
        "columns": [
          "*"
        ] 
      }
    ] 
  }, 
  "inferenceType": "TemporalMultiStep", 
  "inferenceArgs": {
    "predictionSteps": [
      1
    ], 
    "predictedField": "consumption"
  }, 
  "iterationCount": -1, 
  "swarmSize": "small"
}

