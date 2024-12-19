# NeuroMesh

### What is this ?
I do not know anything about neural networks and stuff but i wanted to build something i find quite interesting:

I want to distribute parts of a neural network over multiple devices in order to build a dynamic neural construct like the human body

[![](https://mermaid.ink/img/pako:eNpVj00LwjAMhv9KyUlh_oEhgh9Hvbib1kNos624NaOmDNn2361fiDkleR5I3gEMW4IcyoZ7U2MQtT9qr1KtZwX5G4e5WixWoyfpOVxHtRn2XDkzvaWNWv7R7bkQDljR5cv_8O68NuLYJwoZtBRadDZdH562BqmpJQ15ai2VGBvRoP2UVIzCxd0byCVEyiB2FoV2DquALeQlNre07dCfmH8zWZe-ObwTvoJmEDhW9ceYHj_NVco?type=png)](https://mermaid.live/edit#pako:eNpVj00LwjAMhv9KyUlh_oEhgh9Hvbib1kNos624NaOmDNn2361fiDkleR5I3gEMW4IcyoZ7U2MQtT9qr1KtZwX5G4e5WixWoyfpOVxHtRn2XDkzvaWNWv7R7bkQDljR5cv_8O68NuLYJwoZtBRadDZdH562BqmpJQ15ai2VGBvRoP2UVIzCxd0byCVEyiB2FoV2DquALeQlNre07dCfmH8zWZe-ObwTvoJmEDhW9ceYHj_NVco)


### Naming
I call every instance a "service"
I differentiate between 4 types of service
- Sensor (Takes an input and forwards it)
- Logic (Acts on Sensoric inputs with help from storage)
- Action (Produces Output or actions)
- Storage (Vector DB Backend as longterm storage)


### Network
- Every service forwards an array of float representing its output layer to the next service
[![](https://mermaid.ink/img/pako:eNpNkMFqwzAQRH9F7NlyYzsx2OdeWwK5FV021joxlbRGWR1KyL_HsgPpcee9gWHvMLAl6EFrbYJM4qhXBr4pRXTqiMMviQETVjyvpz6ToAlK7XRTZTkkf6aoeFRhqXG45YJSTa27Q-ajY5R2_1Ftedfq6tD9B_UGqnan67rJpCxLA1CAp-hxssu-ezYMyJU8GciOpRGTW9c9FhWT8OkvDNBLTFRAmi0KfU54ieihH9HdlnTG8MP8vslOwvFr-8H6igIip8v1ZTyeJqtavA?type=png)](https://mermaid.live/edit#pako:eNpNkMFqwzAQRH9F7NlyYzsx2OdeWwK5FV021joxlbRGWR1KyL_HsgPpcee9gWHvMLAl6EFrbYJM4qhXBr4pRXTqiMMviQETVjyvpz6ToAlK7XRTZTkkf6aoeFRhqXG45YJSTa27Q-ajY5R2_1Ftedfq6tD9B_UGqnan67rJpCxLA1CAp-hxssu-ezYMyJU8GciOpRGTW9c9FhWT8OkvDNBLTFRAmi0KfU54ieihH9HdlnTG8MP8vslOwvFr-8H6igIip8v1ZTyeJqtavA)


### Future 
I would like to be able to have a central Logic service or multiple redundant logic services that get fed by a wide array of sensor services from all over the network and work together with a set of vector and other DBs in order to inform actions to take by the action services.

For example have energy and temperature sensors services on esp32 passing information to a central logic service on an raspi with a coral chip to control room temperatures learned from the occupants...
Or have a robot use vision and orientation sensors in order to move through rough terrain ...
Just some scifiy ideas nothing i hope to be able to archieve by myself but i wanted to play with the idea.
