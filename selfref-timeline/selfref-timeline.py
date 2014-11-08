#!/usr/bin/env python

import random
import sys


class Event(object):
    def __init__(self):
        target_event = None


class Prediction(Event):
    def render(self):
        if self.target_event:
            return "predict(%s)" % self.target_event.render()
        return "NOT TIED"


class Memory(Event):
    def render(self):
        if self.target_event:
            return "remember(%s)" % self.target_event.render()
        return "NOT TIED"


def main(argv):
    timeline = [random.choice((Prediction, Memory))() for x in xrange(0, 50)]
    for (pos, event) in enumerate(timeline):
        # not exactly object-oriented (yet)
        if isinstance(event, Prediction):
            event_pool = timeline[pos+1:]
        elif isinstance(event, Memory):
            event_pool = timeline[:pos]
        if event_pool:
            event.target_event = random.choice(event_pool)

    for event in timeline:
        print event.render(event)


if __name__ == '__main__':
    import sys
    main(sys.argv)
