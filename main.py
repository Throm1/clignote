strip = neopixel.create(DigitalPin.P0, 5, NeoPixelMode.RGB)
strip.show_rainbow(1, 360)

def on_forever():
    pass
basic.forever(on_forever)
