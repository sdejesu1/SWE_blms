Music_Artists.json

Queries:

Get all


Normal one:
Get "artist name" if location == "United States"
Get songs if "artist name" == "Taylor swift"
Get "artist name" if genre == pop
Get genre if songs == "beat it"


Compound one:
Get "artist name" if location == "United States" && genre == rock
Get genre if location == "United States" && "end of career" == null

Redundant one:
Get "artist name" if location == Canada && "artist name" == drake


Extreme one:
Get all if location == Canada && "start of career" > 2000 && "end of career" == null && genre == "hip hop/rap"


Error handling:
Get "artist name" if "end of career" < 2000 && "start of career" < 2000 - firebase can’t handle multiple inequalities on multiple properties
get "artist name" if location == "united states" && "end of career" < 2000 - firebase needs extra indexes for strange queries


Help:
Help


Quit:
Quit
