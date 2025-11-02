#iterable iterator generator
from typing import Iterable, Iterator, Generator
ppl: list[str] = ["bob", "rob", "job"]
ppl_iter: Iterator[str] = iter(ppl) #listeyi iteratöre çevirdi
print(next(ppl_iter)) #bob
print(list(ppl))      #['bob', 'rob', 'job'] ppl_iter printlese altta tekliler printlenmezdi
print(next(ppl_iter)) #rob
print(next(ppl_iter)) #job
print(list(ppl_iter)) #[]
#print(next(ppl)) #liste iteratör deil uyarısı

###iteratörden bir bilgi bir kere çağırıldıktan sonra tekrar aynı bilgiyi çıktı olarak ne tekli ne liste olarak verir
###they are exhaustive

