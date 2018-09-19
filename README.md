# aps - Wifi Access Point Explorer
This trivial program was written out frustration with the execrable
output of the `iwlist` command. The wireless-tools are quite powerful
and I found that it produced a lot of great information but the output
was so terrible that it was unusable.

This program captures the messy multi-line output and makes each
access point into an object allowing you to do whatever you need. What
I've mostly done is create a nice one-record-per-line list of
accesspoints. The output will look something like this.

```
01|6CAAB31ACDD8|9|2.452|61/70|-49dBm|e|Master|Comfort Inn
05|6CAAB31AC628|1|2.412|52/70|-58dBm|e|Master|Comfort Inn
09|6CAAB30B8F58|3|2.422|51/70|-59dBm|e|Master|Comfort Inn
08|6CAAB31A8028|10|2.457|50/70|-60dBm|e|Master|Comfort Inn
15|6CAAB319D458|10|2.457|41/70|-69dBm|e|Master|Comfort Inn
10|6CAAB31919B8|11|2.462|40/70|-70dBm|e|Master|Comfort Inn
11|A86BADE4769E|6|2.437|31/70|-79dBm|E|Master|WIFIE4769A
14|90CDB69CD375|6|2.437|26/70|-84dBm|E|Master|Traid@422
13|F8DA0CF854D9|6|2.437|24/70|-86dBm|E|Master|Look Ma, No Wires!
07|6CAAB31A7D18|9|2.452|24/70|-86dBm|e|Master|Comfort Inn
12|6CAAB31AC068|6|2.437|24/70|-86dBm|e|Master|Comfort Inn
04|D80F99AE31C2|1|2.412|19/70|-91dBm|E|Master|WIFIAE31BF
02|3835FBE2E556|1|2.412|18/70|-92dBm|E|Master|IB
06|6CAAB31AAED8|2|2.417|18/70|-92dBm|e|Master|Comfort Inn
03|CCA46242F050|1|2.412|17/70|-93dBm|E|Master|DG860A52
```

The fields are cell, MAC, channel, frequency, strength, loss,
encrypted, mode, AP name. 

For some reason that I don't completely understand, when this is run
by root, it produces a lot more results than when run as a normal
user.

I like to use this alias that further sorts by signal strength.

```
alias aps='sudo /home/${USER}/bin/aps.py | sort -k6 -t'\''|'\'''
```

It is likely that you will need to set the interface constant `IF`
with the name of your wifi device. Use `ip addr` to figure out what
that is.
