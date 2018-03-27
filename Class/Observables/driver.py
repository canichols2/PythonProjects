from observer1 import Subscriber, Publisher

pub = Publisher("update","delete","speak")

cody = Subscriber("Cody")
lauren = Subscriber("Lauren")
brian = Subscriber("Brian")

pub.register(cody)
pub.register(lauren)
pub.register(brian)

pub.dispatch("speak","You have been born")
pub.unregister(brian)
pub.dispatch("Hello World!")
