# python code
# script_name: Dopamine_33772272
# author: Nicole Fronda
# description: Sonification of Heart Rate on Dopamine for Random Patient 33772272

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


dopaMax = [0, 0, 0, 0, 0, 0, 0, 0, 15.0, 10.0, 10.0, 7.5, 7.5, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 7.5, 6.0, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 12.5, 7.5, 7.5, 12.5, 12.5, 12.5, 10.0]

dopaMeans = [0, 0, 0, 0, 0, 0, 0, 0, 15.0, 10.0, 8.75, 7.5, 7.5, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 6.25, 6.0, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 11.67, 7.5, 7.5, 12.5, 12.5, 11.25, 8.75]

dopaOn = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

dopaStds = [0, 0, 0, 0, 0, 0, 0, 0, 0.0, 0.0, 1.25, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.25, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.18, 0.0, 0.0, 0.0, 0.0, 1.25, 1.25]

hrMeans = [140.0, 136.0, 173.63, 188.88, 176.86, 156.11, 176.57, 165.5, 176.5, 165.5, 164.33, 164.6, 160.67, 157.0, 162.14, 177.5, 161.33, 163.25, 159.8, 169.5, 167.8, 177.0, 182.5, 181.6, 175.75, 170.0, 171.0, 182.5, 190.67, 199.6, 184.71, 183.0, 180.43, 178.6]

hrStds = [12.86, 2.92, 19.86, 4.43, 11.98, 2.92, 11.03, 0.5, 2.96, 4.15, 9.88, 14.46, 7.97, 5.71, 6.08, 14.73, 10.66, 1.3, 4.35, 11.28, 5.88, 12.81, 5.5, 7.0, 6.94, 4.0, 0.0, 12.5, 6.32, 9.35, 6.16, 6.09, 5.23, 8.82]


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