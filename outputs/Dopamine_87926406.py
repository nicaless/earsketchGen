# python code
# script_name: Dopamine_87926406
# author: Nicole Fronda
# description: Sonification of Heart Rate on Dopamine for Random Patient 87926406

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


dopaMax = [0, 7.5, 7.5, 7.5, 10.0, 7.5, 7.5, 7.5, 15.0, 10.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 10.0, 7.5, 7.5, 7.5, 7.5, 5.0, 5.0, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 6.5, 6.0, 6.0, 6.0]

dopaMeans = [0, 5.63, 7.5, 7.5, 8.5, 7.5, 7.5, 7.5, 11.25, 9.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 10.67, 8.33, 7.5, 7.5, 7.5, 5.83, 5.0, 5.0, 7.0, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 6.88, 7.25, 6.38, 6.0, 6.0, 5.33]

dopaOn = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

dopaStds = [0, 1.08, 0.0, 0.0, 1.22, 0.0, 0.0, 0.0, 3.75, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.94, 1.18, 0.0, 0.0, 0.0, 1.18, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.08, 0.25, 0.22, 0.0, 0.0, 0.75]

hrMeans = [210.75, 189.75, 199.75, 197.2, 184.17, 193.4, 201.43, 198.14, 194.0, 180.0, 165.0, 183.5, 179.14, 178.43, 171.4, 168.83, 166.25, 154.2, 161.88, 162.4, 157.0, 154.5, 144.75, 137.17, 142.0, 150.0, 141.5, 133.38, 134.4, 134.71, 141.67, 137.0, 149.67, 145.4, 144.5, 167.6, 166.5, 155.8, 136.0, 137.2, 125.83, 131.33, 136.0, 137.17, 133.71, 133.43, 127.0, 143.17, 136.0, 121.71, 129.7, 125.83]

hrStds = [4.49, 6.1, 6.83, 2.79, 2.03, 4.84, 3.5, 5.36, 6.52, 9.2, 6.13, 2.69, 4.45, 2.72, 1.96, 5.15, 5.31, 5.31, 8.52, 12.78, 4.86, 6.34, 4.32, 3.02, 2.19, 2.16, 0.5, 3.04, 5.68, 6.58, 2.62, 8.29, 3.4, 7.23, 3.91, 10.86, 6.18, 7.96, 6.68, 9.13, 6.34, 2.75, 6.14, 2.41, 3.06, 7.5, 9.53, 10.93, 11.51, 6.04, 5.06, 2.54]


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