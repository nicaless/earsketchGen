# python code
# script_name: Dopamine_99903292
# author: Nicole Fronda
# description: Sonification of Heart Rate on Dopamine for Random Patient 99903292

from earsketch import *
from math import *

# ------- FUNCTIONS ------- #

def getMean(ls):
  return sum(ls) / len(ls)


def buildBeatTrack(sounds, track, start, duration, beat, measures=None):
    # Specify what measures to play beat on (play if measure is 1)
    # else make beats between start and duration
    if measures is not None:
        for m in range(len(measures)):
            if measures[m] > 0:
                makeBeat(sounds, track, m+1, beat)
    else:
        for i in range(start, duration):
            makeBeat(sounds, track, i, beat)


def createEffectWithVals(effect, effectParam, effectThresh, vals, track):
  for i in range(len(vals)):
    # if val present
    v = vals[i]
    if v > 0:
      x = v / max(vals)
      distEffect = floor(x * effectThresh)
      setEffect(track, effect, effectParam, 0, i+1, distEffect, i+1+0.5)
      setEffect(track, effect, effectParam, distEffect, i+1+0.5, 0, i+2)


def createEffectWithGauss(effect, effectParam, effectMin, effectMax, means, st_devs, track):
  for i in range(len(means)):
    mean = means[i]
    st_dev = st_devs[i]
    if mean > 0:
      x = gauss(mean, st_dev)
      if effectMin == 0:
        distEffect = floor((abs(x - mean) / mean) * effectMax)
      else:
        distEffect = floor(((x - mean) / mean) * max(abs(effectMax), abs(effectMin)))

      if distEffect < effectMin:
        distEffect = effectMin
      if distEffect > effectMax:
        distEffect = effectMax

      setEffect(track, effect, effectParam, 0, i+1, distEffect, i+1+0.5)
      setEffect(track, effect, effectParam, distEffect, i+1+0.5, 0, i+2)



# ------- CUSTOM FUNCTIONS ------- #



# ------- DATA VARIABLES ------- #
# DATA RULES:
# - A SINGLE DATA POINT TO MAP TO SINGLE MEASURE
# - ALL DATA POINTS HAVE SAME LENGTH


dopaMax = [0, 0, 2.5, 2.5, 0, 0, 0, 12.5, 12.5, 12.5, 10.0, 8.0, 5.0, 5.0, 5.0, 2.5, 2.5]

dopaMeans = [0, 0, 1.25, 1.25, 0, 0, 0, 11.88, 10.63, 12.0, 10.0, 6.5, 5.0, 5.0, 3.75, 2.5, 2.5]

dopaOn = [0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

dopaStds = [0, 0, 1.25, 1.25, 0, 0, 0, 1.08, 1.08, 1.0, 0.0, 1.12, 0.0, 0.0, 1.25, 0.0, 0.0]

hrMeans = [172.83, 181.25, 152.86, 161.6, 160.0, 164.67, 168.29, 153.8, 157.4, 139.17, 133.33, 137.75, 120.0, 118.0, 108.71, 100.4, 113.0]

hrStds = [7.2, 3.53, 12.69, 2.15, 0.0, 5.79, 9.41, 5.04, 10.93, 9.69, 21.25, 12.32, 20.0, 22.79, 16.67, 8.52, 8.75]


# ------- BEGIN EARSKETCH SCRIPT ------- #
# INITIALIZE
init()
tempo = round(getMean(hrMeans),0)
setTempo(tempo)

# SET BEATS

dopaBeat = '0+++0+0+0+++0+0+'

hrBeat = '0+++0+++0+++0+++'


# SET SOUNDS

dopaSound = HOUSE_DEEP_CRYSTALCHORD_001

hrSound = OS_LOWTOM03


# MAKE BEATS

buildBeatTrack(dopaSound,2,' ',' ',dopaBeat, measures=dopaOn)

buildBeatTrack(hrSound,1,1,len(hrMeans)+1,hrBeat, measures=None)


# FIT MEDIA

# SET EFFECTS

setEffect(2,VOLUME,GAIN,-12)

createEffectWithVals(DISTORTION,DISTO_GAIN,35,dopaMax,2)

createEffectWithGauss(PITCHSHIFT,PITCHSHIFT_SHIFT,-12,12,dopaMeans,dopaStds,2)

createEffectWithGauss(PITCHSHIFT,PITCHSHIFT_SHIFT,-12,12,hrMeans,hrStds,1)


# ADDITIONAL CUSTOM CODE

# ------- END EARSKETCH SCRIPT ------- #

finish()
