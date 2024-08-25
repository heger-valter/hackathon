#!/usr/bin/env python

import os
from nupic.swarming import permutations_runner 


from swarm_description import  SWARM_DESCRIPTION


def swarm(inputFile):
	swarmWorkDir()
	permutations_runner.runWithConfig(
		SWARM_DESCRIPTION,
		{"maxWorkers", 1, "overwrite", True},
		outputLable= "rec_center",
		outDir	
	)
	pass

if __name__ = "__main__":
	swarm(rec-center_hourly.csv")

