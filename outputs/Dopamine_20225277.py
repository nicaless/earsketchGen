# python code
# script_name: Dopamine_20225277
# author: Nicole Fronda
# description: Sonification of Heart Rate on Dopamine for Random Patient 20225277

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


dopaMax = [10.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 17.5, 17.5, 17.5, 17.5, 17.5, 17.5, 17.5, 17.5, 17.5, 17.5, 0, 17.5, 17.5, 17.5, 17.5, 17.5, 17.5, 17.5, 17.5, 17.5, 17.5, 17.5, 17.5, 17.5, 17.5, 17.5, 15.0, 15.0, 15.0, 15.0, 12.5, 12.5, 12.5, 10.0, 7.5, 7.5, 5.0, 5.0, 5.0, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 5.0, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 5.0, 5.0, 5.0, 2.5, 2.5]

dopaMeans = [10.0, 17.5, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 17.5, 17.5, 17.5, 17.5, 17.5, 17.5, 17.5, 17.5, 17.5, 17.5, 0, 17.5, 17.5, 17.5, 17.5, 17.5, 17.5, 17.5, 17.5, 17.5, 17.5, 17.5, 17.5, 17.5, 17.5, 15.63, 15.0, 15.0, 15.0, 13.0, 12.5, 12.5, 10.83, 8.75, 7.5, 6.25, 5.0, 3.75, 5.0, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 5.63, 5.0, 5.83, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 6.25, 5.0, 5.0, 3.33, 2.5, 1.25]

dopaOn = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

dopaStds = [0.0, 2.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.08, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.18, 1.25, 0.0, 1.25, 0.0, 1.25, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.08, 0.0, 1.18, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.25, 0.0, 0.0, 1.18, 0.0, 1.25]

hrMeans = [115.88, 117.14, 123.75, 133.33, 132.0, 145.33, 138.4, 145.0, 134.6, 129.0, 126.0, 125.0, 117.5, 124.5, 120.5, 111.0, 117.0, 113.14, 113.0, 122.2, 143.14, 127.2, 121.0, 116.4, 111.0, 113.0, 112.33, 115.33, 116.0, 112.67, 108.0, 107.67, 113.57, 107.8, 112.0, 110.0, 110.5, 112.0, 104.75, 111.0, 107.33, 100.4, 102.33, 101.75, 91.33, 98.67, 92.17, 87.0, 86.0, 91.0, 76.0, 79.2, 89.0, 71.4, 67.67, 76.71, 78.5, 81.0, 83.5, 69.0, 62.29, 68.0, 70.67, 70.5, 70.0, 64.2, 70.0, 73.75, 71.0, 62.2, 55.67, 66.33, 78.75, 61.8, 56.0, 53.67, 60.2, 75.0, 84.33, 69.0, 83.0, 77.0, 83.0, 87.2, 76.0, 75.8]

hrStds = [4.17, 6.2, 6.61, 7.54, 8.37, 0.47, 4.84, 2.83, 1.96, 1.63, 1.87, 0.0, 1.5, 1.5, 2.5, 1.0, 2.28, 6.69, 3.0, 3.31, 39.48, 2.48, 2.45, 5.92, 2.0, 1.0, 0.47, 1.25, 1.0, 1.7, 0.0, 0.47, 4.5, 1.17, 1.87, 2.16, 1.66, 2.16, 1.3, 2.1, 4.5, 3.88, 4.64, 13.16, 2.87, 2.87, 5.34, 3.35, 5.51, 7.07, 8.85, 4.53, 12.9, 10.37, 1.7, 11.97, 7.09, 7.68, 14.2, 1.91, 1.58, 4.08, 9.43, 1.5, 2.16, 7.0, 10.17, 3.63, 1.41, 4.92, 3.09, 2.05, 4.92, 5.15, 2.55, 0.47, 5.38, 18.48, 14.82, 7.87, 5.0, 10.0, 7.07, 19.12, 11.7, 2.48]


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
