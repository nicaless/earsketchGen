# python code
# script_name: {{meta.script_name}}
# author: {{meta.author}}
# description: {{meta.description}}

from earsketch import *
from math import *

# ------- FUNCTIONS ------- #
{% for f in functions %}
{{ f }}
{% endfor %}

# ------- CUSTOM FUNCTIONS ------- #

{% for c in customFunctions %}
{{ c }}
{% endfor %}

# ------- DATA VARIABLES ------- #
# DATA RULES:
# - A SINGLE DATA POINT TO MAP TO SINGLE MEASURE
# - ALL DATA POINTS HAVE SAME LENGTH

{% for d in dataVars %}
{{ d }}
{% endfor %}

# ------- BEGIN EARSKETCH SCRIPT ------- #
# INITIALIZE
init()
tempo = {{ tempo }}
setTempo(tempo)

# SET BEATS
{% for b in beatStrings %}
{{ b }}
{% endfor %}

# SET SOUNDS
{% for s in soundFiles %}
{{ s }}
{% endfor %}

# MAKE BEATS
{% for b in beatTracks %}
{{ b }}
{% endfor %}

# FIT MEDIA

# SET EFFECTS
{% for e in effects %}
{{ e }}
{% endfor %}

# ADDITIONAL CUSTOM CODE

# ------- END EARSKETCH SCRIPT ------- #

finish()
