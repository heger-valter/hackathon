#!/usr/bin/env python
import csv
import sys
import os.path
#""" sys.path.append(os.path.join(os.path.dirname(__file__), '../nupic/src/nupic'))
from nupic.frameworks.opf.modelfactory import ModelFactory
from nupic_output import NuPICFileOutput, NuPICPlotOutput
from nupic.swarming import permutations_runner

import generate_data

# Change this to switch from a matplotlib plot to file output.
PLOT = False
SWARM_CONFIG = {
  "includedFields": [
    {
      "fieldName": "sine",
      "fieldType": "float",
      "maxValue": 1.0,
      "minValue": -1.0
    }
  ],
  "streamDef": {
    "info": "sine",
    "version": 1,
    "streams": [
      {
        "info": "sine.csv",
        "source": "file://sine.csv",
        "columns": [
          "*"
        ]
      }
    ]
  },
  "inferenceType": "TemporalAnomaly",
  "inferenceArgs": {
    "predictionSteps": [
      1
    ],
    "predictedField": "sine"
  },
  "swarmSize": "small"
}



def swarm_over_data():
  return permutations_runner.runWithConfig(SWARM_CONFIG,
    {'maxWorkers': 8, 'overwrite': True})



def run_sine_experiment():
  input_file = "sine.csv"
  generate_data.run(input_file)
  model_params = swarm_over_data()
  if PLOT:
    output = NuPICPlotOutput("sine_output", show_anomaly_score=True)
  else:
    output = NuPICFileOutput("sine_output", show_anomaly_score=True)
  model = ModelFactory.create(model_params)
  model.enableInference({"predictedField": "sine"})

  with open(input_file, "rb") as sine_input:
    csv_reader = csv.reader(sine_input)

    # skip header rows
    csv_reader.next()
    csv_reader.next()
    csv_reader.next()

    # the real data
    for row in csv_reader:
      angle = float(row[0])
      sine_value = float(row[1])
      result = model.run({"sine": sine_value})
      output.write(angle, sine_value, result, prediction_step=1)

  output.close()



if __name__ == "__main__":
  run_sine_experiment()
