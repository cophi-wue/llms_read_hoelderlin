class Text:
   
    def __init__(self, author, title, year):
        self.author = author
        self.title = title
        self.year = year
        self.translations = []

    def set_text(self, text):
        self.text = text
        
    def set_source(self, source):
        self.source = source

    def add_translations(self, list_of_texts):
        self.translations += list_of_texts


poem_text_1 = """
Mit gelben Birnen hänget
Und voll mit wilden Rosen
Das Land in den See,
Ihr holden Schwäne,
Und trunken von Küssen
Tunkt ihr das Haupt
Ins heilignüchterne Wasser.

Weh mir, wo nehm’ ich, wenn
Es Winter ist, die Blumen, und wo
Den Sonnenschein,
Und Schatten der Erde?
Die Mauern stehn
Sprachlos und kalt, im Winde
Klirren die Fahnen. 
"""

#two text correction: nächstens->nächtens. Schlürfen->Schlurfen
poem_text_2 = """
Von Westen und Osten, von Nord und Süd
Schleppen sich nächtens viele Füße müd,
Füße, vom Wandern wund und zerfetzt,
Langsam bedächtig zur Erde gesetzt,
Müh'n sich im zitternden Mondenschein
Rastlos tief nach Deutschland hinein.
Und wer mit lauschendem Ohr noch wacht
Hört sie in jedweder werdenden Nacht,
Hört dies Schlurfen so müde und schwer,
Hört eine Klage voll wilder Begehr,
Eine Klage schmerzzerfressen:
Nur nicht vergessen! Uns nicht vergessen!
"""

#Half of Life. tr. by John Irons. Source: http://johnirons.blogspot.com/2019/07/holderlin-halfte-des-lebens-revised.html
ta1 = """
With yellow pears hangs –
And full of wild roses –
Land hangs into the lake,
O lovely swans,
And drunk with kisses
You dip your heads
Into the sacred-sober water.

Alas, where shall I find,
When winter comes, flowers, and where
The sunlight,
And the shadows of Earth?
The walls stand
Speechless and cold; in the wind
Weathervanes clatter. 
"""

#The middle of life. tr. by Emily Ezust source: https://www.lieder.net/lieder/get_text.html?TextId=8101
ta2 = """
With yellow pears
and full of wild roses,
the land hangs over the lake,
you fair swans,
and drunk with kisses
you dunk your heads
into the sacred, sober water.

Woe is me! where, when 
it is winter, will I get flowers, 
and where the sunshine,
and the shade of the earth?
The walls stand
mute and cold; in the wind
the weathervanes rattle.
"""

#Half of Life tr. James Mitchell Source: https://holderlinpoems.com/poems/half_of_life.html
ta3 = """
The earth hangs down
to the lake, full of yellow
pears and wild roses.
Lovely swans, drunk with
kisses you dip your heads
into the holy, sobering waters.

But when winter comes,
where will I find
the flowers, the sunshine,
the shadows of the earth?
The walls stand
speechless and cold.
The weathervanes
rattle in the wind.
"""

#Halves of Live. Tr. by Kate Flores. in: Angel Flores (ed.): An Anthology of German Poetry from Hölderlin to Rilke in English Translation. Gloucester, Mass.: Peter Smith 1965, S. 26f. 
ta4 = """
The earth with yellow pears
And overgrown with roses wild
Upon the pond is bent,
And swans divine,
With kisses drunk
You drop your heads
In the sublimely sobering water.

But where, with winter come, am I
To find, alas, the flowers, and where
The sunshine 
And the Shadow of the world?
Cold the walls stand
And wordless, in the wind
The weathercocks are rattling.
"""

#Source: DeepL
tb1 = """
From west and east, from north and south
Many feet will soon be dragging themselves wearily,
Feet, sore and torn from walking,
Slowly set to the earth,
Toil in the trembling moonlight
Restlessly deep into Germany.
And who with listening ear still wakes
Hears them in every growing night,
Hears this shuffling so weary and heavy,
Hears a lament full of wild desire,
A lamentation full of pain:
Only do not forget! Do not forget us!
"""

#Source: ChatGPT mit dem Prompt Translate the following text from German into English. keep the rhyme structure in the English version: 
tb2 = """
From west and from east, from north and south
Drag many weary feet, heading towards their mouth,
Feet, torn and worn from endless strife,
Placed on the ground with cautious life,
Struggling in the quivering moon's light,
Restlessly deep into Germany's night.
And those who still awake with listening ear
Hear them each coming night drawing near,
Hear this shuffling so weary and slow,
Hear a lament filled with wild woe,
A lament devoured by sorrow:
Do not forget! Us do not forget tomorrow!
"""

source_1 = """
Taschenbuch für das Jahr 1805. Der Liebe und Freundschaft gewidmet. Frankfurt am Mayn, bei Friedrich Wilmans 1805, S. 85.
"""

source_2 = """
Die deutsche Balladen-Chronik. Ein Balladenbuch von deutscher Geschichte und deutscher Art. Dortmund: Ruhfus 1922, S. xx.
"""

poem_1 = Text("Friedrich Hölderlin", "Hälfte des Lebens", 1804)
poem_1.set_text(poem_text_1)
poem_1.set_source(source_1)
poem_1.add_translations([ta1, ta2, ta3, ta4])
poem_2 = Text("Hans Pfeifer", "Unsere Toten", 1922)
poem_2.set_text(poem_text_2)
poem_2.set_source(source_2)
poem_2.add_translations([tb1, tb2])



