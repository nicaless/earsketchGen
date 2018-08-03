# python code
# script_name: Dopamine_51750752
# author: Nicole Fronda
# description: Sonification of Heart Rate on Dopamine for Random Patient 51750752

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


dopaMax = [0, 0, 0, 0, 0, 0, 0, 7.5, 7.5, 10.0, 7.5, 7.5, 5.0, 5.0, 5.0, 2.5229001045227051, 2.5229001045227051, 2.5229001045227051, 2.5229001045227051, 2.5229001045227051, 2.5229001045227051, 7.5, 7.5, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 8.0, 10.0, 12.5, 12.5, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 12.5, 10.0, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5114498138427734, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 5.0, 5.0, 10.0]

dopaMeans = [0, 0, 0, 0, 0, 0, 0, 7.5, 7.5, 8.33, 7.5, 7.5, 5.0, 5.0, 5.0, 2.52, 2.52, 2.52, 2.52, 2.52, 2.52, 6.25, 6.6, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 7.0, 10.0, 12.5, 12.5, 14.17, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 13.75, 15.0, 12.5, 10.0, 7.5, 7.5, 7.5, 7.5, 7.5, 6.0, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 6.5, 5.0, 5.0, 9.17]

dopaOn = [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

dopaStds = [0, 0, 0, 0, 0, 0, 0, 0.0, 0.0, 1.18, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.25, 0.73, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.18, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.25, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.22, 0.0, 0.0, 1.18]

hrMeans = [166.38, 162.33, 140.25, 121.67, 107.67, 120.2, 129.0, 127.8, 147.5, 137.5, 134.0, 142.0, 156.0, 154.33, 159.25, 157.0, 144.5, 140.13, 144.0, 147.67, 129.0, 131.33, 141.0, 142.5, 144.5, 144.67, 140.67, 134.0, 134.0, 136.83, 136.29, 137.0, 141.67, 144.75, 147.75, 137.17, 139.67, 142.57, 136.33, 127.0, 106.0, 102.67, 109.63, 120.8, 129.67, 135.4, 146.13, 149.29, 146.4, 143.17, 141.33, 140.8, 141.0, 142.5, 143.5, 137.0, 136.75, 132.5, 142.67, 137.5, 137.5, 133.0, 139.0, 135.0, 133.67, 127.0, 134.5, 140.8, 144.75, 139.2, 136.7, 133.5, 142.33, 147.25, 152.33, 148.57, 157.0, 140.75, 138.2, 144.71, 144.11, 143.0, 139.75, 140.5, 137.17, 139.17, 134.4, 124.29]

hrStds = [5.66, 4.19, 5.49, 5.93, 2.49, 12.8, 6.76, 12.22, 3.77, 10.87, 5.55, 8.83, 5.1, 1.89, 4.02, 2.16, 5.65, 5.53, 4.06, 3.77, 0.82, 1.7, 2.53, 2.6, 1.5, 1.25, 4.99, 0.82, 1.0, 3.53, 4.98, 3.51, 2.05, 0.83, 1.48, 1.67, 0.94, 1.4, 3.4, 2.62, 5.1, 1.25, 5.19, 3.82, 2.56, 3.85, 1.17, 2.31, 1.36, 1.21, 1.7, 1.72, 0.0, 0.5, 0.5, 3.0, 4.21, 2.06, 1.25, 1.5, 0.5, 1.41, 2.0, 0.0, 2.05, 2.0, 2.6, 2.79, 2.38, 3.06, 1.33, 5.41, 1.89, 0.43, 3.59, 5.39, 7.18, 1.48, 2.14, 2.12, 0.74, 0.82, 1.3, 1.5, 2.41, 2.34, 6.34, 8.15]


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
