#!/usr/bin/env python

import random
import sys


class Event(object):
    def __init__(self):
        self.target_event = None


class Sighting(Event):
    def __init__(self):
        self.sight = random.choice(
            ('UFO', 'bigfoot', 'ghost', 'black helicopter')
        ) + ' ' + random.choice(
            ('on vacation',
             'just sitting there',
             'cheating at cards',
             'ranting obnoxiously'
            )
        )
        self.target_event = self  # too-clever way of defeating filter


class Prediction(Event):
    pass


class Memory(Event):
    pass


def render_toplevel(event):
    starting_at = event
    mentioned = set([starting_at])

    if isinstance(event, Prediction):
        return (
            'Alice turned to Bob and asked, '
            '"Bob, do you think we will ever %s?"' %
            render(event.target_event, starting_at, mentioned)
        )
    elif isinstance(event, Memory):
        return (
            'Bob turned to Alice and said, '
            '"Alice, do you remember that one time when we %s?"' %
            render(event.target_event, starting_at, mentioned)
        )
    elif isinstance(event, Sighting):
        return 'Alice and Bob saw a %s.' % event.sight
    else:
        raise NotImplementedError(event)


def render(event, starting_at, mentioned):
    # so much for object-orientation
    if not event:
        return 'nothing at all'

    if starting_at == event:
        return 'this moment'

    if event in mentioned:
        return 'that moment'  # hard to be more specific!

    mentioned = mentioned | set([event])  # note that we do not modify the shared set

    if isinstance(event, Prediction):
        return (
            "wonder if we'd ever %s" % render(event.target_event, starting_at, mentioned)
        )
    elif isinstance(event, Memory):
        return (
            "remember that time when %s" % render(event.target_event, starting_at, mentioned)
        )
    elif isinstance(event, Sighting):
        return "see a %s" % event.sight
    else:
        raise NotImplementedError(event)


def main(argv):
    timeline = [random.choice((Prediction, Memory, Sighting))() for x in xrange(0, 50)]
    for (pos, event) in enumerate(timeline):
        event_pool = None
        if isinstance(event, Prediction):
            event_pool = timeline[pos+1:]
        elif isinstance(event, Memory):
            event_pool = timeline[:pos]
        if event_pool:
            event.target_event = random.choice(event_pool)
        else:
            #print event, pos
            pass

    # filter out unlinked events
    timeline = [t for t in timeline if t.target_event]

    for event in timeline:
        print render_toplevel(event)
        print


if __name__ == '__main__':
    import sys
    main(sys.argv)
