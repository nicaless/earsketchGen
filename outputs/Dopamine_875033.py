# python code
# script_name: Dopamine_875033
# author: Nicole Fronda
# description: Sonification of Heart Rate on Dopamine for Random Patient 875033

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


dopaMax = [0, 12.5, 10.0, 10.0, 15.0, 10.0, 10.0, 10.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 7.5, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0]

dopaMeans = [0, 12.5, 10.0, 10.0, 11.67, 10.0, 10.0, 8.33, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 6.25, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 3.33]

dopaOn = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

dopaStds = [0, 0.0, 0.0, 0.0, 2.36, 0.0, 0.0, 2.36, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.25, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.36]

hrMeans = [138.43, 136.8, 143.0, 141.25, 100.4, 83.33, 86.8, 84.33, 71.5, 84.33, 84.8, 72.0, 76.5, 75.57, 77.5, 78.0, 74.6, 73.4, 72.86, 80.13, 89.5, 100.8, 107.8, 115.8, 114.0, 112.5, 114.6, 109.0, 105.67, 106.86, 105.0, 104.0]

hrStds = [4.84, 4.71, 9.82, 13.2, 9.33, 6.13, 12.27, 3.68, 1.5, 9.1, 9.09, 1.63, 4.15, 5.39, 2.69, 6.0, 2.73, 7.2, 3.18, 5.06, 8.44, 6.18, 5.19, 6.14, 6.12, 1.5, 9.07, 1.0, 2.13, 6.45, 2.94, 4.29]


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