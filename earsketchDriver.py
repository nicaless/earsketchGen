import argparse
from earsketchFuncs import *
import inspect
from jinja2 import Environment, PackageLoader, FileSystemLoader
import yaml

p = argparse.ArgumentParser()
p.add_argument('cfg', default='./cfg.yaml', type=str)
args = vars(p.parse_args())

# read settings
with open(args['cfg'], 'r') as fin:
    settings = yaml.load(fin)

# turn args into strings for template
functionStrings = []
for f in settings['functions']:
    functionStrings.append(inspect.getsource(func_aliases[f]))

# will need custom func aliases ...
# need driver to import addtional file with custom funcs that has alias dict
customFunctionStrings = []
for c in settings['customFunctions']:
    functionStrings.append(inspect.getsource(c))

dataStrings = []
for var, vals in settings['data'].items():
    dataStrings.append(var + " = " + str(vals))

def constructStringFromDict(d, root=True):
    if type(d) == str or type(d) == int:
        return str(d)
    if root:
        if len(d) != 1 or type(d) != dict:
            return None
    if type(d) == list:
        outString = ''
        for i in d:
            if type(i) == dict:
                nextString = constructStringFromDict(i, root=False)
            else:
                nextString = str(i)
            outString = outString + nextString + ","
        outString = outString[0:len(outString)-1]
    if type(d) == dict:
        for k, v in d.items():
            outString = str(k) + '(' + constructStringFromDict(v, root=False) + ')'

    return outString

tempo = settings['tempo']
defaultTempo = settings['defaultTempo']

if type(tempo) == int:
    tempoString = str(tempo)
elif type(tempo) == str:
    tempoString = tempo
elif type(tempo) == dict:
    tempoString = constructStringFromDict(tempo)
    if tempoString == None:
        tempoString = defaultTempo
else:
    tempoString = defaultTempo

beatStringsList = []
for var, beatString in settings['beatStrings'].items():
    beatStringsList.append(var + " = \'" + beatString + "\'")

soundFiles = []
for var, file in settings['sounds'].items():
    soundFiles.append(var + " = " + file)

beatTracks = []
for i in settings['buildBeatTracks']:
    beatTrackString = 'buildBeatTrack(' + i['sounds'] + ',' + str(i['track']) + ',' + \
    str(i['start']) + ',' +  str(i['duration']) + ',' + i['beat'] + ', measures=' + \
    str(i['measures']) + ")"
    beatTracks.append(beatTrackString)

effectStrings = []
for i in settings['effects']:
    func = i['func']
    if func == 'createEffectWithVals':
        effectType = str(i['effectType'])
        effectParam = str(i['effectParam'])
        effectThresh = str(i['effectThresh'])
        vals = str(i['vals'])
        track = str(i['track'])
        effectString = func + "(" + effectType + "," + effectParam + "," + \
        effectThresh + "," + vals + "," + track + ")"
    elif func == 'createEffectWithGauss':
        effectType = str(i['effectType'])
        effectParam = str(i['effectParam'])
        effectMin = str(i['effectMin'])
        effectMax = str(i['effectMax'])
        means = str(i['means'])
        st_devs = str(i['st_devs'])
        track = str(i['track'])
        effectString = func + "(" + effectType + "," + effectParam + "," + \
        effectMin + "," + effectMax + "," + means + "," + st_devs + ',' + track + ")"
    else:
        vals = [i['track'], i['effectType'], i['effectParam'], i['effectStartValue'],
        i['effectStartLocation'],i['effectEndValue'],i['effectEndLocation']]
        effectString = "setEffect("
        for v in vals:
            if v == 'None':
                continue
            effectString = effectString + str(v) + ","
        effectString = effectString[0:len(effectString)-1] + ")"
    effectStrings.append(effectString)

# Open Template and Write
templateLoader = FileSystemLoader(searchpath="./templates")
env = Environment(loader=templateLoader)
template = env.get_template(settings['template'])

with open(settings['filename'], "w") as f:
    code = template.render(meta=settings['meta'], functions=functionStrings, dataVars=dataStrings,
    tempo=tempoString, beatStrings=beatStringsList, soundFiles=soundFiles,
    beatTracks=beatTracks, effects=effectStrings)
    f.write(code)
