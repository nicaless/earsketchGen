# python code
# script_name: Dopamine_10374026
# author: Nicole Fronda
# description: Sonification of Heart Rate on Dopamine for Random Patient 10374026

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


dopaMax = [20.0, 20.0, 20.0, 20.0, 19.0, 17.5, 10.0, 0, 0, 0, 0, 10.0, 10.0, 10.0]

dopaMeans = [17.5, 20.0, 20.0, 19.5, 19.0, 17.08, 6.67, 0, 0, 0, 0, 10.0, 10.0, 10.0]

dopaOn = [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1]

dopaStds = [2.5, 0.0, 0.0, 0.5, 0.0, 0.93, 4.71, 0, 0, 0, 0, 0.0, 0.0, 0.0]

hrMeans = [196.2, 198.67, 203.5, 194.17, 180.0, 158.4, 150.0, 148.75, 149.0, 175.25, 160.0, 164.5, 180.75, 174.8]

hrStds = [8.98, 8.79, 4.03, 3.93, 12.0, 16.48, 2.94, 3.96, 3.0, 8.35, 3.81, 6.18, 2.95, 4.79]


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