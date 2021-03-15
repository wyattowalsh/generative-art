resolution_4k = 240
colors = \
{
          "Illuminating":    "#F5DF4D",
          "Ultimate Gray":   "#939597", 
          "Classic Blue":    "#0F4C81",
          "Living Coral":    "#FF6F61",
          "Ultra Violet":    "#5F4B8B",
          "Greenery":        "#88B04B", 
          "Serenity":        "#92A8D1", 
          "Rose Quartz":     "#F7CAC9", 
          "Marsala":         "#955251", 
          "Radiant Orchid":  "#B163A3", 
          "Emerald":         "#009473", 
          "Tangerine Tango": "#DD4124", 
          "Honeysuckle":     "#D94F70",
          "Turquoise":       "#45B5AA",
          "Mimosa":          "#F0C05A",
          "Blue Iris":       "#5A5B9F",
          "Chili Pepper":    "#9B1B30",
          "Sand Dollar":     "#DECDBE",
          "Blue Turquoise":  "#53B0AE",
          "Tigerlily":       "#E2583E",
          "Aqua Sky":        "#7BC4C4",
          "True Red":        "#BF1932",
          "Fuchsia Rose":    "#C74375",
          "Cerulean":        "#9BB7D4" 
}
num_colors = len(colors)
indices = [x + 1 for x in list(range(num_colors))]
to_scale = [x + 2 for x in indices]
to_scale.reverse()
color_codes = list(colors.values())
input_colors = []
for i in range(num_colors):
  input_colors += to_scale[i] * [color_codes[i]]
choices = len(input_colors)
#######################
def setup():
    size(16*resolution_4k,9*resolution_4k, P3D)

num_shapes = [
         2,    3,    5,    7,   11,   13,   17,   19,   23,   29,   31,
         37,   41,   43,   47,   53,   59,   61,   67,   71,   73,   79,
         83,   89,   97,  101
        ]
shapes = [arc, circle, ellipse, point, quad, rect, square, triangle]
arc_types = [noFill(), OPEN, CHORD, PIE]
backgrounds = [0, 255]
max_depth = 100
num_files = 50
seed = 18
######################

def draw():
    randomSeed(seed)
    for bg in backgrounds:
        for i in range(num_files):
            background(bg)
            num_shape = lines[floor(random(len(num_shapes)))]
            for i in range(num_shape):    
                color = input_colors[floor(random(choices))]
                stroke(color)
                strokeWeight(ceil(random(max_depth)))
                shape = shapes[floor(random(len(shapes)))]
            if bg == 0:
                bgcolor = "black"
            else:
                bgcolor = "white"
            name = "2/1/2d-random-1_max-depth-{}_lines-{}_seed-{}_background-{}.tiff".format(max_depth, num_lines, seed, bgcolor)
            save(name)
    exit()
    
    
    
