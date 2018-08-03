# python code
# script_name: Dopamine_73608420
# author: Nicole Fronda
# description: Sonification of Heart Rate on Dopamine for Random Patient 73608420

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


dopaMax = [0, 20.0, 0, 20.0, 17.5, 10.0, 10.0, 12.5, 17.5, 17.5, 20.0, 20.0, 20.0, 20.0, 15.0, 15.0, 15.0, 15.0, 13.006799697875977, 13.0, 13.0, 13.0, 13.0, 10.0, 10.0, 9.0]

dopaMeans = [0, 20.0, 0, 20.0, 15.0, 10.0, 10.0, 11.88, 14.38, 17.5, 20.0, 20.0, 20.0, 18.33, 15.0, 15.0, 15.0, 13.8, 13.01, 10.4, 13.0, 13.0, 13.0, 10.0, 10.0, 8.0]

dopaOn = [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

dopaStds = [0, 0.0, 0, 0.0, 1.77, 0.0, 0.0, 1.08, 2.07, 0.0, 0.0, 0.0, 0.0, 1.18, 0.0, 0.0, 0.0, 0.98, 0.0, 5.2, 0.0, 0.0, 0.0, 0.0, 0.0, 0.93]

hrMeans = [181.33, 158.5, 179.5, 177.67, 176.67, 169.8, 162.0, 164.2, 167.5, 174.33, 186.0, 185.8, 180.57, 170.67, 169.6, 169.5, 162.6, 146.83, 155.89, 158.33, 157.86, 165.14, 167.43, 164.0, 167.44, 164.0]

hrStds = [5.76, 13.5, 2.96, 1.25, 2.05, 4.87, 1.87, 1.6, 0.87, 0.47, 3.74, 1.72, 2.87, 5.41, 0.8, 3.15, 3.88, 2.19, 2.18, 2.05, 1.64, 7.1, 1.76, 5.59, 6.17, 1.83]


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