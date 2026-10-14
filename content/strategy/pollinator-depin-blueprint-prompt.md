# Prompt za Google AI Studio: nacrt kucice (14.10)

Nemanja salje 2-3 slike kucica i trazi nacrt krajnjeg proizvoda: prvo
kompaktno, pa se otvara (kamera se rotira u stranu), i svaki deo je ispisan.
Dole su spisak delova (da nacrt ispise prave stvari) i dva prompta: jedan za
video (Veo), jedan za sliku (eksplodirani nacrt).

## Delovi koje nacrt treba da ispise

Kucica:
1. Wooden body, untreated hardwood
2. Roof with overhang (rain and sun protection)
3. Removable nesting block, channels 6 to 10 mm, paper liners
4. Clear panel in front of the tubes (camera window)
5. Wire mesh guard against birds
6. Mounting bracket (wall or post)
7. ID plate with QR code (on-chain identity)

Elektronika:
8. Camera module with small LED, points at the tube ends
9. Entrance counter, infrared beam at the front
10. Inside sensor: temperature and humidity in the nesting block
11. Outside weather sensor under the roof: temperature, humidity, pressure, light
12. Main board with WiFi / LoRa, antenna
13. Solar panel on the roof
14. Battery in a sealed box (18650)
15. Cable channel from roof to battery box

## Prompt za video (Veo), engleski

    Technical product animation, blueprint style. Use the attached photos as
    reference for the look of the wooden bee house. Start with a compact
    wooden house for solitary bees on a plain light background: wooden body,
    roof with overhang, a block of nesting tubes at the front, a small solar
    panel on the roof. The camera slowly orbits to the side. The house opens
    into an exploded view: the roof lifts, the nesting block slides out, the
    electronics box opens. Each part gets a thin leader line and a clean
    label, drawn like an engineering blueprint. Labels, in this order:
    wooden body (untreated hardwood); roof with overhang; removable nesting
    block, 6 to 10 mm channels; clear camera window; wire mesh bird guard;
    camera module with LED; infrared entrance counter; inside sensor,
    temperature and humidity; outside weather sensor, temperature, humidity,
    pressure, light; main board with WiFi / LoRa and antenna; solar panel;
    battery box, 18650; mounting bracket; ID plate with QR code. Muted
    colors, thin lines, white or light grey background, no text other than
    the labels, no logos. Slow, steady camera movement, 8 seconds.

## Prompt za sliku (eksplodirani nacrt), engleski

    Exploded view technical drawing of a wooden house for solitary bees with
    built in sensors, blueprint style, based on the attached photos. Parts
    separated vertically with thin leader lines and labels: wooden body
    (untreated hardwood); roof with overhang; removable nesting block with
    6 to 10 mm channels; clear camera window; wire mesh bird guard; camera
    module with LED; infrared entrance counter; inside temperature and
    humidity sensor; outside weather sensor (temperature, humidity,
    pressure, light); main board with WiFi / LoRa and antenna; solar panel;
    battery box (18650); mounting bracket; ID plate with QR code. Clean
    engineering style, light background, muted wood and dark grey
    electronics, no logos, no extra text.

## Napomena

Ako model izmisli deo koji nije na spisku (ventilator, ekran, zvucnik),
trazi da ga ukloni. Sta se ne stavlja: "hive", "honey", "beekeeping" u
labelama; ovo je kucica za divlje pcele, ne kosnica.
